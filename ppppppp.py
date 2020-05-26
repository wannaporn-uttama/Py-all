#data_ = open('D:\\pepsy.py\\ProJ.txt','w')
import os
os.system('cls')
count = []
data_ = open('D:\\pepsy.py\\ProJ.txt','r')
datastudent = {
    "623050049-8":"นางสาวฐิติพร สวงโท",
    "623050050-3":"นางสาวณัฐณิชา เวียงเงิน",
    "623050051-1":"นางสาวธิดารัตน์ สีชุมแสง",
    "623050052-9":"นางสาวนันทวัน พูนสุข",
    "623050053-7":"นายพงศกร เฮงสวัสดิ์",
    "623050054-5":"นายภานุวัฒน์ ขมวดทรัพย์",
    "623050055-3":"นางสาววรรณพร อุตตะมะ",
    "623050056-1":"นายวิษณุกร อัดโดดดร",
    "623050272-5":"นายกนกพล ชูศรียิ่ง",
    "623050273-3":"นางสาวกาญจนาภา เอี่ยมศรี",
    "623050274-1":"นายทรงยุทธ บาลี",
    "623050275-9":"นายธนภัทร ทิพศรีราช",
    "623050276-7":"นางสาวธันยชนก ทรวงโพธิ์",
    "623050277-5":"นายนริศร์ ญาติสังกัด",
    "623050278-3":"นางสาวนัฐติกา อนุญาหงษ์",
    "623050279-1":"นายประกฤษฎิ์ ภูวิจิตร",
    "623050280-6":"นายปรัชญา คำครณ์",
    "623050281-4":"นางสาวเสาวภาคย์ นาชัยทอง",
    "623050282-2":"นางสาวอรชพร เมยมงคล",
    "623050283-0":"นางสาวอรพันธุ์ กั้ววัลย์",
    "623050410-9":"นายชยุตม์ ศรีบุญเรือง",
    "623050411-7":"นายนัทธพงศ์ ถวิลการ",
    "623050412-5":"นางสาวภาคินี ทีทา",
    "623050413-3":"นางสาวมนสิชา หมู่สูงเนิน",
    "623050414-1":"นายรุจิภาส นิมิตจตุรงค์",
    "623050415-9":"นางสาวศศินิภา มูลมัง",
    "623050416-7":"นายอภิสิทธิ์ ลุนอุบล",
    "623050502-4":"นายพิเชษฐ์ ดาศรี",
    "623050503-2":"นายสุทธินันท์ พานิพัด",
}
clas = {
    "623050049-8":"COM16",
    "623050050-3":"COM16",
    "623050051-1":"COM16",
    "623050052-9":"COM16",
    "623050053-7":"COM16",
    "623050054-5":"COM16",
    "623050055-3":"COM16",
    "623050056-1":"COM16",
    "623050272-5":"COM16",
    "623050273-3":"COM16",
    "623050274-1":"COM16",
    "623050275-9":"COM16",
    "623050276-7":"COM16",
    "623050277-5":"COM16",
    "623050278-3":"COM16",
    "623050279-1":"COM16",
    "623050280-6":"COM16",
    "623050281-4":"COM16",
    "623050282-2":"COM16",
    "623050283-0":"COM16",
    "623050410-9":"COM16",
    "623050411-7":"COM16",
    "623050412-5":"COM16",
    "623050413-3":"COM16",
    "623050414-1":"COM16",
    "623050415-9":"COM16",
    "623050416-7":"COM16",
    "623050502-4":"COM16",
    "623050503-2":"COM16",
}
#data_.write(datastudent)
def add_student():
    while True : 
        print('\tกรอกข้อมูลนักเรียน\n\t[x]กลับหน้าแรก\n')
        x = input("Student ID : ")
        if x == 'x':
            break
        datastudent[x] = input("Name : ")
        clas[x] = input("class : ")
        os.system('cls')  
        print('  *******ข้อมูลเข้าสู่ระบบ********\n')
    os.system('cls')
        
def show():
    os.system('cls')
    while True:
        print('\t ค้นหาข้อมูลนักเรียน\n\t [x]กลับหน้าแรก')
        y = input('Student ID : ')
        if y in datastudent :
            z = datastudent.get(y)
            n = clas.get(y)
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

def all():
    os.system('cls')
    print('\t\t\t     รายชื่อนักเรียนทั้งหมด\n')
    while True :
        i=0
        for y in datastudent :
            z = datastudent.get(y)
            n = clas.get(y)
            d = count.count(y)
            i += 1
            print('{0: <3}.'.format(i),end='')
            print('{0: <14}{1:<40}{2:<7}'.format(y,z,n),end='')
            print('{0:<10}'.format('เข้าใช้ '),end='')
            print('{0: <4}'.format(d),end='')
            print(' ครั้ง')
        e = len(count)
        print('รวมทั้งหมด ----> ',end='')
        print(e,end='')
        print(' ครั้ง ')
        f = input('[1]ลบข้อมูลนักเรียน\n[x]กลับหน้าแรก\n--> ')
        if f == '1':
            os.system('cls')
            l = input('\tลบข้อมูลนักเรียน\nStudent ID : ')
            datastudent.pop(l)
            clas.pop(l)
            for o in count:
                count.remove('%s'%l)
            os.system('cls')
        elif f == '2':
            os.system('cls')
            break
        else :
            os.system('cls')
            print('\t***Error***')
    
def check():
    os.system('cls')
    while True:
        print('\t ลงชื่อเข้าใช้\n\t [x]กลับหน้าแรก')
        y = input('Student ID : ')
        if y in datastudent :
            count.append(y)
            os.system('cls')
            print('*****ข้อมูลเข้าสู่ระบบแล้ว******\n')
        elif y == 'x':
            os.system('cls')
            break
        else :
            os.system('cls')
            print('\t***Error***')

while True :
    print('{0:*<32}'.format(''))
    x = input('**** จำนวณการเข้าใช้งานห้องสมุด ****\n[1]ลงชื่อเข้าใช้ \n[2]เพิ่มข้อมูลนักเรียน \n[3]แสดงข้อมูลนักเรียน \n[4]ข้อมูลทั้งหมด \n[5]Exit \n--> ')
    if x == '1':
        check()
        continue
    elif x == '2':
        add_student()
        continue
    elif x == '3':
        show()
        continue
    elif x == '4':
        all()
        continue
    elif x == '5':
        #data_.write()
        data_.close()
        break
    else :
        print('Error')