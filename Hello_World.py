"""
1.变量名只能包含字母、数字、下划线。可以字母或下划线开头，不能以数字开头。
2.变量名不能包含空格，但可使用下划线来分隔其中的单词。
3.不要将Python关键字和函数名用作变量名。
4.变量名要既简短又具有描述性。
5.慎用大小写 I 和 O ，因为有时候会被看成数字 1 和 0
"""


# 打印一个字符串
print('Hello_World\'你好世界')

# 设置一个变量，将字符串赋值给变量并打印
message = 'hello pythone world!'
print(message)

message = 'hello pythone crash course world!'
print(message)

# 使用变量时避免命名错误,运行程序时候会指出错误
message = 'hello python crash course reader!'
print(message)
'''
Traceback (most recent call last):
  File "D:/PyCharm-L/Pythone_Code/1/Hello_World.py", line 22, in <module>
    print(mesage)
NameError: name 'mesage' is not defined
'''

# 练习1： 将一条消息存储到变量中，再打印出来。
message = "你好世界！这是一句简单的消息。"
print(message)

# 练习2： 将一条消息存储到变量中，再打印出来，然后修改变量的值，并将其打印出来。
message = '这是第一条消息。'
print(message)
message = '这是修改后的第二条消息。'
print(message)