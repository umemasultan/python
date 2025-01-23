students={
    "x":{"urdu":76,"math":64},
    "y":{"eng":76,"phy":64}

}
x=students["x"]["urdu"]
print(x)
x=students["x"]["math"]
print(x)



#    "name":"umema",
#     "lname":"khan",
#     "password":"umema@gmail.com",
#     "age":19





#// how to create calculator in python//

print("python calculator")
num1 =int(input("enter ur 1st num"))
num2 =int(input("enter ur 1st num"))
print("Operators types")
print(" + for Add")
print(" - for sub")
print(" * for mul")
print(" / for div")

operators=(input("select the symbol above on:"))
if operators=="+":
    result=num1+num2
if operators=="-":
    result=num1-num2
if operators=="*":
    result=num1*num2
if operators=="/":
    result=num1/num2
else:
    print(f"Result:{result}")