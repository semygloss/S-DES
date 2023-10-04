# Development manual
This manual introduce more details of our S-DES data encryption algorithm
## Overview
As an encryption algorithm for teaching rather than security use, the best way to understand S-DES is to know the boxs inside. Here are the standard and boxs we use in our S-DES:
## Standard
Length of plaintext/ciphertext: 8-bit
Length of main key: 10-bit
Algorithm:
[more details about S-DES algorithm please click here](https://terenceli.github.io/%E6%8A%80%E6%9C%AF/2014/04/17/SDES)
Key Expansion
```math
P10=(3,5,2,7,4,10,1,9,8,6)
```
```math
P8=(6,3,7,4,8,5,10,9)
```
```math
Leftshift1=(2,3,4,5,1)
```
```math
Leftshift2=(3,4,5,1,2)
```
Initial Permutation
IP=(2,6,3,1,4,8,5,7)
Final Permutation
IP^-1=(4,1,3,5,7,2,8,6)
Round Function
EPBox=(4,1,2,3,2,3,4,1)
SBox1=[(1,0,3,2),(3,2,1,0),(0,2,1,3),(3,1,0,2)]
SBox2=[(0,1,2,3),(2,3,0,1),(3,0,1,2),(2,1,0,3)]
SPBox=(2,4,3,1)      

## Reference file
[More details about standard and rules](https://shimo.im/docs/m5kvdlMaKvcENy3X/)
