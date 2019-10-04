






class TestClass():

    def __init__(self, shit, num, domi):

        print(shit)
        self.shit = shit
        self.domi = domi
        self.num = num

    def was_steht_drin(self):
        print(self.shit)








def add(a,b):
    return a + b


x = add(4,3)
print(x)


c = TestClass("mein zeug", 7, 48)

c.was_steht_drin()

print(c.domi)
print(c.num)

z = 42.


print(str(c.domi) + c.shit)

print(c.domi + z)


f = lambda x,y: x+y

l = []

l.append(2)
l.append("werswerasdf")
l.append(48)

print(f(2,3))

print(l)

for i,element in enumerate(l):
    print(i, element)


dic = {}

dic["domi"] = "nico"
dic["marc"] = 22

print(dic)

print(dic["domi"])

print("Hello World!")

print("git test")