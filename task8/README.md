# **МАҢЫЗДЫ: СТУДЕНТТЕРГЕ АРНАЛҒАН ТАПСЫРМАЛАР!**

Дағдыларды бекітуге арналған практикалық тапсырмалар. Қателерден қорықпа, бұл оқу процесінің бір бөлігі!

---

# **Жоба 8/10: Іздеу және Сүзу**

Тауарлар каталогын имитациялайтын, санаттар бойынша іздеу және сүзу мүмкіндігі бар full-stack қосымшасы.

---

**🚀 Технологиялар**

* **Бэкенд**: FastAPI (опционалды query-параметрлерді өңдеу)
* **Фронтенд**: Next.js, React (`useEffect` бірнеше тәуелділіктермен)

**✨ Функционал**

* Бэкенд сүзудің барлық логикасын орындайтын бірыңғай `/api/products` эндпоинтін ұсынады.
* Фронтенд сүзгілерді (іздеу және ашылмалы тізім) көрсетеді.
* Сүзгілердің кез келгені өзгерген кезде, фронтенд автоматты түрде жаңартылған тауарлар тізімін сұрайды және көрсетеді.

# **Сенің міндетің:**

## Сенің тапсырмаң:

# 1. **Сұрыптауды қосу:**
> * ## **Бэкенд**: Опционалды `sort` query-параметрін қос (мысалы, `?sort=price_asc` немесе `?sort=price_desc`). Тізімді жібермес бұрын сұрыптау логикасын іске қос.
> * ## **Фронтенд**: Сұрыптау опцияларын таңдау үшін ашылмалы тізімді қос (Бағасы бойынша: алдымен арзан; Бағасы бойынша: алдымен қымбат).

# 2. **Баға диапазоны бойынша сүзу:**
> * ## **Бэкенд**: `min_price` және `max_price` параметрлерін қос.
> * ## **Фронтенд**: Минималды және максималды бағаны енгізу үшін екі өріс қос.

# 3. **Іздеуге арналған Debouncing (күрделі):**
> * ## Қазір API-сұраныс іздеу өрісіндегі әрбір пернені басқанда жіберіледі. Бұл тиімсіз.
> * ## **Фронтенд**: "Debouncing" механизмін іске қос. Сұраныс пайдаланушы теруді ~300-500 миллисекундқа тоқтатқаннан кейін ғана жіберілуі керек. Ол үшін `setTimeout` және `clearTimeout` ішінде `useEffect` қолдануға болады.

---

# **IMPORTANT: TASKS FOR STUDENTS!**

These are practical assignments to consolidate your skills. Don't be afraid of mistakes; they are part of the learning process!

---

# **Project 8/10: Search and Filtering**

A full-stack application mimicking a product catalog with search and category filtering capabilities.

---

**🚀 Technologies**

* **Backend**: FastAPI (handling optional query parameters)
* **Frontend**: Next.js, React (`useEffect` with multiple dependencies)

**✨ Functionality**

* The backend provides a single `/api/products` endpoint that performs all filtering logic.
* The frontend displays filters (search and dropdown list).
* When any filter changes, the frontend automatically requests and displays an updated list of products.

# **Your Task:**

## Your Mission:

# 1. **Add Sorting:**
> * ## **Backend**: Add an optional `sort` query parameter (e.g., `?sort=price_asc` or `?sort=price_desc`). Implement the sorting logic for the list before sending.
> * ## **Frontend**: Add a dropdown list for selecting sorting options (By price: cheapest first; By price: most expensive first).

# 2. **Price Range Filter:**
> * ## **Backend**: Add `min_price` and `max_price` parameters.
> * ## **Frontend**: Add two input fields for entering minimum and maximum prices.

# 3. **Debouncing for Search (Advanced):**
> * ## Currently, an API request is sent on every keystroke in the search field. This is inefficient.
> * ## **Frontend**: Implement a "debouncing" mechanism. The request should only be sent after the user has stopped typing for ~300-500 milliseconds. This can be achieved using `setTimeout` and `clearTimeout` within `useEffect`.

---

# **ВАЖНО: ЗАДАЧИ ДЛЯ СТУДЕНТОВ!**

Перед тобой практические задания для закрепления навыков. Не бойся ошибок, это часть обучения!

---

# **Проект 8/10: Поиск и Фильтрация**

Full-stack приложение, имитирующее каталог товаров с возможностью поиска и фильтрации по категориям.

---

**🚀 Технологии**

* **Бэкенд**: FastAPI (обработка опциональных query-параметров)
* **Фронтенд**: Next.js, React (`useEffect` с несколькими зависимостями)

**✨ Функционал**

* Бэкенд предоставляет единый эндпоинт `/api/products`, который выполняет всю логику фильтрации.
* Фронтенд отображает фильтры (поиск и выпадающий список).
* При изменении любого из фильтров, фронтенд автоматически запрашивает и отображает обновленный список товаров.

# **Твоя задача:**

## Твоя миссия:

# 1. **Добавить сортировку:**
> * ## **Бэкенд**: Добавь опциональный query-параметр `sort` (например, `?sort=price_asc` или `?sort=price_desc`). Реализуй логику сортировки списка перед отправкой.
> * ## **Фронтенд**: Добавь выпадающий список для выбора опций сортировки (По цене: сначала дешевые; По цене: сначала дорогие).

# 2. **Фильтр по диапазону цен:**
> * ## **Бэкенд**: Добавь параметры `min_price` и `max_price`.
> * ## **Фронтенд**: Добавь два поля для ввода минимальной и максимальной цены.

# 3. **Debouncing для поиска (сложное):**
> * ## Сейчас API-запрос отправляется при каждом нажатии клавиши в поле поиска. Это неэффективно.
> * ## **Фронтенд**: Реализуй механизм "debouncing". Запрос должен отправляться только после того, как пользователь перестал печатать на ~300-500 миллисекунд. Для этого можно использовать `setTimeout` и `clearTimeout` внутри `useEffect`.

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

# Проект 8/10: Поиск и Фильтрация

Full-stack приложение, имитирующее каталог товаров с возможностью поиска и фильтрации по категориям.

## 🚀 Технологии

* **Бэкенд:** FastAPI (обработка опциональных query-параметров)
* **Фронтенд:** Next.js, React (`useEffect` с несколькими зависимостями)

## ✨ Функционал

* Бэкенд предоставляет единый эндпоинт `/api/products`, который выполняет всю логику фильтрации.
* Фронтенд отображает фильтры (поиск и выпадающий список).
* При изменении любого из фильтров, фронтенд автоматически запрашивает и отображает обновленный список товаров.

## 🎓 Задание для студентов

### Ваша миссия:

1.  **Добавить сортировку:**
    * **Бэкенд:** Добавьте опциональный query-параметр `sort` (например, `?sort=price_asc` или `?sort=price_desc`). Реализуйте логику сортировки списка перед отправкой.
    * **Фронтенд:** Добавьте выпадающий список для выбора опций сортировки (По цене: сначала дешевые; По цене: сначала дорогие).

2.  **Фильтр по диапазону цен:**
    * **Бэкенд:** Добавьте параметры `min_price` и `max_price`.
    * **Фронтенд:** Добавьте два поля для ввода минимальной и максимальной цены.

3.  **Debouncing для поиска (сложное):**
    * Сейчас API-запрос отправляется при каждом нажатии клавиши в поле поиска. Это неэффективно.
    * **Фронтенд:** Реализуйте механизм "debouncing". Запрос должен отправляться только после того, как пользователь перестал печатать на ~300-500 миллисекунд. Для этого можно использовать `setTimeout` и `clearTimeout` внутри `useEffect`.

## ⚙️ Локальный запуск

1.  Клонируйте репозиторий.
2.  **Бэкенд:** в `backend` установите зависимости (`pip install "fastapi[all]"`) и запустите `uvicorn main:app --reload`.
3.  **Фронтенд:** в `frontend` установите зависимости (`pnpm install`) и запустите `pnpm dev`.
