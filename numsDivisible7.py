count = 0
sum_num = 0

for i in range(200, 800, 1):
    if i % 7 == 0:
        count = count + 1
        sum_num = sum_num + i
        print(i)

print("Count: ", count)