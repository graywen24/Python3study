
'''
Sequence是Python的一种内置类型（built-in type），内置类型就是构建在Python Interpreter里面的类型，
三种基本的Sequence Type是list（表），tuple（定值表，或翻译为元组），range（范围）。可以看作是Python Interpreter定义了这样三个class。
字符串也是一种序列
序列类型是一个基类包括：
字符串
元组 tuple
列表 list
'''
#list sample
ls = ["python",1,2,3,4,5]
newls = ls[::-1]
print(newls) #[5, 4, 3, 2, 1, 'python']
print(len(newls)) #6





#emple
lt = ()
print(type(lt))
#add 5 new elements to the turple

