list = []
price = []
l1 = input("enter first product name:")
list.append(l1)
s1 = int(input("enter the price of first product:"))
price.append(s1)
l2 = input("enter second product name:")
list.append(l2)
s2 = int(input("enter the price of second product:"))
price.append(s2)
l3 = input("enter third product name:")
list.append(l3)
s3 = int(input("enter the price of third product:"))
price.append(s3)
l4 = input("enter fourth product name:")
list.append(l4)
s4 = int(input("enter the price of fourth product:"))
price.append(s4)
list.sort()
price.sort()
print("products in the list are:", list)
print("prices in the list are:", price)

print("sum of the prices is :", sum(price))


