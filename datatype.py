# Q1
국어 = 80
영어 = 75
수학 = 55
avg = (국어+영어+수학)/3
print(avg)

# Q2
num = 13
if (num%2 == 0):
    print("짝수")
else:
    print("홀수")

# Q3
pin = "881120-1068234"
birth = pin[0:6]
onum = pin[7:14]
print(birth)
print(onum)

# Q4
print(pin[7])

# Q5
a = "a:b:c:d"
a = a.replace(":", "#")
print(a)

# Q6
l = [1, 3, 5, 4, 2]
l.sort()
print(l)

# Q7
sen = ["Life", "is", "too", "short"]
print(" ".join(sen))

# Q8
#t1 = (1, 2, 3)
#t1 = t1 + tuple(4)
#print(t1)

# Q9
'''
2
'''

# Q10
aa = {"A": 90, "B": 80, "C": 70}
aa.pop("B")

# Q11
adup = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
adup = set(adup)
print(adup)

# Q12
a = b = [1, 2, 3]
a[1] = 4
print(b)
