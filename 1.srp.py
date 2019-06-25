"""
Single Responsibility Principle
“…You had one job” — Loki to Skurge in Thor: Ragnarok

A class should have only one job. 
If a class has more than one responsibility, it becomes coupled. 
A change to one responsibility results to modification of the other responsibility.
单一职责原则 （对象应该仅具有一种单一功能的概念。 wiki）
"...你已经有一个工作了" — Loki to Skurge in Thor: Ragnarok
- 一个类应该只有一份职责。
如果一个class有多个职责，那么它就会变得耦合。
改变一项职责会导致修改另一项职责。
"""

class Animal:
    def __init__(self, name: str):
        self.name = name
    
    def get_name(self) -> str:
        pass

    def save(self, animal: Animal):
        pass

"""
The Animal class violates the SRP.

How does it violate SRP?

SRP states that classes should have one responsibility, here, we can draw out two responsibilities: animal database management and animal properties management. 
The constructor and get_name manage the Animal properties while the save manages the Animal storage on a database.

How will this design cause issues in the future?

If the application changes in a way that it affects database management functions. The classes that make use of Animal properties will have to be touched and recompiled to compensate for the new changes.

You see this system smells of rigidity, it’s like a domino effect, touch one card it affects all other cards in line.

To make this conform to SRP, we create another class that will handle the sole responsibility of storing an animal to a database:

-Animal类违反了SRP。

它是如何违反SRP的？

SRP声明class应该有一个职责，在这里，我们给出了两个职责：动物数据库管理和动物财产管理。
构造函数和get_name管理Animal属性，而save管理数据库上的Animal存储。

这种设计将来会如何引发问题？

如果应用程序以影响数据库管理功能的方式更改，就必须修改和重新编译使用动物属性的类，以补偿新的更改。

你可以看到这个系统有点僵硬，就像多米诺骨牌效应，触摸一张牌它会影响到其他所有的牌。

为了使这个符合SRP，我们创建了另一个类，它将处理将动物存储到数据库的唯一的职责:

"""

class Animal:
    def __init__(self, name: str):
            self.name = name
    
    def get_name(self):
        pass


class AnimalDB:
    def get_animal(self, id) -> Animal:
        pass

    def save(self, animal: Animal):
        pass

"""
When designing our classes, we should aim to put related features together, 
so whenever they tend to change they change for the same reason. 
And we should try to separate features if they will change for different reasons. - Steve Fenton
- 在设计我们的类时，我们应该把相关的特性放在一起，这样当它们想要改变时，它们就会因为同样的原因而改变。
如果因为不同的原因而发生变化，我们应该尝试分离这些特性。——史蒂夫•芬顿
"""



"""
The downside of this solution is that the clients of the this code have to deal with two classes.
A common solution to this dilemma is to apply the Facade pattern.
Animal class will be the Facade for animal database management and animal properties management.

- 此解决方案的缺点是此代码的客户端必须处理两个类。
解决这一难题的一个常见方法是应用Facade模式
动物类将成为动物数据库管理和动物财产管理的Facade。

"""


class Animal:
    def __init__(self, name: str):
        self.name = name
        self.db = AnimalDB()

    def get_name(self):
        return self.name

    def get(self, id):
        return self.db.get_animal(id)
    
    def save(self):
        self.db.save(animal=self)


"""
The most important methods are kept in the Animal class and used as Facade for the lesser functions.

- 最重要的方法都保存在Animal类中，用轻量的方法作为Facade。
- 
"""
