def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[0 : pick]
    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:  
            tmp = xor('0'*pick, tmp) + dividend[pick]
        pick += 1
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)
    checkword = tmp
    return checkword

def CRC_gen(dataword, word_size, CRC_type) :
    if CRC_type == 0 :
        #CRC-32
        divisor = "100000100110000010001110110110111"
    elif CRC_type == 1 :
        #CRC-24
        divisor = "1100000000101000100000001"
    elif CRC_type == 2 :
        #CRC-16
        divisor = "11000000000000101"
    elif CRC_type == 3 :
        #Reversed CRC-16
        divisor = "10100000000000011"
    elif CRC_type == 4 :
        #CRC-8
        divisor = "111010101"
    elif CRC_type == 5 :
        #CRC-4
        divisor = "11111"
    else :
        print("========================")
        print("Type of CRC is Invalid")
        print("========================")
        exit()
    l_divisor = len(divisor)
    appended_dataword = dataword + '0'*(l_divisor-1)
    remainder = mod2div(appended_dataword, divisor)
    print(appended_dataword ," % ",divisor)
    print("= ",remainder)
    
    codeword = dataword + remainder
    return codeword
        
def CRC_check(codeword, CRC_type):
    if CRC_type == 0 :
        #CRC-32
        divisor = "100000100110000010001110110110111"
    elif CRC_type == 1 :
         #CRC-24
        divisor = "1100000000101000100000001"
    elif CRC_type == 2 :
         #CRC-16
        divisor = "11000000000000101"
    elif CRC_type == 3 :
        #Reversed CRC-16
        divisor = "10100000000000011"
    elif CRC_type == 4 :
        #CRC-8
        divisor = "111010101"
    elif CRC_type == 5 :
        #CRC-4
        divisor = "11111"
    else :
        print("========================")
        print("Type of CRC is Invalid")
        print("========================")
        exit()
    l_divisor = len(divisor)
    appended_codeword = codeword + '0'*(l_divisor-1)
    remainder = mod2div(appended_codeword, divisor)
    print(appended_codeword ," % ",divisor)
    print("= ",remainder)
    if remainder == '0'*(l_divisor-1) :
        return "PASS"
    else :
        return "FAIL"
    
def binary_check(dataword) :
    if len(dataword) < 5 :
        print("========================")
        print("Word size must be atleast 5")
        print("========================")
        exit()
    for i in dataword :
        if i != '0' and i != '1' :
            print("========================")
            print("dataword should contain only '0' and '1'")
            print("========================")
            exit()

#== Main ==#
print("CRC")
print("========================")
print("Type of services")
print("   0 : crc-generator")
print("   1 : crc-checker")
service_type = int(input("Insert value: "))
if service_type == 0 :
    #CRC-Generator
    print("---------------------")
    print("CRC-Generator")
    print("---------------------")
    dataword = input("Dataword: ")
    binary_check(dataword)
    word_size = len(dataword)
    print("---------------------")
    print("CRC-Type")
    print("   0 : CRC-32")
    print("   1 : CRC-24")
    print("   2 : CRC-16")
    print("   3 : Reversed CRC-16")
    print("   4 : CRC-8")
    print("   5 : CRC-4")
    CRC_type = int(input("Insert value: "))
    print("---------------------")
    codeword = CRC_gen(dataword, word_size, CRC_type)
    print("========================")
    print("output : ",codeword)
    print("========================")
elif service_type == 1:
    #CRC-Checker
    print("---------------------")
    print("CRC-Checker")
    print("---------------------")
    codeword = input("codeword: ")
    binary_check(codeword)
    print("---------------------")
    print("CRC-Type")
    print("   0 : CRC-32")
    print("   1 : CRC-24")
    print("   2 : CRC-16")
    print("   3 : Reversed CRC-16")
    print("   4 : CRC-8")
    print("   5 : CRC-4")
    CRC_type = int(input("Insert value: "))
    print("---------------------")
    validity = CRC_check(codeword, CRC_type)
    print("========================")
    print("output : ",validity)
    print("========================")
else :
    print("========================")
    print("Type of services is Invalid")
    print("========================")