Number = int(input("Enter Amount:"))


def mod(a, b):
    return a % b


def div(a, b):
    return a / b


if mod(Number, 500) == 0:
    print("500 Notes:", int(div(Number, 500)))
else:
    print("500 Notes:", int(div(Number, 500)))
    Number = Number - (int(div(Number, 500)) * 500)
    if mod(Number, 200) == 0:
        print("200 Notes:", int(div(Number, 200)))

    else:
        print("200 Notes:", int(div(Number, 200)))
        Number = Number - (int(div(Number, 200)) * 200)
        print("100 Notes:", int(div(Number, 100)))

