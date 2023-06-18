# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.


def nMin(a,b):
    m = a*b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)

def nMax(a,b):
    while a!= 0 and b!= 0:
        if a>b:
            a%=b
        else:
            b%=a
    return a+b
   


num1=input('введите дробь вида a/b:  ')
num2=input('введите дробь вида a/b:  ')
s1=num1.split('/')
s2=num2.split('/')
value=nMin(int(s1[1]),int(s2[1]))
n1=value/int(s1[1])
n2=value/int(s2[1])
answerSum=str(int((int(s1[0])*n1)+(int(s2[0])*n2)))+'/'+str(value)
print('sum: ',answerSum)

numerator=int(s1[0])*int(s2[0])
denominator=int(s1[1])*int(s2[1])

if nMax(numerator,denominator)!=0:
    product=str(int(numerator/nMax(numerator,denominator)))+'/'+str(int(denominator/nMax(numerator,denominator)))
print('Произведение: ',product)