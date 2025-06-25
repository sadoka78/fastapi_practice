# **МАҢЫЗДЫ: СТУДЕНТТЕРГЕ АРНАЛҒАН ТАПСЫРМАЛАР!**

Дағдыларды бекітуге арналған практикалық тапсырмалар. Қателерден қорықпа, бұл оқу процесінің бір бөлігі!

---

# **Жоба 3/10: Ауа райы қосымшасы**

Бұл жоба FastAPI-дегі бэкенд-прокси арқылы сыртқы API (OpenWeatherMap) жұмысын көрсетеді. Бұл құпия кілттері бар API-ді қауіпсіз пайдалану әдісі.

---

**🚀 Архитектура**

* Next.js (Фронтенд) біздің бэкендке сұраныс жібереді (мысалы, "Лондон үшін ауа райын бер").
* FastAPI (Бэкенд) бұл сұранысты қабылдайды, оған құпия API-кілтін қосады және оны OpenWeatherMap серверіне бағыттайды.
* OpenWeatherMap деректерді біздің бэкендке қайтарады.
* FastAPI жауапты өңдейді, тек қажетті өрістерді (температура, сипаттама) таңдайды және оларды фронтендке береді.
* Next.js алынған деректерді пайдаланушыға көрсетеді.

# **Сенің міндетің:**

## Сенің тапсырмаң:

# 1. **Жобаны баптау:**
> * ## OpenWeatherMap-тан өзіңнің API-кілтіңді ал және оны `backend/.env` файлына жаз.

# 2. **5 күндік болжам:**
> * ## OpenWeatherMap болжам үшін эндпоинт ұсынады.
> * ## **Бэкенд**: Жаңа `/api/forecast/{city}` эндпоинтін жаса.
> * ## **Фронтенд**: Ағымдағы ауа райы нәтижелерінің астында бірнеше күн алға қарапайым болжамды көрсет.

# 3. **Геолокация бойынша анықтау:**
> * ## Пайдаланушының координаттарын анықтау үшін браузер API-ін (`navigator.geolocation`) пайдалан.
> * ## **Бэкенд**: Ендік пен бойлықты қабылдайтын `/api/weather/coords` эндпоинтін жаса.
> * ## **Фронтенд**: Бетті жүктеу кезінде геолокацияға кіруге рұқсат сұра және ағымдағы орналасқан жер үшін ауа райын көрсет.

---

# **IMPORTANT: TASKS FOR STUDENTS!**

These are practical assignments to consolidate your skills. Don't afraid of mistakes; they are part of the learning process!

---

# **Project 3/10: Weather Application**

This project demonstrates working with an external API (OpenWeatherMap) via a FastAPI backend proxy. This is a secure way to use APIs with secret keys.

---

**🚀 Architecture**

* Next.js (Frontend) sends a request (e.g., "Give me the weather for London") to our backend.
* FastAPI (Backend) receives this request, adds the secret API key to it, and forwards it to the OpenWeatherMap server.
* OpenWeatherMap returns the data to our backend.
* FastAPI processes the response, selects only the necessary fields (temperature, description), and sends them to the frontend.
* Next.js displays the received data to the user.

# **Your Task:**

## Your Mission:

# 1. **Set up the project:**
> * ## Obtain your OpenWeatherMap API key and write it to the `backend/.env` file.

# 2. **5-day forecast:**
> * ## OpenWeatherMap provides a forecast endpoint.
> * ## **Backend**: Create a new `/api/forecast/{city}` endpoint.
> * ## **Frontend**: Below the current weather results, display a simple forecast for a few days ahead.

# 3. **Geolocation detection:**
> * ## Use the browser's API (`navigator.geolocation`) to determine the user's coordinates.
> * ## **Backend**: Create a `/api/weather/coords` endpoint that accepts latitude and longitude.
> * ## **Frontend**: When the page loads, ask for permission to access geolocation and show the weather for the current location.

---

# **ВАЖНО: ЗАДАЧИ ДЛЯ СТУДЕНТОВ!**

Перед тобой практические задания для закрепления навыков. Не бойся ошибок, это часть обучения!

---

# **Проект 3/10: Приложение Погоды**

Этот проект демонстрирует работу с внешним API (OpenWeatherMap) через бэкенд-прокси на FastAPI. Это безопасный способ использовать API с секретными ключами.

---

**🚀 Архитектура**

* Next.js (Фронтенд) отправляет запрос (например, "Дай погоду для Лондона") на наш бэкенд.
* FastAPI (Бэкенд) получает этот запрос, добавляет к нему секретный API-ключ и перенаправляет его на сервер OpenWeatherMap.
* OpenWeatherMap возвращает данные на наш бэкенд.
* FastAPI обрабатывает ответ, выбирает только нужные поля (температура, описание) и отдает их фронтенду.
* Next.js отображает полученные данные пользователю.

# **Твоя задача:**

## Твоя миссия:

# 1. **Настройте проект:**
> * ## Получи свой API-ключ от OpenWeatherMap и пропиши его в файле `backend/.env`.

# 2. **Прогноз на 5 дней:**
> * ## OpenWeatherMap предоставляет эндпоинт для прогноза.
> * ## **Бэкенд**: Создай новый эндпоинт `/api/forecast/{city}`.
> * ## **Фронтенд**: Под результатами текущей погоды отобрази простой прогноз на несколько дней вперед.

# 3. **Определение по геолокации:**
> * ## Используй API браузера (`navigator.geolocation`) чтобы определить координаты пользователя.
> * ## **Бэкенд**: Создай эндпоинт `/api/weather/coords`, который принимает широту и долготу.
> * ## **Фронтенд**: При загрузке страницы спрашивай разрешение на доступ к геолокации и показывай погоду для текущего местоположения.


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

# Проект 3/10: Приложение Погоды

Этот проект демонстрирует работу с внешним API (OpenWeatherMap) через бэкенд-прокси на FastAPI. Это безопасный способ использовать API с секретными ключами.

## 🚀 Архитектура

1.  **Next.js (Фронтенд)** отправляет запрос (например, "Дай погоду для Лондона") на наш бэкенд.
2.  **FastAPI (Бэкенд)** получает этот запрос, добавляет к нему секретный API-ключ и перенаправляет его на сервер OpenWeatherMap.
3.  **OpenWeatherMap** возвращает данные на наш бэкенд.
4.  **FastAPI** обрабатывает ответ, выбирает только нужные поля (температура, описание) и отдает их фронтенду.
5.  **Next.js** отображает полученные данные пользователю.

## 🎓 Задание для студентов

### Ваша миссия:

1.  **Настройте проект:** Получите свой API-ключ от OpenWeatherMap и пропишите его в файле `backend/.env`.
2.  **Прогноз на 5 дней:** OpenWeatherMap предоставляет эндпоинт для прогноза.
    * **Бэкенд:** Создайте новый эндпоинт `/api/forecast/{city}`.
    * **Фронтенд:** Под результатами текущей погоды отобразите простой прогноз на несколько дней вперед.
3.  **Определение по геолокации:**
    * Используйте API браузера (`navigator.geolocation`) чтобы определить координаты пользователя.
    * **Бэкенд:** Создайте эндпоинт `/api/weather/coords`, который принимает широту и долготу.
    * **Фронтенд:** При загрузке страницы спрашивайте разрешение на доступ к геолокации и показывайте погоду для текущего местоположения.

## ⚙️ Локальный запуск

1.  Клонируйте репозиторий.
2.  **Настройте бэкенд:**
    * `cd backend`
    * Создайте файл `.env` и вставьте ваш ключ: `OPENWEATHER_API_KEY="ВАШ_КЛЮЧ"`
    * `pip install httpx "fastapi[all]" python-dotenv`
    * `uvicorn main:app --reload`
3.  **Настройте фронтенд:**
    * `cd frontend`
    * `pnpm install`
    * `pnpm dev`
