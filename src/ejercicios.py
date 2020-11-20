def factorial(num):
    resultado = 1
    if num == 0 or num == 1 or num == -0:
        resultado = 1
    elif num < 0:
        resultado = -1
    else:
        for i in range(1,num+1):
            resultado = resultado * i
    return resultado


def leapYear(num):    
    if num <= 0:
        return (-1)
    elif (num % 400 == 0) or (num % 4 == 0 and num % 100 != 0):
        return (1)
    else:
        return (-1)
     

def daysInMonth(num,num1):  
    if num <= 0 or num1 <= 0:
        return (-1)
    elif leapYear(num1) == 1 and num == 2:
        return (29)
    elif num == 2:
        return (28)
    elif num == 1 or num == 3 or num == 5 or num == 7 or num==8 or num == 10 or num ==12:
        return (31)
    elif num == 4 or num == 6 or num==9 or num==11:
        return (30)
    return (-1)

def dayOfWeek(num,num1,num2):
    a = int((14 - num1) / 12)
    y = num2 - a
    m = num1 + 12 * a - 2
    d = (num + y + int(y/4) - int(y/100) + int(y/400) + int((31*m)/12)) % 7
    return (d)

def myPower(base,potencia):
    contador = 1
    operacion = base
    if potencia < 0:
        return (-1)
    if potencia == 0:
        return (1)
    else:
        while potencia != contador:
            contador = contador + 1
            base = operacion * potencia
            return (base)
        
def numberOfNumbers(numero):
    if numero<0:
        return -1
    cont=1
    while numero > 9:
        numero=numero/10
        cont+=1
    return cont
    
def isPrime(numero):
    if numero<=0:
        return -1
    cont=0
    for i in range(1,numero+1):
        if numero%i==0:
            cont+=1
    if cont>2:
        return 0
    else:
        return 1
    
def secondOrder(a,b,c):
    #if a<0 or b<0 or c<0:
        #return -1
    solucion=(b*b)-(4*a*c)
    if solucion<0:
        return 0
    elif solucion==0:
        return 1
    else:
        return 2
    
def numberDivisorPrime(numero):
#     if numero<0:
#         return -1
    cont=0
    for i in range(1,numero+1):
        if numero%i==0:
            if isPrime(i)==1:
                cont+=1
    return cont 

def friend(numero1,numero2):
    if numero1<0 or numero2<0:
        return False
    cont=0
    for i in range(1,numero1):
        if numero1%i==0:
            cont=cont+i
    cont2=0
    for i in range(1,numero2):
        if numero2%i==0:
            cont2=cont2+i
    if cont ==numero2 and cont2==numero1:
        return True 
    else:
        return False
        
            
            
               
        