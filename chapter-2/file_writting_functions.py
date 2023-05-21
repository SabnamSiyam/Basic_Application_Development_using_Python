# simply writing a text using the writing function
file = open('my-info.txt', 'w')
file.write('Congratulations!! Now You are a Python Programmer!!')

file.close()


#  Now open the file in append mode for writing in multi-line text

My_info = open('my-info.txt', 'a')
My_info.write('\nMy name is Sabnam Ahmed Siyam.')
My_info.write("\nI'm studying at Munshiganj Polytechnic Institute.")
My_info.write('\nThe name of my district is Narayanganj.')
My_info.write("\nI'm a student at Munshiganj polytechnic institute.")
My_info.write('\nThe name of my department is CST.')
My_info.write("\nI'm a student of the 21-22 sessions.")

My_info.close()

# to see the text :
x = open('my-info.txt', 'r')
print(x.read())
x.close()

#     <<<---(File Writing Fucntions done)---->>>
# By Sabnam
# 21-05-2023