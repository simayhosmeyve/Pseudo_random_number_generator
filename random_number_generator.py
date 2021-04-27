#Simay Hoşmeyve
#180401017

def prime_number():
    lower = 2
    upper = 19997
    for num in range(lower, upper + 1):
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            prime_numbers.append(num)

def gcd(p,q):
    while q != 0:
        p, q = q, p%q
    return p

def is_coprime(num1, num2):
    return gcd(num1, num2) == 1

prime_numbers = []
prime_number()

#print(prime_numbers)
import random

m = 2**15
a = random.choice(prime_numbers)
x0 = random.choice(prime_numbers)
c = 0

#print("Gcd:",gcd(13,47))
#print("Coprime:",is_coprime(13,47))

print("m:",m,"a:",a,"x0:",x0,"c:0")

while(a==x0 or is_coprime(m,x0)==False):
    a = random.choice(prime_numbers)

count = int(input('Rastgele sayilarin uretilecegi dizi uzunlugu: '))

file = open("numbers.txt", "a")
file.write("Uretilen sozde rastgele sayi dizisi:  ")
file.write(str(x0) + ",")
print("seed:", x0)

test_array = []
test_array.append(x0)
for i in range(count-1):
    x1 = (a * x0 + c) % m
    print("(", a, "*", x0, "+", c, ")", "mod(", m, ") =", x1)
    if(i!=count-2):
        file.write(str(x1) + ",")
        test_array.append(x1)
        x0=x1
    else:
        file.write(str(x1))
        test_array.append(x1)
file.write("\n")
file.close()

#print(test_array)
from matplotlib import pyplot as plt
plt.plot(test_array)
plt.title('Lehmer algoritması ile sözde random dizi')
plt.xlabel("Dizi elemanları")
plt.ylabel("Değerler")
plt.show()