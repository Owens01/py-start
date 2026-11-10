file = open("My_data.txt", "r")

print(file.read()) # reads the entire content of the file
print(file.readline()) # reads the first line of the file
print(file.readlines(), end="") # reads all the lines of the file and returns them as a list
print(file.readable()) # checks if the file is readable


file2 = open("data.txt", "w")
file2.write("This is a new line of text.\n") # writes a new line to data.txt
file2.write("This is another line of text.\n") # writes another line to data.txt
file2.close() # closes the file

file2 = open("data.txt", "a")
file2.write("This line is appended to the file.\n") # appends a new line to data.txt
file2.close() # closes the file