import os

os.chdir(os.getenv("HOME"))
os.chdir('..')
os.chdir('..')
os.chdir("../mnt")
print (os.getcwd())
#real_root = os.open("/", os.O_RDONLY)
#os.chroot("/mnt/new_root")
#Chrooted environment
# Put statements to be executed as chroot here
#os.fchdir(real_root)
#print os.getcwd()
#os.chroot("/bin/etc/lib/lib64")
os.system("/lib/x86_64-linux-gnu/libc.so.6")
os.system("/lib64/ld-linux-x86-64.so.2")
os.system("sudo chroot /bashjail/ /bin/bash")
print(cwd)
os.path.realpath(path)
