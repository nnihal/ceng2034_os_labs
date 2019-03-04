import os

"""
myfolder = os.getcwd()
print(os.system("clear"))
print(myfolder)
print(os.listdir())
print("second index", os.listdir()[1])
#print("_______________________________")
#print("ls -la ", os.system('ls -la'))
print("is it directory? ",os.path.isdir(myfolder))
mypath = os.path.join(myfolder , "another")
print(mypath)
print("is it dir ?", os.path.isdir(mypath))
"""

os.chdir(os.getenv("HOME"))
os.mkdir("os_lab_0")
os.chdir("os_lab_0")
os.system("touch ilayda.txt nihal.txt 1.py")
print (os.system("ls -lt"))
print (os.system("ls *txt"))
