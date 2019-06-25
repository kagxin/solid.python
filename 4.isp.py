"""
Interface Segregation Principle
Make fine grained interfaces that are client specific
Clients should not be forced to depend upon interfaces that they do not use.
This principle deals with the disadvantages of implementing big interfaces.

Let’s look at the below IShape interface:
接口隔离原则

-创建细粒度的特定于客户端的接口（多个特定客户端接口要好于一个宽泛用途的接口 wiki）
不应该强迫客户机依赖于它们不使用的接口。
这个原则处理了实现大接口的缺点。
让我们看看下面的IShape接口:
"""

class IShape:
    def draw_square(self):
        raise NotImplementedError
    
    def draw_rectangle(self):
        raise NotImplementedError
    
    def draw_circle(self):
        raise NotImplementedError

"""
This interface draws squares, circles, rectangles. class Circle, Square or Rectangle implementing the IShape 
interface must define the methods draw_square(), draw_rectangle(), draw_circle().
- 这个接口绘制正方形。 圆形、矩形、圆、正方形或矩形这几个类实现了IShape
接口必须定义方法draw_square()、draw_rectangle()、draw_circle()。
"""

class Circle(IShape):
    def draw_square(self):
        pass

    def draw_rectangle(self):
        pass
    
    def draw_circle(self):
        pass

class Square(IShape):
    def draw_square(self):
        pass

    def draw_rectangle(self):
        pass
    
    def draw_circle(self):
        pass

class Rectangle(IShape):
    def draw_square(self):
        pass

    def draw_rectangle(self):
        pass
    
    def draw_circle(self):
        pass

"""
It’s quite funny looking at the code above. class Rectangle implements methods (draw_circle and draw_square) it has no use of, 
likewise Square implementing draw_circle, and draw_rectangle, and class Circle (draw_square, draw_rectangle).

If we add another method to the IShape interface, like draw_triangle(),
- 查看上面的代码非常有趣。类矩形实现了它没有用的方法(draw_circle和draw_square)，
同样，Square实现了draw_circle、draw_rectangle，类Circle 实现了(draw_square、draw_rectangle)。

如果我们向IShape接口添加另一个方法，比如draw_triangle()
"""

class IShape:
    def draw_square(self):
        raise NotImplementedError
    
    def draw_rectangle(self):
        raise NotImplementedError
    
    def draw_circle(self):
        raise NotImplementedError
    
    def draw_triangle(self):
        raise NotImplementedError


"""
the classes must implement the new method or error will be thrown.

We see that it is impossible to implement a shape that can draw a circle but not a rectangle or a square or a triangle. 
We can just implement the methods to throw an error that shows the operation cannot be performed.

ISP frowns against the design of this IShape interface. clients (here Rectangle, Circle, and Square) should not be forced to depend on methods that they do not need or use. 
Also, ISP states that interfaces should perform only one job (just like the SRP principle) any extra grouping of behavior should be abstracted away to another interface.

Here, our IShape interface performs actions that should be handled independently by other interfaces.

To make our IShape interface conform to the ISP principle, we segregate the actions to different interfaces.
Classes (Circle, Rectangle, Square, Triangle, etc) can just inherit from the IShape interface and implement their own draw behavior.
- 类必须实现新方法，否则将抛出错误。

我们看到，要实现一个只能画圆而不能画矩形、正方形或三角形的形状是不可能的。
我们可以实现一些方法来抛出一个错误，表明操作无法执行。

ISP反对这种IShape接口的设计。不应该强迫客户端(这里是矩形、圆形和正方形)依赖于它们不需要或不使用的方法。
而且，ISP声明接口应该只执行一个任务(就像SRP原则一样)，任何额外的行为分组都应该抽象到另一个接口。

这里，IShape接口执行的操作应该由其他接口独立处理。

为了使IShape接口符合ISP原则，我们将操作隔离到不同的接口。
类(圆形、矩形、正方形、三角形等)可以继承IShape接口并实现它们自己的绘制行为。
"""

class IShape:
    def draw(self):
        raise NotImplementedError

class Circle(IShape):
    def draw(self):
        pass

class Square(IShape):
    def draw(self):
        pass

class Rectangle(IShape):
    def draw(self):
        pass

"""
We can then use the I -interfaces to create Shape specifics like Semi Circle, Right-Angled Triangle, Equilateral Triangle, Blunt-Edged Rectangle, etc.
- 然后我们可以使用 I-interfaces 创建形状细节，如半圆、直角三角形、等边三角形、钝边矩形等。
"""
