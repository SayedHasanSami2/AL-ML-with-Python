numbers = input()
x = numbers.split()
first_num = int(x[0])
second_num = int(x[1])
third_num = int(x[2])
max = first_num
if second_num > max:
    max = second_num
if third_num > max:
    max = third_num 
min = first_num
if second_num < min:
    min = second_num 
if third_num < min:
    min = third_num 
print(min, max)
