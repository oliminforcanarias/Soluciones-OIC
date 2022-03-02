import fileinput

code = ""
control=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]

for line in fileinput.input():
    code = line.strip()

    if code.isnumeric() and (len(str(code)) == 8):
        code=int(code)
        print(str(code)+control[code%23])
    else:
        print("ERROR")