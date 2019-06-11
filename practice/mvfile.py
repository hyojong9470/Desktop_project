#파이썬으로 폴더 및 파일 옮기기

import shutil
import os

dst = "C:\\Users\\hyojong\\Desktop\\대죄\\show\\"   # 저장이 되는 폴더
#f_num = len(os.listdir("C:\\Users\\hyojong\\Desktop\\대죄\\"))
f_list = os.listdir("C:\\Users\\hyojong\\Desktop\\대죄\\")

first=0
second=0
third=0


for i in f_list:
    filenames = os.listdir("C:\\Users\\hyojong\\Desktop\\대죄\\%s\\" %i)
    for h in filenames:

        file = os.listdir("C:\\Users\\hyojong\\Desktop\\대죄\\%s\\%s" %(i,h))
        length=len(file)
        a=chr(97+first) #파일 첫째자리 알파벳
        b=chr(97+second) #파일갯수가 알파벳 a~z를 초과할떄를 대비한 여분의 둘째자리 a~z
        c=chr(97+third) #파일개수가 300개가 넘어 알파벳 갯수(26*26)를 초과하여 3째자리로 대비
        first +=1
        if a=='z':
            first=0
            second+=1
        if b=='z':third+=1

        for j in range(0, length):
            shutil.move("C:\\Users\\hyojong\\Desktop\\대죄\\%s\\%s\\%s" %(i,h,file[j]),dst+"%s%s%s%02d.jpg" %(c,b,a,j))

print("Done")


