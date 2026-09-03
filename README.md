# Expense Tracker

> **A practical financial management system built from the ground up.**

Expense Tracker is a personal finance application designed to make expense tracking simple, structured, and extensible.

The project began as a Python-based CLI application and is evolving into a full-stack system powered by a REST API and a dedicated frontend.

Rather than building everything at once, the project follows an incremental engineering approach — starting with a working core and progressively expanding its architecture, interface, and capabilities.

---

## ✦ Features

* Add and record expenses
* View expense history
* Edit existing expenses
* Delete expenses
* Calculate total spending
* Filter expenses by tag
* Find the highest expense
* Calculate spending totals by tag
* RESTful API
* Dedicated frontend interface

---

## ⚙️ Tech Stack

| Layer             | Technology |
| ----------------- | ---------- |
| Backend           | Python     |
| API               | FastAPI    |
| Database          | SQLite     |
| Frontend          | HTML       |
| Styling           | CSS        |
| Client-side Logic | JavaScript |
| Development       | Git        |

---

## 🏗️ Architecture

The application is structured around three main layers:

```text
┌──────────────────────────┐
│        Frontend          │
│      HTML / CSS / JS     │
└────────────┬─────────────┘
             │
             │ HTTP / REST
             ▼
┌──────────────────────────┐
│        FastAPI           │
│          API             │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│         Database         │
│          SQLite          │
└──────────────────────────┘
```

This separation allows each part of the system to evolve independently while keeping the overall architecture understandable and maintainable.

---

## 📁 Project Structure

```text
expense-tracker/
│
├── frontend/
│   ├── add_expense/
│   ├── delete_expense/
│   ├── edit_expense/
│   ├── show_biggest/
│   ├── show_by_tag/
│   ├── show_expenses/
│   ├── show_total/
│   ├── total_by_tag/
│   ├── menu.html
│   └── style.css
│
├── commands.py
├── database.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd expense-tracker
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Linux / macOS**

```bash
source venv/bin/activate
```

**Windows**

```powershell
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the API

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

### 5. Start the frontend

Open another terminal:

```bash
python -m http.server 5500
```

Then open:

```text
http://127.0.0.1:5500/frontend/menu.html
```

---

## 🔌 API

The backend exposes REST endpoints for interacting with expenses.

| Method   | Endpoint              | Purpose                  |
| -------- | --------------------- | ------------------------ |
| `POST`   | `/expenses`           | Add an expense           |
| `GET`    | `/expenses`           | Retrieve expenses        |
| `GET`    | `/expenses/total`     | Calculate total spending |
| `PUT`    | `/expenses/{id}`      | Edit an expense          |
| `DELETE` | `/expenses/{id}`      | Delete an expense        |
| `GET`    | `/expenses/tag/{tag}` | Filter by tag            |
| `GET`    | `/expenses/biggest`   | Find the largest expense |

---

## 🧠 Engineering Approach

The project is intentionally developed incrementally.

Instead of starting with a large architecture, the system is built in stages:

```text
CLI
 │
 ▼
Core Logic
 │
 ▼
Database
 │
 ▼
REST API
 │
 ▼
Frontend
 │
 ▼
Expanded Financial System
```

Each stage provides a functional foundation for the next one.

This approach keeps the system understandable while providing room for future improvements.

---

## 🛣️ Roadmap

### Current

* [x] Expense management
* [x] SQLite database
* [x] CLI foundation
* [x] FastAPI backend
* [x] REST endpoints
* [x] Basic frontend
* [x] Multi-page interface

### Next

* [ ] Improve UI/UX
* [ ] Improve API architecture
* [ ] Add stronger validation
* [ ] Add expense analytics
* [ ] Add data visualization
* [ ] Improve error handling
* [ ] Add authentication
* [ ] Expand financial insights

### Long Term

* [ ] External financial API integration
* [ ] Automated transaction importing
* [ ] Advanced financial analytics
* [ ] Budget management
* [ ] Financial dashboards

---

## 📌 Project Status

**Active Development**

This project is continuously evolving from a small expense-tracking application into a more complete financial management platform.

The architecture, interface, and feature set are expected to change as the system grows.

---

## 🎯 Why This Project?

Expense tracking is a simple problem with surprisingly deep engineering potential.

The project provides a practical environment for exploring:

* Backend development
* REST API design
* Database integration
* Frontend development
* Software architecture
* Data processing
* Application design
* Incremental system development

The goal is not simply to build an expense tracker.

**The goal is to build a system that can grow.**
