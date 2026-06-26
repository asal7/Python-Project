num = 100
sum_num = 0
count = 0

for i in range(num, 1000, 2):
    sum_num = sum_num + i
    count = count + 1

avg = sum_num / count
print("میانگین اعداد زوج سه رقمی", avg)