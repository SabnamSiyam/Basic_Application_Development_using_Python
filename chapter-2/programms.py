# Programs of chapter 2:

# প্রোগ্রাম-১ঃ "MyFile.txt" নামে একটি টেক্সট ফাইল তৈরি করে কী-বোর্ড / ইউজার থেকে তিনটি লাইন লিখতে পাইথন প্রোগ্রাম।
# Programm:1
def Programm_1():
    f = open('MyFile.txt', 'w')
    line_1 = input('Enter the line_1 text:')
    line_2 = input('Enter the line_2 text:')
    line_3 = input('Enter the line_3 text:')
    new_line = "\n"
    f.write(line_1)
    f.write(new_line)
    f.write(line_2)
    f.write(new_line)
    f.write(line_3)
    f.write(new_line)
    f.close()

# Programm_1()

# প্রোগ্রাম-২ঃ "info.txt" ফাইল থেকে বড় হাতের অক্ষর (Capital letter) , ছোট হাতের অক্ষর(Small letter) এবং সংখ্যা(Digit) গননা করার জন্য পাইথন প্রোগ্রাম।
# Programm:2


def calcutate_character():
    f = open('my-info.txt', 'r')
    data = f.read()
    count_capital = 0
    count_small = 0
    count_digit = 0
    for x in data:
        if x.islower():
            count_small += 1
        if x.isupper():
            count_capital += 1
        if x.isdigit():
            count_digit += 1
    print('Total Number of Capital Letters are:', count_capital)
    print('Total Number of Small Letters are:', count_small)
    print('Total Number of Digit are:', count_digit)

# calcutate_character()


# প্রোগ্রাম-৩ঃ নিচের স্পেসিফিকেশন অনুযায়ী কার্সরের অবস্থান জানতে পাথন প্রোগ্রাম তৈরিঃ

# i.ইনিশিয়াল পজিশন প্রিন্ট করতে হবে।
# ii.কার্সরকে চতুর্থ অবস্থানে নিয়ে যেতে হবে।
# iii.পরবর্তী পাঁচটি ক্যারেক্টার প্রিন্ট করতে হবে।
# iv. দশম ক্যারেক্টারে কার্সর নিয়ে যেতে হবে।
# v.বর্তমান কার্সর পজিশন প্রিন্ট করতে হবে।
# vi.বর্তমান কার্সর পজিশন থেকে পরবর্তী ১০ টি ক্যারেক্টার প্রিন্ট করতে হবে।

# Programm:3
def Specification():
    f = open('my-info.txt', 'r')
    print(f.tell())  # (i)
    f.seek(4, 0)  # (ii)
    print(f.read(5))  # (iii)
    f.seek(10, 0)  # (iv)
    print(f.tell())  # (v)
    print(f.read(10))  # (vi)

# Specification()


# <<<----(Programs done)---->>>>
# By Sabnam
# 21-05-2023
