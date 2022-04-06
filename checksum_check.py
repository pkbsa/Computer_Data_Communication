def Checksum_check(codeword, word_size, num_blocks):
    sum_code = 0
    for i in codeword:
        sum_code = sum_code+ int(i,2)

    sum_code = str(bin(sum_code)[2:])
    checksum=''
    for i in str(sum_code):
        if i=="1":
            checksum = checksum + '0'
        else:
            checksum = checksum + '1'

    if int(checksum,2) == 0:
        return 1
    else:
        return 0

codeword = ['10101001', '00111001', '00011101']
word_size = 8
num_blocks = 3
validity = Checksum_check(codeword, word_size, num_blocks)
print('validity',validity)