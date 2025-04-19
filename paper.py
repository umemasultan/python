# Operators
# there are four main types of operators

# 1) Arithimetic operator

a = 8
b = 2

# Add a value
print(a + b)

# Sub a value
print(a - b)

# Mul a value
print(a * b)

# Divi a value
print(a / b)

# exponent a value
print(a ** b)

# floor-divi a value
print(a // b)

# modulus/reminder a value
print(a % b)

# 2) Assignment operator => equal two value


x = "umema"
y = "Sultan"

print(x ==y)
print(x == x)

a :int =12
a  = a + 7
print (a)

a  = a - 7
print (a)

a  = a * 7
print (a)

a  = a / 7
print (a)

a  = a % 7
print (a)

# 3) Comparison operator => compare a two value true or false

#  ==   (equal to) 
#  >    (greater than)
#  <    (less than)
#  >=   (greater or equal to)
#  <=    (less than or equal to)
#  !=    (not equal to)

x = 20
y = 12

print(x == y)

print(x < y)

print(y > x)

print(y <= x)

print(x >= y)

print(x != x)


name =(input("name"))

if name == "umema":
    print("Hello how are you dear")

else:
    ("Invaild Name")

print("how's the day")

# # 2nd condition //

# # check weather
timeofday = input("Enter time of day (morning/evening/afternoon): ")

if timeofday == "morning":
    print("The time is too late.")

elif timeofday == "evening":
    print("The time is too short.")

elif timeofday == "afternoon":
    print("Now you may go.")

else:
    print("Time is up now.")


#4) logical operator ( and or not )

# combine conditionol statment

# True + True = True
# True + False = False
# False + False =False

a = 10
b = 20 
print(a > 10 and b < 20)     #   => and operator
print(a == 10 and b == 20)


# True + False = True
# if one statment is true than a than output will be True
print(a < 10 or b > 20)
print(b > 10 or a < 20)


# not operator

print (not(a == 10 and b == 20))




















# if elif else condition

# marks = 82


# if marks >= 84 :
#     print(" Grade : A")

# elif marks >= 74:
#     print(" Grade : B")

# elif marks >= 62:
#     print(" Grade : C")

# else:
#     print("keep it up")



# marks = 82

# if marks >= 85:
#     print("Grade: A")  # Only for 85 or above
# elif marks >= 75:
#     print("Grade: B")  # 75-84
# elif marks >= 63:
#     print("Grade: C")  # 63-74
# else:
#     print("Keep it up")  # Below 63







