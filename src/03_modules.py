"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
print(sys.argv)
print(sys.argv[0])
for i in sys.argv:
    print(i)

# Print out the OS platform you're using:
# YOUR CODE HERE
print(sys.platform)
print("OS Platform:", sys.platform.upper())

# Print out the version of Python you're using:
# YOUR CODE HERE
print(sys.version)
print("Python version:", sys.version)

import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print(os.getpid())
print("OS process ID:", os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE
print(os.getcwd())
print("OS CWD:", os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE
print(os.getlogin())
print("machine login name:", os.getlogin())
