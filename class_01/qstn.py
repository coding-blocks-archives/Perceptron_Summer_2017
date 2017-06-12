"""class A():
	x = 1

a = A()
print a.x

b = [A() for ix in range(5)]
# for ix in range(5):
# 	b.append(A())

for ix in b:
	print ix.x

b[2].x = 10

for ix in b:
	print ix.x"""


class Obj:
	def __init__(self, x=0, y=10):
		self.x = x
		self.y = y

objects = [Obj(1, 0), Obj(70, -1), Obj(11, -1), Obj(4, 2), Obj(-1, 10)]

for ix in objects:
	print ix.x, ix.y

print '-'*80
X = sorted(objects, key=lambda z: [z.y, z.x])

for ix in X:
	print ix.x, ix.y

# s.split('a', 2)
