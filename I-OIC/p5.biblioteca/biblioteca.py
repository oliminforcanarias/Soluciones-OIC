import fileinput

estanteria = ""
libros = ""
cnt = 0
actual = 0
actual_min = 0

for line in fileinput.input():
    code = line.strip()
    
    if len(str(code)) == 1:
        estanteria = code
    else:
        libros = code.split(" ")
        
        for i in libros:
            if i[0] == estanteria:
                actual = int(i[1:])
                if actual_min <= actual:
                    actual_min = actual
                else:
                    cnt += 1
                    actual_min = actual
            else:
                cnt += 1
        actual = 0
        actual_min = 0
        print(str(cnt))
        cnt = 0