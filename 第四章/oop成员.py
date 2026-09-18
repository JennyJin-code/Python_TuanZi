


class Student:
    # 类变量
    nums = 0

    def __init__(self, name, age):
         #实例变量
         self.name = name
         self.age = age
         Student.nums += 1

     #类方法
    def introduce(student):
         print(f'调用类方法{student.nums}')

    def instance_method(self):
        print(self.name)
        print(f'调用实例方法年龄{self.age}')

    @staticmethod
    def static_method():
        print('this is static method')

#创建实例
student1 = Student("sansan",2)
student2 = Student("sisi",5)
#调用实例
student1.instance_method()
student2.instance_method()

Student.introduce(student1)
Student.static_method()








