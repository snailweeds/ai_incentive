'''
1 in [1, 2, 3] => True
1 not in [1, 2, 3] => False
j not in "python" => True
'''
a = [1, 2, 3, 4]
result = [num*3 for num in a if num%2 == 0]
print(result)

b = [x*y for x in range(2, 10)
         for y in range(1, 10)]
print(b)

#Q1
code = "Life is too short, you need python"
if "wife" in code:
    print("wife")
elif "python" in code and "you" not in code:
    print("python")
elif "shirt" not in code:
    print("shirt")
else:
    print("none")

#Q2
num = 0
sum = 0
while(num < 1000):
    num = num + 1
    if num%3 == 0:
        sum = num + sum
    else:
        continue
print(sum)

#Q3
star = 0
while(star < 5):
    star = star + 1
    print("*" * star)


#Q4
for i in range(1, 101):
    print(i)

#Q5
sum = 0
score = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
for i in score:
    sum = sum+i
avg = sum/len(score)
print(avg)

#Q6
numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n%2 == 1]
print(result)
