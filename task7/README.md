# **МАҢЫЗДЫ: СТУДЕНТТЕРГЕ АРНАЛҒАН ТАПСЫРМАЛАР!**

Дағдыларды бекітуге арналған практикалық тапсырмалар. Қателерден қорықпа, бұл оқу процесінің бір бөлігі!

---

# **Жоба 7/10: JSON-ға сақтаумен Қонақ кітабы**

JSON-файлға деректерді серверде сақтау арқылы персистенттілікті (тұрақтылықты) көрсететін full-stack қосымшасы.

---

**🚀 Технологиялар**

* **Бэкенд**: FastAPI, aiofiles
* **Фронтенд**: Next.js, React, Axios

**✨ Функционал**

* Атау мен хабарламаны жіберуге арналған форма.
* Бэкенд әр жазбаны `guestbook.json` файлында сақтайды.
* Барлық жазбалар басты бетте көрсетіледі және сервер қайта жүктелгеннен кейін жоғалмайды.

# **Сенің міндетің:**

## Сенің тапсырмаң:

# 1. **Жазбаларды жою:**
> * ## **Бэкенд**: ID бойынша жазбаны табатын, оны тізімнен жоятын және файлды қайта жазатын `DELETE /api/entries/{entry_id}` эндпоинтін жаса.
> * ## **Фронтенд**: Әр жазбаға "Жою" батырмасын қос.

# 2. **Жазбаларды өңдеу:**
> * ## **Бэкенд**: Хабарлама мәтінін өңдеу үшін `PUT /api/entries/{entry_id}` эндпоинтін жаса.
> * ## **Фронтенд**: Хабарлама мәтінін енгізу өрісіне айналдыратын "Өңдеу" батырмасын қос.

# 3. **Пагинация:**
> * ## **Бэкенд**: `GET /api/entries` эндпоинтін өзгерт, ол `page` және `limit` query-параметрлерін қабылдайтын болсын (мысалы, `/api/entries?page=1&limit=10`) және жазбалардың тек бір бөлігін қайтаратын болсын.
> * ## **Фронтенд**: Қонақ кітабының беттері бойынша шарлау үшін "Алға" және "Артқа" батырмаларын қос.

---

# **IMPORTANT: TASKS FOR STUDENTS!**

These are practical assignments to consolidate your skills. Don't be afraid of mistakes; they are part of the learning process!

---

# **Project 7/10: Guestbook with JSON Persistence**

A full-stack application demonstrating data persistence by saving it to a JSON file on the server.

---

**🚀 Technologies**

* **Backend**: FastAPI, aiofiles
* **Frontend**: Next.js, React, Axios

**✨ Functionality**

* Form for submitting a name and message.
* Backend saves each entry to `guestbook.json`.
* All entries are displayed on the main page and do not disappear after server restarts.

# **Your Task:**

## Your Mission:

# 1. **Delete Entries:**
> * ## **Backend**: Create a `DELETE /api/entries/{entry_id}` endpoint that finds an entry by ID, removes it from the list, and rewrites the file.
> * ## **Frontend**: Add a "Delete" button to each entry.

# 2. **Edit Entries:**
> * ## **Backend**: Create a `PUT /api/entries/{entry_id}` endpoint for editing the message text.
> * ## **Frontend**: Add an "Edit" button that transforms the message text into an input field.

# 3. **Pagination:**
> * ## **Backend**: Modify the `GET /api/entries` endpoint to accept `page` and `limit` query parameters (e.g., `/api/entries?page=1&limit=10`) and return only a portion of the entries.
> * ## **Frontend**: Add "Next" and "Previous" buttons for navigating through the guestbook pages.

---

# **ВАЖНО: ЗАДАЧИ ДЛЯ СТУДЕНТОВ!**

Перед тобой практические задания для закрепления навыков. Не бойся ошибок, это часть обучения!

---

# **Проект 7/10: Гостевая книга с сохранением в JSON**

Full-stack приложение, демонстрирующее персистентность (постоянство) данных с помощью их сохранения в JSON-файл на сервере.

---

**🚀 Технологии**

* **Бэкенд**: FastAPI, aiofiles
* **Фронтенд**: Next.js, React, Axios

**✨ Функционал**

* Форма для отправки имени и сообщения.
* Бэкенд сохраняет каждую запись в `guestbook.json`.
* Все записи отображаются на главной странице и не исчезают после перезагрузки сервера.

# **Твоя задача:**

## Твоя миссия:

# 1. **Удаление записей:**
> * ## **Бэкенд**: Создай эндпоинт `DELETE /api/entries/{entry_id}`, который находит запись по ID, удаляет её из списка и перезаписывает файл.
> * ## **Фронтенд**: Добавь кнопку "Удалить" к каждой записи.

# 2. **Редактирование записей:**
> * ## **Бэкенд**: Создай эндпоинт `PUT /api/entries/{entry_id}` для редактирования текста сообщения.
> * ## **Фронтенд**: Добавь кнопку "Редактировать", которая превращает текст сообщения в поле для ввода.

# 3. **Пагинация:**
> * ## **Бэкенд**: Измени эндпоинт `GET /api/entries`, чтобы он принимал query-параметры `page` и `limit` (например, `/api/entries?page=1&limit=10`) и возвращал только часть записей.
> * ## **Фронтенд**: Добавь кнопки "Вперед" и "Назад" для навигации по страницам гостевой книги.

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

# Проект 7/10: Гостевая книга с сохранением в JSON

Full-stack приложение, демонстрирующее персистентность (постоянство) данных с помощью их сохранения в JSON-файл на сервере.

## 🚀 Технологии

* **Бэкенд:** FastAPI, aiofiles
* **Фронтенд:** Next.js, React, Axios
* **Ключевая концепция:** Чтение и запись в файл из эндпоинтов API для сохранения состояния между перезапусками сервера.

## ✨ Функционал

* Форма для отправки имени и сообщения.
* Бэкенд сохраняет каждую запись в `guestbook.json`.
* Все записи отображаются на главной странице и не исчезают после перезагрузки сервера.

## 🎓 Задание для студентов

### Ваша миссия:

1.  **Удаление записей:**
    * **Бэкенд:** Создайте эндпоинт `DELETE /api/entries/{entry_id}`, который находит запись по ID, удаляет её из списка и перезаписывает файл.
    * **Фронтенд:** Добавьте кнопку "Удалить" к каждой записи.

2.  **Редактирование записей:**
    * **Бэкенд:** Создайте эндпоинт `PUT /api/entries/{entry_id}` для редактирования текста сообщения.
    * **Фронтенд:** Добавьте кнопку "Редактировать", которая превращает текст сообщения в поле для ввода.

3.  **Пагинация:**
    * **Бэкенд:** Измените эндпоинт `GET /api/entries`, чтобы он принимал query-параметры `page` и `limit` (например, `/api/entries?page=1&limit=10`) и возвращал только часть записей.
    * **Фронтенд:** Добавьте кнопки "Вперед" и "Назад" для навигации по страницам гостевой книги.

## ⚙️ Локальный запуск

1.  Клонируйте репозиторий.
2.  **Бэкенд:** в `backend` создайте папку `data`, в ней файл `guestbook.json` с содержимым `[]`. Установите зависимости (`pip install "fastapi[all]" aiofiles`) и запустите `uvicorn main:app --reload`.
3.  **Фронтенд:** в `frontend` установите зависимости (`pnpm install`) и запустите `pnpm dev`.
