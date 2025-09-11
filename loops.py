age = 23
is_member = True

if age >= 18 and age <= 25 and is_member:
    discount = 15
elif is_member:
    discount = 10
else:
    discount = 0

print(f"Your Discount: {discount}%")
