import database


def add_expense(amount, tag):
    database.add_expense(amount, tag)


def show_expenses():
    expenses = database.get_expenses()
    return expenses


def show_total():
    total = database.get_total()
    return (f"Total Expenses: {total}")


def delete_expense(expense_id):
    result = database.delete_expense(expense_id)
    if result == 0:
        return ("not deleted. try again later")
    else:
        return ("done")


def edit_expense(id, amount, tag):
    result = database.update_expense(id, amount, tag)
    if result == 0:
        return ("not updated. try again later")
    else:
        return ("done")


def show_by_tag(tag):
    expenses = database.get_expenses_by_tag(tag)

    if expenses == []:
        return ("failed")
    else:
        return (expenses)


def amount_verification(value):
    return value.isdigit() and value != "0"


def id_verification(id_value):
    if id_value.isdigit():
        integer_id = int(id_value)
        all_ids = database.get_all_ids()
        return integer_id in all_ids
    else:
        return False


def get_high_amount():
    expenses = database.get_expenses()

    if expenses:
        return max(expenses, key=lambda expense: expense[1])
    else:
        return None


def all_by_tag(tag2):
    all_expenses = database.get_expenses_by_tag(tag2)

    total = sum(expense[1] for expense in all_expenses)

    return (total)


def tag_verification(tag_value):
    if tag_value != "":
        all_tags = database.get_all_tags()
        return tag_value in all_tags
    else:
        return False
