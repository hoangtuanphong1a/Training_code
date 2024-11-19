# -*- coding: utf-8 -*-
"""HoangTuanPhong_98662.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AOxZylcfB16XHOpAYXKSm6xogACLX7Nn
"""

# Question 1: Write a program to find Perimeter and Area of a Rectangle with integers of Width and
# Height
# Step 1: Input : Width, Height
Width  = int(input("Enter Width : "))
Height = int(input("Enter Height: "))
# Step 2: Calculate: Area, Perimeter
Area      = Width*Height
Perimeter = (Width+Height)*2
# Step 3: Ouput
print(f"The rectange with Width - {Width} and Height - {Height} : ")
print(f"\t- Perimeter: {Perimeter}")
print(f"\t- Area     : {Area5}")

import Centimeter

# Question 2: Write a program to convert centimeter to decimeter and inch with float centimeter

#step 1: imput -Centimetar
Centimeter = float(input("Please input Centimeter:"))
#step2: Convert to decimeter anh inch
decimeter = Centimeter*0.1
Inch      = Centimeter/2.54
#step3: ouput
print(f"{Centimeter} Centimeter={decimeter} Decimeter={Inch : 0.3} Inch")

import random

# Question 3: Write a program to random an integer number and check whether this number having two or three digits
# Step 1: Input - number from 1 to 999
number = random.randint(1, 999)

# Step 2: Count digits
def count_digits(num):
    return len(str(num))

# Generate the random number
random_number = random.randint(1, 999)

# Count the digits of the random number
digit_count = count_digits(random_number)

print(f"The random number is: {random_number}")
print(f"Number of digits: {digit_count}")

import random
# Question 3: Write a program to random an integer number and check whether this number having
#two or three digits
# Step 1: Input - number from -999 to 999
number = random.randint(-999,999)
# Step 2: Count digits
count = len(str(abs(number)))
# if 10<= abs(number)<100:
#   count=2
# elif 100<=abs(number)<1000:
#   count=3
# else:
#   count=1
# Step 3: Output
print(f"The number {number} has {count} digits")

# Question 5: Write a program to random an integer number in range [10, 150] and normalize it into range [0, 1]
import random

# Generate a random integer in the range [10, 150]
x = random.randint(10, 150)

# Normalize the number to the range [0, 1]
normalized_x = (x - 10) / (150 - 10)

print(f"The random number is: {x}")
print(f"The normalized number is: {normalized_x}")

# Question 6: Write a program to find degree and radian angle between hours and minute hands
# with integers hour and minite
import math

def find_angle(hour, minute):

    if hour >= 12:
        hour -= 12


    hour_angle = 0.5 * (hour * 60 + minute)
    minute_angle = 6 * minute


    angle = abs(hour_angle - minute_angle)


    angle = min(360 - angle, angle)

    return angle

def degrees_to_radians(degrees):
    return degrees * (math.pi / 180)


hour = 3
minute = 30

angle_in_degrees = find_angle(hour, minute)
angle_in_radians = degrees_to_radians(angle_in_degrees)

print(f"Angle: {angle_in_degrees} degrees")
print(f"Angle: {angle_in_radians} radians")

import math
# Question 7: Write a program to Solve the quadratic equation x^2 + 5*x + 6 = 0
# and print step by step (discriminant, check condition of discriminant, solutions)k
# Function to solve the quadratic equation
def solve_quadratic(a, b, c):
    print(f"Solving the quadratic equation: {a}x^2 + {b}x + {c} = 0")


    discriminant = b**2 - 4*a*c
    print(f"Discriminant: {discriminant}")

    if discriminant > 0:
        print("Discriminant is positive. Two real solutions exist.")
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print(f"Solution 1: {root1}")
        print(f"Solution 2: {root2}")
    elif discriminant == 0:
        print("Discriminant is zero. One real solution exists.")
        root = -b / (2*a)
        print(f"Solution: {root}")
    else:
        print("Discriminant is negative. No real solutions exist.")
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        print(f"Solution 1: {real_part} + {imaginary_part}i")
        print(f"Solution 2: {real_part} - {imaginary_part}i")

a = 1
b = 5
c = 6

solve_quadratic(a, b, c)

# Question 8: Assume we have a string "Today is Sunday and we don't need to wake up at 6 am".
# # Print how many words in the string and check whether number in string. Print position of that
# number in string
def analyze_string(s):

    words = s.split()
    word_count = len(words)

    positions = []
    for i, word in enumerate(words):
        if any(char.isdigit() for char in word):
            positions.append(i)

    print(f"Số từ trong chuỗi: {word_count}")

    if positions:
        print(f"Có số trong chuỗi. Vị trí của số trong chuỗi là: {positions}")
    else:
        print("Không có số trong chuỗi.")


s = "Today is Sunday and we don't need to wake up at 6 am"


analyze_string(s)

# Question 9: From the keyboard input the student profile including :
# Name of Subject 1,2,3 and Mark of Subject 1,2,3.
# Name of Student and Date of Birth
# And print the profile of these students with Average Mark
# Function to calculate average mark
def calculate_average(mark1, mark2, mark3):
    return (mark1 + mark2 + mark3) / 3

def input_student_profile():

    student_name = input("Name of Student: ")
    date_of_birth = input("Date of Birth (dd/mm/yyyy): ")


    subject1 = input("Name of Subject 1: ")
    mark1 = float(input(f"Mark of {subject1}: "))

    subject2 = input("Name of Subject 2: ")
    mark2 = float(input(f"Mark of {subject2}: "))

    subject3 = input("Name of Subject 3: ")
    mark3 = float(input(f"Mark of {subject3}: "))


    average_mark = calculate_average(mark1, mark2, mark3)


    print("\nStudent Profile:")
    print(f"Name: {student_name}")
    print(f"Date of Birth: {date_of_birth}")
    print(f"{subject1}: {mark1}")
    print(f"{subject2}: {mark2}")
    print(f"{subject3}: {mark3}")
    print(f"Average Mark: {average_mark:.2f}")


input_student_profile()

# Câu hỏi 10: Nhập từ bàn phím hai điểm với (x,y)
# và in ra khoảng cách Euclidean, Manhattan, Cosine của các điểm.
import math

#  Euclidean
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

#  Manhattan
def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

#  Cosine
def cosine_similarity(p1, p2):
    dot_product = p1[0] * p2[0] + p1[1] * p2[1]
    magnitude_p1 = math.sqrt(p1[0] ** 2 + p1[1] ** 2)
    magnitude_p2 = math.sqrt(p2[0] ** 2 + p2[1] ** 2)
    if magnitude_p1 == 0 or magnitude_p2 == 0:
        return 0
    return dot_product / (magnitude_p1 * magnitude_p2)

# Nhập tọa độ hai điểm từ bàn phím
x1, y1 = map(float, input("Nhập tọa độ điểm thứ nhất (x1, y1): ").split())
x2, y2 = map(float, input("Nhập tọa độ điểm thứ hai (x2, y2): ").split())

point1 = (x1, y1)

# Question 11: Input from keyboards your birthday with day, month year
# and print information about weekday name, month name, and your age now
from datetime import datetime

def get_weekday_name(date):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[date.weekday()]

def get_month_name(date):
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    return months[date.month - 1]

def calculate_age(birthday):
    today = datetime.today()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    return age

# Input your birthday
birthday_input = input("Enter your birthday (dd/mm/yyyy): ")
birthday = datetime.strptime(birthday_input, "%d/%m/%Y")

# Calculate and print the information
weekday_name = get_weekday_name(birthday)
month_name = get_month_name(birthday)
age = calculate_age(birthday)

print(f"You were born on a {weekday_name}.")
print(f"The month of your birth is {month_name}.")
print(f"You are {age} years old.")
#co tham khao

# Question 12: Input four lists of Customer, Product, Quantity
# A. Create a DataFrame from three lists above
# B. Seperate column QuantityList to Quantity and Unit
# C. Find customer information who bought Pork over 2kg
#CustomerList = ["John", "John", "Marry", "Marry", "Marry"]
#ProductList = ["Beer", "Pork", "Milk", "Vegetable", "Pork"]
#QuantityList = ["2 Bottles", "1 kg", "5 boxes", "2 bunches", "3 kg"]
import pandas as pd

# Dữ liệu đầu vào
CustomerList = ["John", "John", "Marry", "Marry", "Marry"]
ProductList = ["Beer", "Pork", "Milk", "Vegetable", "Pork"]
QuantityList = ["2 Bottles", "1 kg", "5 boxes", "2 bunches", "3 kg"]

# A. Tạo DataFrame từ ba danh sách trên
data = {
    'Customer': CustomerList,
    'Product': ProductList,
    'QuantityList': QuantityList
}

df = pd.DataFrame(data)
print("DataFrame:")
print(df)

# B. Tách cột QuantityList thành Quantity và Unit
df[['Quantity', 'Unit']] = df['QuantityList'].str.extract(r'(\d+)\s*(\w+)')
df['Quantity'] = df['Quantity'].astype(int)
print("\nDataFrame sau khi tách cột QuantityList:")
print(df)

# C. Tìm thông tin khách hàng mua Pork trên 2kg
pork_over_2kg = df[(df['Product'] == 'Pork') & (df['Unit'] == 'kg') & (df['Quantity'] > 2)]
print("\nKhách hàng mua Pork trên 2kg:")
print(pork_over_2kg)

#co tham khao