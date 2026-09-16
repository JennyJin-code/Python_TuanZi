
# n=1
# if n>1:
#     print('n比1大')
# elif n==1:
#     print('n是1')
# else:
#     print('n比1小')


# names = ['张三','李四','王五','赵六']
# for name in names:
#     print(name)

# count=1
# while count<=4:
#     print(count)
#     count+=1

# nums = [1,2,3,4,5]
#
# for num in nums:
#     if num == 3:
#         pass    #占位语句，不做任何操作
#     print(num)


# try:
#     print(10/2)     #尝试执行代码
# except ZeroDivisionError:
#     print('0不能作为除数')   #如果发生异常，输出语句
# else:
#     print('没有发行异常')    #如果没有异常，输出语句
# finally:
#     print('任何情况都会执行')  #无论什么情况，都要输出语句


# names = ['张三','李四','王五','赵六']
# for i in  range(len(names)):
#     print(f'第{i}个名字是{names[i]}')

# nums  = list(range(1,11))
# for num in nums:
#     print(num)


# 1.
# 位置参数：调用函数时，参数依次传递
# def main1(a,b,c):
#     print(f'和是{a+b+c}')
#
# main1(1,2,3)

#
# 2.
# 默认参数：调用时没传参，急用默认参数
# def main2(a,b,c=35):
#     print(f'和是{a+b+c}')
#
# main2(1,2,)


#
# 3.
# 可变位置参数：使用 * args来接受可变数量的参数
# def main3(*a):
#     print(f'和是{sum(a)}')
#
# main3(1,2,10,20)

#
# 4.
# 关键字参数：调用函数时，可使用参数名指定参数值，可以不按顺序依次传参
# def main4(name,age):
#     print(f'学生{name}，{age}岁了')
#
# main4(age=23,name='张三')



#
# 5.
# 可变关键字参数
# def main5(**valus):
#     for key,value in valus.items():
#         print(f'{key}:{value}')
# main5(name = '1', age = 23)

# def main6(a,b,/):
#     print(a+b)
# main6(3,4)

# def main7(name,*,age):
#     print(f'{name} is {age} years old')
# main7(name='san',age=2)

# result = lambda a,b: a+b
# print(result(1,2))

class NameException(Exception):
    pass

try:
    raise NameException
except NameException:
    print("zidingyi-exception")








# for num in nums:
#     print(num)
#     if num == 3:
#         continue
#     print(num)







