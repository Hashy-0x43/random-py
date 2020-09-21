# Creating a file named "hello.txt".
a = open("hello.txt","w")

# Making the contents of "hello.txt".
a.write("I like Turtles!")

# Telling the computer that I am done with the "hello.txt" file.
a.close()

# Telling the computer that I need to append (modify) the "hello.txt" file.
b = open("hello.txt","a")

# Adding contents to the "hello.txt" file.
b.write("\n")

# Telling the computer that I am done with "hello.txt".
b.close()

# Tell the computer I want to read a file named "hello.txt".
c = open("hello.txt","r")

# Telling the computer to read the file assigned to "c".
print(c)
