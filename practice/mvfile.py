import shutil
import os
    #C:\Users\hyojong\Desktop\h1
    #C:\Users\hyojong\Desktop\h2
#shutil.copy("C:\\Users\\hyojong\\Desktop\\h1\\01.jpg","C:\\Users\\hyojong\\Desktop\\h2\\02.jpg")
src = "C:\\Users\\hyojong\\Desktop\\대죄3\\02\\"
dst = "C:\\Users\\hyojong\\Desktop\\대죄3\\01\\"

i=1

while (os.path.isfile(src+"%02d.jpg" %i))==True:
    shutil.move(src+"%02d.jpg" %i, dst+"a%02d.jpg" %i)
    i=i+1