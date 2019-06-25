"""
Open-Closed Principle
- 开闭原则
Software entities(Classes, modules, functions) should be open for extension, not modification.
- 软件体(类,模块,函数)应该对扩展开放,而不是修改。（软件体应该是对于扩展开放的，但是对于修改封闭的。wiki）
"""
class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

animals = [
    Animal('lion'),
    Animal('mouse')
]

def animal_sound(animals: list):
    for animal in animals:
        if animal.name == 'lion':
            print('roar')

        elif animal.name == 'mouse':
            print('squeak')

animal_sound(animals)

"""
The function animal_sound does not conform to the open-closed principle because it cannot be closed against new kinds of animals.
If we add a new animal, Snake, We have to modify the animal_sound function.
You see, for every new animal, a new logic is added to the animal_sound function. 
This is quite a simple example. When your application grows and becomes complex, 
you will see that the if statement would be repeated over and over again 
in the animal_sound function each time a new animal is added, all over the application.
- animal_sound函数不符合开闭原则, 因为它不是封闭的对于新类型的动物。
- 如果我们新添加一个动物，Snake， 我们不得不修改animal_sound函数。
- you see， 对于一个新的动物，要新添加一个逻辑到animal_sound函数。这是一个简单的例子。
- 当您的应用程序增长并变得复杂时，你会看到每次在整个应用程序中添加新动物时，都会在animal_sound函数中反复重复if语句。
"""

animals = [
    Animal('lion'),
    Animal('mouse'),
    Animal('snake')
]

def animal_sound(animals: list):
    for animal in animals:
        if animal.name == 'lion':
            print('roar')
        elif animal.name == 'mouse':
            print('squeak')
        elif animal.name == 'snake':
            print('hiss')

animal_sound(animals)


"""
How do we make it (the animal_sound) conform to OCP?
- 我们如何让它(animal_sound)符合开闭 OCP?
"""
class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

    def make_sound(self):
        raise NotImplementedError


class Lion(Animal):
    def make_sound(self):
        return 'roar'


class Mouse(Animal):
    def make_sound(self):
        return 'squeak'


class Snake(Animal):
    def make_sound(self):
        return 'hiss'


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())

animal_sound(animals)

"""
Animal now has a virtual method make_sound. We have each animal extend the Animal class and implement the virtual make_sound method.

Every animal adds its own implementation on how it makes a sound in the make_sound. 
The animal_sound iterates through the array of animal and just calls its make_sound method.

Now, if we add a new animal, animal_sound doesn’t need to change. 
All we need to do is add the new animal to the animal array.

animal_sound now conforms to the OCP principle.
- Animal现在有了一个虚方法make_sound。 我们让每只动物扩展Animal类并实现虚拟的make_sound方法。

- 每个动物都会在make_sound中添加自己的实现方式。
animal_sound遍历animal数组并调用其make_sound方法。

现在，如果我们添加一个新动物，animal_sound不需要改变。
我们只需要做的就是将新动物添加到动物数组中。

animal_sound现在符合OCP原则。
"""

"""
Another example:

Let’s imagine you have a store, and you give a discount of 20% to your favorite customers using this class:
When you decide to offer double the 20% discount to VIP customers. You may modify the class like this:
- 假设您有一个商店，并且您使用此类给您喜爱的客户提供20％的折扣：
- 当您决定为VIP客户提供双倍的20％折扣。 您可以像这样修改类：
"""

class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        if self.customer == 'fav':
            return self.price * 0.2
        if self.customer == 'vip':
            return self.price * 0.4


"""
No, this fails the OCP principle. OCP forbids it. If we want to give a new percent discount maybe, to a diff
type of customers, you will see that a new logic will be added.

To make it follow the OCP principle, we will add a new class that will extend the Discount. 
In this new class, we would implement its new behavior:
- 不，这不符合OCP原则。 OCP禁止它。如果我们想给一个新的百分比折扣，对一个不同
客户类型，你将看到会添加新逻辑。
- 为了使其遵循OCP原则，我们将添加一个扩展折扣的新类。
在这个新类中，我们将实现其新行为：
"""

class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount(self):
        return self.price * 0.2


class VIPDiscount(Discount):
    def get_discount(self):
        return super().get_discount() * 2

"""
If you decide 80% discount to super VIP customers, it should be like this:
You see, extension without modification.
- 如果您决定向超级VIP客户提供80％的折扣，它应该是这样的：
你看，扩展没有修改。
"""

class SuperVIPDiscount(VIPDiscount):
    def get_discount(self):
        return super().get_discount() * 2
