def numberCategories(num):
    if(num > 0):
        return "positive"
    elif(num < 0):
        return "negative"
    else:
        return 4

print("3",numberCategories(3))
print("-3",type(numberCategories(-3)))
print("0",type(numberCategories(0)))


def numberCategoriesSwtich(num):
    match num:
        case num if num > 0:
            return "+ve"
        case num if num < 0:
            return "-ve"
        case _:
            return "0"
print("3",numberCategoriesSwtich(3))
print("-3",numberCategoriesSwtich(-3))
print("0",type(numberCategoriesSwtich(0)))
