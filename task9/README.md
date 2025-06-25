# **МАҢЫЗДЫ: СТУДЕНТТЕРГЕ АРНАЛҒАН ТАПСЫРМАЛАР!**

Дағдыларды бекітуге арналған практикалық тапсырмалар. Қателерден қорықпа, бұл оқу процесінің бір бөлігі!

---

# **Жоба 9/10: Қарапайым аутентификация қосымшасы**

Токен-аутентификацияның базалық ағынын көрсететін full-stack қосымшасы.

---

**🚀 Технологиялар**

* **Бэкенд**: FastAPI (`Depends`, `Header`, `OAuth2PasswordRequestForm` тәуелділіктері)
* **Фронтенд**: Next.js (клиенттік маршруттау, токенді сақтау үшін `localStorage`)

**✨ Функционал**

* Бэкендтен токен сұрайтын кіру беті.
* Токен браузердің `localStorage` ішінде сақталады.
* Тек `Authorization` тақырыбында жарамды токен болған кезде ғана қол жетімді қорғалған бет.
* Жүйеден шығу мүмкіндігі (токенді жою және қайта бағыттау).

# **Сенің міндетің:**

## Сенің тапсырмаң:

# 1. **Пайдаланушы рөлдерін қосу:**
> * ## **Бэкенд**: `FAKE_USER` ішіне `role: 'admin'` немесе `role: 'user'` өрісін қос. Тек әкімшіге ғана қолжетімді болатын бөлек `/api/admin-data` эндпоинтін жаса. Тәуелділік тек токенді ғана емес, рөлді де тексеруі керек.
> * ## **Фронтенд**: Кіргеннен кейін пайдаланушы рөлін сақта және әкімші панеліне сілтемені көрсет/жасыр.

# 2. **"Жанды" токен:**
> * ## **Бэкенд**: Статикалық `SECRET_TOKEN` орнына, әр сәтті кіру кезінде жаңа бірегей токен генерацияла (мысалы, `uuid.uuid4()` көмегімен). Оны серверде `{ "token": "username" }` сөздігінде сақта. Тексеру кезінде токенді осы сөздіктен ізде. Шыққан кезде (logout) токенді сөздіктен жойып, оны жарамсыз ет.

# 3. **Токеннің өмір сүру уақыты (күрделі):**
> * ## **Бэкенд**: Токен жасау кезінде онымен бірге жасалған уақытын сақта. Тәуелділікті тексеру кезінде жасалған сәттен бастап 1 сағаттан аспағанына көз жеткіз.

---

# **IMPORTANT: TASKS FOR STUDENTS!**

These are practical assignments to consolidate your skills. Don't be afraid of mistakes; they are part of the learning process!

---

# **Project 9/10: Simple Authentication Application**

A full-stack application demonstrating a basic token authentication flow.

---

**🚀 Technologies**

* **Backend**: FastAPI (`Depends`, `Header`, `OAuth2PasswordRequestForm` dependencies)
* **Frontend**: Next.js (client-side routing, `localStorage` for token storage)

**✨ Functionality**

* Login page that requests a token from the backend.
* The token is stored in the browser's `localStorage`.
* A protected page that is accessible only with a valid token in the `Authorization` header.
* Logout functionality (deleting the token and redirecting).

# **Your Task:**

## Your Mission:

# 1. **Add User Roles:**
> * ## **Backend**: Add a `role: 'admin'` or `role: 'user'` field to `FAKE_USER`. Create a separate `/api/admin-data` endpoint that is only accessible to admins. The dependency should check not only the token but also the role.
> * ## **Frontend**: After login, store the user's role and show/hide the link to the admin panel accordingly.

# 2. **"Live" Token:**
> * ## **Backend**: Instead of a static `SECRET_TOKEN`, generate a new unique token (e.g., using `uuid.uuid4()`) on each successful login. Store it on the server in a dictionary `{ "token": "username" }`. When validating, look for the token in this dictionary. On logout, remove the token from the dictionary, invalidating it.

# 3. **Token Lifetime (Advanced):**
> * ## **Backend**: When creating a token, save its creation time along with it. In the dependency check, ensure that no more than, for example, 1 hour has passed since its creation.

---

# **ВАЖНО: ЗАДАЧИ ДЛЯ СТУДЕНТОВ!**

Перед тобой практические задания для закрепления навыков. Не бойся ошибок, это часть обучения!

---

# **Проект 9/10: Простое приложение с аутентификацией**

Full-stack приложение, демонстрирующее базовый поток токен-аутентификации.

---

**🚀 Технологии**

* **Бэкенд**: FastAPI (зависимости `Depends`, `Header`, `OAuth2PasswordRequestForm`)
* **Фронтенд**: Next.js (клиентская маршрутизация, `localStorage` для хранения токена)

**✨ Функционал**

* Страница входа, которая запрашивает у бэкенда токен.
* Токен сохраняется в `localStorage` браузера.
* Защищенная страница, которая доступна только при наличии валидного токена в `Authorization` заголовке.
* Возможность выхода из системы (удаление токена и редирект).

# **Твоя задача:**

## Твоя миссия:

# 1. **Добавить роли пользователей:**
> * ## **Бэкенд**: Добавь в `FAKE_USER` поле `role: 'admin'` или `role: 'user'`. Создай отдельный эндпоинт `/api/admin-data`, доступ к которому будет только у админа. Зависимость должна проверять не только токен, но и роль.
> * ## **Фронтенд**: После логина сохраняй роль пользователя и отображай/скрывай ссылку на админ-панель.

# 2. **"Живой" токен:**
> * ## **Бэкенд**: Вместо статичного `SECRET_TOKEN`, при каждом успешном логине генерируй новый уникальный токен (например, с помощью `uuid.uuid4()`). Храни его на сервере в словаре `{ "token": "username" }`. При проверке ищи токен в этом словаре. При выходе (logout) удаляй токен из словаря, делая его невалидным.

# 3. **Время жизни токена (сложное):**
> * ## **Бэкенд**: При создании токена сохраняй вместе с ним время его создания. В зависимости-проверке убедись, что с момента создания прошло не больше, например, 1 часа.

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

# Проект 9/10: Простое приложение с аутентификацией

Full-stack приложение, демонстрирующее базовый поток токен-аутентификации.

## 🚀 Технологии

* **Бэкенд:** FastAPI (зависимости `Depends`, `Header`, `OAuth2PasswordRequestForm`)
* **Фронтенд:** Next.js (клиентская маршрутизация, `localStorage` для хранения токена)

## ✨ Функционал

* Страница входа, которая запрашивает у бэкенда токен.
* Токен сохраняется в `localStorage` браузера.
* Защищенная страница, которая доступна только при наличии валидного токена в `Authorization` заголовке.
* Возможность выхода из системы (удаление токена и редирект).

## 🎓 Задание для студентов

### Ваша миссия:

1.  **Добавить роли пользователей:**
    * **Бэкенд:** Добавьте в `FAKE_USER` поле `role: 'admin'` или `role: 'user'`. Создайте отдельный эндпоинт `/api/admin-data`, доступ к которому будет только у админа. Зависимость должна проверять не только токен, но и роль.
    * **Фронтенд:** После логина сохраняйте роль пользователя и отображайте/скрывайте ссылку на админ-панель.

2.  **"Живой" токен:**
    * **Бэкенд:** Вместо статичного `SECRET_TOKEN`, при каждом успешном логине генерируйте новый уникальный токен (например, с помощью `uuid.uuid4()`). Храните его на сервере в словаре `{ "token": "username" }`. При проверке ищите токен в этом словаре. При выходе (`logout`) удаляйте токен из словаря, делая его невалидным.

3.  **Время жизни токена (сложное):**
    * **Бэкенд:** При создании токена сохраняйте вместе с ним время его создания. В зависимости-проверке убедитесь, что с момента создания прошло не больше, например, 1 часа.

## ⚙️ Локальный запуск

1.  Клонируйте репозиторий.
2.  **Бэкенд:** в `backend` установите зависимости (`pip install "fastapi[all]" python-multipart`) и запустите `uvicorn main:app --reload`.
3.  **Фронтенд:** в `frontend` установите зависимости (`pnpm install`) и запустите `pnpm dev`.
