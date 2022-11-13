num_list = []
largest_num = 0


for n in range(10):
    num_list.append(int(input(f"Enter Number {n+1}: ")))

for m in range(len(num_list)):
    if num_list[m] > largest_num:
        largest_num = num_list[m]

print(f"{largest_num} is our largest number.")