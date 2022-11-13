user_input = int(input("Enter Budget Price: "))

if user_input < 500000 or user_input > 300000:
    down_payment = user_input * 10/ 100
    print(f' Your down payment is {down_payment}')

if user_input > 500000:
    down_payment = user_input * 20/ 100
    print(f' Your down payment is {down_payment}')