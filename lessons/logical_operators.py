""" 
Logical Operators
> and: both should be true
> or: atleast one should be true
> not: inverses any boolean value
"""

has_high_income = True
has_good_credit = True
has_criminal_record = False

if has_high_income and not has_criminal_record:
    print('Eligable for loan')

