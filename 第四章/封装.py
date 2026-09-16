class Student:
    def __init__(self, name, age):
        # 双下划线：私有属性，外部不能直接访问，实现封装
        self.__name = name
        self.__age = age

    # 【getter】获取私有属性
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    # 【setter】修改私有属性，可以加校验（封装的好处：过滤非法数据）
    def set_age(self, new_age):
        if 0 < new_age < 150:
            self.__age = new_age
        else:
            print("年龄输入错误！")

    def show_info(self):
        print(f"姓名：{self.__name}，年龄：{self.__age}")


# 测试
s = Student("张三", 22)
# s.__age  直接写这个会报错！外部无法访问私有变量
print(s.get_name())
print(s.get_age())

# 修改年龄，会走校验逻辑
s.set_age(25)
s.show_info()

s.set_age(200) # 非法年龄，不会修改
