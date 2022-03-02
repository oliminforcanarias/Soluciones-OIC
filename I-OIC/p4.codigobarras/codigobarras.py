import fileinput

for line in fileinput.input():
    code = line.strip()

    if code.isnumeric() and (len(str(code)) == 7):
      str(code)
      sum1 = int(code[1]) + int(code[3]) + int(code[5] )
      sum2 = 3 * (int(code[0]) + int(code[2]) + int(code[4]) + int(code[6]))
      checksum_value = sum1 + sum2
    
      checksum_digit = 10 - (checksum_value % 10)
      if (checksum_digit == 10):
        checksum_digit = 0
      code = code + str(checksum_digit)
      print(code)
    else:
      print("ERROR")