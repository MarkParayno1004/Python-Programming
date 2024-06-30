import math

is_house_price = 10 ** 6
has_good_credit = True

if has_good_credit:
    print("10% downpayment is needed")
    down_payment = math.ceil(is_house_price * 0.1)
else:
    print("20% downpayment is needed")
    down_payment = math.ceil(is_house_price * 0.2)

print(f'Total Down Payment: ${down_payment}')