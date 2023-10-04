# Cryptology S-DES
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
```python
#加密过程
python app.py 
```
#### Key Generation
generate a 10 bit binary key
sample code:
```python
key='1010101010'
```
#### Plaintext Input
input a plaintext to suppose this encrypt program, you can choose ASCII、string or binary string to input:
example:
```python
'plaintext='11010110'
'plaintext='hello''
'plaintext='104 101 108 108 111'' #using space to seperate each letter's ASCII encode
```

#### Encryption Results
The encrypted ciphertext will be displayed

### Decryption 
Run app.py file, terminal input:
```python
'#解密过程'
'python app.py'
```

#### Key Generation
generate a 10 bit binary key
sample code:
```python
'key='1010101010'
```

#### Ciphertext Input
input a cipher text to suppose decrypt program, you can choose ASCII or binary string to input:
example:
```python
'ciphertext='26 204 191 191 9''
'ciphertext='10110111''
```

#### Decryption Result
The edcrypted plaintext will be displayed

### Matters Need Attention
the key length is limited to 10 bits
for the input and output format of plaintext and ciphertext, please read the **running** part

### Example Application
#### Encryption
```python
'#Input'
'Plaintext String: hello'
'Key String: 1010101010'
click the 'Encrypt' button
'#output'
'Returned Message: Encrypt successfully! The ciphertext is:26 204 191 191 9'
```

#### Decryption
```python
'#Input'
'Ciphertext String: 26 204 191 191 9'
'Key String: 1010101010'
click the 'Decrypt' button
'#output'
'Returned Message: Decrypt successfully! The plaintext is:104 101 108 108 111'
```

### Advanced Usage
We design a function called brute_force(plaintext,ciphertext) to acquire the key in the situation of just knowing a set of plaintext and ciphertext.The method we use is the most traditional of the brute force method -- enumeration method.
you can run this function by running the main.py file, terminal input:
```python
'python main.py'
```
Then, input a plaintext and a ciphertext one by one and you'll get the key you want. In fact, you can find that there are always more than one key returned, and that's why we select to print the account of key in the end. 
sample code:
```python
'#brute force attack'
'python main.py'
'please input the plaintext: 00111011'
'please input the ciphertext: 10101010'
'# suitable key:'
'0100100100'
'0101101100'
'The number of main key?'
'2'
```

### Reference File
[More details for S-DES](https://terenceli.github.io/%E6%8A%80%E6%9C%AF/2014/04/17/SDES)
