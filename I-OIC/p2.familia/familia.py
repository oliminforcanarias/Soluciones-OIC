import fileinput

for line in fileinput.input():
    linea = line.strip().split()
    
    if len(linea) != 2:
        print ("ERROR")
    else:
        a = linea[0]
        b = linea[1]
        if a.isnumeric() and len(str(a)) == 4 and b.isnumeric() and len(str(b)) == 4:
            a = int(a)
            b = int(b)
            if (b-a < 44) and (b-a >= 22) and (a==1926):
                print ("HIJO")
            elif (b-a < 66) and (b-a >= 44) and (a==1926):
                print ("NIETO")
            elif (b-a >= 66) and (a==1926):
                print ("BISNIETO")
            else:
                print("ERROR")
        else:
            print ("ERROR")