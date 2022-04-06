
def binary_check(dataword) :
    if len(dataword) < 5 :
        print("=================================================")
        print("Word size must be atleast 5")
        print("=================================================")
        exit()
    for i in dataword :
        if i != '0' and i != '1' :
            print("=================================================")
            print("dataword should contain only '0' and '1'")
            print("=================================================")
            exit()

def Checksum_gen(dataword, word_size, num_block):
    all_sum=0
    for i in range(len(dataword)):
        if len(dataword[i])!= word_size:
            dataword[i] = dataword[i].zfill(word_size) #add 0 to front if size < word_size
        all_sum = all_sum + int(dataword[i],2) #to base 10
    all_sum = str(bin(all_sum)[2:]) #to base 2
    print('all_sum',all_sum)
    if len(all_sum) > word_size:
        front = str(all_sum)[:-word_size] #cut
        print("front :",front)
        base = str(all_sum)[-word_size:] #cut
        print("base :",base)
        
        front = int(front,2)
        base = int(base,2)
        all_sum = front + base
        
        all_sum = str(bin(all_sum)[2:])
        print('all_sum', all_sum)
        all_sum = all_sum.zfill(word_size)
    checksum=''
    for i in all_sum:
        if i=="1":
            checksum = checksum + '0'
        else:
            checksum = checksum + '1'
    return checksum

listdata = []
num_block = int(input('how many word '))
for i in range(num_block):
    listdata.append(str(input()))
    binary_check(listdata[i])
    if(i==0):
        word_size = len(listdata[i])
    elif len(listdata[i])>word_size:
        word_size = len(listdata[i])
print('listdata',listdata)
print('word_size',word_size)
codeword = Checksum_gen(listdata,word_size,num_block)
print('codeword',codeword)
listdata.append(codeword)
print('The pattern codeword',listdata)