# type casting => convert a value into another datatype

a = 1 
print(type(a))

b = "1"
print(type(b))

c = int (b)
print(type(c))
 
print(a + int(b))

# all str type can't be casted into numerical type


name = "umema"
new_name = int (name)

# all numerical type can be into string
num = 26
my_num = str(num)
print(type(my_num))

# change into int
x=22.53
y= int (x)
print(y)
print(type(y))

# change int float value




a = 22
print(type(float(a)))

# implicit casting  => automatic change by interpreter

var1 = 23  # int  type
var2 = 72.3  # float  type
var3 = var1 + var2
print(var3)
print(type(var3))


# explicit type casting  =>  manually change coder

a = 101
b = str (a)
print(type(b))


a1= bool(0)
print(a1)
print(type(a1))

a= bool(1)
print(a)
print(type(a))





