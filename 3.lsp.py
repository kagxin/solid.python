"""
Liskov Substitution Principle
A sub-class must be substitutable for its super-class.
The aim of this principle is to ascertain that a sub-class can assume the place of its super-class without errors. 
If the code finds itself checking the type of class then, it must have violated this principle.

Let’s use our Animal example.
- 里氏替换原则

子类必须可以替换它的超类。（程序中的对象应该是可以在不改变程序正确性的前提下被它的子类所替换的。wiki）

这个原则的目的是确定一个子类可以在没有错误的情况下代替它的超类。

如果代码发现自己正在 ** 检查类的类型 ** ，那么它一定违反了这个原则。

让我们以动物为例。
"""

def animal_leg_count(animals: list):
    for animal in animals:
        if isinstance(animal, Lion):
            print(lion_leg_count(animal))
        elif isinstance(animal, Mouse):
            print(mouse_leg_count(animal))
        elif isinstance(animal, Pigeon):
            print(pigeon_leg_count(animal))
        
animal_leg_count(animals)

"""
To make this function follow the LSP principle, we will follow this LSP requirements postulated by Steve Fenton:

If the super-class (Animal) has a method that accepts a super-class type (Animal) parameter. 
Its sub-class(Pigeon) should accept as argument a super-class type (Animal type) or sub-class type(Pigeon type).
If the super-class returns a super-class type (Animal). 
Its sub-class should return a super-class type (Animal type) or sub-class type(Pigeon).
Now, we can re-implement animal_leg_count function:

- 为了使该函数遵循LSP原则，我们将遵循Steve Fenton提出的LSP要求:

1、如果超类(Animal)有接受 Animal对象 参数的方法。
它的子类(Pigeon)应该接受Animal 类型的对象或Pigeon类型的对象作为参数。
2、如果超类返回一个Animal，
它的子类应该返回一个Animal类型的对象或Pigeon类型的对象。
现在，我们可以重新实现animal_leg_count函数:
"""

def animal_leg_count(animals: list):
    for animal in animals:
        print(animal.leg_count())
        
animal_leg_count(animals)

"""
The animal_leg_count function cares less the type of Animal passed, it just calls the leg_count method. 
All it knows is that the parameter must be of an Animal type, either the Animal class or its sub-class.

The Animal class now have to implement/define a leg_count method.
And its sub-classes have to implement the leg_count method:
- animal_leg_count函数不关心传递的Animal类型，它只调用leg_count方法。
它只需要知道参数必须是动物类型，要么是动物类，要么是它的子类。

Animal类现在必须实现/定义一个leg_count方法。
它的子类必须实现leg_count方法:
"""

import abc 

class Animal(metaclass=abc.ABCMeta):
    
    @abc.abstractclassmethod
    def leg_count(self):
        """几条腿"""


class Lion(Animal):
    def leg_count(self):
        pass


"""
When it’s passed to the animal_leg_count function, it returns the number of legs a lion has.

You see, the animal_leg_count doesn’t need to know the type of Animal to return its leg count, 
it just calls the leg_count method of the Animal type because by contract a sub-class of Animal class must implement the leg_count function.
- 当它被传递给animal_leg_count函数时，它返回lion的腿数。

你看，animal_leg_count不需要知道返回它的腿部计数的动物的类型，
它只调用动物类型的leg_count方法，因为根据约定，动物类的子类必须实现leg_count函数。
"""
