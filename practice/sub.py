

#안녕하세요 조교님 조교님 덕분쓰 :)
#50 이상이면 조교님은 천재 출력
#50 이하면 조교님은 멍청이 출력


import subprocess

x = int(input("50이상의 값이나 50이하의 값 둘중하나 넣어랑"))

if(x>50):
    subprocess.run(['python','print_1.py'], shell=True, check=True, encoding='utf-8')  # 조교님은 천재 출력하는

else:
    subprocess.run(['python','print_2.py'], shell=True, check=True, encoding='utf-8')  # 멍청이 출력하는


#print_1.py
#print("조교님은 천재")

#print_2.py
#print("조교님은 멍청이")