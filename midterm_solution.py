student_name = input("Student name: ")
weekly_budget = float(input("Weekly budget: "))

categories = [
    "Food & Drinks       [e.g. Lunch, snacks, coffee]",
    "Transportation      [e.g. Bus, jeepney, ride-share]",
    "Mobile / Internet   [e.g. Load, data plan, WiFi top-up]",
    "School Supplies     [e.g. Notebook, pen, bond paper]",
    "Entertainment       [e.g. Games, movies, hangout]"
]

category_names = [
    "Food & Drinks",
    "Transportation",
    "Mobile / Internet",
    "School Supplies",
    "Entertainment"
]

print("==========================================")
print("   WEEKLY EXPENSE -- CATEGORIES")
print("==========================================")
count = 1
for cat in categories:
    print(count, ". ", cat)
    count = count + 1
print("==========================================")

total_spent = 0
expense_display_count = 0
high_expense_limit = weekly_budget * 0.25
report_lines = []

for i in [1, 2, 3, 4]:
    print(" ")
    print("--- EXPENSE", i, "---")
    cat_choice = int(input("Category (0 to skip): "))
    
    if cat_choice >= 1 and cat_choice <= 5:
        description = input("Description: ")
        amount = float(input("Amount: "))
        
        alert = ""
        if amount > high_expense_limit:
            alert = " ! High Expense Alert!"
        
        total_spent = total_spent + amount
        expense_display_count = expense_display_count + 1
        
        name_only = category_names[cat_choice - 1]
        
        report_lines.append("[" + str(expense_display_count) + "] " + name_only)
        report_lines.append("      " + description + "              P" + str(amount) + alert)

remaining = weekly_budget - total_spent
status = "Budget OK! Keep it up."
if remaining < 0:
    status = "Overspent! Reduce spending."

print(" ")
print("======================================================")
print("     ", student_name.upper(), "-- WEEKLY EXPENSE LOG")
print("======================================================")
print(" Weekly Budget : P" + str(weekly_budget))

for line in report_lines:
    print(line)

print("------------------------------------------------------")
print(" Total Spent   : P" + str(total_spent))
print(" Remaining     : P" + str(remaining))
print(" Status        : ", status)
print("======================================================")
