# 父类
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"我叫{self.name}，今年{self.age}岁")


# 子类Student，继承Person
class Student(Person):
    # 子类新增自己的构造，用super()调用父类构造
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # 继承父类的name、age
        self.student_id = student_id  # 子类自己独有的属性

    # 子类新增自己的方法
    def study(self):
        print(f"{self.name}正在学习，学号：{self.student_id}")


# 测试
stu = Student("张三", 18, "2026001")
stu.introduce()   # 直接调用【父类继承过来的方法】
stu.study()       # 调用【子类自己新增的方法】
