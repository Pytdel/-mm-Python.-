#библиотека mm
def menu(a, b, c, d, e, f, g, nomber_mm):
    if a != 0 and nomber_mm == 1:
        print('1.', a)
    elif b != 0 and nomber_mm == 1:
        print('2 ', a)
    if c != 0 and nomber_mm == 1:
        print('3.', a)
    if d != 0 and nomber_mm == 1:
        print('4.', a)
    if e != 0 and nomber_mm == 1:
        print('5.', a)
    if f != 0 and nomber_mm == 1:
        print('6.', a)
    if g != 0 and nomber_mm == 1:
        print('7.', a)

    
    if a != 0 and nomber_mm == 0:
        print(a)
    elif b != 0 and nomber_mm == 0:
        print(a)
    elif c != 0 and nomber_mm == 0:
        print(a)
    elif d != 0 and nomber_mm == 0:
        print(a)
    elif e != 0 and nomber_mm == 0:
        print(a)
    elif f != 0 and nomber_mm == 0:
        print(a)
    elif g != 0 and nomber_mm == 0:
        print(a)

def line(a, b, c, d, e, f, g, nomber_mm):
    if nomber_mm == 0:
        print(a,b,c,d,e,f,g)
    elif nomber_mm == 1:
        print('1.', a, ' ', '2.', b ,' ', '3.', c ,'', '4. ', d, '', '5. ', e, '', '6. ', f,'', '7.', g)    

def helpm():
    print('-------------------------------- helpm ---------------------------------------------------')
    print('Создайте переменные a,b,c,d,e,f,g и дайте им номер или символы и если вы вызавити menu()')
    print('и создадите переменную nomber_mm = 0 ')
    print('То вам должна выдасть столбик с вашими переменными/символами')
    print('если вы напишите nomber_mm = 1 то будет нумерация столбиков')
    print('когда будете вызывать столбик напишите: mm.menu(a, b, c, d, e, f, g, nomber_mm)')
    print()
    print('если надо чтобы было в строку mm.line(a, b, c, d, e, f, g, nomber_mm)')
    print('-------------------------------- helpm ---------------------------------------------------')
    print()

def add_mm():
    print('-------------------------------Add_mm menu-----------------------------------------------------')
    print('Список в столбик')
    print('1.Зайдите в фаул с библеотекой и найтиде def menu()')
    print('2.Добавьте в menu() такие строчки для доп.переменных:')
    print('if (переменная вне скобак) != 0 and nomber_mm == 1(или 2):')
    print('(под if с TAB) print(переменная в скобках)')
    print()
    print('Список в  строчку')
    print('1.Добавьте в def line() строчки для доп переменных:')
    print('elif nomber_mm == 0:')
    print('(TAB)print(a,b,c,d,e,f,g,(и дальше через запетую ваши переменный вне скобак))')
    print('ИЛИ')
    print('elif nomber_mm == 1:')
    print('(TAB) (Подробно там где вы скачивали библеотеку)')
    print('-------------------------------Add_mm menu-----------------------------------------------------')
    print()