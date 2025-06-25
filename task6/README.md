# **МАҢЫЗДЫ: СТУДЕНТТЕРГЕ АРНАЛҒАН ТАПСЫРМАЛАР\!**

Дағдыларды бекітуге арналған практикалық тапсырмалар. Қателерден қорықпа, бұл оқу процесінің бір бөлігі\!

-----

# **Жоба 6/10: Суреттер Галереясы**

Клиенттен серверге файлдарды жүктеуді көрсететін қарапайым full-stack қосымшасы.

-----

**🚀 Технологиялар**

  * **Бэкенд**: FastAPI (UploadFile, StaticFiles), aiofiles
  * **Фронтенд**: Next.js (\<Image\>, FormData)

**✨ Функционал**

  * Суретті таңдау және жүктеуге арналған форма.
  * Бэкенд файлдарды `/backend/static/images` қалтасында сақтайды.
  * Бэкенд сақталған файлдарды статика ретінде таратады.
  * Фронтендтегі галерея барлық жүктелген суреттерді көрсетеді.

# **Сенің міндетің:**

## Сенің тапсырмаң:

# 1\. **Суреттерді жою:**

>   * ## **Бэкенд**: Серверден файлды жоятын `DELETE /api/images/{filename}` эндпоинтін жаса.
>   * ## **Фронтенд**: Галереядағы әр суретке "Жою" батырмасын (қоқыс жәшігінің белгішесін) қос. Басқан кезде жою сұрауын жібер және тізімді жаңарт.

# 2\. **Сервердегі валидация:**

>   * ## **Бэкенд**: `/api/upload` эндпоинтіндегі валидацияны жақсарт. Тек `image/*` түрін ғана емес, сонымен қатар файлдың максималды өлшемін (мысалы, 5 МБ-тан аспайтын) тексеруді қосыңыз.

# 3\. **Жүктеу прогресінің индикаторы (күрделі):**

>   * ## **Фронтенд**: Жүктеу прогресін бақылау үшін `axios` мүмкіндіктерін пайдалан (сұрау конфигурациясындағы `onUploadProgress` параметрі). Файл жүктелген кезде прогресс жолағын көрсет.

-----

# **IMPORTANT: TASKS FOR STUDENTS\!**

These are practical assignments to consolidate your skills. Don't be afraid of mistakes; they are part of the learning process\!

-----

# **Project 6/10: Image Gallery**

A simple full-stack application demonstrating file uploads from client to server.

-----

**🚀 Technologies**

  * **Backend**: FastAPI (UploadFile, StaticFiles), aiofiles
  * **Frontend**: Next.js (\<Image\>, FormData)

**✨ Functionality**

  * Form for selecting and uploading an image.
  * Backend saves files to the `/backend/static/images` folder.
  * Backend serves saved files as static assets.
  * Frontend gallery displays all uploaded images.

# **Your Task:**

## Your Mission:

# 1\. **Delete Images:**

>   * ## **Backend**: Create a `DELETE /api/images/{filename}` endpoint that deletes the file from the server.
>   * ## **Frontend**: Add a "Delete" button (trash can icon) to each image in the gallery. When clicked, send a delete request and refresh the list.

# 2\. **Server-side Validation:**

>   * ## **Backend**: Improve validation in the `/api/upload` endpoint. Add checks not only for `image/*` type, but also for maximum file size (e.g., no more than 5 MB).

# 3\. **Upload Progress Indicator (Advanced):**

>   * ## **Frontend**: Use `axios` capabilities to track upload progress (`onUploadProgress` parameter in request config). Display a progress bar during file upload.

-----

# **ВАЖНО: ЗАДАЧИ ДЛЯ СТУДЕНТОВ\!**

Перед тобой практические задания для закрепления навыков. Не бойся ошибок, это часть обучения\!

-----

# **Проект 6/10: Галерея Изображений**

Простое full-stack приложение, демонстрирующее загрузку файлов с клиента на сервер.

-----

**🚀 Технологии**

  * **Бэкенд**: FastAPI (UploadFile, StaticFiles), aiofiles
  * **Фронтенд**: Next.js (\<Image\>, FormData)

**✨ Функционал**

  * Форма для выбора и загрузки изображения.
  * Бэкенд сохраняет файлы в папке `/backend/static/images`.
  * Бэкенд раздает сохраненные файлы как статику.
  * Галерея на фронтенде отображает все загруженные изображения.

# **Твоя задача:**

## Твоя миссия:

# 1\. **Удаление изображений:**

>   * ## **Бэкенд**: Создай эндпоинт `DELETE /api/images/{filename}`, который удаляет файл с сервера.
>   * ## **Фронтенд**: Добавь кнопку "Удалить" (иконку корзины) на каждое изображение в галерее. При нажатии отправляй запрос на удаление и обновляй список.

# 2\. **Валидация на сервере:**

>   * ## **Бэкенд**: Улучши валидацию в эндпоинте `/api/upload`. Добавь проверку не только на тип `image/*`, но и на максимальный размер файла (например, не больше 5 МБ).

# 3\. **Индикатор прогресса загрузки (сложное):**

>   * ## **Фронтенд**: Используй возможности `axios` для отслеживания прогресса загрузки (параметр `onUploadProgress` в конфиге запроса). Отображай прогресс-бар во время загрузки файла.

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

# Проект 6/10: Галерея Изображений

Простое full-stack приложение, демонстрирующее загрузку файлов с клиента на сервер.

## 🚀 Технологии

* **Бэкенд:** FastAPI (`UploadFile`, `StaticFiles`), aiofiles
* **Фронтенд:** Next.js (`<Image>`, `FormData`)

## ✨ Функционал

* Форма для выбора и загрузки изображения.
* Бэкенд сохраняет файлы в папке `/backend/static/images`.
* Бэкенд раздает сохраненные файлы как статику.
* Галерея на фронтенде отображает все загруженные изображения.

## 🎓 Задание для студентов

### Ваша миссия:

1.  **Удаление изображений:**
    * **Бэкенд:** Создайте эндпоинт `DELETE /api/images/{filename}`, который удаляет файл с сервера.
    * **Фронтенд:** Добавьте кнопку "Удалить" (иконку корзины) на каждое изображение в галерее. При нажатии отправляйте запрос на удаление и обновляйте список.

2.  **Валидация на сервере:**
    * **Бэкенд:** Улучшите валидацию в эндпоинте `/api/upload`. Добавьте проверку не только на тип `image/*`, но и на максимальный размер файла (например, не больше 5 МБ).

3.  **Индикатор прогресса загрузки (сложное):**
    * **Фронтенд:** Используйте возможности `axios` для отслеживания прогресса загрузки (параметр `onUploadProgress` в конфиге запроса). Отображайте прогресс-бар во время загрузки файла.

## ⚙️ Локальный запуск

1.  Клонируйте репозиторий.
2.  **Бэкенд:** в `backend` установите зависимости (`pip install "fastapi[all]" python-multipart aiofiles`) и запустите `uvicorn main:app --reload`.
3.  **Фронтенд:** в `frontend` установите зависимости (`pnpm install`), настройте `next.config.mjs` для работы с `localhost:8000` и запустите `pnpm dev`.
