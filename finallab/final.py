import magic
import os
import shutil
from os import path
#import time

folders = ['pngF', 'jpegF','txtF', 'mp3F']
for f in folders:
	os.makedirs(f)



def main():

    if path.exists("pngF"):
	
        src = path.realpath("pngF");
		

	os.rename('pngF','pngFOL') 
	
if __name__ == "__main__":
    main()


def main():

    if path.exists("jpegF"):
	
        src = path.realpath("jpegF");
	os.rename('jpegF','jpegFOL') 	
if __name__ == "__main__":
    main()
 

def main():

    if path.exists("txtF"):
	
        src = path.realpath("txtF");
	os.rename('txtF','txtFOL')
	
if __name__ == "__main__":
    main()


def main():

    if path.exists("mp3F"):
	
        src = path.realpath("mp3F");
        os.rename('mp3F','mp3FOL') 	
if __name__ == "__main__":
    main()

#check file types???

files = os.listdir(".")
for f in files:
    os.rename(f, f+filetype(f))



 magic.from_file('jpegF')
'JPEG image data'
 magic.from_file('jpegF', mime=True)
'image/jpeg'

 magic.from_file('pngF')
'PNG image data'

magic.from_file('pngF', mime=True)
'image/png'



for i in range (1,0):
    name = "{0}/{1}{2}".format(a, "file", i)
    origin = "{0}{1}".format("file", random.randint(1,4))
    shutil.copyfile(origin, name )





