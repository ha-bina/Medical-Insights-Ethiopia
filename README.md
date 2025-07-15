# Ethiopian Medical Business Data Pipeline

This project is designed to extract, load, and transform Telegram data relevant to Ethiopian medical businesses. It is built with a focus on reproducibility, modularity, and scalability using Python, Docker, PostgreSQL, and dbt.

---

## ⚙️ Task 0 - Project Setup & Environment Management

### 📁 Project Initialization

* Initialize the project using Git:

  ```bash
  git init
  ```
* Create a Python environment and track dependencies in `requirements.txt`:

  ```bash
  pip freeze > requirements.txt
  ```

### 📅 Docker & Docker Compose

* Create a `Dockerfile` to containerize the Python scraping environment.
* Create a `docker-compose.yml` file to orchestrate both Python and PostgreSQL services.

### 🔐 Environment Secrets

* Store secrets such as Telegram API credentials and DB passwords in a `.env` file.
* Add `.env` to `.gitignore` to prevent committing sensitive data:

  ```bash
  echo ".env" >> .gitignore
  ```
* Use `python-dotenv` to load secrets inside Python scripts:

  ```python
  from dotenv import load_dotenv
  load_dotenv()
  ```

---

## 📁 Task 1 - Data Scraping and Collection (Extract & Load)

### 🤖 Telegram Scraping

* Use the Telegram API via `telethon` to scrape messages from:

  * \[Chemed Telegram Channel]
  * [https://t.me/lobelia4cosmetics](https://t.me/lobelia4cosmetics)
  * [https://t.me/tikvahpharma](https://t.me/tikvahpharma)
  * More sources via: [https://et.tgstat.com/medicine](https://et.tgstat.com/medicine)

### 📷 Image Scraping

* Collect and store images from messages for future object detection use cases.

### 📊 Data Lake Structure

* Store raw, unaltered Telegram data in a structured, date-partitioned directory:

  ```
  data/raw/telegram_messages/YYYY-MM-DD/channel_name/messages.json
  ```

### ⛏ Logging & Monitoring

* Implement logging to capture:

  * Successfully scraped channels and dates
  * Failures and rate-limiting events

---

## 📊 Task 2 - Data Modeling and Transformation (Transform)

### 🔢 Loading to PostgreSQL

* Write a script to load raw `.json` files into a `raw.telegram_messages` table using `psycopg2` or `sqlalchemy`.

### 👾 DBT Setup

* Install dbt:

  ```bash
  pip install dbt-postgres
  ```
* Initialize project:

  ```bash
  dbt init my_project
  ```
* Configure `profiles.yml` to connect to PostgreSQL.

### 🔧 DBT Model Layers

#### ✨ Staging Models (`stg_telegram_messages.sql`)

* Light cleaning, type casting, renaming, and extracting key fields.

#### 📊 Data Mart Models

* **`dim_channels`**: Info per Telegram channel.
* **`dim_dates`**: Time-based breakdown.
* **`fct_messages`**: One row per message with FK references and metrics (e.g., message length, has\_image).

### ✅ Testing & Documentation

* Use built-in dbt tests:

  ```yaml
  tests:
    - unique
    - not_null
  ```
* Write at least one custom test (e.g., messages must have timestamps).
* Generate and serve documentation:

  ```bash
  dbt docs generate
  dbt docs serve
  ```

