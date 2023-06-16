# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата
number=int(input('Введите число: '))
hexlist=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
numberHex=[]
s=''
print('Проверка: ',hex(number)[2:])
while number>0:
    numberHex.append(number%16)
    number//=16
numberHex.reverse()
for i in range(len(numberHex)):
    numberHex[i]=hexlist[numberHex[i]]
    s=s+str(numberHex[i])
print('Полученый рещультат: ',s)
