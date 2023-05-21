# To read the full text:
info = open('my-info.txt', 'r')
print(info.read())

# To read fixed character text from text file:
file = open('my-info.txt', 'r')

First_5_character = file.read(5)
print(First_5_character)

Remaining_10_character = file.read(10)
print(Remaining_10_character)

rest_of_the_file = file.read()
print(rest_of_the_file)

file.close()

# -------------------------------------------------------------------
# To read file content line by line:
# Using Readlines function:

f = open('app.log', 'w')
# first line
f.write("Wow! I'm now a python programmer. \n")
# second line

f.write("Yes, buddy now I can do programming!\n")
# third Line
f.write("So now it's time to play python python!!")
f.close()

f = open('app.log', 'r')
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

# Using For loop:
file=open('app.log','r')

for x in file:
    print(x)
file.close()

#  <<<---(File Reading Fucntions done)---->>>