from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title = "datastudent" #ชื่อ worksheet

datastudent = {}
checkk = {}
clas = {}
count = []
def add_student():
    while True : 
        print('\tกรอกข้อมูลนักเรียน\n\t      [x]Exit\n')
        x = input("Student ID : ")
        if x == 'x':
            break
        datastudent[x] = input("Name : ")
        clas[x] = input("class : ")  
        print('  *******ข้อมูลเข้าสู่ระบบ********\n')
        
def show():
    y = input('Student ID : ')
    if y in datastudent :
        z = datastudent.get(y)
        n = clas.get(y)
        d = count.count(y)
        print(y + '  '+ z +'  ' + n,end='  ')
        print('เข้าใช้ ',end='')
        print(d,end='')
        print(' ครั้ง')

def all():
    for y in datastudent :
        i = 0
        z = datastudent.get(y)
        n = clas.get(y)
        d = count.count(y)
        i += 1
        print('%d. '%i,end='')
        print(y + '  '+ z +'  ' + n,end='  ')
        print('เข้าใช้ ',end='')
        print(d,end='')
        print(' ครั้ง')
    e = len(count)
    print('รวมทั้งหมด \t',end='')
    print(e)

def check():
    y = input('Student ID : ')
    if y in datastudent :
        count.append(y)
        print('*****ข้อมูลเข้าสู่ระบบ******\n')

while True :
    print('{0:*<32}'.format(''))
    x = input('**** จำนวณการเข้าใช้งานห้องสมุด ****\n[1]เพิ่มข้อมูลนักเรียน \n[2]แสดงข้อมูลนักเรียน \n[3]เข้าใช้ \n[4]ข้อมูลทั้งหมด \n[5]Exit \n--> ')
    if x == '1':
        add_student()
        continue
    elif x == '2':
        show()
        continue
    elif x == '3':
        check()
        continue
    elif x == '4':
        all()
        continue
    elif x == '5':
        wb.save("D:\\pepsy.py\\ProJ.xlsx")
        break
    else :
        print('Error')
