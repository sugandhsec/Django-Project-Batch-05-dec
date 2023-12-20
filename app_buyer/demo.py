import random
# print(random.randint(100000,999999))
list1=["a","4","p","8","c"]
a=random.choices(list1,k=9)

print("".join(a))