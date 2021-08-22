#Q1
def is_odd(a):
    if a%2 == 0:
        print("EVEN")
    else:
        print("ODD")
is_odd(10)

#Q2
def avg(*args):
    a = 0
    for i in args:
        a += i
    return a/len(args)
print(avg(90, 80, 50, 60))


#Q3
input1 = int(input("첫번째 숫자를 입력하세요: "))
input2 = int(input("두번째 숫자를 입력하세요: "))

total = input1 + input2
print("두 수의 합은 %s입니다.." %total)

#Q4
#3
print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))

#Q5
f1 = open("test.txt", "w")
f1.write("Life is too short")
f1.close()
f2 = open("test.txt", "r")
print(f2.read())

#Q6

with open("test.txt", "a") as f:
    f.write("\nyou need java")
    
#Q7
with open("test.txt", "r") as f:
    a = f.read()
a = a.replace("java", "python")
with open("test.txt", "w") as f:
    f.write(a)
