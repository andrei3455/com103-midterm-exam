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
