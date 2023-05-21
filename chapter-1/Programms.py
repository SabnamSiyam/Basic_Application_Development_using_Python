
# # # প্রোগ্রাম-১:ফাংশন ব্যবহার করে আয়তক্ষেত্রের ক্ষেত্রফল নির্ণয়ের প্রোগ্রাম।
import math


def Area():
    lenght = int(input('Enter the value of lenght:'))
    width = int(input('Enter the value of width:'))
    RectangleArea = lenght*width
    print('Area of Rectangle is=', RectangleArea)

# Area()

# # # প্রোগ্রাম-২:ফাংশন ব্যবহার করে দুটি সংখ্যার মধ্যে বৃহত্তম সংখ্যাটি নির্ণয়ের প্রোগ্রাম।


def largest():
    Number1 = int(input('Enter the value of number-1:'))

    Number2 = int(input('Enter the value of number-2:'))

    if (Number1 > Number2):
        print('Largest Number is Number-1 and it is =', Number1)
    else:
        print('The largest number is number-2 & it is =', Number2)

# largest()


# # # প্রোগ্রাম-৩:ফাংশন ব্যবহার করে কতগুলো সংখ্যার গুণফল  নির্ণয়ের প্রোগ্রাম।

def Multiply(numbers):
    total = 1
    for x in numbers:
        total *= x

    return total


# print(Multiply((10, 1, 1, 1, 1)))

# প্রোগ্রাম-৩:ফাংশন ব্যবহার করে কতগুলো সংখ্যার গুণফল  নির্ণয়ের প্রোগ্রাম। (same function with input field)

# numbers = input("Enter the numbers you want to multiply, separated by commas: ").split(",")

def Multiply(numbers):
    total = 1
    for x in numbers:
        total *= int(x.strip())

    return total

# print(Multiply(numbers))


# # # প্রোগ্রাম-৪:ফাংশন ব্যবহার করে  কোনো সংখ্যার ফ্যাক্টরিয়ার মান  নির্ণয়ের প্রোগ্রাম
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

# n = int(input("Input a number to compute the factorial:"))

# print(factorial(n))

# # প্রোগ্রাম-৫:ফাংশন ব্যবহার করে  কোনো সংখ্যা মৌলিক কি না তা নির্ণয়ের প্রোগ্রাম।


def test_prime(n):
    if (n == 1):
        return False
    elif (n == 2):
        return True
    else:
        for x in range(2, n):
            if (n % x == 0):
                return False
            return True
# print(test_prime(int(input("Input number: "))))


# # প্রোগ্রাম-৬:ফাংশন ব্যবহার করে  কোনো স্ট্রিং -কে রিভার্স অর্ডারে সাজানোর   প্রোগ্রাম।


def string_reverse(str1):
    rstr1 = ""
    index = len(str1)
    while index > 0:
        rstr1 += str1[index-1]
        index = index-1
    print(rstr1)

# str1 = input('Enter the string you want to reverse:')
# string_reverse(str1)

# # প্রোগ্রাম-৭:ফাংশন ব্যবহার করে এিভুজ ক্ষেত্রের ক্ষেত্রফল নির্ণয় করার   প্রোগ্রাম লেখ।


def Triangle():
    a = int(input("Enter the value of a :"))
    b = int(input("Enter the value of b :"))
    c = int(input("Enter the value of c :"))
    if ((a+b) > c and (b+c) > a and (c+a) > b):
        s = (a+b+c)/2
        Area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        print("Area of the triangle is :", Area)
    else:
        print("The triangle is not possible")

# Triangle()


# # প্রোগ্রাম-৮:ফাংশন ব্যবহার করে বৃওের ক্ষেত্রফল নির্ণয়ের   প্রোগ্রাম তৈরি কর।
def calculate_area(radius):
    myarea = math.pi*radius**2
    return myarea

# radius = calculate_area(int(input("Please input the radius:")))
# print("The Area of circle is:", radius)


# প্রোগ্রাম-৯:ফাংশন ব্যবহার করে ১ হতে ১০০ পর্যন্ত বিজোড় সংখ্যাগুলোর যোগফল নির্ণয়ের  একটি   প্রোগ্রাম তৈরি কর।
def summation():
    n = 1
    sum = 0
    for n in range(100):
        if n % 2 == 0:
            continue
        sum = sum+n
    return sum


add = summation()
# print("The summation is :", add)


# প্রোগ্রাম-১০:ফাংশন ব্যবহার করে  ফিবোনাকি সিরিজ বের  করার   প্রোগ্রাম লেখ।
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


n = 10
# print("Fibonacci Series:")
# for i in range(n):

# print(fibo(i), end=" ")


# <<<--Have a nice day-->>>

# By Sabnam
# 08-05-2023
