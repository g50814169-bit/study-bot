import os
TOKEN = os.getenv("BOT_TOKEN")
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

# Заглушка для порта 7860, чтобы Hugging Face не отключал контейнер
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is alive and running 24/7!")

def run_web_server():
    server = HTTPServer(('0.0.0.0', 7860), HealthCheckHandler)
    server.serve_forever()

# Запускаем веб-сервер в фоновом потоке
threading.Thread(target=run_web_server, daemon=True).start()
import asyncio
import random
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# Импортируем нашу базу уроков из файла lessons.py
from lessons import LESSONS

BOT_TOKEN = "8998678112:AAHjYwgf84rfvkgJcgAFmGLpdZ1FfsC73EU"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# --- КЛАВИАТУРЫ ---

def get_main_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="📚 Выбрать тему по уровню")
    builder.button(text="🎲 Мне повезет! (Случайная лекция)")
    builder.button(text="💡 Как учиться эффективно?")
    builder.adjust(1, 1, 1)
    return builder.as_markup(resize_keyboard=True)

def get_categories_inline():
    builder = InlineKeyboardBuilder()
    builder.button(text="Science 🔬", callback_data="cat:Science 🔬")
    builder.button(text="Technology 💻", callback_data="cat:Technology 💻")
    builder.button(text="Engineering ⚙️", callback_data="cat:Engineering ⚙️")
    builder.button(text="Mathematics 📐", callback_data="cat:Mathematics 📐")
    builder.adjust(2, 2)
    return builder.as_markup()

def get_levels_inline(category):
    builder = InlineKeyboardBuilder()
    builder.button(text="🟢 Beginner (Новичок)", callback_data=f"lvl:{category}:Beginner 🟢")
    builder.button(text="🟡 Intermediate (Средний)", callback_data=f"lvl:{category}:Intermediate 🟡")
    builder.button(text="🔴 Advanced (Продвинутый)", callback_data=f"lvl:{category}:Advanced 🔴")
    builder.adjust(1)
    return builder.as_markup()

# --- ОБРАБОТЧИКИ СООБЩЕНИЙ И КНОПОК ---

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    text = (
        f"Hello, **{message.from_user.first_name}**! 👋\n\n"
        f"Добро пожаловать в **STEM English**.\n"
        f"Здесь ты можешь учить английский язык для науки и IT **в своем темпе**.\n\n"
        f"Выбирай предмет и уровень сложности: от простых базовых терминов до научных статей!"
    )
    await message.answer(text, reply_markup=get_main_keyboard(), parse_mode="Markdown")

@dp.message(F.text == "💡 Как учиться эффективно?")
async def info_cmd(message: types.Message):
    text = (
        "💡 **Советы по изучению STEM English:**\n\n"
        "1. **Начинайте с Beginner 🟢:** Даже если вы знаете предмет, простые объяснения помогут запомнить базовые термины (*soil, solve, heavy*).\n"
        "2. **Читайте вслух:** Произносите транскрипцию в блоке Vocabulary.\n"
        "3. **Занимайтесь по 5 минут в день:** Проходите по 1 лекции в день, не перегружая себя!"
    )
    await message.answer(text, parse_mode="Markdown")

@dp.message(F.text == "📚 Выбрать тему по уровню")
async def choose_cat(message: types.Message):
    await message.answer("Шаг 1 из 2: Выберите дисциплину 👇", reply_markup=get_categories_inline())

@dp.callback_query(F.data.startswith("cat:"))
async def handle_category(callback: types.CallbackQuery):
    cat_name = callback.data.split(":")[1]
    await callback.message.edit_text(
        f"Выбрано: **{cat_name}**\n\nШаг 2 из 2: Выберите ваш уровень знаний 👇",
        reply_markup=get_levels_inline(cat_name),
        parse_mode="Markdown"
    )
    await callback.answer()

@dp.callback_query(F.data.startswith("lvl:"))
async def handle_level(callback: types.CallbackQuery):
    _, category, level = callback.data.split(":")
    
    filtered = [l for l in LESSONS if l['category'] == category and l['level'] == level]
    
    if filtered:
        lecture = random.choice(filtered)
        text = (
            f"📌 **{lecture['category']}** | Уровень: *{lecture['level']}*\n\n"
            f"### {lecture['title']}\n\n"
            f"{lecture['text']}\n\n"
            f"― ― ― ― ― ― ― ― ― ― ― ― ― ― ―\n"
            f"{lecture['vocab']}"
        )
        await callback.message.edit_text(text, parse_mode="Markdown")
    else:
        await callback.message.edit_text(
            f"😔 В разделе **{category}** на уровне **{level}** лекции ещё пополняются.\nПопробуйте выбрать другой уровень!",
            parse_mode="Markdown"
        )
    
    await callback.answer()

@dp.message(F.text == "🎲 Мне повезет! (Случайная лекция)")
async def random_lecture(message: types.Message):
    lecture = random.choice(LESSONS)
    text = (
        f"📌 **{lecture['category']}** | Уровень: *{lecture['level']}*\n\n"
        f"### {lecture['title']}\n\n"
        f"{lecture['text']}\n\n"
        f"― ― ― ― ― ― ― ― ― ― ― ― ― ― ―\n"
        f"{lecture['vocab']}"
    )
    await message.answer(text, parse_mode="Markdown")

async def main():
    print("Бот STEM English запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())