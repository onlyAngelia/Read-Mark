[TOC]

#数据挖掘知识清单

![数据挖掘知识清单](数据挖掘知识清单.jpg)



#数据分析之Python基础

Python语言采用代码缩进和冒号的方式来区分代码之间的层次关系，所以代码缩进在Python中是一种语法，如果代码缩进不统一，会产生错误或者异常，相同层次的代码一定要采用相同层次的缩进。

Python IDE：  PyCharm(写爬虫) 、 Sublime Text 、 Vim、Eclipse + PyDev 、IDLE  、jupyter notebook+spyder3（数据分析主要IDE）

若用IDLE 编译  一行代码一回车   

**基本语法**： 输入输出 ： input (Python 2.7  用 raw_input)、 print (与其它语言一样%s 代表字符串，%d代表整数)

**注释**： 注释在Python中使用#，如果注释中有中文，一般会在代码前添加#— coding：utf-8 -  

如果是多行注释，使用三个单引号，或者三个双引号。

**引用模块** ：导入一个模块  import model_name ,导入多个模块  import model_name, anthor_model,导入包中指定模块 from package_name import moudule_name;导入包中所有模块 from package_name import *

##**循环控制**

###**if … else ...**

```python
      if score>= 90:
      print 'Excellent'
else:
       if score < 60:
           print 'Fail'
       else:
           print 'Good Job'
```

###**for … in** 

```python
sum = 0
for number in range(11):
    sum = sum + number
print sum
```

若规定循环次数，可以使用range函数，在for循环里比较常见，range(11)代表从0到10，不包括11，也相当于range(0，11)，range里面还可以增加步长，比如range(1，11，2)代表的是[1，3，5，7，9]

###**while循环**

```python
sum = 0
number = 1
while number < 11:
       sum = sum + number
       number = number + 1
print sum
```

while循环对于变量计算方式更加灵活。因此while循环适合循环次数不确定的循环，而for 循环的条件相对确定，适合固定次数的循环。

**多重赋值**

```python
a = b = c = 100
```

##**标准数据类型**

Python中目前定义了五种标准数据类型，用于存储各种数据类型

```python
.Numbers (数字)
.String ()
.List
.Tuple
.Dictionary
```

此外还有集合Set 标准数据类型，同Dictionary类型

###**列表 List**

```python
lists = ['a','b','c']
lists.append('d')
print lists
print len(lists)
lists.insert(0,'mm')
lists.pop()
print (len(lists)) //Python3.0 语法
del lists[0]
print (max(lists))
print (lists.count('a'))

```

列表是Python中的常用数据结构，append()在尾部添加元素，insert()在列表中插入元素，使用pop()删除尾部的元素，使用len()计算列表长度，使用del删除列表指定位置的元素，使用max()找出列表中最大的元素，使用count()计算某个目标值在数组中出现的次数

###**元组(Tuple)**

```python
>>> tupe = ('tupeA','tupeB')
>>> tupe_first = "a","b","c"
>>> tupe_second = (50,)
>>> print (tupe[0])
tupeA
>>> tupe_third = tupe + tupe_first
>>> print (tupe_third)
('tupeA', 'tupeB', 'a', 'b', 'c')
>>> del tupe_third
>>> print (len(tupe))
2
>>> 
```

Python的元组与列表类似，但是元组一旦创建就不能修改，不过我们可以通过两个元组拼接的形式进行修改，元组不能删除某个指定元素，但用del()函数可以直接将整个元组删除；元组中只包含一个元素时，需要在后面添加逗号，否则最后一个）会当运算符计算;len()函数会返回元组的个数。

###**字典(Dictonary)**

字典是key:value的容器模型，键值必须唯一，但值则不必唯一

```python
>>> dictionary = {'Alice': 17,'Beth': 19}
>>> dictionary = {'Name': 'Alice', 'Age': 17, 'Class': 'First'}
>>> print (dictionary['Name'])
Alice
>>> dictionary['Age'] = 18
>>> del dictionary['Class']
>>> dictionary.clear
<built-in method clear of dict object at 0x10d85ebd0>
>>> del dictionary
>>> dictionary = {'Name': 'Beth', 'Age': 17, 'Class': 'First','Name': 'Alice'}
>>> print (len(dictionary))
3
>>> str(dictionary)
"{'Name': 'Alice', 'Age': 17, 'Class': 'First'}"
```

访问字典里的值直接通过访问key的形式，修改字典中的元素也是同样用直接访问key的形式进行重新赋值；

del dictionary['key'] 是删除字典中key：value键值对  clear()函数是清空字典， del dictionary 是直接将整个字典删除；因字典中不允许同一个键出现两次，所以后赋值的会替换掉前面的，键必须不可变，所以用数字，字符串或元组充当，而不能用列表；len()函数计算字典中元素个数，即建的总数。str()函数是以可打印字符串表示输出字典。

###**集合(Set)**

集合与列表存储结构相似，不同的是集合是无序的且不重复。

```python
>>> basket = {'apple','orange','apple','pear','orange','banana'}
>>> print (basket)
{'pear', 'apple', 'banana', 'orange'}
>>> 'orange' in basket
True
>>> 'pich' in basket
False
>>> a_set = set('abracadabra')
>>> a_set
{'a', 'd', 'c', 'b', 'r'}
>>> b_set = set('alacazam')
>>> b_set
{'m', 'c', 'z', 'l', 'a'}
>>> a_set - b_set  #集合a中包含而集合b中不包含的元素
{'d', 'r', 'b'}
>>> a_set | b_set #集合a或集合b中包含的所有元素
{'m', 'd', 'c', 'z', 'l', 'a', 'b', 'r'}
>>> a_set & b_set #集合a和集合b中共同包含了的元素
{'c', 'a'}
>>> a_set ^ b_set #不同时包含于a和b的元素
{'m', 'z', 'l', 'd', 'b', 'r'}
>>> s_set = {x for x in 'abracadabra' if x not in 'abc'}
>>> s_set
{'d', 'r'}
>>> a_set.add(x)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    a_set.add(x)
NameError: name 'x' is not defined
>>> a_set.add('x')
>>> a_set.update('s')
>>> a_set.remove('s')
>>> a_set.discard('s')
>>> a_set.pop
<built-in method pop of set object at 0x10d906668>
>>> len(a_set)
6
>>> 'a' in a_set
True
>>> a_set.clear()
>>> a_set.isdisjoint(b_set)
True
>>> a_set.issubset(b_set)
True
>>> a_set.issuperset(b_set)
False
>>> 
```

空集合的创建不能用{},必须用set()，因为{}是创建空字典。 与字典相同 可直接通过'x' in 结合的形式判断集合中是否有该元素，若有则返回True，若没有该元素，则返回False；两个集合可通过 '-' 、'|'、'&'、'^'四个运算符求与或非等操作；add()可以向集合中添加元素，另外一种添加方式是update()，该方式可以将列表、字典等元素添加到集合中；remove()可以移除集合中的元素，另一种移除方式是discard(),此种方式在集合中没有要移除的元素的时候不会报错；pop()是随机移除，len()是求集合长度；clear()是清空集合；isdisjoint()是判断集合中是否包含相同的元素，如果没有返回True，否则返回False；issubset()判断指定集合是否为该方法参数集合的子集合，issuperset()判断该方法的参数集合是否为指定集合的子集。

##**函数**

Python中函数分为内建函数和自定义函数，自定义函数以 def关键字开头，后接函数标识符名称和圆括号。

任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。

函数的第一行语句可以选择性地使用文档字符串-用于存放函数说明

函数内容以冒号起始，并且缩进。

return[表达式]结束函数，选择性德返回一个值给调用方，不带表达式的return相当于返回None

```python
>>> def area(width, height):
	return width * height

>>> print ("with =",w,"height =",h,"area =",area(w,h))
with = 34 height = 25 area = 850
```

###**参数传递**

Python中，类型属于对象，变量是没有类型的。

####**可更改(mutable)与不可更(immutable)改对象**:

在Python中，string，tuples和numbers是不可更改的对象，而list，dictionary等则是可以修改的对象

**.不可变类型** ： 变量赋值a = 5后，再赋值 a = 10，这里实际是新生成一个int对象10，再让a指向它，而原来的5以及原来占用的内存都被废弃，相当于重新生成了a。

**.可变类型** : 变量赋值la = [1,2,3,4]后再赋值 la[2] = 5 则是将 list la中的第三个元素更改，并没有改变list la的内存指向。

####**参数类型**

**.必需参数** :以正确的方式传入函数，调用时的数量必须和声明时一致

**.关键字参数** ：使用关键字参数允许函数调用时参数的顺序与生命不一致，因为Python解释器能够用参数名称匹配参数值

```python
#可写函数说明
def printinfo( name, age ):
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return
 
#调用printinfo函数
printinfo( age=50, name="runoob" )
```



**.默认参数**  调用函数时，如果没有传递参数，则会使用默认参数

```python
>>> def printinfo(name, age = 35):
	"打印任何传入的字符"
	print ("名字:", name)
	print ("年龄:", age)
	return

>>> printinfo( age = 50, name = "Joe")
名字: Joe
年龄: 50
>>> printinfo( name = "Joe")
名字: Joe
年龄: 35
```

**.不定长参数**： 一个函数要处理比声明时更多的参数，这些参数叫不定长参数，不定长参数声明时不会命名，加了*的参数会以元组的形式导入，存放所有未命名参数，如果函数调用时没有指定参数，参数就是一个空元组。

```python
>>> def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vartuple)
   return

>>> printinfo( 70, 60, 59)
输出: 
70
(60, 59)
>>> printinfo( 70)
输出: 
70
()
>>> 
```

还有一种不定长参数是加了两个**，该类型参数会以字典的形式导入。

```python
>>> def printinfo( arg1, **vardict ):
	"打印任何输入的参数"
	print ("输出：")
	print (arg1)
	print (vardict)
	return

>>> printinfo(1, a = 2, b = 3)
输出：
1
{'a': 2, 'b': 3}
```

声明函数时，参数中星号*可以单独出现，

```python
def f(a,b,*,c):
    return a+b+c
```

如果单独出现星号*后的参数必须用关键字传入,否则会报异常

```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: f() takes 2 positional arguments but 3 were given
```

正确调用如下：

```python
>>> def f(a,b,*,c ):
	return a + b + c

>>> f(1,2,c = 3)
6
>>> 
```

###**匿名函数**

Python中使用lambda来创建匿名函数。

.lambda只是一个表达式，函数体比def简单很多

.lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去

.lambda函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数

.虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用内存，从而增加运行效率

```
>>> sum = lambda arg1, arg2: arg1 + arg2
>>> print ("两数相加后的值为： ", sum( 10, 20))
两数相加后的值为：  30
```

###**变量作用域**

变量的作用域决定了在哪一部分可以访问哪个特定的变量名称,Python的作用域一共有四种：

.Local 局部作用域

.Enclosing  闭包函数外的函数中

.Global 全局作用域

.Built -in  内置作用域

查找规则是L->E->G->B

 ```python
g_count = 0  # 全局作用域
def outer():
    o_count = 1  # 闭包函数外的函数中
    def inner():
        i_count = 2  # 局部作用域
 ```

内置作用域是通过一个名为builtin的标准模块来实现的，但是这个变量自身并没有放入内置作用域内，所以必须导入该模块。

```python
>>> import builtins
>>> dir(builtins)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
>>> 
```

Python 中只有模块module、类class、以及函数(def、lambda)才会引入新的作用域。其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的

```python
>>> if True:
	message = 'Come on, you can do it'

	
>>> message
'Come on, you can do it'
>>> 
```

如上，message变量定义在if语句块中，但外部还可以访问。若定义在函数中，则就是局部变量，外部无法访问。

```python
>>> def function_test():
	message_inner = 'Come on, you can do it'

	
>>> message_inner
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    message_inner
NameError: name 'message_inner' is not defined
>>> 
```

### **全局变量和局部变量**

定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。调用函数时，所有在函数内声明的变量名称都将在被加入到作用域中。

###**global 和 nonlocal关键字**

当内部作用域想修改外部作用域的变量时，就要用到golbal和nonlocal关键字。

```python
>>> def fun1():
	global num
	print (num)
	num = 23
	print (num)

	
>>> fun1()
2
23
```

若需要修改嵌套作用域 (enclosing作用域，外层非全局作用域)中的变量则需要nonlocal关键字

```python
>>> def outer():
	num = 10
	def inner():
		nonlocal num
		num = 100
		print (num)
	inner()
	print (num)

	
>>> outer()
100
100
```



## **Python基础简单应用**

###**1+3+5+7+…+99 的求和**

第一种方案，直接运用系统sum函数

```python
>>> print(sum(range(1,100,2)))
2500
```

第二种方案，for循环

```python
>>> total_number = 0
>>> for number in range(1,100,2)
SyntaxError: invalid syntax
>>> for number in range(1,100,2):
	total_number += number

>>> print ("1+3+5+7+…+99之和", total_number)
1+3+5+7+…+99之和 2500
```

第三种方案，while循环

```python
>>> while number < 100:
	total_number += number
	number += 2

>>> print ("1+3+5+7+…+99之和", total_number)
1+3+5+7+…+99之和 2500
```

优化方案：

```python
>>> while length < 25:
	total_number += (number + (100 - number))
	number += 2
	length += 1

>>> print ("1+3+5+7+…+99之和", total_number)
```

###**斐波那切数列Fibonacci series**

1，1，2，3，5，……..

```python
>>> total_max = input("斐波那切数列最后一位不大于？ 请输入：")
斐波那切数列最后一位不大于？ 请输入  100
>>> a, b = 0, 1
>>> while b < int(total_max):
	print (b)
	a, b= b, a+b

1
1
2
3
5
8
13
21
34
55
89
>>> 
```

其中，a, b= b, a+b的计算方式为先计算右边表达式，然后同时赋值给左边，等价于

n = b

m = a+b

a = n

b = m