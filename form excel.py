datastudent = open('D:\\pepsy.py\\ProJ.txt','r')
import os
count = []
def show():
    os.system('cls')
    while True:
        print('\t ค้นหาข้อมูลนักเรียน\n\t [x]กลับหน้าแรก')
        y = input('Student ID : ')
        if y in datastudent :
            z = datastudent.readline(y)
            n = datastudent.readline(y)
            d = count.count(y)
            os.system('cls')
            print(y + '  '+ z +'  ' + n,end='  ')
            print('เข้าใช้ ',end='')
            print(d,end='')
            print(' ครั้ง\n')
        elif y == 'x':
            os.system('cls')
            break
        else:
            os.system('cls')
            print('\t***Error***')
show()




