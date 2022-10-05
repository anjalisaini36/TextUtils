import os
import sys
print("current working directory", os.getcwd())
path = "C:\Users\HP\PycharmProjects\textutils\textutils"
os.chdir(path)
print("current working directory", os.getcwd())