value = input('input a string:')

# 分割
value_list = value.split()
num = []
for i in range(len(value_list)):
    num.append(int(value_list[i]))
n= len(num)
helpBit = []

# 转二进制字符
for i in range(n):
    helpBit.append("0"*(32 - len(bin(num[i])[2:])) + bin(num[i])[2:])
#交换位置
newHelpBit = [0] * 32 * n
for i in range(n):
    for j in range(32):
        if j%2 == 0:
            newHelpBit[ i*32 + j] = helpBit[i][j+1]
        else:
            newHelpBit[i * 32 + j] = helpBit[i][j - 1]
#右移
res= [0] * n
res[0] = "".join(newHelpBit[-2:] + newHelpBit[:30])
for i in range(1,n):
    res[i] = "".join(newHelpBit[-2+i*32:-2 + (i+1)*32])
#输出整数
ans = [0] * n
for i in range(n):
    ans[i] = str(int(res[i],2))
#输出字符串

ansString = " ".join(ans)
print(ansString)