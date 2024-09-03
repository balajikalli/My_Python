# it is the process of working with files(Reading from or writing to them) - to handle files easily

# 1. basic file operations
# opening file - opened using - open()
# Syntax--   file_object = open("filename", "mode")   # filename- name of the file  -- mode- purpose of opening the file
# Common modes- "read", "Write", "append", "binary mode", "exclusive creation"

# Example-- file = open("example_1.txt", "r")   # i opened file, example_1 for reading


"""
2. 
reading from a file
read() - reads entire content of file as string
readline()- reads one line from the file
readlines()- read all the lines from the file and returns them as a list of strings

Example-- 
file = open("example_1.txt", "r")
content = file.read()
print(content)
file.close()

"""


# 3.  writing to file  -- write(string) - writes given string to file, writelines(list) - writes a list of string to the file

# Example--
# file = open("example_1.txt", "w")
# file.write("Hello Balaji!\n")
# file.writelines(["line 1\n, line 2\n"])
# file.close()


