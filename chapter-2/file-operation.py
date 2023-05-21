#  File opening modes: [Basic idea]

# 1.Create Mode:(for creat a new file)
# New_created_file=open('New_created_file.txt','x')
# New_created_file.close()

# 2.Write Mode: (For writing in the file)
file = open('New_created_file.txt', 'w')
file.write('hello world.')
file.close()

# 3.Read Mode: (For reading the file)
file = open('New_created_file.txt', 'r')
read = file.read()
# print(read)
file.close()

# 4.Append Mode: (For adding something in the last of the existing file)
old_file = open('New_created_file.txt', 'a')
Write_Newly = old_file.write(
    '\nWelcome To Python Programming Language.(it was newly appended to the Previous text)')
old_file.close()

text = open('New_created_file.txt', 'r')
read = text.read()
print(read)
text.close()

#    <<<--- File Opening Modes Done--->>>
# By Sabnam
# 21-05-2023
