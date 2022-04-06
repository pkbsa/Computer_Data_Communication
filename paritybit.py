def check_word(dataword, word_size):
    missing = word_size - len(dataword)
    for i in range (missing) :
        dataword += "0"
    return dataword
    
def parity_gen(dataword, word_size, parity_type, array_size) :
    total = 0;
    output_str = ''
    output_array = []
    if parity_type == 0 or parity_type == 1 :
        #one-dimensional-even,odd
        if parity_type == 0 :
            print("One-Dimensional-Even")
        else :
            print("One-Dimensional-Odd")
        for word in dataword :
            output_str_tmp = ''
            total = 0
            for i in word :
                output_str_tmp += i
                total = total + int(i);
                print(i," ",end="")
            if total%2 == 0 :
                if parity_type == 0 :
                    output_str_tmp += "0"
                    print("| 0",end="")
                else :
                    output_str_tmp += "1"
                    print("| 1",end="")
            else :
                if parity_type == 0 :
                    output_str_tmp += "1"
                    print("| 1",end="")
                else :
                    output_str_tmp += "0"
                    print("| 0",end="")
            print("")
            output_array.append(output_str_tmp)
        return output_array
    elif parity_type == 2 or parity_type == 3 :
        #two-dimensional-even,odd
        if parity_type == 2 :
            print("Two-Dimensional-Even")
        else :
            print("Two-Dimensional-Odd")
        for word in range (len(dataword)) :
            dataword[word] = check_word(dataword[word],word_size)
        sum_last = 0
        for word in dataword :
            total = 0
            output_str_tmp = ''
            for i in word :
                output_str_tmp += i
                total = total + int(i);
                print(i," ",end="")
            if total%2 == 0 :
                if parity_type == 2 :
                    output_str_tmp += '0'
                    print("| 0",end="")
                else :
                    output_str_tmp += '1'
                    print("| 1",end="")
            else :
                sum_last += 1
                if parity_type == 2 :
                    output_str_tmp += '1'
                    print("| 1",end="")
                else :
                    output_str_tmp += '0'
                    print("| 0",end="")
            print("")
            output_array.append(output_str_tmp)
        print("-------------------------")
        i=0;
        output_str_tmp = ''
        while(1):
            sumrow = 0
            for word in dataword :
                sumrow += int(word[i])
            if(sumrow%2 == 0):
                if parity_type == 2 :
                    output_str_tmp += '0'
                    print("0  ",end="")
                else :
                    output_str_tmp += '1'
                    print("1  ",end="")
            else :
                if parity_type == 2 :
                    output_str_tmp += '1'
                    print("1  ",end="")
                else :
                    output_str_tmp += '0'
                    print("0  ",end="")
            i+=1;
            if i == word_size : break
        if(sum_last%2== 0):
            if parity_type == 2 :
                output_str_tmp += '0'
                print("  0")
            else :
                output_str_tmp += '1'
                print("  1")
        else :
            if parity_type == 2 :
                output_str_tmp += '1'
                print("  1")
            else :
                output_str_tmp += '0'
                print("  0")
        output_array.append(output_str_tmp)
        return output_array
    else :
        print("========================")
        print("Type of parity is Invalid")
        print("========================")
        exit()
    return output_array;

def parity_check(codeword, parity_type, array_size) :
    output_array = []
    status_array = []
    if parity_type == 0 :
        #one-dimensional-even
        print("One-Dimensional-Even")
        for word in codeword:
            total = 0
            for i in word:
                total = total + int(i)
                print(i," ",end="")
            if(total%2 == 0) :
                print("| PASS")
                output_array.append("Codeword "+str(len(output_array)+1)+": Passed")
            else :
                print("| FAIL")
                output_array.append("Codeword "+str(len(output_array)+1)+": Failed")
        return output_array
    elif parity_type == 1 :
        #one-dimensional-odd
        print("One-Dimensional-Odd")
        for word in codeword:
            total = 0
            for i in word:
                total = total + int(i)
                print(i," ",end="")
            if(total%2 == 0) :
                print("| FAIL")
                output_array.append("Codeword "+str(len(output_array)+1)+": Failed")
            else :
                print("| PASS")
                output_array.append("Codeword "+str(len(output_array)+1)+": Passed")
        return output_array
    elif parity_type == 2 :
        #two-dimensional-even
        print("Two-Dimensional-Even")
        for word in codeword:
            total = 0
            for i in word:
                total = total + int(i)
                print(i," ",end="")
            if(total%2 == 0) :
                print("| PASS")
                status_array.append(1)
            else :
                print("| FAIL")
                status_array.append(0)
        print("-------------------------")
        i=0;
        output_str_tmp = ''
        while(1):
            sumrow = 0
            for word in codeword :
                sumrow += int(word[i])
            if(sumrow%2 == 0):
                print("P  ",end="")
                status_array.append(1)
            else :
                print("F  ",end="")
                status_array.append(0)
            i+=1;
            if i == len(word) : break
        print("")
        for i in status_array :
            if i == 0 :
                return "FAIL"
        return "PASS"
    elif parity_type == 3 :
        #two-dimensional-odd
        print("Two-Dimensional-Odd")
        for word in codeword:
            total = 0
            for i in word:
                total = total + int(i)
                print(i," ",end="")
            if(total%2 == 0) :
                print("| FAIL")
                status_array.append(0)
            else :
                print("| PASS")
                status_array.append(1)
        print("-------------------------")
        i=0;
        output_str_tmp = ''
        while(1):
            sumrow = 0
            for word in codeword :
                sumrow += int(word[i])
            if(sumrow%2 == 0):
                print("F  ",end="")
                status_array.append(0)
            else :
                print("P  ",end="")
                status_array.append(1)
            i+=1;
            if i == len(word) : break
        print("")
        for i in status_array :
            if i == 0 :
                return "FAIL"
        return "PASS"
    else :
        print("========================")
        print("Type of parity is Invalid")
        print("========================")
        exit()
    return output_array;

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
print("Parity bit")
print("========================")
print("Type of services")
print("   0 : parity-bit-generator")
print("   1 : parity-bit-checker")
service_type = int(input("Insert value: "))
if service_type == 0 :
    print("---------------------")
    print("Parity-Bit-Generator")
    print("---------------------")
    array_size = int(input("Array of dataword: "))
    print("---------------------")
    dataword = []
    word_size = 0
    for i in range (array_size) :
        currentword = input("Dataword "+str(i+1)+" : ")
        binary_check(currentword)
        dataword.append(currentword)
    for word in dataword :
        if len(word) > word_size:
            word_size = len(word)
    print("---------------------")
    print("Type of parity")
    print("   0 : one-dimensional-even")
    print("   1 : one-dimensional-odd")
    print("   2 : two-dimensional-even")
    print("   3 : two-dimensional-odd")
    parity_type = int(input("Insert value: "))
    print("---------------------")
    codeword = parity_gen(dataword, word_size, parity_type, array_size)
    print("========================")
    print("output : ",codeword)
    print("========================")
elif service_type == 1 :
    print("---------------------")
    print("Parity-Bit-Checker")
    print("---------------------")
    array_size = int(input("Array of codeword: "))
    print("---------------------")
    codeword = []
    check_lens = 0
    for i in range (array_size) :
        currentword = input("Codeword "+str(i+1)+" : ")
        check_lens = len(currentword)
        binary_check(currentword)
        codeword.append(currentword)  
    print("---------------------")
    print("Type of parity")
    print("   0 : one-dimensional-even")
    print("   1 : one-dimensional-odd")
    print("   2 : two-dimensional-even")
    print("   3 : two-dimensional-odd")
    parity_type = int(input("Insert value: "))
    print("---------------------")
    for word in codeword :
        if len(word) != check_lens and (parity_type == 2 or parity_type == 3) :
            print("========================")
            print("All codeword must have the same size")
            print("========================")
            exit() 
    validity = parity_check(codeword, parity_type, array_size)
    print("========================")
    print("output : ",validity)
    print("========================")
else:
    print("========================")
    print("Type of services is Invalid")
    print("========================")