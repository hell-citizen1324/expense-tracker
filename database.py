import sqlite3
from datetime import datetime
from pathlib import Path


APP_DATA_DIR = Path.home() / ".local" / "share" / "ExpenseTracker"

APP_DATA_DIR.mkdir(
    parents=True,
    exist_ok=True
)

DATABASE_NAME = APP_DATA_DIR / "expenses.db"


def get_connection():
    return sqlite3.connect(DATABASE_NAME)


def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount INTEGER NOT NULL,
        tag TEXT NOT NULL,
        date_time TEXT NOT NULL
    )
    """)

    connection.commit()
    connection.close()


def add_expense(amount, tag):
    connection = get_connection()
    cursor = connection.cursor()

    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute(
        """
        INSERT INTO expenses (amount, tag, date_time)
        VALUES (?, ?, ?)
        """,
        (amount, tag, date_time)
    )

    connection.commit()
    connection.close()


def get_expenses():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    SELECT * FROM expenses
    """)

    expenses = cursor.fetchall()

    connection.close()

    return expenses


def get_total():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    SELECT SUM(amount) FROM expenses
    """)

    total = cursor.fetchone()[0]

    connection.close()

    return total or 0


def delete_expense(expense_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM expenses
        WHERE id = ?
        """,
        (expense_id,)
    )
    deleted_count = cursor.rowcount
    connection.commit()
    connection.close()
    return deleted_count


def update_expense(expense_id, amount, tag):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE expenses
        SET amount = ?, tag = ?
        WHERE id = ?
        """,
        (amount, tag, expense_id)
    )
    updated_expense = cursor.rowcount
    connection.commit()
    connection.close()
    return updated_expense


def get_expenses_by_tag(tag):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT * FROM expenses
        WHERE tag = ?
        """,
        (tag,)
    )

    expenses = cursor.fetchall()

    connection.close()

    return expenses


def get_all_ids():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    SELECT id FROM expenses
    """)

    ids = cursor.fetchall()

    connection.close()

    return [id[0] for id in ids]


def get_all_amounts():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    SELECT amount FROM expenses
    """)

    amounts = cursor.fetchall()

    connection.close()

    return [amount[0] for amount in amounts]


def get_all_tags():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    SELECT tag FROM expenses
    """)

    tags = cursor.fetchall()

    connection.close()

    return [tag[0] for tag in tags]
