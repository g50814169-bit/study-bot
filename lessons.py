# lessons.py — Полная база уроков STEM по уровням сложности

LESSONS = [
    # =========================================================================
    # 🔬 SCIENCE (ЕСТЕСТВЕННЫЕ НАУКИ)
    # =========================================================================
    
    # --- Science 🔬 | Beginner 🟢 ---
    {
        "category": "Science 🔬",
        "level": "Beginner 🟢",
        "title": "🌱 Photosynthesis (Как растения питаются)",
        "text": (
            "**Photosynthesis** is the process plants use to make their own food.\n\n"
            "Plants absorb **water** from the soil, **carbon dioxide** from the air, and **sunlight** from the sun. "
            "They turn these into **oxygen** (which we breathe) and **sugar** (their food).\n\n"
            "💡 *Simple Example:* Just like you need food to get energy, plants need sunlight to make sugar!"
        ),
        "vocab": (
            "🔑 **Vocabulary for Beginners:**\n"
            "• **Absorb** (`/əbˈzɔːb/`) — Впитывать, поглощать\n"
            "• **Soil** (`/sɔɪl/`) — Почва, земля\n"
            "• **Oxygen** (`/ˈɒksɪdʒən/`) — Кислород\n"
            "• **Plant** (`/plɑːnt/`) — Растение"
        )
    },
    {
        "category": "Science 🔬",
        "level": "Beginner 🟢",
        "title": "💧 The Water Cycle (Круговорот воды в природе)",
        "text": (
            "The **water cycle** shows how water moves around the Earth.\n\n"
            "1. **Evaporation:** The sun heats water in rivers and oceans, turning it into vapor (gas).\n"
            "2. **Condensation:** Water vapor cools down in the sky and forms clouds.\n"
            "3. **Precipitation:** Clouds get heavy and water falls back to Earth as rain or snow."
        ),
        "vocab": (
            "🔑 **Vocabulary for Beginners:**\n"
            "• **Evaporation** (`/ɪˌvæpəˈreɪʃn/`) — Испарение\n"
            "• **Vapor** (`/ˈveɪpə/`) — Пар\n"
            "• **Cool down** (`/kuːl daʊn/`) — Остывать, охлаждаться\n"
            "• **Cloud** (`/klaʊd/`) — Облако"
        )
    },

    # --- Science 🔬 | Intermediate 🟡 ---
    {
        "category": "Science 🔬",
        "level": "Intermediate 🟡",
        "title": "🧬 CRISPR-Cas9 (Gene Editing)",
        "text": (
            "**CRISPR-Cas9** is a technology used by scientists to edit DNA sequences.\n\n"
            "It acts like a pair of 'molecular scissors' that can cut a specific strand of DNA, "
            "allowing scientists to remove or replace bad genes that cause hereditary diseases."
        ),
        "vocab": (
            "🔑 **Intermediate Vocabulary:**\n"
            "• **Genome** (`/ˈdʒiːnəʊm/`) — Геном\n"
            "• **Alter** (`/ˈɔːltə/`) — Изменять\n"
            "• **Strand** (`/strænd/`) — Нить / цепь (ДНК)\n"
            "• **Hereditary** (`/hɪˈredɪtri/`) — Наследственный"
        )
    },
    {
        "category": "Science 🔬",
        "level": "Intermediate 🟡",
        "title": "🧪 Chemical Reactions and Catalyst",
        "text": (
            "A **chemical reaction** happens when chemical bonds break and form new substances.\n\n"
            "Substances that start a reaction are called **reactants**, and what is produced is called the **product**. "
            "A **catalyst** is a substance that speeds up a chemical reaction without being consumed by it."
        ),
        "vocab": (
            "🔑 **Intermediate Vocabulary:**\n"
            "• **Substance** (`/ˈsʌbstəns/`) — Вещество\n"
            "• **Reactant** (`/riˈæktənt/`) — Реагент\n"
            "• **Catalyst** (`/ˈkætəlɪst/`) — Катализатор\n"
            "• **Consume** (`/kənˈsjuːm/`) — Расходовать, потреблять"
        )
    },

    # --- Science 🔬 | Advanced 🔴 ---
    {
        "category": "Science 🔬",
        "level": "Advanced 🔴",
        "title": "🌌 Quantum Entanglement and Superposition",
        "text": (
            "**Quantum Mechanics** fundamentally differs from classical physics.\n\n"
            "**Superposition:** A quantum particle can exist in multiple states simultaneously until it is measured. "
            "Before observation, its state is described by a wave function.\n\n"
            "**Entanglement:** When two particles become entangled, measuring one instantaneously dictates the state of the other, "
            "regardless of the physical distance separating them."
        ),
        "vocab": (
            "🔑 **Advanced Vocabulary:**\n"
            "• **Simultaneously** (`/ˌsɪmlˈteɪniəsli/`) — Одновременно\n"
            "• **Instantaneously** (`/ˌɪnstənˈteɪniəsli/`) — Мгновенно\n"
            "• **Observation** (`/ˌɒbzəˈveɪʃn/`) — Наблюдение / Измерение\n"
            "• **Dictate** (`/dɪkˈteɪt/`) — Предписывать, определять"
        )
    },

    # =========================================================================
    # 💻 TECHNOLOGY (ТЕХНОЛОГИИ И ИТ)
    # =========================================================================

    # --- Technology 💻 | Beginner 🟢 ---
    {
        "category": "Technology 💻",
        "level": "Beginner 🟢",
        "title": "🤖 What is an Algorithm? (Что такое алгоритм)",
        "text": (
            "An **algorithm** is just a step-by-step set of instructions to solve a problem.\n\n"
            "Think of it like a cooking recipe: if you follow the steps in order, you get a cake. "
            "Computers follow algorithms to open apps, show videos, and run programs."
        ),
        "vocab": (
            "🔑 **Vocabulary for Beginners:**\n"
            "• **Instructions** (`/ɪnˈstrʌkʃnz/`) — Инструкции, правила\n"
            "• **Solve** (`/sɒlv/`) — Решать (задачу)\n"
            "• **Recipe** (`/ˈresəpi/`) — Рецепт\n"
            "• **Run a program** — Запускать программу"
        )
    },
    {
        "category": "Technology 💻",
        "level": "Beginner 🟢",
        "title": "💾 Hardware vs Software (Железо и ПО)",
        "text": (
            "Computers are made of two main parts:\n\n"
            "• **Hardware:** The physical parts you can touch, like the screen, keyboard, mouse, or processor.\n"
            "• **Software:** The programs and apps inside that give instructions to the hardware."
        ),
        "vocab": (
            "🔑 **Vocabulary for Beginners:**\n"
            "• **Physical** (`/ˈfɪzɪkl/`) — Физический, материальный\n"
            "• **Screen** (`/skriːn/`) — Экран\n"
            "• **Keyboard** (`/ˈkiːbɔːd/`) — Клавиатура\n"
            "• **Touch** (`/tʌtʃ/`) — Касаться, трогать"
        )
    },

    # --- Technology 💻 | Intermediate 🟡 ---
    {
        "category": "Technology 💻",
        "level": "Intermediate 🟡",
        "title": "🧠 Artificial Neural Networks",
        "text": (
            "**Artificial Neural Networks (ANNs)** are computer systems inspired by the human brain.\n\n"
            "They consist of connected layers of artificial neurons that process input data and recognize complex patterns, "
            "allowing computers to recognize objects in images or generate speech."
        ),
        "vocab": (
            "🔑 **Intermediate Vocabulary:**\n"
            "• **Layer** (`/ˈleɪə/`) — Слой\n"
            "• **Pattern** (`/ˈpætən/`) — Шаблон, закономерность\n"
            "• **Recognize** (`/ˈrekəɡnaɪz/`) — Распознавать\n"
            "• **Speech** (`/spiːtʃ/`) — Речь"
        )
    },
    {
        "category": "Technology 💻",
        "level": "Intermediate 🟡",
        "title": "🔒 Encryption and Cybersecurity",
        "text": (
            "**Encryption** is the process of scrambling readable text so that only authorized parties can read it.\n\n"
            "When you send a message, encryption transforms it into unreadable code using a secret **cryptographic key**. "
            "Without the key, hackers cannot decipher your passwords or personal messages."
        ),
        "vocab": (
            "🔑 **Intermediate Vocabulary:**\n"
            "• **Scramble** (`/ˈskræmbl/`) — Перемешивать, шифровать\n"
            "• **Authorized** (`/ˈɔːθəraɪzd/`) — Авторизованный, имеющий доступ\n"
            "• **Decipher** (`/dɪˈsaɪfə/`) — Расшифровывать\n"
            "• **Key** (`/kiː/`) — Ключ (в криптографии)"
        )
    },

    # --- Technology 💻 | Advanced 🔴 ---
    {
        "category": "Technology 💻",
        "level": "Advanced 🔴",
        "title": "🌐 Microservices Architecture vs Monolith",
        "text": (
            "When building enterprise software, developers choose between structural architectures:\n\n"
            "• **Monolithic:** A single unified codebase. All features share memory, making initial setup easy but long-term scaling difficult.\n"
            "• **Microservices:** The app is broken into independent, loosely-coupled services communicating via REST or gRPC APIs. "
            "This allows individual services to scale independently on demand."
        ),
        "vocab": (
            "🔑 **Advanced Vocabulary:**\n"
            "• **Unified** (`/ˈjuːnɪfaɪd/`) — Единый, объединенный\n"
            "• **Loosely-coupled** — Слабосвязанные\n"
            "• **Scalability** (`/ˌskeɪləˈbɪləti/`) — Масштабируемость\n"
            "• **On demand** — По требованию"
        )
    },

    # =========================================================================
    # ⚙️ ENGINEERING (ИНЖЕНЕРИЯ И МЕХАНИКА)
    # =========================================================================

    # --- Engineering ⚙️ | Beginner 🟢 ---
    {
        "category": "Engineering ⚙️",
        "level": "Beginner 🟢",
        "title": "⚖️ Levers and Simple Machines (Рычаг)",
        "text": (
            "A **lever** is a simple machine that makes lifting heavy objects much easier.\n\n"
            "It consists of a stiff bar that rotates around a fixed point called a **fulcrum**. "
            "A playground see-saw or a pair of scissors are everyday examples of levers!"
        ),
        "vocab": (
            "🔑 **Vocabulary for Beginners:**\n"
            "• **Lever** (`/ˈliːvə/`) — Рычаг\n"
            "• **Lift** (`/lɪft/`) — Поднимать\n"
            "• **Stiff** (`/stɪf/`) — Жесткий, негнущийся\n"
            "• **Scissors** (`/ˈsɪzəz/`) — Ножницы"
        )
    },
    {
        "category": "Engineering ⚙️",
        "level": "Beginner 🟢",
        "title": "🏗️ Why do Bridges need Triangles? (Геометрия мостов)",
        "text": (
            "Have you noticed that steel bridges are full of triangle shapes?\n\n"
            "The **triangle** is the strongest geometric shape in engineering. "
            "When weight is applied to a triangle, the force is distributed evenly across all three sides, preventing the bridge from collapsing."
        ),
        "vocab": (
            "🔑 **Vocabulary for Beginners:**\n"
            "• **Bridge** (`/brɪdʒ/`) — Мост\n"
            "• **Shape** (`/ʃeɪp/`) — Форма, фигура\n"
            "• **Weight** (`/weɪt/`) — Вес, нагрузка\n"
            "• **Collapse** (`/kəˈlæps/`) — Обрушиваться, рушиться"
        )
    },

    # --- Engineering ⚙️ | Intermediate 🟡 ---
    {
        "category": "Engineering ⚙️",
        "level": "Intermediate 🟡",
        "title": "🏎️ Aerodynamics and Drag Force",
        "text": (
            "**Aerodynamics** studies how air moves around solid objects.\n\n"
            "When a vehicle moves forward, it experiences an opposing air resistance called **drag force**. "
            "Engineers design streamlined shapes to minimize drag and reduce fuel consumption."
        ),
        "vocab": (
            "🔑 **Intermediate Vocabulary:**\n"
            "• **Drag force** — Сила лобового сопротивления воздуха\n"
            "• **Opposing** (`/əˈpəʊzɪŋ/`) — Противодействующий\n"
            "• **Streamlined** (`/ˈstriːmlaɪnd/`) — Обтекаемый\n"
            "• **Consumption** (`/kənˈsʌmpʃn/`) — Расход, потребление"
        )
    },

    # --- Engineering ⚙️ | Advanced 🔴 ---
    {
        "category": "Engineering ⚙️",
        "level": "Advanced 🔴",
        "title": "🔥 Thermodynamics: The Carnot Cycle",
        "text": (
            "The **Carnot cycle** is an ideal thermodynamic cycle that defines the maximum theoretical efficiency for heat engines.\n\n"
            "It consists of four reversible processes:\n"
            "1. **Isothermal expansion** (constant temperature absorption).\n"
            "2. **Adiabatic expansion** (work done without heat exchange).\n"
            "3. **Isothermal compression** (heat rejection).\n"
            "4. **Adiabatic compression** (returning gas to its initial state)."
        ),
        "vocab": (
            "🔑 **Advanced Vocabulary:**\n"
            "• **Efficiency** (`/ɪˈfɪʃnsi/`) — КПД\n"
            "• **Isothermal** — Изотермический\n"
            "• **Adiabatic** — Адиабатический\n"
            "• **Reversible** (`/rɪˈvɜːsəbl/`) — Обратимый"
        )
    },

    # =========================================================================
    # 📐 MATHEMATICS (МАТЕМАТИКА)
    # =========================================================================

    # --- Mathematics 📐 | Beginner 🟢 ---
    {
        "category": "Mathematics 📐",
        "level": "Beginner 🟢",
        "title": "🔢 Variables and Equations (Переменные)",
        "text": (
            "In algebra, a **variable** is a symbol (usually a letter like `x` or `y`) that represents an unknown number.\n\n"
            "An **equation** shows that two expressions are equal using an `=` sign. "
            "For example, in `x + 3 = 5`, `x` is the variable, and its value is `2`."
        ),
        "vocab": (
            "🔑 **Vocabulary for Beginners:**\n"
            "• **Variable** (`/ˈveəriəbl/`) — Переменная\n"
            "• **Equation** (`/ɪˈkweɪʒn/`) — Уравнение\n"
            "• **Unknown** (`/ˌʌnˈnəʊn/`) — Неизвестный\n"
            "• **Value** (`/ˈvæljuː/`) — Значение"
        )
    },
    {
        "category": "Mathematics 📐",
        "level": "Beginner 🟢",
        "title": "📊 Mean, Median, and Mode (Среднее значение)",
        "text": (
            "These are three ways to analyze a set of numbers:\n\n"
            "• **Mean:** The average (sum of all numbers divided by how many numbers there are).\n"
            "• **Median:** The middle number in a sorted list.\n"
            "• **Mode:** The number that appears most frequently."
        ),
        "vocab": (
            "🔑 **Vocabulary for Beginners:**\n"
            "• **Average** (`/ˈævərɪdʒ/`) — Среднее арифм.\n"
            "• **Divided by** — Деленный на...\n"
            "• **Sorted list** — Отсортированный список\n"
            "• **Frequently** (`/ˈfriːkwəntli/`) — Часто"
        )
    },

    # --- Mathematics 📐 | Intermediate 🟡 ---
    {
        "category": "Mathematics 📐",
        "level": "Intermediate 🟡",
        "title": "🎲 Probability and Event Outcomes",
        "text": (
            "**Probability** measures the likelihood that a specific event will occur, expressed as a number between `0` (impossible) and `1` (certain).\n\n"
            "The formula is: `P(E) = Number of favorable outcomes / Total possible outcomes`.\n"
            "For example, rolling a 6 on a standard 6-sided die has a probability of `1/6`."
        ),
        "vocab": (
            "🔑 **Intermediate Vocabulary:**\n"
            "• **Likelihood** (`/ˈlaɪklihʊd/`) — Вероятность\n"
            "• **Favorable** (`/ˈfeɪvərəbl/`) — Благоприятный\n"
            "• **Outcome** (`/ˈaʊtkʌm/`) — Исход, результат\n"
            "• **Certain** (`/ˈsɜːtn/`) — Достоверный, определенный"
        )
    },

    # --- Mathematics 📐 | Advanced 🔴 ---
    {
        "category": "Mathematics 📐",
        "level": "Advanced 🔴",
        "title": "📈 Fundamental Theorem of Calculus",
        "text": (
            "The **Fundamental Theorem of Calculus** connects differential calculus with integral calculus.\n\n"
            "It establishes that **differentiation** (finding the rate of change) and **integration** (finding the area under a curve) are inverse operations. "
            "Evaluating a definite integral can be achieved by finding an **antiderivative** function."
        ),
        "vocab": (
            "🔑 **Advanced Vocabulary:**\n"
            "• **Differential** (`/ˌdɪfəˈrenʃl/`) — Дифференциальный\n"
            "• **Integral** (`/ˈɪntɪɡrəl/`) — Интегральный\n"
            "• **Inverse operation** — Обратная операция\n"
            "• **Antiderivative** — Первообразная"
        )
    },
# =========================================================================
    # 🔬 SCIENCE (ЕСТЕСТВЕННЫЕ НАУКИ — ДЕТАЛЬНЫЕ ЛЕКЦИИ)
    # =========================================================================

    # --- Science 🔬 | Beginner 🟢 ---
    {

        "category": "Science 🔬",
        "level": "Beginner 🟢",
        "title": "🧪 Scientific Inquiry & Scientific Method (Научный метод)",
        "text": (
            "Science is not just a book full of facts; it is a systematic process of exploring the natural world around us.\n\n"
            "At the heart of all scientific exploration lies the **Scientific Method**. "
            "This structured approach allows scientists, researchers, and students to investigate questions, learn new information, and verify theories using empirical evidence.\n\n"
            "### Step 1: Observation\n"
            "The scientific process always starts with **observation**. An observation happens when you notice something interesting in your environment using your five senses or scientific tools. "
            "For example, you might observe that plants sitting near a window grow taller and greener than plants kept in a dark corner of the room.\n\n"
            "### Step 2: Asking a Question\n"
            "Observations naturally lead to questions. A good scientific question must be specific, objective, and testable. "
            "Instead of asking 'Do plants like sunlight?', a scientist asks: 'How does the number of daily sunlight hours affect the height of a tomato plant?'\n\n"
            "### Step 3: Forming a Hypothesis\n"
            "A **hypothesis** is an educated guess or a testable explanation for what you observed. "
            "A proper hypothesis is usually written as an 'If... then...' statement. "
            "For example: 'If a plant receives 8 hours of direct sunlight per day, then it will grow taller than a plant that receives only 2 hours of sunlight.'\n\n"
            "### Step 4: Conducting an Experiment\n"
            "To see if your hypothesis is correct, you must design a controlled **experiment**. "
            "In every experiment, there are key factors called **variables**:\n"
            "• **Independent Variable:** The factor you deliberately change or manipulate (e.g., the amount of daily sunlight).\n"
            "• **Dependent Variable:** The factor you measure to see if it changes in response (e.g., the plant's height in centimeters).\n"
            "• **Controlled Variables (Constants):** Factors that must stay exactly the same across all tests so they do not interfere with the results (e.g., soil type, water volume, pot size, and temperature).\n\n"
            "An experiment typically compares a **control group** (plants kept in standard conditions) with an **experimental group** (plants receiving altered sunlight levels).\n\n"
            "### Step 5: Data Collection and Analysis\n"
            "During the experiment, you carefully collect **data**. Data can be **quantitative** (numerical measurements like height, weight, or temperature) or **qualitative** (descriptive details like leaf color, leaf shape, or texture).\n"
            "After gathering the data, you analyze it by creating charts, tables, or graphs to spot clear patterns and trends.\n\n"
            "### Step 6: Drawing Conclusions\n"
            "Finally, you draw a **conclusion**. Your conclusion answers whether your experimental data supports or rejects your original hypothesis. "
            "If the data supports the hypothesis, scientists re-test it to make sure the results are repeatable. "
            "If the hypothesis is rejected, scientists form a new hypothesis and design a different experiment!"
        ),
        "vocab": (
            "🔑 **Vocabulary for Beginners:**\n"
            "• **Observation** (`/ˌɒbzəˈveɪʃn/`) — Наблюдение\n"
            "• **Hypothesis** (`/haɪˈpɒθəsɪs/`) — Гипотеза, предположение\n"
            "• **Experiment** (`/ɪkˈsperɪmənt/`) — Эксперимент, опыт\n"
            "• **Variable** (`/ˈveəriəbl/`) — Переменная величина\n"
            "• **Independent Variable** (`/ˌɪndɪˈpendənt/`) — Независимая переменная\n"
            "• **Dependent Variable** (`/dɪˈpendənt/`) — Зависимая переменная\n"
            "• **Control Group** (`/kənˈtrəʊl ɡruːp/`) — Контрольная группа\n"
            "• **Quantitative Data** (`/ˈkwɒntɪtətɪv/`) — Количественные данные\n"
            "• **Qualitative Data** (`/ˈkwɒlɪtətɪv/`) — Качественные данные\n"
            "• **Conclusion** (`/kənˈkluːʒn/`) — Вывод, заключение"
        )
    },

    # --- Science 🔬 | Intermediate 🟡 ---
    {
        "category": "Science 🔬",
        "level": "Intermediate 🟡",
        "title": "🧬 Cellular Biology & Modern Genetics (Клеточная биология)",
        "text": (
            "All living organisms, from tiny bacteria to massive blue whales, are composed of basic biological units called **cells**. "
            "Cellular biology focuses on understanding how these microscopic units operate, maintain internal balance, and transmit genetic instructions to future generations.\n\n"
            "### Prokaryotic vs. Eukaryotic Cells\n"
            "Living organisms are divided into two main categories based on their fundamental cellular structure:\n"
            "• **Prokaryotes:** Single-celled organisms like bacteria. They lack a true membrane-bound nucleus, meaning their genetic material floats freely in the cytoplasm.\n"
            "• **Eukaryotes:** Complex organisms including plants, animals, and fungi. Their cells contain a defined nucleus housing DNA, alongside specialized internal structures called **organelles**.\n\n"
            "### Key Cell Organelles and Their Functions\n"
            "Inside a eukaryotic cell, specialized organelles perform specific tasks required for survival:\n"
            "1. **Nucleus:** The control center of the cell that contains **DNA** (deoxyribonucleic acid), the chemical instructions for life.\n"
            "2. **Mitochondria:** Often referred to as the 'powerhouses of the cell.' They generate **ATP** (adenosine triphosphate) through cellular respiration, providing energy for cellular activities.\n"
            "3. **Ribosomes:** Tiny molecular structures that synthesize proteins by reading instructions sent from the nucleus.\n"
            "4. **Endoplasmic Reticulum (ER) & Golgi Apparatus:** Systems that produce, fold, modify, and transport proteins and lipids throughout or outside the cell.\n"
            "5. **Cell Membrane:** A selective phospholipid bilayer that regulates what enters and exits the cell.\n\n"
            "### Genetics: DNA, Genes, and Inheritance\n"
            "Inside the nucleus, long strands of DNA are organized into structures called **chromosomes**. "
            "A **gene** is a specific segment of DNA that contains the code for building a specific protein or determining a trait, such as eye color or blood type.\n\n"
            "Cells reproduce through two primary processes:\n"
            "• **Mitosis:** A type of cell division resulting in two genetically identical daughter cells. Mitosis is responsible for tissue growth, repair, and asexual reproduction.\n"
            "• **Meiosis:** A specialized form of cell division that reduces chromosome numbers by half, producing gametes (sperm and egg cells) for sexual reproduction with unique genetic diversity."
        ),
        "vocab": (
            "🔑 **Intermediate Vocabulary:**\n"
            "• **Organelle** (`/ˌɔːɡəˈnel/`) — Органелла (органоид клетки)\n"
            "• **Prokaryote** (`/prəʊˈkæriəʊt/`) — Прокариот (доядерный организм)\n"
            "• **Eukaryote** (`/juːˈkæriəʊt/`) — Эукариот (ядерный организм)\n"
            "• **Cytoplasm** (`/ˈsaɪtəʊplæzəm/`) — Цитоплазма\n"
            "• **Respiration** (`/ˌrespəˈreɪʃn/`) — Дыхание (клеточное)\n"
            "• **Synthesize** (`/ˈsɪnθəsaɪz/`) — Синтезировать, производить\n"
            "• **Chromosome** (`/ˈkrəʊməsəʊm/`) — Хромосома\n"
            "• **Gene** (`/dʒiːn/`) — Ген\n"
            "• **Mitosis** (`/maɪˈtəʊsɪs/`) — Митоз (деление клеток)\n"
            "• **Meiosis** (`/maɪˈəʊsɪs/`) — Мейоз (редукционное деление)"
        )
    },

    # --- Science 🔬 | Advanced 🔴 ---
    {
        "category": "Science 🔬",
        "level": "Advanced 🔴",
        "title": "⚛️ Quantum Mechanics & Wave-Particle Duality (Квантовая механика)",
        "text": (
            "Classical physics, built largely upon Newton's laws of motion and Maxwell's electrodynamics, successfully explains the behavior of macroscopic objects—from falling apples to orbiting planets. "
            "However, when physicists began investigating subatomic scales at the start of the 20th century, classical principles broke down completely. "
            "This failure led to the development of **Quantum Mechanics**, a revolutionary branch of physics governing subatomic matter and radiation.\n\n"
            "### Wave-Particle Duality\n"
            "One of the cornerstone concepts of quantum mechanics is **wave-particle duality**. "
            "Electromagnetic radiation (like light) and subatomic entities (like electrons) exhibit both wave-like and particle-like properties depending on how they are measured.\n\n"
            "This principle was famously demonstrated by the **Double-Slit Experiment**:\n"
            "• When electrons are fired one by one through two narrow slits onto a detection screen, they do not create two simple strips (as solid marbles would).\n"
            "• Instead, they build up an **interference pattern** of alternating bright and dark bands, characteristic of overlapping waves.\n"
            "• Remarkably, if scientists place a detector at the slits to observe which specific slit each electron passes through, the interference pattern vanishes, and the electrons act purely as discrete particles!\n\n"
            "### The Wave Function and Superposition\n"
            "In quantum mechanics, a physical system is described mathematically by a **wave function** (denoted by the Greek letter Psi, $\\Psi$). "
            "Formulated by Erwin Schrödinger, the wave function calculates the probability distribution of finding a particle in a given position or state.\n\n"
            "According to the **Copenhagen Interpretation**, before a measurement is performed, a quantum entity exists in a state of **superposition**—meaning it occupies all possible states simultaneously. "
            "Upon measurement, the wave function 'collapses' into a single, definite observable state.\n\n"
            "### Heisenberg's Uncertainty Principle\n"
            "Formulated by Werner Heisenberg in 1927, the **Uncertainty Principle** states that it is physically impossible to simultaneously measure both the precise position ($x$) and momentum ($p$) of a quantum particle with absolute accuracy.\n\n"
            "Mathematically expressed as $\\Delta x \\cdot \\Delta p \\ge \\frac{\\hbar}{2}$, this limitation is not caused by faulty measuring instruments; rather, it is a fundamental property of wave-like quantum nature itself. "
            "The more precisely you determine a particle's location, the less precisely you can know its velocity, and vice versa.\n\n"
            "### Quantum Entanglement\n"
            "When two particles interact closely, they can become **entangled**. "
            "In an entangled system, the quantum state of each particle cannot be described independently of the other. "
            "Measuring the spin or polarization of one particle instantly determines the state of the other entangled particle, regardless of whether they are separated by centimeters or light-years. "
            "Albert Einstein famously referred to this phenomenon as 'spooky action at a distance', yet modern experiments consistently confirm its validity, paving the way for quantum computing and modern cryptography."
        ),
        "vocab": (
            "🔑 **Advanced Vocabulary:**\n"
            "• **Macroscopic** (`/ˌmækrəˈskɒpɪk/`) — Макроскопический (видимый глазом)\n"
            "• **Subatomic** (`/ˌsʌbəˈtɒmɪk/`) — Субатомный\n"
            "• **Wave-particle duality** — Корпускулярно-волновой дуализм\n"
            "• **Interference Pattern** (`/ˌɪntəˈfɪərəns/`) — Интерференционная картина\n"
            "• **Wave Function** (`/weɪv ˈfʌŋkʃn/`) — Волновая функция\n"
            "• **Superposition** (`/ˌsuːpərəpəˈzɪʃn/`) — Суперпозиция (сочетание состояний)\n"
            "• **Collapse** (`/kəˈlæps/`) — Коллапс, схлопывание (волновой функции)\n"
            "• **Momentum** (`/məˈmentəm/`) — Импульс, количество движения\n"
            "• **Uncertainty Principle** (`/ʌnˈsɜːtnti/`) — Принцип неопределенности\n"
            "• **Quantum Entanglement** (`/ɪnˈtæŋɡlmənt/`) — Квантовая запутанность"
        )
    },
# =========================================================================
    # 💻 TECHNOLOGY (ТЕХНОЛОГИИ И ИТ — ДЕТАЛЬНЫЕ ЛЕКЦИИ)
    # =========================================================================

    # --- Technology 💻 | Beginner 🟢 ---
    {
        "category": "Technology 💻",
        "level": "Beginner 🟢",
        "title": "🤖 What is an Algorithm and How Computers Process Data (Алгоритмы и компьютеры)",
        "text": (
            "At the core of every modern computer, smartphone, and digital application lies a fundamental concept: the **algorithm**. "
            "Without algorithms, electronic devices would be nothing more than expensive pieces of silicon and plastic. "
            "Understanding how algorithms work is the very first step into the world of computer science and technology.\n\n"
            "### What is an Algorithm?\n"
            "An **algorithm** is simply a finite, step-by-step set of instructions designed to solve a specific problem or perform a particular task. "
            "Think of it like a recipe for baking a cake: you start with raw ingredients (**input**), follow a strict sequence of mixing and baking steps (**processing**), and end up with a finished cake (**output**).\n\n"
            "If you skip a step, mix ingredients in the wrong order, or use spoiled components, the recipe fails. "
            "Computers operate on the exact same logic. They cannot 'think' creatively on their own; instead, they execute human-written algorithms with absolute, relentless precision.\n\n"
            "### The Core Components of Computing\n"
            "To understand how a computer runs an algorithm, we look at three fundamental stages:\n"
            "1. **Input:** The raw data provided to the system (e.g., typing text on a keyboard, tapping a smartphone screen, or uploading a photo).\n"
            "2. **Processing:** The internal calculations and logic performed by the computer's central processor (**CPU**), transforming the input based on the programmed algorithm.\n"
            "3. **Output:** The final result presented to the user (e.g., displaying text on a monitor, playing sound through headphones, or saving a file to storage).\n\n"
            "### Hardware vs. Software\n"
            "Computers are divided into two essential domains:\n"
            "• **Hardware:** The physical, tangible components of a computer system that you can actually touch—such as the processor, memory sticks, hard drives, motherboard, screen, and keyboard.\n"
            "• **Software:** The intangible set of instructions, operating systems, and applications (like web browsers, video games, or mobile apps) that tell the hardware what to do.\n\n"
            "### Why Logic Matters: Debugging\n"
            "Because computers follow instructions literally, even a tiny mistake in an algorithm causes errors. "
            "Finding and fixing these errors is known as **debugging**. "
            "Learning to write clear, logical, and error-free algorithms builds the problem-solving mindset required for all software development."
        ),
        "vocab": (
            "🔑 **Vocabulary for Beginners:**\n"
            "• **Algorithm** (`/ˈælɡərɪðəm/`) — Алгоритм\n"
            "• **Input** (`/ˈɪnpʊt/`) — Входные данные, ввод\n"
            "• **Output** (`/ˈaʊtpʊt/`) — Выходные данные, вывод\n"
            "• **Processing** (`/ˈprəʊsesɪŋ/`) — Обработка\n"
            "• **Hardware** (`/ˈhɑːdweə/`) — Аппаратное обеспечение («железо»)\n"
            "• **Software** (`/ˈsɒftweə/`) — Программное обеспечение (ПО)\n"
            "• **Processor / CPU** (`/ˈprəʊsesə/`) — Центральный процессор\n"
            "• **Instruction** (`/ɪnˈstrʌkʃn/`) — Инструкция, команда\n"
            "• **Debugging** (`/diːˈbʌɡɪŋ/`) — Отладка (поиск и исправление ошибок)\n"
            "• **Application** (`/ˌæplɪˈkeɪʃn/`) — Приложение, программа"
        )
    },

    # --- Technology 💻 | Intermediate 🟡 ---
    {
        "category": "Technology 💻",
        "level": "Intermediate 🟡",
        "title": "🧠 Artificial Neural Networks & Machine Learning (Искусственный интеллект)",
        "text": (
            "Traditional computer programming relies on explicit instructions: programmers write exact rules telling the computer how to solve a problem (e.g., 'If user clicks X, close window'). "
            "However, tasks like recognizing human faces, translating languages, or driving autonomous cars cannot be easily broken down into rigid rules. "
            "This is where **Machine Learning (ML)** and **Artificial Neural Networks (ANNs)** revolutionize technology.\n\n"
            "### What is Machine Learning?\n"
            "Instead of manually writing rules, machine learning algorithms use massive amounts of **training data** to allow computers to learn patterns automatically. "
            "By analyzing thousands of examples, the system builds a statistical model capable of making accurate predictions or decisions on brand-new, unseen data.\n\n"
            "### Anatomy of an Artificial Neural Network\n"
            "Inspired by the biological human brain, an Artificial Neural Network consists of thousands or millions of interconnected artificial 'neurons' (or nodes) organized into distinct layers:\n"
            "1. **Input Layer:** Receives raw data features (such as pixel values from an image or audio frequencies from speech).\n"
            "2. **Hidden Layers:** Intermediate layers where complex mathematical transformations, feature extraction, and pattern recognition take place.\n"
            "3. **Output Layer:** Produces the final prediction or classification (e.g., identifying whether an image contains a cat, a dog, or a car).\n\n"
            "### Weights, Biases, and Training\n"
            "Each connection between neurons has a numerical value called a **weight**, which determines the strength or importance of that signal. "
            "During the training phase, the network passes data forward (**forward propagation**), compares its prediction to the correct answer, calculates the error, and adjusts its weights backward (**backpropagation**). "
            "Over millions of iterations, the network optimizes its weights to minimize errors, effectively 'learning' how to perform the task.\n\n"
            "### Challenges: Overfitting\n"
            "A major challenge in machine learning is **overfitting**, which occurs when a model memorizes the training data too perfectly—including noise and random quirks—failing to generalize when presented with new real-world data."
        ),
        "vocab": (
            "🔑 **Intermediate Vocabulary:**\n"
            "• **Machine Learning** (`/məˈʃiːn ˈlɜːnɪŋ/`) — Машинное обучение\n"
            "• **Artificial Neural Network** (`/ˌɑːtɪˈfɪʃl ˈnʊərəl ˈnetwɜːk/`) — Искусственная нейросеть\n"
            "• **Neuron / Node** (`/ˈnʊərɒn/`) — Нейрон, узел\n"
            "• **Hidden Layer** (`/ˈhɪdn ˈleɪə/`) — Скрытый слой\n"
            "• **Training Data** (`/ˈtreɪnɪŋ ˈdeɪtə/`) — Обучающие данные\n"
            "• **Weight** (`/weɪt/`) — Весовой коэффициент (вес)\n"
            "• **Backpropagation** (`/ˌbækprɒpəˈɡeɪʃn/`) — Обратное распространение ошибки\n"
            "• **Prediction** (`/prɪˈdɪkʃn/`) — Предсказание, прогноз\n"
            "• **Overfitting** (`/ˌəʊvəˈfɪtɪŋ/`) — Переобучение\n"
            "• **Generalize** (`/ˈdʒenərəlaɪz/`) — Обобщать"
        )
    },

    # --- Technology 💻 | Advanced 🔴 ---
    {
        "category": "Technology 💻",
        "level": "Advanced 🔴",
        "title": "🌐 Microservices Architecture vs. Monolithic Systems (Микросервисы)",
        "text": (
            "When designing large-scale enterprise software applications that serve millions of concurrent users, software architects face crucial decisions regarding structural design. "
            "The choice of system architecture dictates how code is organized, deployed, scaled, and maintained over years of development.\n\n"
            "### Monolithic Architecture\n"
            "Traditionally, applications were built as **monoliths**. In a monolithic architecture, the entire application—user interface logic, business rules, database access layers, and background workers—is bundled into a single unified codebase and deployed as one massive executable file.\n\n"
            "• **Advantages:** Simple initial setup, straightforward debugging during early development, and easy transactional consistency because all modules share the same database and memory space.\n"
            "• **Disadvantages:** As the product grows, the codebase becomes bloated and difficult to navigate ('spaghetti code'). If a single minor bug causes a memory leak or crash, the entire application goes down. Furthermore, scaling requires duplicating the entire heavy application rather than specific resource-heavy features.\n\n"
            "### Microservices Architecture\n"
            "To overcome the limitations of monoliths, modern distributed systems employ **Microservices Architecture**. "
            "In this model, an application is broken down into a suite of small, independent, autonomous services. Each microservice focuses on a single business capability (e.g., user authentication, payment processing, notification delivery) and runs in its own process.\n\n"
            "Key characteristics of microservices include:\n"
            "• **Decentralized Data Management:** Each microservice typically maintains its own private database, eliminating tight coupling across teams.\n"
            "• **Independent Scalability:** If the payment service experiences massive traffic spikes during a sale, engineers can scale up just that specific service without duplicating the entire app.\n"
            "• **Inter-Process Communication (IPC):** Services communicate with each other over a network using lightweight protocols such as REST APIs, GraphQL, or high-performance gRPC.\n\n"
            "### Challenges of Distributed Systems\n"
            "While microservices offer exceptional agility and fault isolation, they introduce significant complexity: network latency, distributed transactions (handling failures across multiple databases), complex deployment pipelines, and rigorous service monitoring requirements."
        ),
        "vocab": (
            "🔑 **Advanced Vocabulary:**\n"
            "• **Monolithic Architecture** (`/ˌmɒnəˈlɪθɪk ˈɑːkɪtektʃə/`) — Монолитная архитектура\n"
            "• **Microservices** (`/ˌmaɪkrəʊˈsɜːvɪsɪz/`) — Микросервисы\n"
            "• **Scalability** (`/ˌskeɪləˈbɪləti/`) — Масштабируемость\n"
            "• **Decoupling** (`/diːˈkʌplɪŋ/`) — Депликация, разъединение связей\n"
            "• **Distributed System** (`/dɪˈstrɪbɪtɪd ˈsɪstəm/`) — Распределенная система\n"
            "• **Concurrent Users** (`/kənˈkʌrənt ˈjuːzəz/`) — Одновременные пользователи\n"
            "• **Fault Isolation** (`/fɔːlt ˌaɪsəˈleɪʃn/`) — Изоляция сбоев\n"
            "• **Latency** (`/ˈleɪtənsi/`) — Задержка сети\n"
            "• **Deployment** (`/dɪˈplɔɪmənt/`) — Развертывание, деплой\n"
            "• **API Gateway** (`/ˌeɪ piː aɪ ˈɡeɪtwei/`) — Шлюз API"
        )
    },
# =========================================================================
    # ⚙️ ENGINEERING (ИНЖЕНЕРИЯ И МЕХАНИКА — ДЕТАЛЬНЫЕ ЛЕКЦИИ)
    # =========================================================================

    # --- Engineering ⚙️ | Beginner 🟢 ---
    {
        "category": "Engineering ⚙️",
        "level": "Beginner 🟢",
        "title": "⚖️ Levers and Simple Machines (Рычаги и простые механизмы)",
        "text": (
            "Since ancient times, human engineering has relied on **simple machines**—basic mechanical devices that change the direction or magnitude of a force. "
            "Among these, the **lever** is one of the most powerful and intuitive tools ever conceived.\n\n"
            "### What is a Lever?\n"
            "A lever is simply a rigid bar that pivots around a fixed point known as the **fulcrum**. "
            "When you apply a force (called the **effort**) at one point on the bar, the lever rotates around the fulcrum and exerts a different force (called the **load**) at another point.\n\n"
            "By adjusting the position of the fulcrum relative to the effort and the load, engineers can achieve **mechanical advantage**—meaning you can lift heavy objects using very little muscle power.\n\n"
            "### The Three Classes of Levers\n"
            "Depending on where the fulcrum, effort, and load are positioned, levers are divided into three classes:\n"
            "• **First-Class Levers:** The fulcrum is located in the middle, between the effort and the load. Examples include a seesaw, crowbar, and a pair of scissors.\n"
            "• **Second-Class Levers:** The load is located in the middle, between the fulcrum and the effort. Examples include a wheelbarrow, a nutcracker, and a bottle opener. The effort force is always smaller than the load.\n"
            "• **Third-Class Levers:** The effort is applied in the middle, between the fulcrum and the load. Examples include tweezers, a broom, and human arm movements. While they don't multiply force, they significantly increase speed and range of motion.\n\n"
            "### Everyday Impact\n"
            "Simple machines like levers, pulleys, and inclined planes form the foundational building blocks of all complex machinery—from bicycle gears and construction cranes to automotive steering systems."
        ),
        "vocab": (
            "🔑 **Vocabulary for Beginners:**\n"
            "• **Lever** (`/ˈliːvə/`) — Рычаг\n"
            "• **Fulcrum** (`/ˈfʊlkrəm/`) — Точка опоры (фукр)\n"
            "• **Simple Machine** (`/ˈsɪmpl məˈshiːn/`) — Простой механизм\n"
            "• **Mechanical Advantage** (`/mɪˈkænɪkl ədˈvɑːntɪdʒ/`) — Механическое преимущество\n"
            "• **Effort** (`/ˈefət/`) — Усилие, прикладываемая сила\n"
            "• **Load** (`/ləʊd/`) — Нагрузка, поднимаемый груз\n"
            "• **Rigid bar** (`/ˈrɪdʒɪd bɑː/`) — Жесткий стержень\n"
            "• **Pivot** (`/ˈpɪvət/`) — Вращаться вокруг точки\n"
            "• **Wheelbarrow** (`/ˈwiːlbærəʊ/`) — Тачка (строительная или садовая)\n"
            "• **Crowbar** (`/ˈkrəʊbɑː/`) — Лом, монтировка"
        )
    },

    # --- Engineering ⚙️ | Intermediate 🟡 ---
    {
        "category": "Engineering ⚙️",
        "level": "Intermediate 🟡",
        "title": "🏎️ Aerodynamics and Drag Force (Аэродинамика и сопротивление воздуха)",
        "text": (
            "When vehicles, aircraft, or high-speed trains travel through the atmosphere, they constantly push against surrounding air molecules. "
            "**Aerodynamics** is the branch of fluid mechanics that studies how gases (specifically air) interact with moving solid bodies.\n\n"
            "### Drag Force and Resistance\n"
            "As an object moves forward, it experiences an opposing aerodynamic resistance known as **drag force**. "
            "Drag is caused by two primary factors:\n"
            "1. **Form Drag (Pressure Drag):** Caused by the shape of the object. A blunt, flat surface pushes air apart violently, creating a high-pressure zone in front and a low-pressure suction wake behind the object, which pulls it backward.\n"
            "2. **Skin Friction:** Caused by the friction of air molecules sliding directly along the smooth surface of the moving object.\n\n"
            "### Streamlining and the Drag Coefficient\n"
            "To minimize drag, engineers design vehicles with **streamlined** shapes—curved, teardrop-like profiles that allow air to flow smoothly around the body without breaking into turbulent vortices.\n\n"
            "The efficiency of an object's shape is measured by its **drag coefficient ($C_d$)**. "
            "A brick has a very high drag coefficient (around 2.1), meaning it wastes massive amounts of energy pushing air. "
            "In contrast, modern hypercars and commercial airplanes feature sleek designs with drag coefficients as low as 0.2, drastically reducing fuel consumption and increasing top speed.\n\n"
            "### Lift and Downforce\n"
            "In addition to drag, airflow over engineered surfaces generates **lift** (the upward force that keeps airplanes in the air) or **downforce** (the downward aerodynamic push used in racing cars to press tires against the track for superior cornering grip)."
        ),
        "vocab": (
            "🔑 **Intermediate Vocabulary:**\n"
            "• **Aerodynamics** (`/ˌeərəʊdaɪˈnæmɪks/`) — Аэродинамика\n"
            "• **Drag Force** (`/dræɡ fɔːs/`) — Сила лобового сопротивления\n"
            "• **Streamlined** (`/ˈstriːmlaɪnd/`) — Обтекаемый\n"
            "• **Drag Coefficient** (`/ˌkəʊɪˈfɪʃnt/`) — Коэффициент сопротивления\n"
            "• **Turbulent** (`/ˈtɜːbjʊlənt/`) — Турбулентный, вихревой\n"
            "• **Wake** (`/weɪk/`) — Спутный след (турбулентный поток позади тела)\n"
            "• **Friction** (`/ˈfrɪkʃn/`) — Трение\n"
            "• **Lift** (`/lɪft/`) — Подъемная сила\n"
            "• **Downforce** (`/ˈdaʊnfɔːs/`) — Прижимная сила\n"
            "• **Consumption** (`/kənˈsʌmpʃn/`) — Потребление, расход"
        )
    },

    # --- Engineering ⚙️ | Advanced 🔴 ---
    {
        "category": "Engineering ⚙️",
        "level": "Advanced 🔴",
        "title": "🔥 Thermodynamics and the Carnot Cycle (Термодинамика: Цикл Карно)",
        "text": (
            "Thermodynamics is the branch of physics and engineering that deals with heat, work, temperature, and their relation to energy and radiation. "
            "In mechanical and power engineering, understanding thermodynamic cycles is vital for designing high-efficiency engines, power plants, and refrigeration systems.\n\n"
            "### The Laws of Thermodynamics\n"
            "Engineering systems are bound by absolute physical laws:\n"
            "• **First Law (Conservation of Energy):** Energy cannot be created or destroyed, only transformed from one form to another (e.g., chemical energy in fuel turning into mechanical motion).\n"
            "• **Second Law (Entropy):** Thermal energy naturally flows from hot objects to cold objects. Furthermore, every energy conversion loses some useful energy as waste heat, meaning no real-world engine can ever be 100% efficient.\n\n"
            "### The Carnot Cycle: The Ideal Engine\n"
            "In 1824, French physicist Sadi Carnot conceptualized an idealized thermodynamic cycle called the **Carnot Cycle**. "
            "The Carnot cycle establishes the absolute maximum theoretical efficiency any heat engine can achieve operating between two specific temperature reservoirs ($T_{hot}$ and $T_{cold}$).\n\n"
            "The cycle consists of four reversible sequential processes:\n"
            "1. **Isothermal Expansion:** The working gas absorbs heat from a high-temperature reservoir while maintaining a constant temperature, expanding and doing work.\n"
            "2. **Adiabatic Expansion:** The gas continues to expand without exchanging heat with the environment, causing its temperature to drop.\n"
            "3. **Isothermal Compression:** The gas is compressed while releasing heat to a low-temperature cold reservoir at constant temperature.\n"
            "4. **Adiabatic Compression:** The gas undergoes final compression without heat exchange, returning its pressure, volume, and temperature to their exact initial states.\n\n"
            "### Engineering Significance\n"
            "No real engine can match the Carnot efficiency because real-world processes involve friction, turbulence, and thermal losses. "
            "However, the Carnot cycle serves as the ultimate golden benchmark against which mechanical engineers measure the performance of modern gas turbines, steam engines, and internal combustion motors."
        ),
        "vocab": (
            "🔑 **Advanced Vocabulary:**\n"
            "• **Thermodynamics** (`/ˌθɜːməʊdaɪˈnæmɪks/`) — Термодинамика\n"
            "• **Entropy** (`/ˈentrəpi/`) — Энтропия (мера беспорядка/потерь)\n"
            "• **Carnot Cycle** (`/kɑːˈnəʊ ˈsaɪkl/`) — Цикл Карно\n"
            "• **Thermal Efficiency** (`/ˈθɜːml ɪˈfɪʃnsi/`) — Тепловой КПД\n"
            "• **Isothermal** (`/ˌaɪsəʊˈθɜːml/`) — Изотермический (при постоянной температуре)\n"
            "• **Adiabatic** (`/ˌeɪdiəˈbætɪk/`) — Адиабатический (без теплообмена с внешней средой)\n"
            "• **Reservoir** (`/ˈrezəvwɑː/`) — Резервуар, источник тепла\n"
            "• **Reversible** (`/rɪˈvɜːsəbl/`) — Обратимый\n"
            "• **Combustion** (`/kəmˈbʌstʃn/`) — Горение, сгорание\n"
            "• **Benchmark** (`/ˈbentʃmɑːk/`) — Эталон, ориентир для сравнения"
        )
    },
# =========================================================================
    # 📐 MATHEMATICS (МАТЕМАТИКА — ДЕТАЛЬНЫЕ ЛЕКЦИИ)
    # =========================================================================

    # --- Mathematics 📐 | Beginner 🟢 ---
    {
        "category": "Mathematics 📐",
        "level": "Beginner 🟢",
        "title": "🔢 Variables and Algebraic Equations (Переменные и уравнения)",
        "text": (
            "Arithmetic deals with known numbers and basic operations (addition, subtraction, multiplication, division). "
            "However, when mathematicians need to solve problems involving unknown quantities that can change or vary, they step into **algebra**. "
            "Algebra is the foundational language of higher mathematics, computer science, and engineering.\n\n"
            "### What is a Variable?\n"
            "In algebra, a **variable** is a symbol—usually an English letter like `x`, `y`, or `n`—that represents an unknown or changeable number. "
            "Think of a variable as an empty box or a placeholder. Depending on the rules of the problem, you can put different numbers inside the box.\n\n"
            "### Understanding Equations\n"
            "An **equation** is a mathematical statement showing that two expressions are equal, joined by an equals sign (`=`). "
            "For example, consider the simple linear equation:\n\n"
            "`x + 3 = 7`\n\n"
            "Here, the goal is to **solve for x**—meaning you must find the exact numerical value that makes the statement true. "
            "To isolate `x`, you perform inverse operations: subtract `3` from both sides of the equation. "
            "This gives `x = 7 - 3`, which simplifies to `x = 4`.\n\n"
            "### Why Variables Matter\n"
            "Variables allow us to write universal formulas that work for any situation. "
            "For instance, the formula for the perimeter of a square is `P = 4s`, where `s` represents the length of any side. "
            "Whether a square has sides of 2 cm or 100 meters, the same algebraic formula instantly gives the correct answer."
        ),
        "vocab": (
            "🔑 **Vocabulary for Beginners:**\n"
            "• **Algebra** (`/ˈældʒɪbrə/`) — Алгебра\n"
            "• **Variable** (`/ˈveəriəbl/`) — Переменная\n"
            "• **Equation** (`/ɪˈkweɪʒn/`) — Уравнение\n"
            "• **Expression** (`/ɪkˈspreʃn/`) — Математическое выражение\n"
            "• **Unknown** (`/ˌʌnˈnəʊn/`) — Неизвестная величина\n"
            "• **Isolate** (`/ˈaɪsəleɪt/`) — Изолировать (выразить переменную)\n"
            "• **Inverse Operation** (`/ɪnˈvɜːs ˌɒpəˈreɪʃn/`) — Обратная операция\n"
            "• **Perimeter** (`/pəˈrɪmɪtə/`) — Периметр\n"
            "• **Formula** (`/ˈfɔːmjʊlə/`) — Формула\n"
            "• **Simplify** (`/ˈsɪmplɪfaɪ/`) — Упрощать"
        )
    },

   # =========================================================================
    # 📐 MATHEMATICS (МАТЕМАТИКА — ДЕТАЛЬНЫЕ ЛЕКЦИИ)
    # =========================================================================

    # --- Mathematics 📐 | Beginner 🟢 ---
    {
        "category": "Mathematics 📐",
        "level": "Beginner 🟢",
        "title": "🔢 Variables and Algebraic Equations (Переменные и уравнения)",
        "text": (
            "Arithmetic deals with known numbers and basic operations (addition, subtraction, multiplication, division). "
            "However, when mathematicians need to solve problems involving unknown quantities that can change or vary, they step into **algebra**. "
            "Algebra is the foundational language of higher mathematics, computer science, and engineering.\n\n"
            "### What is a Variable?\n"
            "In algebra, a **variable** is a symbol—usually an English letter like `x`, `y`, or `n`—that represents an unknown or changeable number. "
            "Think of a variable as an empty box or a placeholder. Depending on the rules of the problem, you can put different numbers inside the box.\n\n"
            "### Understanding Equations\n"
            "An **equation** is a mathematical statement showing that two expressions are equal, joined by an equals sign (`=`). "
            "For example, consider the simple linear equation:\n\n"
            "`x + 3 = 7`\n\n"
            "Here, the goal is to **solve for x**—meaning you must find the exact numerical value that makes the statement true. "
            "To isolate `x`, you perform inverse operations: subtract `3` from both sides of the equation. "
            "This gives `x = 7 - 3`, which simplifies to `x = 4`.\n\n"
            "### Why Variables Matter\n"
            "Variables allow us to write universal formulas that work for any situation. "
            "For instance, the formula for the perimeter of a square is `P = 4s`, where `s` represents the length of any side. "
            "Whether a square has sides of 2 cm or 100 meters, the same algebraic formula instantly gives the correct answer."
        ),
        "vocab": (
            "🔑 **Vocabulary for Beginners:**\n"
            "• **Algebra** (`/ˈældʒɪbrə/`) — Алгебра\n"
            "• **Variable** (`/ˈveəriəbl/`) — Переменная\n"
            "• **Equation** (`/ɪˈkweɪʒn/`) — Уравнение\n"
            "• **Expression** (`/ɪkˈspreʃn/`) — Математическое выражение\n"
            "• **Unknown** (`/ˌʌnˈnəʊn/`) — Неизвестная величина\n"
            "• **Isolate** (`/ˈaɪsəleɪt/`) — Изолировать (выразить переменную)\n"
            "• **Inverse Operation** (`/ɪnˈvɜːs ˌɒpəˈreɪʃn/`) — Обратная операция\n"
            "• **Perimeter** (`/pəˈrɪmɪtə/`) — Периметр\n"
            "• **Formula** (`/ˈfɔːmjʊlə/`) — Формула\n"
            "• **Simplify** (`/ˈsɪmplɪfaɪ/`) — Упрощать"
        )
    },

    # --- Mathematics 📐 | Intermediate 🟡 ---
    {
        "category": "Mathematics 📐",
        "level": "Intermediate 🟡",
        "title": "🎲 Probability and Event Outcomes (Теория вероятностей)",
        "text": (
            "In daily life, we constantly encounter uncertainty: Will it rain tomorrow? Will my investment grow? Will I roll a winning number in a game? "
            "**Probability** is the mathematical branch that measures the likelihood that a specific event will occur.\n\n"
            "### The Scale of Probability\n"
            "Probability values are always expressed as a real number between `0` and `1` (or as a percentage from `0%` to `100%`):\n"
            "• A probability of **`0`** means the event is completely **impossible**.\n"
            "• A probability of **`1`** means the event is absolute **certainty**.\n"
            "• A probability of **`0.5` (or 50%)** means an event has an equal chance of happening or not happening (like tossing a fair coin).\n\n"
            "### Calculating Basic Probability\n"
            "The fundamental formula for calculating the probability $P(E)$ of a simple event $E$ is:\n\n"
            "$P(E) = \\frac{\\text{Number of favorable outcomes}}{\\text{Total number of possible outcomes}}$\n\n"
            "For example, consider rolling a standard 6-sided die. The total number of possible outcomes is 6 (numbers 1 through 6). "
            "If you want to calculate the probability of rolling an even number (2, 4, or 6), there are 3 favorable outcomes. "
            "Therefore, $P(\\text{even}) = \\frac{3}{6} = \\frac{1}{2}$ (or 50%).\n\n"
            "### Independent and Dependent Events\n"
            "In statistics, events can be **independent** (the outcome of the first event does not affect the second, like flipping a coin twice) or **dependent** (where the first event alters the odds of the next, such as drawing cards from a deck without putting them back)."
        ),
        "vocab": (
            "🔑 **Intermediate Vocabulary:**\n"
            "• **Probability** (`/ˌprɒbəˈbɪləti/`) — Вероятность\n"
            "• **Likelihood** (`/ˈlaɪklihʊd/`) — Вероятность, шанс\n"
            "• **Favorable Outcome** (`/ˈfeɪvərəbl ˈaʊtkʌm/`) — Благоприятный исход\n"
            "• **Certainty** (`/ˈsɜːtnti/`) — Достоверность, определенность\n"
            "• **Coin Toss** (`/kɔɪn tɒs/`) — Подбрасывание монеты\n"
            "• **Independent Event** (`/ˌɪndɪˈpendənt ɪˈvent/`) — Независимое событие\n"
            "• **Dependent Event** (`/dɪˈpendənt ɪˈvent/`) — Зависимое событие\n"
            "• **Random Variable** (`/ˈrændəm ˈveəriəbl/`) — Случайная величина\n"
            "• **Odds** (`/ɒdz/`) — Шансы, соотношение вероятностей\n"
            "• **Statistics** (`/stəˈtɪstɪks/`) — Статистика"
        )
    },

    # --- Mathematics 📐 | Advanced 🔴 ---
    {
        "category": "Mathematics 📐",
        "level": "Advanced 🔴",
        "title": "📈 The Fundamental Theorem of Calculus (Математический анализ)",
        "text": (
            "Calculus is the mathematical study of continuous change, developed independently by Isaac Newton and Gottfried Wilhelm Leibniz in the 17th century. "
            "While algebra deals with static equations, calculus unlocks the dynamics of motion, growth, and optimization. "
            "At the heart of calculus lies the **Fundamental Theorem of Calculus**, which bridges its two major branches.\n\n"
            "### The Two Pillars of Calculus\n"
            "Before calculus, math treated geometry and rates of change as separate worlds. Calculus unites them through two primary operations:\n"
            "1. **Differential Calculus (Differentiation):** Focuses on the concept of the derivative, which measures the **instantaneous rate of change** (e.g., finding the exact speed of a car at a specific microsecond, or the slope of a curved line at any point).\n"
            "2. **Integral Calculus (Integration):** Focuses on the concept of the integral, which calculates the **accumulated total** (e.g., finding the exact area underneath a complex curved graph or total distance traveled over time).\n\n"
            "### The Core Bridge: The Fundamental Theorem\n"
            "For centuries, calculating the area under curves required tedious geometric approximations. "
            "The **Fundamental Theorem of Calculus** revealed a stunning mathematical reality: **differentiation and integration are inverse operations** of one another—much like multiplication and division, or squaring and taking a square root.\n\n"
            "The theorem states that if you take a function, integrate it to find its accumulated area, and then differentiate that result, you get your original function back.\n\n"
            "### Real-World Applications\n"
            "This theorem allows engineers and physicists to bypass impossible geometric calculations. By finding an **antiderivative**, they can instantly compute complex physical phenomena—such as rocket trajectories escaping Earth's gravity, alternating electrical currents in microchips, or predicting financial market fluctuations."
        ),
        "vocab": (
            "🔑 **Advanced Vocabulary:**\n"
            "• **Calculus** (`/ˈkælkjʊləs/`) — Математический анализ (исчисление)\n"
            "• **Derivative** (`/dɪˈrɪvətɪv/`) — Производная\n"
            "• **Integral** (`/ˈɪntɪɡrəl/`) — Интеграл\n"
            "• **Differentiation** (`/ˌdɪfəˌrenʃiˈeɪʃn/`) — Дифференцирование\n"
            "• **Integration** (`/ˌɪntɪˈɡreɪʃn/`) — Интегрирование\n"
            "• **Instantaneous Rate** (`/ˌɪnstənˈteɪniəs reɪt/`) — Мгновенная скорость изменения\n"
            "• **Accumulation** (`/əˌkjuːmjʊˈleɪʃn/`) — Накопление, суммирование\n"
            "• **Antiderivative** (`/ˌænti-dɪˈrɪvətɪv/`) — Первообразная\n"
            "• **Trajectory** (`/trəˈdʒektəri/`) — Траектория\n"
            "• **Inverse Operation** (`/ɪnˈvɜːs ˌɒpəˈreɪʃn/`) — Обратная операция"
        )
    }
]