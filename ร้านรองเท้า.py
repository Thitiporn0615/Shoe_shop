a = []
h = 0
while True:
    b=input('\nWOW BEWBEW Shop\n\n[1]NIKE ลด20%\n[2]Adidas ลด30%\n[3]Reebok ลด70%\n[4]BODY GLOVE ลด50%\n[x]บิล\n[z]ออก\n>>>เลือกรายการสินค้าที่ท่านต้องการ')
    b = b.lower()
    if b == '1' :
        c = input('[1]NIKE air max97 ราคา 2,500\n[2]NIKE air froce ราคา 5,000\n[3]NIKE air ราคา 2,000\n')
        if c == '1':
            a.append('NIKE air max: 2,500 : 20% : 2,000 ')
            g = int(2000)
            h += g
        elif c=='2':
            a.append('NIKE air froce: 5,000 : 20% : 2,800')
            g =int(2800)
            h += g
        elif c == '3':
            a.append('NIKE aie : 2,000 : 20% : 1,600')
            g = int(1600)
            h += g
        print('\nเพิ่มสินค้าลงในรถเข็นแล้ว')
        print('>>>เลือกรายการสินค้าที่ท่านต้องการ')
    elif b=='2':
        c = input('[1]OZWEEGO ราคา 3,500\n[2]Continetal 80 ราคา 4,000\n[3]Gazelle shoes ราคา 3,000\n')
        if c == '1':
            a.append('OZWEEGO : 3,500 : 30% : 2,450')
            g = int(2450)
            h +=g
        elif c == '2':
            a.append('Continetal 80 : 4,000 : 30% : 2,800 ')
            g = int(2800)
            h +=g
        elif c == '3':
            a.append('Gazelle shoes : 3,000 : 30% : 2,100 ')
            g = int(2100)
            h +=g
        print ('\nเพิ่มสินค้าลงในรถเข็นแล้ว')

    elif b=='3':
        c=input('[1]LIQUIFECT LS AP ราคา 3,000\n[2]Interval 96 ราคา 2,500\n[3]LIQUIFECT LS AD ราคา 4,500\n')
        if c =='1':
            a.append('LIQUIFFCT LS AP : 3,000 : 70% :   900 ')
            g = int(900)
            h +=g
        elif c=='2':
            a.append('LIQUIFFCT LS AD : 4,500 : 70% : 1,350 ')
            g = int(1350)
            h +=g 
        elif c=='3':
            a.append('Interval 96 : 2,500 : 70% :   750 ')
            g = (750)
            h +=g 
        print ('\nเพิ่มสินค้าลงในรถเข็นแล้ว')     

    elif b=='4':
        c=input('[1]Girls Basic Polo-Red[S] ราคา 500\n[2]Mens Sport Jacket[XL] ราคา 1,250\n[3]Mens Basic Polo-Burgandy[L] ราคา 690\n')
        if c =='1':
            a.append('Girls Basic Polo-Red[S] :   500 : 50% :   250 ')
            g = int(250)
            h +=g
        elif c=='2':
            a.append('Mens Basic Polo-Burgandy[L]:   690 : 50% :   345')
            g = int(345)
            h +=g 
        elif c=='3':
            a.append('Mens Sport Jacket[XL]:  1250 : 50% :   625 ')
            g = int(625)
            h +=g 
        print ('\nเพิ่มสินค้าลงในรถเข็นแล้ว\n')         

    elif b== 'x':
        print('------------------------------------------------------------------------')
        print('{0:<35}{1:<15}{2:<15}{3:<10}'.format('สินค้า','ราคา','ส่วนลด','จ่ายจริง'))
        print('------------------------------------------------------------------------')
        count=0
        for x in a:
            count+=1
            print(count,end=" ") 
            y = x.split(":")
            print('{0[0]:<30} {0[1]:<15} {0[2]:<15} {0[3]:<10}'.format(y))
        print('------------------------------------------------------------------------')
        print('ราคารวม                                                         %d บาท'%h)
        print('------------------------------------------------------------------------')
        print('>>>>>>>>>>>ช่องทางการชำระเงิน พร้อมเพย์ 0910577485<<<<<<<<<<<<<<<')
        print('\n')
        
    elif b=='z': exit