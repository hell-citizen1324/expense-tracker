from commands import *
import database

database.create_table()
# menu
while True:
    print("===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Show Total")
    print("4. Delete Expense")
    print("5. Edit Expense")
    print("6. Show By Tag")
    print("7. Show Bigest use")
    print("8. Show Total By Tag")
    print("9. Exit")
    choice = input("enter code or object: ").lower()
    # procces
    if choice in ["1", "add expense", "۱"]:
        amount = input("enter amount of money: ")
        tag = input("please leave a tag for it: ")
        if amount_verification(amount) and not tag == "":
            final_amount_1 = int(amount)
            add_expense(final_amount_1, tag)
            print("added succesfully.")
    elif choice in ["2", "show expenses", "۲"]:
        show_expenses()
    elif choice in ["3", "show total", "۳"]:
        show_total()
    elif choice in ["9", "exit", "۹"]:
        print("goodbye")
        break
    elif choice in ["4", "delete expense", "۴"]:
        delete_expense_id = input("please enter ID of target expense: ")
        if id_verification(delete_expense_id):
            final_delete_expense_id = int(delete_expense_id)
            delete_expense(final_delete_expense_id)
            print("deleted")
        else:
            print("something went wrong")
    elif choice in ["5", "edit expense", "۵"]:
        edit_expense_id = input("please enter ID of target expense: ")
        new_amount = input("please enter new amount: ")
        new_tag = input("please enter new tag: ")
        if amount_verification(new_amount) and tag_verification(new_tag) and id_verification(edit_expense_id):
            final_expense_id = int(edit_expense_id)
            final_amount = int(new_amount)
            edit_expense(final_expense_id, final_amount, new_tag)
        elif not amount_verification(new_amount):
            print("new amount must only contain numbers higher than zero")
        elif not id_verification(edit_expense_id):
            print("ID is not correct")
    elif choice in ["6", "show by tag", "۶"]:
        target_tag = input("please enter tag of target expense: ")
        if tag_verification(target_tag):
            show_by_tag(target_tag)
        else:
            print("invalid tag, try again")
    elif choice in ["7", "show biggest use", "۷"]:
        get_high_amount()
    elif choice in ["8", "show total by tag", "۸"]:
        target_tag2 = input("please enter tag of target expense: ")
        if tag_verification(target_tag2):
            all_by_tag(target_tag2)
        else:
            print("invalid tag, try again")
