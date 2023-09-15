# 数据类型
counter = 100
i = 0.1
a = "s"

print(counter)
print(i)
print(a)

b = "d"
print(a == b)

a, b, c = 1, 4.1, "c"
print(type(a), end=" ")
print(type(b), end=" ")
print(type(c), end=" ")

print(isinstance(a, int))


class A:
    i = 10


class B(A):
    j = 11


var1 = 1
var10 = 10
del var1

print(1 + 2)
print(4.3 - 2.1)  # 2.1999999999999997 精度问题
print(2 * 3)
print(2 / 3)
print(2 // 3)  # 第一个整数
print(15 % 4)
print(2 ** 3)  # 乘方
print(4 + 5j)  # 虚数

str1 = "hello, python"
print(str1)
print(str1[0:-1])  # 到倒数第二个字符 包括倒数第二个字符
print(str1[5:])  # 从第N个开始向后
print(str1[5:10])  # 截取从5到10的所有字符，5≤str＜10
print(str1[7])  # 输出第六个字符
print(str1 * 2)  # 输出两遍
print(str1 + "\n" + str1)  # 换行
print(r"\n" + str1)  # 输出\n

a = True
b = False
# 比较运算符
print(2 < 3)   # True
print(2 == 3)  # False

# 逻辑运算符
print(a and b)  # False
print(a or b)   # True
print(not a)    # False

# 类型转换
print(int(a))   # 1
print(float(b))  # 0.0
print(str(a))   # "True"

list1 = ["a", "bc", "12", ["ew", "le"]]
print(list1)
print(list1[2:])
print(list1[2:-1])
print(list1[3:])
list1[2] = 12
print(list1)
print(list1[1:3:2])

#  反转列表
def reverseWords(input):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")

    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords = inputWords[-1::-1]

    # 重新组合字符串
    output = ' '.join(inputWords)

    return output


if __name__ == "__main__":
    input = 'I like runoob'
    rw = reverseWords(input)
    print(rw)