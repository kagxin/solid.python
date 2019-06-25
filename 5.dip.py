"""
Dependency Inversion Principle
Dependency should be on abstractions not concretions
A. High-level modules should not depend upon low-level modules. Both should depend upon abstractions.
B. Abstractions should not depend on details. Details should depend upon abstractions.

There comes a point in software development where our app will be largely composed of modules. 
When this happens, we have to clear things up by using dependency injection. 
High-level components depending on low-level components to function.

- 依赖反转原则
依赖关系应该是抽象的，而不是具体的 (依赖于抽象而不是一个实例 wiki)
A.高级模块不应该依赖于低级模块。两者都应该依赖于抽象。
B.抽象不应该依赖于细节。细节应该依赖于抽象。

在软件开发中，我们的应用程序将主要由模块组成。
当这种情况发生时，我们必须使用依赖注入来清理。
高级组件取决于要运行的低级组件。
"""

class XMLHttpService(XMLHttpRequestService):
    pass

class Http:
    def __init__(self, xml_http_service: XMLHttpService):
        self.xml_http_service = xml_http_service
    
    def get(self, url: str, options: dict):
        self.xml_http_service.request(url, 'GET')

    def post(self, url, options: dict):
        self.xml_http_service.request(url, 'POST')

"""
Here, Http is the high-level component whereas HttpService is the low-level component. 
This design violates DIP A: High-level modules should not depend on low-level level modules. It should depend upon its abstraction.

Ths Http class is forced to depend upon the XMLHttpService class. 
If we were to change the Http connection service, maybe we want to connect to the internet through cURL or even Mock the http service. 
We will painstakingly have to move through all the instances of Http to edit the code and this violates the OCP principle.

The Http class should care less the type of Http service you are using. We make a Connection interface:

- 这里，Http是高级组件，而HttpService是低级组件。
这种设计违反了DIP A:高级模块不应该依赖于低级模块。它应该依赖于它的抽象。

Http类被迫依赖于XMLHttpService类。
如果要更改Http连接服务，可能需要通过cURL甚至Mock Http服务连接到internet。
我们将费力地遍历所有Http实例来编辑代码，这违反了OCP原则。

Http类不应该太关心您正在使用的Http服务的类型。我们做一个连接接口:
"""

class Connection:
    def request(self, url: str, options: dict):
        raise NotImplementedError

"""
The Connection interface has a request method. With this, we pass in an argument of type Connection to our Http class:
"""

class Http:
    def __init__(self, http_connection: Connection):
        self.http_connection = http_connection
    
    def get(self, url: str, options: dict):
        self.http_connection.request(url, 'GET')

    def post(self, url, options: dict):
        self.http_connection.request(url, 'POST')

"""
So now, no matter the type of Http connection service passed to Http it can easily connect to a network 
without bothering to know the type of network connection.

We can now re-implement our XMLHttpService class to implement the Connection interface:
- 所以现在，无论传递给Http的Http连接服务的类型是什么，它都可以轻松地连接到网络
不需要知道网络连接的类型。

我们现在可以重新实现XMLHttpService类来实现连接接口:
"""

class XMLHttpService(Connection):
    xhr = XMLHttpRequest()

    def request(self, url: str, options:dict):
        self.xhr.open()
        self.xhr.send()

"""
We can create many Http Connection types and pass it to our Http class without any fuss about errors.
- 我们可以创建许多Http连接类型并将其传递给我们的Http类，而无需担心错误。
"""
class NodeHttpService(Connection):
    def request(self, url: str, options:dict):
        pass

class MockHttpService(Connection):
    def request(self, url: str, options:dict):
        pass

"""
Now, we can see that both high-level modules and low-level modules depend on abstractions. 
Http class(high level module) depends on the Connection interface(abstraction) and 
the Http service types(low level modules) in turn, depends on the Connection interface(abstraction).

Also, this DIP will force us not to violate the Liskov Substitution Principle: 
The Connection types Node-XML-MockHttpService are substitutable for their parent type Connection.
- 现在，我们可以看到高级模块和低级模块都依赖于抽象。
Http类(高级模块)依赖于连接接口(抽象)和
Http服务类型(低层模块)反过来又依赖于连接接口(抽象)。

此外，这种下降将迫使我们不违反里氏替换原则:
连接类型Node-XML-MockHttpService可以替代它们的父类型连接。
"""
