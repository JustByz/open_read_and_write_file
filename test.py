

# import pathlib
# from pathlib import Path, PureWindowsPath
# # C:\Users\Denis\Desktop\open, read and write file\task3
# p = pathlib.Path('1.txt')
# print(p)

import os
p = os.path.abspath('1.txt ')
# with open(p, encoding='utf-8') as one_file:
#     print(one_file.read())
f = open(p, encoding='utf-8')