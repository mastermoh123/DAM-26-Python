num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

for i in range(num1, num2):
    if(i % 7 == 0):
        print(i)