# Questions to practice

## Questions

1. Calculate length of a list

2. which will create a list:
    - `some_list = list()`
    - `some_list = list([1, 2, 3])`
    - `some_list = [1, 2, 3]`
    - `some_list = list(1, 2, 3)`

3. let a list be `s = [1, 3, 2, 1, 5, 3, 9]`. use `min(s)`, `max(s)`, `sum(s)`.
    also calculate the average of the list.

4. use `import random` and call `random.shuffle(some_list)` to shuffle the contents of the list `some_list`.

5. print the last 3 elements of a list without using for loops.

6. let `some_list = [1, 2, 3, 6, 5, 1, 7, 3]`. what is the output of:
 - `some_list[:-1]`
 - `some_list[-4:-2]`
 - `some_list[2:-3]`

7. Let this section of code
```python
    def extendList(val, list=[]):
    	list.append(val)
    	return list

	list1 = extendList(10)
	list2 = extendList(123,[])
	list3 = extendList('a')

	print "list1 = %s" % list1
	print "list2 = %s" % list2
	print "list3 = %s" % list3
```
> What should be the output?

> Why is it different?

> How to fix this?

. 
8. given some code using classes:
```python
    class A():
        x = 1
    
    a = A()
    print a.x
    
    b = [A()] * 10
    
    for ix in b:
        print ix.x
    
    b[2].x = 5
    
    for ix in b:
        print ix.x
```

> Why is output different from expected? 

> How can we fix this problem?

.
9. use `sorted` in lists. consider the code below:
```python
class Obj:
	def __init__(self, a=0, b=1):
		self.a = a
		self.b = b

if __name__ == "__main__":
	objects = [Obj(1, 2), Obj(5, 4), Obj(7, 3),
				Obj(11, 42), Obj(8, 0), Obj(5, 9)]
	
``` 
> Sort the above list of objects using
>> a as key
>> b as key

.
10. List and string slicing	
```python
s = "This is introduction to python for web development"

# Obtain each word of the string in a list.
```
.
11. Print Pyramid patterns using for and while loops
> @
> 
> @@
> 
> @@@
> 
> @@@@
> 
> @@@@@

.
12. What will the following code print
```python
some_string = "abacdaegakialaop"
print some_string.split('a', 2)
```
