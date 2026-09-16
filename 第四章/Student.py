# 定义一个类
class Student:
    # 构造器（初始化方法）
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 自定义方法
    def show_info(self):
        print(f"学生：{self.name}，年龄：{self.age}")

# 创建对象，调用方法
s1 = Student("张三", 20)
s1.show_info()

s1.age = 101
s1.show_info()
