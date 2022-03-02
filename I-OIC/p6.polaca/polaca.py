import fileinput

def check_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def RPN(operacion):
    pila=[]
    cnt=0
    for i in operacion:
        if check_float(i):
            pila.append(float(i))
        else:
            try:
                num1 = pila.pop()
                num2 = pila.pop()
            except:
                return "ERROR"
            
            if i=="+":
                pila.append(float(num2+num1))
                cnt+=1
            elif i=="-":
                pila.append(float(num2-num1))
                cnt+=1
            elif i=="*":
                pila.append(float(num2*num1))
                cnt+=1
            elif i=="/":
                pila.append(float(num2/num1))
                cnt+=1
            elif i=="^":
                pila.append(float(num2**num1))
                cnt+=1
            elif i=="%":
                pila.append(float(num2%num1))
                cnt+=1
            else:
                return "ERROR"
    if cnt==0:
        return "ERROR"
    else:
        result = pila.pop()
        if result.is_integer():
            return int(result)
        else:
            return round(result, 4)

for line in fileinput.input():
    operacion = line.strip().split()
    print(str(RPN(operacion)))