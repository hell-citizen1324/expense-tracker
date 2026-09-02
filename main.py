from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import commands

from pathlib import Path

import database


BASE_DIR = Path(__file__).resolve().parent
FRONTEND_DIR = BASE_DIR / "frontend"


app = FastAPI()

database.create_table()
# =========================
# CORS
# =========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================
# Models
# =========================

class ExpenseCreate(BaseModel):
    amount: int
    tag: str


# =========================
# API
# =========================

@app.post("/expenses")
def add_expense_api(expense: ExpenseCreate):

    commands.add_expense(
        expense.amount,
        expense.tag
    )

    return {
        "message": "Expense added successfully"
    }


@app.get("/expenses")
def show_expenses_api():

    return commands.show_expenses()


@app.get("/expenses/total")
def show_total_api():

    return commands.show_total()


@app.delete("/expenses/{expense_id}")
def delete_expense_api(expense_id: int):

    return commands.delete_expense(expense_id)


@app.put("/expenses/{expense_id}")
def edit_expense_api(
    expense_id: int,
    expense: ExpenseCreate
):

    return commands.edit_expense(
        expense_id,
        expense.amount,
        expense.tag
    )


@app.get("/expenses/tag/{tag}")
def show_by_tag_api(tag: str):

    return commands.show_by_tag(tag)


@app.get("/expenses/biggest")
def show_biggest_api():

    return commands.get_high_amount()


@app.get("/expenses/tag/{tag}/total")
def show_total_by_tag_api(tag: str):

    return commands.all_by_tag(tag)


# =========================
# Frontend
# =========================

@app.get("/")
def read_root():

    return FileResponse(FRONTEND_DIR / "menu.html")


app.mount(
    "/",
    StaticFiles(directory=FRONTEND_DIR),
    name="frontend"
)
