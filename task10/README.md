# **МАҢЫЗДЫ: СТУДЕНТТЕРГЕ АРНАЛҒАН ТАПСЫРМАЛАР!**

Дағдыларды бекітуге арналған практикалық тапсырмалар. Қателерден қорықпа, бұл оқу процесінің бір бөлігі!

---

# **Жоба 10/10: Микроблог**

Аутентификацияны, CRUD-операцияларды және деректерді файлға сақтауды біріктіретін қарапайым көп пайдаланушылы микроблогты жасауға арналған соңғы жоба.

---

**🚀 Технологиялар**

* **Бэкенд**: FastAPI (тәуелділіктерді өңдеу, CRUD, файлдармен жұмыс)
* **Фронтенд**: Next.js (күйді басқару, қорғалған беттер, шартты рендеринг)
* **Негізгі концепциялар**: Аутентификацияны, CRUD-ты және деректердің тұрақтылығын бір қосымшада біріктіру. Контентке иелік құқығын тексеру.

**✨ Функционал**

* Екі алдын ала конфигурацияланған пайдаланушы (user1, user2).
* Токен (пайдаланушы аты) беретін кіру жүйесі.
* Барлық пайдаланушылардың посттары көрінетін басты таспа.
* Авторланған пайдаланушылар жаңа посттар жасай алады.
* Пайдаланушылар *тек өздерінің* посттарын жоя алады.
* Посттар туралы деректер `posts.json` файлында сақталады және қайта жүктегеннен кейін жоғалмайды.

# **Сенің міндетің:**

## Бұл жобаны одан әрі дамыту үшін соңғы сынақ!

# **Сенің тапсырмаң:**

# 1. **Нақты ДБ-ға көшу:**
> * ## `posts.json` файлын толыққанды дерекқорға ауыстыр. SQLite — бастау үшін тамаша таңдау, өйткені ол жеке серверді қажет етпейді.
> * ## Дерекқормен жұмыс істеу үшін FastAPI-да SQLAlchemy немесе SQLModel пайдалан (кестелерді жасау, сессиялар, сұраныстар). Бұл кәсіби өсу үшін ең маңызды қадам.

# 2. **"Лайктарды" іске асыру:**
> * ## ДБ-да `user_id` және `post_id` байланыстыратын лайктар үшін жаңа кесте жаса.
> * ## `POST /api/posts/{post_id}/like` және `DELETE /api/posts/{post_id}/like` эндпоинттерін қос.
> * ## Фронтендте әр постқа "лайк" батырмасын және лайктар санауышын қос.

# 3. **Пайдаланушы профильдері:**
> * ## Next.js-те динамикалық `app/users/[username]/page.tsx` бетін жаса.
> * ## Бұл бетте тек осы пайдаланушының барлық посттары көрсетілуі керек.
> * ## FastAPI-да бір автордың посттарын алу үшін `GET /api/users/{username}/posts` эндпоинтін қос.

---

# **IMPORTANT: TASKS FOR STUDENTS!**

These are practical assignments to consolidate your skills. Don't be afraid of mistakes; they are part of the learning process!

---

# **Project 10/10: Microblog**

The final project, combining authentication, CRUD operations, and data persistence to a file, to create a simple multi-user microblog.

---

**🚀 Technologies**

* **Backend**: FastAPI (dependency handling, CRUD, file operations)
* **Frontend**: Next.js (state management, protected pages, conditional rendering)
* **Key Concepts**: Integration of authentication, CRUD, and data persistence in one application. Checking content ownership rights.

**✨ Functionality**

* Two pre-configured users (user1, user2).
* Login system that issues a token (username).
* Main feed showing posts from all users.
* Authenticated users can create new posts.
* Users can delete *only their own* posts.
* Post data is saved in `posts.json` and does not disappear after a restart.

# **Your Task:**

## This is your final challenge to turn this project into something bigger!

# **Your Mission:**

# 1. **Migrate to a Real DB:**
> * ## Replace `posts.json` with a full-fledged database. SQLite is an ideal choice to start with, as it doesn't require a separate server.
> * ## Use SQLAlchemy or SQLModel in FastAPI to work with the database (table creation, sessions, queries). This is the most important step for professional growth.

# 2. **Implement "Likes":**
> * ## Create a new table in the DB for likes that will link `user_id` and `post_id`.
> * ## Add `POST /api/posts/{post_id}/like` and `DELETE /api/posts/{post_id}/like` endpoints.
> * ## On the frontend, add a "like" button and a like counter to each post.

# 3. **User Profiles:**
> * ## Create a dynamic page `app/users/[username]/page.tsx` in Next.js.
> * ## This page should display all posts from only that specific user.
> * ## Add a `GET /api/users/{username}/posts` endpoint in FastAPI to retrieve posts by a single author.

---

# **ВАЖНО: ЗАДАЧИ ДЛЯ СТУДЕНТОВ!**

Перед тобой практические задания для закрепления навыков. Не бойся ошибок, это часть обучения!

---

# **Проект 10/10: Микроблог**

Финальный проект, объединяющий аутентификацию, CRUD-операции и сохранение данных в файл для создания простого многопользовательского микроблога.

---

**🚀 Технологии**

* **Бэкенд**: FastAPI (обработка зависимостей, CRUD, работа с файлами)
* **Фронтенд**: Next.js (управление состоянием, защищенные страницы, условный рендеринг)
* **Ключевые концепции**: Интеграция аутентификации, CRUD и персистентности данных в одном приложении. Проверка прав владения контентом.

**✨ Функционал**

* Два преднастроенных пользователя (user1, user2).
* Система входа, выдающая токен (имя пользователя).
* Главная лента, где видны посты всех пользователей.
* Авторизованные пользователи могут создавать новые посты.
* Пользователи могут удалять *только свои собственные* посты.
* Данные о постах сохраняются в `posts.json` и не пропадают после перезагрузки.

# **Твоя задача:**

## Финальный вызов, чтобы превратить этот проект в нечто большее!

# **Твоя миссия:**

# 1. **Переход на настоящую БД:**
> * ## Замени `posts.json` на полноценную базу данных. SQLite — идеальный выбор для начала, так как не требует отдельного сервера.
> * ## Используй SQLAlchemy или SQLModel в FastAPI для работы с базой данных (создание таблиц, сессии, запросы). Это самый важный шаг для профессионального роста.

# 2. **Реализовать "Лайки":**
> * ## Создай новую таблицу в БД для лайков, которая будет связывать `user_id` и `post_id`.
> * ## Добавь эндпоинты `POST /api/posts/{post_id}/like` и `DELETE /api/posts/{post_id}/like`.
> * ## На фронтенде добавь кнопку "лайк" и счетчик лайков к каждому посту.

# 3. **Профили пользователей:**
> * ## Создай в Next.js динамическую страницу `app/users/[username]/page.tsx`.
> * ## На этой странице должны отображаться все посты только этого конкретного пользователя.
> * ## Добавь в FastAPI эндпоинт `GET /api/users/{username}/posts` для получения постов одного автора.

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

# Проект 10/10: Микроблог

Финальный проект, объединяющий аутентификацию, CRUD-операции и сохранение данных в файл для создания простого многопользовательского микроблога.

## 🚀 Технологии

* **Бэкенд:** FastAPI (обработка зависимостей, CRUD, работа с файлами)
* **Фронтенд:** Next.js (управление состоянием, защищенные страницы, условный рендеринг)
* **Ключевые концепции:** Интеграция аутентификации, CRUD и персистентности данных в одном приложении. Проверка прав владения контентом.

## ✨ Функционал

* Два преднастроенных пользователя (`user1`, `user2`).
* Система входа, выдающая токен (имя пользователя).
* Главная лента, где видны посты всех пользователей.
* Авторизованные пользователи могут создавать новые посты.
* Пользователи могут удалять **только свои собственные** посты.
* Данные о постах сохраняются в `posts.json` и не пропадают после перезагрузки.

## 🎓 Финальное Задание для Студентов (Следующий Уровень)

Это ваш финальный вызов, чтобы превратить этот проект в нечто большее!

### Ваша миссия:

1.  **Переход на настоящую БД:**
    * Замените `posts.json` на полноценную базу данных. `SQLite` — идеальный выбор для начала, так как не требует отдельного сервера.
    * Используйте `SQLAlchemy` или `SQLModel` в FastAPI для работы с базой данных (создание таблиц, сессии, запросы). Это самый важный шаг для профессионального роста.

2.  **Реализовать "Лайки":**
    * Создайте новую таблицу в БД для лайков, которая будет связывать `user_id` и `post_id`.
    * Добавьте эндпоинты `POST /api/posts/{post_id}/like` и `DELETE /api/posts/{post_id}/like`.
    * На фронтенде добавьте кнопку "лайк" и счетчик лайков к каждому посту.

3.  **Профили пользователей:**
    * Создайте в Next.js динамическую страницу `app/users/[username]/page.tsx`.
    * На этой странице должны отображаться все посты только этого конкретного пользователя.
    * Добавьте в FastAPI эндпоинт `GET /api/users/{username}/posts` для получения постов одного автора.

## ⚙️ Локальный запуск

1.  Клонируйте репозиторий.
2.  **Бэкенд:** в `backend` создайте папку `data`, в ней файл `posts.json` с содержимым `[]`. Установите зависимости (`pip install "fastapi[all]" python-multipart aiofiles`) и запустите `uvicorn main:app --reload`.
3.  **Фронтенд:** в `frontend` установите зависимости (`pnpm install`) и запустите `pnpm dev`.
