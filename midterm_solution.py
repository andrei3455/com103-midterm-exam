run_program = True
while run_program:
    error = False

    student_name = input("Student name: ")
    if student_name == "":
        error = True
    if " " in student_name:
        error = True

    if error == False:
        budget_str = input("Weekly budget: ")
        if budget_str == "":
            error = True
        if " " in budget_str:
            error = True
        for char in budget_str:
            if char not in "0123456789":
                error = True

    if error == False:
        budget = int(budget_str)
        threshold = budget * 25 / 100

        print("")
        print("==========================================")
        print("   WEEKLY EXPENSE -- CATEGORIES")
        print("==========================================")

        categories = [
            "Food & Drinks       [e.g. Lunch, snacks, coffee]",
            "Transportation      [e.g. Bus, jeepney, ride-share]",
            "Mobile / Internet   [e.g. Load, data plan, WiFi top-up]",
            "School Supplies     [e.g. Notebook, pen, bond paper]",
            "Entertainment       [e.g. Games, movies, hangout]"
        ]

        short_cats = [
            "Food & Drinks",
            "Transportation",
            "Mobile / Internet",
            "School Supplies",
            "Entertainment"
        ]

        idx = 1
        for c in categories:
            print(f" {idx}. {c}")
            idx = idx + 1

        print("==========================================")
        print("")

        total_spent = 0
        count = 0

        log1_1 = ""
        log1_2 = ""
        log2_1 = ""
        log2_2 = ""
        log3_1 = ""
        log3_2 = ""
        log4_1 = ""
        log4_2 = ""

        for i in [1, 2, 3, 4]:
            if error == False:
                print(f"--- EXPENSE {i} ---")
                cat_in = input("Category (0 to skip): ")
                
                if cat_in == "":
                    error = True
                if " " in cat_in:
                    error = True
                for char in cat_in:
                    if char not in "0123456789":
                        error = True

                if error == False:
                    cat_num = int(cat_in)
                    if cat_num < 0:
                        error = True
                    if cat_num > 5:
                        error = True

                    if error == False:
                        if cat_num == 0:
                            print("")
                        if cat_num > 0:
                            desc = input("Description: ")
                            if desc == "":
                                error = True
                            if desc[0:1] == " ":
                                error = True

                            if error == False:
                                amt_in = input("Amount: ")
                                if amt_in == "":
                                    error = True
                                if " " in amt_in:
                                    error = True
                                for char in amt_in:
                                    if char not in "0123456789":
                                        error = True

                                if error == False:
                                    amt = int(amt_in)
                                    total_spent = total_spent + amt
                                    count = count + 1

                                    flag = ""
                                    if amt > threshold:
                                        flag = "  ! High Expense Alert!"

                                    cat_name = short_cats[cat_num - 1]
                                    line1 = f"  [{count}] {cat_name}"
                                    line2 = f"      {desc}                  P{amt}.00{flag}"

                                    if count == 1:
                                        log1_1 = line1
                                        log1_2 = line2
                                    if count == 2:
                                        log2_1 = line1
                                        log2_2 = line2
                                    if count == 3:
                                        log3_1 = line1
                                        log3_2 = line2
                                    if count == 4:
                                        log4_1 = line1
                                        log4_2 = line2
                                    print("")

        if error == False:
            rem = budget - total_spent
            status = "Budget OK! Keep it up."
            if rem < 0:
                status = "Overspent! Reduce spending."

            upper_name = ""
            for char in student_name:
                if char == "a": upper_name = upper_name + "A"
                elif char == "b": upper_name = upper_name + "B"
                elif char == "c": upper_name = upper_name + "C"
                elif char == "d": upper_name = upper_name + "D"
                elif char == "e": upper_name = upper_name + "E"
                elif char == "f": upper_name = upper_name + "F"
                elif char == "g": upper_name = upper_name + "G"
                elif char == "h": upper_name = upper_name + "H"
                elif char == "i": upper_name = upper_name + "I"
                elif char == "j": upper
