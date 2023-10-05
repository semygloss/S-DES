'''以下与生成密钥ki有关'''
# S盒子
import re

S0 = [[1, 0, 3, 2],
      [3, 2, 1, 0],
      [0, 2, 1, 3],
      [3, 1, 0, 2]]

S1 = [[0, 1, 2, 3],
      [2, 3, 1, 0],
      [3, 0, 1, 2],
      [2, 1, 0, 3]]


# 置换P10
def P10(key):
    return key[2] + key[4] + key[1] + key[6] + key[3] + key[9] + key[0] + key[8] + key[7] + key[5]


# 左移
# def Shift(key, n):
#     key = key[n:].ljust(5, '0')
#     print(key)
#     return key

def Shift(key,n):
    if n==1:
        return key[1]+key[2]+key[3]+key[4]+key[0]
    elif n==2:
        return key[2]+key[3]+key[4]+key[0]+key[1]
    else:
        return 0


# 置换P8
def P8(key):
    return key[5] + key[2] + key[6] + key[3] + key[7] + key[4] + key[9] + key[8]


'''以下与明文处理有关'''


# 初始置换IP
def IP(value):
    return value[1] + value[5] + value[2] + value[0] + value[3] + value[7] + value[4] + value[6]


# 最终置换逆IP
def IP_re(value):
    return value[3] + value[0] + value[2] + value[4] + value[6] + value[1] + value[7] + value[5]


# 置换P4
def P4(value):
    return value[1] + value[3] + value[2] + value[0]


# 映射F
def F(Rvalue, K):
    Rvalue_EP = Rvalue[3] + Rvalue[0] + Rvalue[1] + Rvalue[2] + Rvalue[1] + Rvalue[2] + Rvalue[3] + Rvalue[0]
    result = (bin(int(Rvalue_EP, 2) ^ int(K, 2))[2:]).rjust(8, '0')
    result_L = result[:4]
    result_R = result[4:]
    PL_row = int(result_L[0] + result_L[3], 2)
    PL_col = int(result_L[1] + result_L[2], 2)
    PL = (bin(S0[PL_row][PL_col])[2:]).rjust(2, '0')
    PR_row = int(result_R[0] + result_R[3], 2)
    PR_col = int(result_R[1] + result_R[2], 2)
    PR = (bin(S1[PR_row][PR_col])[2:]).rjust(2, '0')
    F_result = P4(PL + PR)
    return F_result


# 复合函数Fk
def Fk(L, R, SK):
    F_result = F(R, SK)
    L = bin(int(L, 2) ^ int(F_result, 2))[2:].rjust(4, '0')
    Fk_result = L + R
    return Fk_result


# SW置换
def SW(value):
    return value[4:] + value[:4]


# 加密,输入明文，明文为ascii用第一个条件
def Encry(plaintext, key):
    ciphertext = []
    if re.search('^[01]+$', plaintext) is None:  # 判断字符串中是否只含0或1，trans返回文本array
        for i in range(len(trans_ASC(plaintext))):
            plaintext_asc = trans_ASC(plaintext)[i]
            # print(plaintext_asc)
            plaintext_IP = IP(plaintext_asc)
            print(P10(key)[:5])
            K1 = P8(Shift(P10(key)[:5], 1) + Shift(P10(key)[5:], 1))
            K2 = P8(Shift(Shift(P10(key)[:5], 1), 2) + Shift(Shift(P10(key)[5:], 1), 2))
            print('K1:')
            print(K1)
            print('K2:')
            print(K2)
            plaintext_Fk1 = Fk(plaintext_IP[:4], plaintext_IP[4:], K1)
            plaintext_Fk1 = SW(plaintext_Fk1)
            plaintext_Fk2 = Fk(plaintext_Fk1[:4], plaintext_Fk1[4:], K2)
            ciphertext.append(IP_re(plaintext_Fk2))
            # print(ciphertext)
        return get_ASC(ciphertext)

    elif re.search('^[01]+$', plaintext):
        plaintext_IP = IP(plaintext)
        print(plaintext_IP)
        K1 = P8(Shift(P10(key)[:5], 1) + Shift(P10(key)[5:], 1))
        K2 = P8(Shift(Shift(P10(key)[:5], 1), 2) + Shift(Shift(P10(key)[5:], 1), 2))
        print('K1:')
        print(K1)
        print('K2:')
        print(K2)
        plaintext_Fk1 = Fk(plaintext_IP[:4], plaintext_IP[4:], K1)
        plaintext_Fk1 = SW(plaintext_Fk1)
        plaintext_Fk2 = Fk(plaintext_Fk1[:4], plaintext_Fk1[4:], K2)
        ciphertext = IP_re(plaintext_Fk2)
        return ciphertext

#解密输入密文，为ascii码先转化
def Decry(ciphertext, key):
    plaintext = []
    if re.search('^[01]+$', ciphertext) is None:
        # print(len(trans_ASC(ciphertext)))
        for i in range(len(trans_ASC(ciphertext))):
            ciphertext_asc = trans_ASC(ciphertext)[i]
            #print(ciphertext_asc)
            ciphertext_IP = IP(ciphertext_asc)
            K1 = P8(Shift(P10(key)[:5], 1) + Shift(P10(key)[5:], 1))
            K2 = P8(Shift(Shift(P10(key)[:5], 1), 2) + Shift(Shift(P10(key)[5:], 1), 2))
            ciphertext_Fk1 = Fk(ciphertext_IP[:4], ciphertext_IP[4:], K2)
            ciphertext_Fk1 = SW(ciphertext_Fk1)
            ciphertext_Fk2 = Fk(ciphertext_Fk1[:4], ciphertext_Fk1[4:], K1)
            plaintext.append(IP_re(ciphertext_Fk2))
            # print(plaintext)
            # print(get_ASC(plaintext))
        return get_ASC(plaintext)

    elif re.search('^[01]+$', ciphertext):
        ciphertext_IP = IP(ciphertext)
        K1 = P8(Shift(P10(key)[:5], 1) + Shift(P10(key)[5:], 1))
        K2 = P8(Shift(Shift(P10(key)[:5], 1), 2) + Shift(Shift(P10(key)[5:], 1), 2))
        ciphertext_Fk1 = Fk(ciphertext_IP[:4], ciphertext_IP[4:], K2)
        ciphertext_Fk1 = SW(ciphertext_Fk1)
        ciphertext_Fk2 = Fk(ciphertext_Fk1[:4], ciphertext_Fk1[4:], K1)
        plaintext = IP_re(ciphertext_Fk2)
        return plaintext

# 识别ascii码
def trans_ASC(text):
    cipher_letter = []
    i = 0
    text = (''.join(text)).split(' ')
    #text = text.split(' ')
    letter = []
    # 如果是字符则经此转换
    if re.search('^[a-zA-Z]+$', ''.join(text)):
        text = ''.join(text)
        for i in range(len(text)):
            letter.append(ord(text[i:i + 1]))
        for i in range(len(letter)):
            get_asc = bin(int(letter[i]))[2:].rjust(8,'0')
            # print(get_asc)
            cipher_letter.append(get_asc)

    if len(text) < 2 and re.search('^[a-zA-Z]+$', ''.join(text)) is None:
        get_asc = bin(int(text[0]))[2:].rjust(8,'0')
        # print(get_asc)
        cipher_letter.append(get_asc)

    elif len(text) >= 2 and re.search('^[a-zA-Z]+$', ''.join(text)) is None:
        for i in range(len(text)):
            # print(text)
            get_asc = bin(int(text[i]))[2:].rjust(8,'0')
            cipher_letter.append(get_asc)
            i = i + 1
    return cipher_letter


# 解ascii,输入text为arr
def get_ASC(text):
    i = 0
    str_out = ""
    x = ""
    for i in range(len(text)):
        if i <len(text)-1:
         str_out = str_out + str(int(text[i], 2))+" "
        elif i >=len(text)-1:
         str_out = str_out + str(int(text[i], 2))
    return str_out

# test = '01100001'
# print(test[:1])
# print((test[:1] != 0 or test[:1] != 1) and len(test) != 8)
# print(trans_ASC('b'))
# print(get_ASC(['10110100','11111101','01100001','11110100']))
print(Encry('10101010', '1111100000'))
#print(Decry('255 95 175', '0011111111'))
# print(get_ASC(trans_ASC('blue')))

# ciphertext='153 5 97 244'
#暴力求解密码
def brute_force(plaintext1,ciphertext):
    key_num=0
    for key in range(1024):  # 遍历所有可能的密钥
        binary_key = bin(key)[2:].zfill(10)  # 转换为二进制字符串并添加前导零
        # print(binary_key)
        # print(ciphertext)
        plaintext = trans_ASC(plaintext1)
        # print(plaintext)
        through_plaintext = Decry(ciphertext, binary_key)
        through_plaintext = trans_ASC(through_plaintext)
        # print(through_plaintext)
        if plaintext == through_plaintext:
            print(binary_key)  # 找到正确的密钥
            key_num = key_num + 1
    return key_num
