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
