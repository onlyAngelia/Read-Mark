[TOC]

#**第一题：1+3+5+7+…+99 的求和**

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

利用等差数列求和公式计算：Sn=n(a1+an)/2

```python
>>> Sn = 0,a1 = 1,an = 99
>>> Sn = (a1 + an)/2 * 50
>>> print ('1+3+5+7+...+99 = ',int(Sn))
1+3+5+7+...+99 =  2500
```

#**第二题：斐波那切数列Fibonacci series**

1，1，2，3，5，……..

```python
>>> total_max = input("斐波那切数列最后一位不大于？ 请输入：")
斐波那切数列最后一位不大于？ 请输入  100
>>> a, b = 0, 1
>>> while b < int(total_max):
	print (b)
	a, b = b, a+b

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