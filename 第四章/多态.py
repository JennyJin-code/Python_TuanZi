# 父类
class Animal:
    def speak(self):
        pass

# 子类1，重写speak方法
class Dog(Animal):
    def speak(self):
        print("汪汪汪")

# 子类2，重写speak方法
class Cat(Animal):
    def speak(self):
        print("喵喵喵")

# 多态函数：接收任意动物对象，统一调用speak
def make_sound(animal):
    animal.speak()   # 同一个方法名，不同对象，行为不一样


# 创建对象
dog = Dog()
cat = Cat()

#调用方法
make_sound(dog)
make_sound(cat)
