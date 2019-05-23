#concepts about "lists" type in python

#record from thinkCSpy.pdf (Users\39438\OneDrive\Mit_ocw\MIT6.189\Python)
'''
Lists
	• is an ordered set of values
	• can have any type
	• sequences
'''
# 8.1 List values
# Lists that contain consecutive integers are common, so Python provides a simple way to create them:
>>> range(1,5)
[1, 2, 3, 4]
>>> range(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(1, 10, 2)
[1, 3, 5, 7, 9]

# 8.4 List membership
>>> horsemen = [’war’, ’famine’, ’pestilence’, ’death’]
>>> ’pestilence’ in horsemen
True
>>> ’debauchery’ not in horsemen
True

# 8.6 List operations
>>> a = [1, 2, 3]
>>> b = [4, 5, 6]
>>> c = a + b
>>> print c
[1, 2, 3, 4, 5, 6]
>>> [0] * 4
[0, 0, 0, 0]
>>> [1, 2, 3] * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]

# 8.9 List deletion
>>> a = [’one’, ’two’, ’three’]
>>> del a[1]
>>> a
[’one’, ’three’]
>>> list = [’a’, ’b’, ’c’, ’d’, ’e’, ’f’]
>>> del list[1:5]
>>> print list
[’a’, ’f’]

# 8.10 Objects and values
# In one case, a and b refer to two different things that have the same value. In the second case, they refer to the same thing. These “things” have names—they are called objects. An object is something a variable can refer to. Every object has a unique identifier, which we can obtain with the id function. By printing the identifier of a and b, we can tell whether they refer to the same object.
>>> id(a)
135044008
>>> id(b)
135044008
# In fact, we get the same identifier twice, which means that Python only created one string, and both a and b refer to it. Interestingly, lists behave differently. When we create two lists, we get two objects:
>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>> id(a)
135045528
>>> id(b)
135041704
# a and b have the same value but do not refer to the same object.

# 8.12 Cloning lists
# The easiest way to clone a list is to use the slice operator:
>>> a = [1, 2, 3]
>>> b = a[:]
>>> print b
[1, 2, 3]
# Now we are free to make changes to b without worrying about a

# 8.13 List parameters
# If a function modifies a list parameter, the caller sees the change. For example, deleteHead removes the first element from a list:
def deleteHead(list):
	del list[0]
# Here’s how deleteHead is used:
>>> numbers = [1, 2, 3]
>>> deleteHead(numbers)
>>> print numbers
[2, 3]
# If a function returns a list, it returns a reference to the list. For example, tail returns a list that contains all but the first element of the given list:
def tail(list):
	return list[1:]
# Here’s how tail is used:
>>> numbers = [1, 2, 3]
>>> rest = tail(numbers)
>>> print rest
[2, 3]
# Because the return value was created with the slice operator, it is a new list. Creating rest, and any subsequent changes to rest, have no effect on numbers.

# 8.16 Strings and lists
>>> import string
>>> song = "The rain in Spain..."
>>> string.split(song)
[’The’, ’rain’, ’in’, ’Spain...’]
>>> string.split(song, ’ai’)
[’The r’, ’n in Sp’, ’n...’]
# The join function is the inverse of split. It takes a list of strings and concatenates the elements with a space between each pair:
>>> list = [’The’, ’rain’, ’in’, ’Spain...’]
>>> string.join(list)
’The rain in Spain...’
>>> string.join(list, ’_’)
’The_rain_in_Spain...’

#--------------------------------------------------------------

#record from MIT6_01SCS11_notes.pdf (Users\39438\OneDrive\Mit_ocw\MIT6.189\Python)
# list comprehensions(列表解析式, 语法糖):
# 将一个列表转换成另一个列表的工具
# The basic template is
# [<resultExpr> for <var> in <listExpr> if <conditionExpr>]

# *resultVar* = []
# for <var> in <listExpr>:
# 	if <conditionExpr>:
# 		*resultVar*.append(<resultExpr>)
# *resultVar*

# Whew. It is probably easier to understand it by example. 
>>> [x/2.0 for x in [4, 5, 6]]
[2.0, 2.5, 3.0]
>>> [y**2 + 3 for y in [1, 10, 1000]]
[4, 103, 1000003]
>>> [a[0] for a in [[’Hal’, ’Abelson’],[’Jacob’,’White’],[’Leslie’,’Kaelbling’]]]
[’Hal’, ’Jacob’, ’Leslie’]
>>> [a[0]+’!’ for a in [[’Hal’, ’Abelson’],[’Jacob’,’White’],[’Leslie’,’Kaelbling’]]]
[’Hal!’, ’Jacob!’, ’Leslie!’]

# Another built-in function that is useful with list comprehensions is  zip . Here are some examples of how it works: 
> zip([1, 2, 3],[4, 5, 6])
[(1, 4), (2, 5), (3, 6)]
> zip([1,2], [3, 4], [5, 6])
[(1, 3, 5), (2, 4, 6)]
# Here is an example of using  zip with a list comprehension: 
>>> [first+last for (first, last) in zip([’Hal’, ’Jacob’, ’Leslie’],[’Abelson’,’White’,’Kaelbling’])]
[’HalAbelson’, ’JacobWhite’, ’LeslieKaelbling’]
# Note that this last example is very different from this one: 
>>> [first+last for first in [’Hal’, ’Jacob’, ’Leslie’] \
			for last in [’Abelson’,’White’,’Kaelbling’]]
[’HalAbelson’, ’HalWhite’, ’HalKaelbling’, ’JacobAbelson’, ’JacobWhite’,’JacobKaelbling’, ’LeslieAbelson’, ’LeslieWhite’, ’LeslieKaelbling’]
# Nested list comprehensions behave like nested  for loops, the expression in the list comprehen-sion is evaluated for every combination of the values of the variables. 

#--------------------------------------------------------------
#python list 增加元素的三种方法
# append 翻译成中文是：追加
# 在Python中append 用来向 list 的末尾追加单个元素，此元素如果是一个list，那么这个list将作为一个整体进行追加。
# 例如：
# Python代码
li=['a', 'b']   
li.append([2,'d'])   
li.append('e')   
#输出为：['a', 'b', [2, 'd'], 'e']  
li=['a', 'b'] li.append([2,'d']) li.append('e') 
#输出为：['a', 'b', [2, 'd'], 'e']
 
# insert 翻译成中文是：插入
# 在Python中 insert 用来将单个元素插入到list中。数值参数是插入点的索引。
# 例如：
# Python代码
li=['a', 'b']   
li.insert(0,"c")   
#输出为:['c', 'a', 'b']  
li=['a', 'b'] li.insert(0,"c") 
#输出为:['c', 'a', 'b']
 
# extend 翻译成中文是：延长
# 在Python中extend用来连接list。请注意不要使用多个参数来调用extend，要使用单个 list 参数进行调用。
# 例如：
# Python代码
li=['a','b']   
li.extend([2,'e'])   
#输出为：['a', 'b', 2, 'e']  
li=['a','b'] li.extend([2,'e']) 
#输出为：['a', 'b', 2, 'e'] 
# 这三者之间如何选用：
# append多用于把元素作为一个整体插入
# insert多用于固定位置插入
# extend多用于list中多项分别插入
