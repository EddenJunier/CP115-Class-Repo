name = input()
price = float(input())
quantity = int(input())
member_answer = input()

order_total = price * quantity
free_shipping = order_total >= 100
is_member = member_answer

print(name.upper())
print(order_total)
print(free_shipping)
print(is_member)
