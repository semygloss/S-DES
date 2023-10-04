# cryptology
A repository to submit and restore semygloss' homework of cryptology
# User Guide
## Overview
S-DES（Simplified Data Encryption Standard）is a simpified data encryption standard. It is suitable for encryption and decryption of small-scale data, whose structure and operating steps is easy to learn.
This user guide introduce how to encrpt and decrypt data by using S-DES encryption program.

## Environment and Configuration
IDE: Pycharm 2023.2
Environment configuration: python3

## Running

### Encryption
Run app.py file, terminal input:
'#加密过程'
'python app.py '
#### Key Generation
generate a 10 bit binary key
sample code:
'key='1010101010''
#### Plaintext Input
input a plaintext to suppose this encrypt program, you can choose ASCII、string or binary string to input:
example:
'plaintext='11010110'
'plaintext='hello''
'plaintext='104 101 108 108 111'' #using space to seperate each letter's ASCII encode
#### Encryption Results
The encrypted ciphertext will be displayed

### Decryption 
Run app.py file, terminal input:
'#解密过程'
'python app.py'
#### Key Generation
generate a 10 bit binary key
sample code:
'key='1010101010'
#### Ciphertext Input
input a cipher text to suppose decrypt program, you can choose ASCII or binary string to input:
example:
'ciphertext='26 204 191 191 9''
'ciphertext='10110111''
#### Decryption Result
The edcrypted plaintext will be displayed

### Matters Need Attention
the key length is limited to 10 bits
for the input and output format of plaintext and ciphertext, please read the **running** part

### Example Application
#### Encryption
'#Input'
'Plaintext String: hello'
'Key String: 1010101010'
click the 'Encrypt' button
'#output'
'Returned Message: Encrypt successfully! The ciphertext is:26 204 191 191 9'
#### Decryption
'#Input'
'Ciphertext String: 26 204 191 191 9'
'Key String: 1010101010'
click the 'Decrypt' button
'#output'
'Returned Message: Decrypt successfully! The plaintext is:104 101 108 108 111'

### Advanced Usage
We design a function called brute_force(plaintext,ciphertext) to acquire the key in the situation of just knowing a set of plaintext and ciphertext.The method we use is the most traditional of the brute force method -- enumeration method.
you can run this function by running the main.py file, terminal input:
'python main.py'
Then, input a plaintext and a ciphertext one by one and you'll get the key you want. In fact, you can find that there are always more than one key returned, and that's why we select to print the account of key in the end. 
sample code:
'#brute force attack'
'python main.py'
'please input the plaintext: 00111011'
'please input the ciphertext: 10101010'
'# suitable key:'
'0100100100'
'0101101100'
'The number of main key?'
'2'

### Reference File
参考文档
在此部分提供其他参考文档、链接或资源，以便用户深入了解S-DES加密算法和其应用。

这个示例展示了一个S-DES加密程序用户指南的基本结构，包括概述、安装说明、使用方法、配置选项、异常处理、注意事项、示例应用、常见问题和参考文档。

请注意，实际编写用户指南时，应根据具体的S-DES加密程序的特点和需求进行适当调整和扩展。确保文档内容准确、清晰，并提供足够的示例代码和说明，以便用户可以理解和正确使用S-DES加密程序。
