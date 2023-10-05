# This is a sample Python script.
from althgram import brute_force
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# def brute_force(plaintext,ciphertext):
#     for key in range(1024):  # 遍历所有可能的密钥
#         binary_key = bin(key)[2:].zfill(10)  # 转换为二进制字符串并添加前导零
#         print(binary_key)
#         through_plaintext = Decry(ciphertext, binary_key)
#         if plaintext==through_plaintext:
#             return binary_key  # 找到正确的密钥
#     return None  # 没有找到正确的密钥

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    plaintext=input('Please input the plaintext: ')
    ciphertext=input('please input the ciphertext: ')
    #ciphertext = '255 95 175'
    key=brute_force(plaintext,ciphertext)
    print('The number of main key?')
    print(key)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
