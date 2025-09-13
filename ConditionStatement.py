age = 18

if age >= 18:
    print("You are an adult.")

age = 6

if age >= 18:
    print("Adult")
else:
    print("Not adult")


marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# ternary operator

age = 20
status = "Adult" if age >= 18 else "Not Adult"
print(status)


day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Other day")

match day:
    case 1 | 2 | 3:
        print("Weekday")
    case _ as d:
        print(f"Other day: {d}")
