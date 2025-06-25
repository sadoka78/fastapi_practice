# **МАҢЫЗДЫ: СТУДЕНТТЕРГЕ АРНАЛҒАН ТАПСЫРМАЛАР!**

Дағдыларды бекітуге арналған практикалық тапсырмалар. Қателерден қорықпа, бұл оқу процесінің бір бөлігі!

---

# **Жоба 2/10: Минималистік Блог**

Бұл сериядағы екінші жоба, Next.js-ті фронтенд үшін және FastAPI-ді бэкенд үшін пайдалана отырып, қарапайым блог жасауды көрсетеді. Бұл жобаның басты ерекшелігі — жеке жазбаларды көрсету үшін Next.js-тегі динамикалық маршруттау.

---

**🚀 Технологиялар**

* **Фронтенд**: Next.js (React, TypeScript, Tailwind CSS)
* **Бэкенд**: FastAPI (Python)
* **Негізгі концепция**: Динамикалық маршруттар pages/posts/[slug]

**✨ Функционал**

* Барлық посттар тізімі бар басты бет.
* Әр постқа арналған жеке беттер, динамикалық түрде генерацияланады.
* Бэкенд екі эндпоинтты ұсынады: посттар тізімін алу үшін және бір постты алу үшін.

# **Сенің міндетің:**

## Бұл блогтың функционалдығын кеңейт.

# **Сенің тапсырмаң:**

# 1. **Клондау және іске қосу:**
> * ## Бұл жобаны жергілікті машинаңа клонда.
> * ## Фронтенд пен бэкендті іске қос.

# 2. **Автор мен күнді посттарға қосу:**
> * ## **Бэкенд**: `main.py` файлына `author` (str) және `date` (str) өрістерін `PostFull` моделіне және `fake_posts_db` "дерекқорына" қос.
> * ## **Фронтенд**: Басты бетте тақырыптың астына және пост бетінде автор мен күнді көрсет.

# 3. **Санаттарды жасау:**
> * ## **Бэкенд**: Пост моделіне `category` (str) өрісін қос.
> * ## **Фронтенд**: Басты бетте посттарды санаттар бойынша топтастыр немесе олар бойынша сүзу мүмкіндігін қос.

# 4. **(Күрделі) Markdown-рендер:**
> * ## Посттардағы `content` өрісін жарамды Markdown-ға өзгерт.
> * ## Фронтендте `dangerouslySetInnerHTML` орнына контентті әдемі рендерлеу үшін кітапхананы (мысалы, `react-markdown`) пайдалан.

---

# **IMPORTANT: TASKS FOR STUDENTS!**

These are practical assignments to consolidate your skills. Don't be afraid of mistakes; they are part of the learning process!

---

# **Project 2/10: Minimalist Blog**

This is the second project in the series, demonstrating the creation of a simple blog using Next.js for the frontend and FastAPI for the backend. A key feature of this project is dynamic routing in Next.js for displaying individual posts.

---

**🚀 Technologies**

* **Frontend**: Next.js (React, TypeScript, Tailwind CSS)
* **Backend**: FastAPI (Python)
* **Key Concept**: Dynamic routes pages/posts/[slug]

**✨ Functionality**

* Home page with a list of all posts.
* Separate pages for each post, dynamically generated.
* The backend provides two endpoints: one for getting a list of posts and one for getting a single post.

# **Your Task:**

## Extend the functionality of this blog.

# **Your Mission:**

# 1. **Clone & Run:**
> * ## Clone this project to your local machine.
> * ## Run both the frontend and the backend.

# 2. **Add Author and Date to Posts:**
> * ## **Backend**: In `main.py`, add `author` (str) and `date` (str) fields to the `PostFull` model and to the `fake_posts_db` "database".
> * ## **Frontend**: Display the author and date on the homepage below the title and on the post's individual page.

# 3. **Create Categories:**
> * ## **Backend**: Add a `category` (str) field to the post model.
> * ## **Frontend**: On the homepage, group posts by categories or add the ability to filter by them.

# 4. **(Advanced) Markdown Renderer:**
> * ## Change the `content` field in posts to valid Markdown.
> * ## On the frontend, use a library (e.g., `react-markdown`) to beautifully render the content instead of using `dangerouslySetInnerHTML`.

---

# **ВАЖНО: ЗАДАЧИ ДЛЯ СТУДЕНТОВ!**

Перед тобой практические задания для закрепления навыков. Не бойся ошибок, это часть обучения!

---

# **Проект 2/10: Минималистичный Блог**

Это второй проект из серии, демонстрирующий создание простого блога с использованием Next.js для фронтенда и FastAPI для бэкенда. Ключевая особенность этого проекта — динамическая маршрутизация в Next.js для отображения отдельных записей.

---

**🚀 Технологии**

* **Фронтенд**: Next.js (React, TypeScript, Tailwind CSS)
* **Бэкенд**: FastAPI (Python)
* **Ключевая концепция**: Динамические маршруты pages/posts/[slug]

**✨ Функционал**

* Главная страница со списком всех постов.
* Отдельные страницы для каждого поста, генерируемые динамически.
* Бэкенд предоставляет два эндпоинта: для получения списка постов и для получения одного поста.

# **Твоя задача:**

## Расширь функционал этого блога.

# **Твоя миссия:**

# 1. **Клонирование и запуск:**
> * ## Клонируй этот проект на свою локальную машину.
> * ## Запусти фронтенд и бэкенд.

# 2. **Добавление автора и даты к постам:**
> * ## **Бэкенд**: В `main.py` добавь поля `author` (str) и `date` (str) в модель `PostFull` и в "базу данных" `fake_posts_db`.
> * ## **Фронтенд**: Отобрази автора и дату на главной странице под заголовком и на странице самого поста.

# 3. **Создание категорий:**
> * ## **Бэкенд**: Добавь поле `category` (str) в модель поста.
> * ## **Фронтенд**: На главной странице сгруппируй посты по категориям или добавь возможность фильтрации по ним.

# 4. **(Сложное) Markdown-рендер:**
> * ## Измени поле `content` в постах на валидный Markdown.
> * ## На фронтенде используй библиотеку (например, `react-markdown`), чтобы красиво отрендерить контент вместо использования `dangerouslySetInnerHTML`.

# Next.js және FastAPI орнату: Жылдам бастау нұсқаулығы

**НАЗАР АУДАРЫҢЫЗ\! Осы жобаны іске қосу үшін қазір бірден ЕКІ БӨЛЕК ТЕРМИНАЛ (пәрмен жолы) ТЕРЕЗЕСІН ашуыңыз керек\!**

**Екі терминалды ашыңыз және әрқайсысы үшін төмендегі нұсқауларды орындаңыз.**

-----

## Терминал №1: FRONT-END (Next.js) іске қосу

1.  **Front-end қалтасына өту:**

    ```bash
    cd frontend
    ```

2.  **JavaScript тәуелділіктерін орнату (БІР РЕТ немесе жобаны жаңартқанда орындаңыз):**

    ```bash
    pnpm install
    ```

3.  **Front-end серверін іске қосу:**

    ```bash
    pnpm dev
    ```

      * **Егер `pnpm dev` "next танылмады" деген қате берсе**, мына пәрменді қолданыңыз:
        ```bash
        .\node_modules\.bin\next dev --turbopack
        ```
      * **Бұл терминалды жаппаңыз.** Front-end онда жұмыс істеуін жалғастырады.

-----

## Терминал №2: BACK-END (FastAPI) іске қосу

1.  **Back-end қалтасына өту:**

    ```bash
    cd backend
    ```

2.  **Python ортасын орнату (БІР РЕТ немесе жобаны жаңартқанда орындаңыз):**

    -----

    **МАҢЫЗДЫ PYTHON НҰСҚАСЫ ТУРАЛЫ ЕСКЕРТУ:**

      * **Егер Python нұсқасы сәйкес келсе**, жай ғана бар `venv` (3-қадам) белсендіріңіз және тәуелділіктерді орнатыңыз (`pip install -r requirements.txt`). Егер `venv` жобада бұрыннан бар болса, оны көшіру қажет емес.
      * **Егер Python нұсқасы әртүрлі болса**, міндетті түрде жаңа `venv` жасаңыз: `python -m venv venv`. Содан кейін оны белсендіріңіз және тәуелділіктерді орнатыңыз.
      * `venv` Python-ның нақты нұсқасына байланысты. `python --version` арқылы тексеріңіз.

    -----

      * **Виртуалды ортаны жасау (Python venv, Conda емес):**
        ```bash
        python -m venv venv
        ```
      * **Ортаны белсендіру:**
          * **Windows үшін (PowerShell):**
            ```bash
            .\venv\Scripts\activate
            ```
          * **macOS / Linux үшін (Bash/Zsh):**
            ```bash
            source venv/bin/activate
            ```
      * **`requirements.txt` файлынан Python тәуелділіктерін орнату:**
        ```bash
        pip install -r requirements.txt
        ```
        [cite\_start]`aiofiles` [cite: 1, 2] [cite\_start]және `httpx` [cite: 4] орнатылғанына көз жеткізіңіз.
      * **Ортаны белсенділігін тоқтату (орнатқаннан кейін):**
        ```bash
        deactivate
        ```

3.  **Виртуалды ортаны белсендіру (әр серверді іске қоспас бұрын):**

      * **Windows үшін (PowerShell):**
        ```bash
        .\venv\Scripts\activate
        ```
      * **macOS / Linux үшін (Bash/Zsh):**
        ```bash
        source venv/bin/activate
        ```

4.  **FastAPI Back-end серверін іске қосу:**

    ```bash
    fastapi dev main.py
    ```

      * **Бұл терминалды жаппаңыз.** Back-end онда жұмыс істеуін жалғастырады. API құжаттамасы: `http://127.0.0.1:8000/docs`.

-----

**Екі терминал да өз серверлерінің іске қосылғанын көрсеткеннен кейін, веб-шолғышты ашып, мына мекенжайға өтіңіз:**

**`http://localhost:3000`**

**Дәл осы жерде сіз жобаның жұмыс істеп тұрған Front-end бөлігін көресіз.**

-----

# Setting Up Next.js and FastAPI: A Quick Start Guide

**ATTENTION\! To run this project, you need to open TWO SEPARATE TERMINAL (command prompt) WINDOWS RIGHT NOW\!**

**Open two terminals and follow the instructions below for each one.**

-----

## Terminal №1: Starting the FRONT-END (Next.js)

1.  **Navigate to the Front-end folder:**

    ```bash
    cd frontend
    ```

2.  **Install JavaScript dependencies (perform ONCE, or when updating the project):**

    ```bash
    pnpm install
    ```

3.  **Start the Front-end server:**

    ```bash
    pnpm dev
    ```

      * **If `pnpm dev` throws an "next is not recognized" error**, use this command:
        ```bash
        .\node_modules\.bin\next dev --turbopack
        ```
      * **Do not close this terminal.** The Front-end will continue to run in it.

-----

## Terminal №2: Starting the BACK-END (FastAPI)

1.  **Navigate to the Back-end folder:**

    ```bash
    cd backend
    ```

2.  **Set up the Python environment (perform ONCE, or when updating the project):**

    -----

    **IMPORTANT PYTHON VERSION WARNING:**

      * **If your Python version matches**, simply activate the existing `venv` (step 3) and install dependencies (`pip install -r requirements.txt`). Copying `venv` is not needed if it's already in the project.
      * **If your Python version differs**, you **must** create a new `venv`: `python -m venv venv`. Then activate it and install dependencies.
      * `venv` is tied to a specific Python version. Check `python --version`.

    -----

      * **Create a virtual environment (Python venv, not Conda):**
        ```bash
        python -m venv venv
        ```
      * **Activate the environment:**
          * **For Windows (PowerShell):**
            ```bash
            .\venv\Scripts\activate
            ```
          * **For macOS / Linux (Bash/Zsh):**
            ```bash
            source venv/bin/activate
            ```
      * **Install Python dependencies from `requirements.txt`:**
        ```bash
        pip install -r requirements.txt
        ```
        [cite\_start]Ensure that `aiofiles` [cite: 1, 2] [cite\_start]and `httpx` [cite: 4] are installed.
      * **Deactivate the environment (after installation):**
        ```bash
        deactivate
        ```

3.  **Activate the virtual environment (before each server start):**

      * **For Windows (PowerShell):**
        ```bash
        .\venv\Scripts\activate
        ```
      * **For macOS / Linux (Bash/Zsh):**
        ```bash
        source venv/bin/activate
        ```

4.  **Start the FastAPI Back-end server:**

    ```bash
    fastapi dev main.py
    ```

      * **Do not close this terminal.** The Back-end will continue to run in it. API Documentation: `http://127.0.0.1:8000/docs`.

-----

**Once both terminals show their servers are running, open your web browser and navigate to:**

**`http://localhost:3000`**

**This is where you will see the running Front-end of the project.**

-----

# Настройка Next.js и FastAPI: Руководство по быстрому старту

**ВНИМАНИЕ\! Для запуска проекта тебе нужно открыть ДВА ОТДЕЛЬНЫХ ОКНА ТЕРМИНАЛА (командной строки) ПРЯМО СЕЙЧАС\!**

**Открой два терминала и следуй инструкциям ниже для каждого из них.**

-----

## Терминал №1: Запуск FRONT-END (Next.js)

1.  **Переход в папку Front-end:**

    ```bash
    cd frontend
    ```

2.  **Установка JavaScript-зависимостей (выполнить ОДИН РАЗ, или при обновлении проекта):**

    ```bash
    pnpm install
    ```

3.  **Запуск Front-end сервера:**

    ```bash
    pnpm dev
    ```

      * **Если `pnpm dev` выдает ошибку "next не распознан"**, используй эту команду:
        ```bash
        .\node_modules\.bin\next dev --turbopack
        ```
      * **Не закрывай этот терминал.** Front-end будет продолжать работать в нем.

-----

## Терминал №2: Запуск BACK-END (FastAPI)

1.  **Переход в папку Back-end:**

    ```bash
    cd backend
    ```

2.  **Настройка Python-окружения (выполнить ОДИН РАЗ, или при обновлении проекта):**

    -----

    **ВАЖНОЕ ПРЕДУПРЕЖДЕНИЕ О ВЕРСИЯХ PYTHON:**

      * **Если версия Python совпадает**, просто активируй существующее `venv` (шаг 3) и установи зависимости (`pip install -r requirements.txt`). Копирование `venv` не требуется, если оно уже в проекте.
      * **Если версия Python отличается**, **обязательно** создай новое `venv`: `python -m venv venv`. Затем активируй его и установи зависимости.
      * `venv` привязан к конкретной версии Python. Проверяй `python --version`.

    -----

      * **Создание виртуального окружения (Python venv, не Conda):**
        ```bash
        python -m venv venv
        ```
      * **Активация окружения:**
          * **Для Windows (PowerShell):**
            ```bash
            .\venv\Scripts\activate
            ```
          * **Для macOS / Linux (Bash/Zsh):**
            ```bash
            source venv/bin/activate
            ```
      * **Установка Python-зависимостей из `requirements.txt`:**
        ```bash
        pip install -r requirements.txt
        ```
        [cite\_start]Убедись, что `aiofiles` [cite: 1, 2] [cite\_start]и `httpx` [cite: 4] установлены.
      * **Деактивация окружения (после установки):**
        ```bash
        deactivate
        ```

3.  **Активация виртуального окружения (перед каждым запуском сервера):**

      * **Для Windows (PowerShell):**
        ```bash
        .\venv\Scripts\activate
        ```
      * **Для macOS / Linux (Bash/Zsh):**
        ```bash
        source venv/bin/activate
        ```

4.  **Запуск Back-end сервера FastAPI:**

    ```bash
    fastapi dev main.py
    ```

      * **Не закрывай этот терминал.** Back-end будет продолжать работать в нем. Документация API: `http://127.0.0.1:8000/docs`.

-----

**Как только оба терминала покажут, что их серверы запущены, открой веб-браузер и перейди по адресу:**

**`http://localhost:3000`**

**Именно здесь ты увидишь работающий Front-end проекта.**


