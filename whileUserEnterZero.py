num = int(input("Enter a number: "))
sum_num_even = 0
sum_num_odd = 0

while num != 0:
    if num % 2 == 0:
        sum_num_even = sum_num_even + num
    else:
        sum_num_odd = sum_num_odd + num
    num = int(input("Enter a number: "))

print("مجموع اعداد زوج: ", sum_num_even)
print("مجموع اعداد فرد: ", sum_num_odd)