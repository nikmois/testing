import re

# Функции для проверки строчек на соответствие указанному формату
# Все методы принимают строку, и проверяют, соответствует ли она
# указанному формату (в полном объеме, лишних символов не должно
# быть ни до, ни после).

# все функции возвращают либо значение true, если соответсвуют формату
# либо false, если не соответсвуют

# Принимает: целое число в двоичном представлении
# Цифры: 0,1
# Впереди может быть маркер 0b
# Любые другие символы недопустимы
def CheckBinary(s):
    return re.fullmatch(r'^(0b)?[01]+$',s) != None

# Принимает: строка даты в формате DD-MM-YYYY
# Где DD,MM,YYYY - целые десятичные числа
# DD - день (1-31)
# MM - месяц (1-12)
# YYYY - год, может быть любым, кроме 0000 (0001-9999)
def CheckDate(s):
    return re.fullmatch(r'^\d{2}-\d{2}-\d{4}$',s) != None

# Принимает: действительное число в десятичном виде
# В начале может стоять знак + или -
# Далее от 1 до N цифр (0-9)
# Далее знак разделителя дробной части (. или ,)
# Далее от 0 до N цифр (0-9)
def CheckDecimal(s):
    return re.fullmatch(r'^[+-]?\d+[.,]?\d*$',s) != None

# Принимает: Адрес IPv4
# В каждом сегменте значения от 0 до 255
# Правильно: 128.3.55.10, 0.0.0.0, 255.255.255.255
# Неправильно: 260.30.5.1, a30.5.2.1
def CheckIP(s):
    return re.fullmatch(r'^(((25[0-4])|(1\d{2,2})|(2[0-4]\d)|(\d{1,2}))\.){3}((25[0-4])|(1\d{2,2})|(2[0-4]\d)|(\d{1,2}))$',s) != None

# Принимает: обозначение цвета в HTML (с # или без): #ff00f4, 004cbb
def CheckHtmlColor(s):
    return re.fullmatch(r'$\b#?[0-9A-Fa-f]{6,6}^',s) != None

# Принимает email, с поддержкой точек: john.doe@example.com
def CheckEmail(s):
    return re.fullmatch(r'(^|\n)\w?[\w\.]+@\w+\.\w+(\s|\n|$)',s) != None

# Проверка строки в CSV с инфо по книжке
# Принимает: строку из CSV файла со следующим форматом:
# ID;Заголовок;Издание;Издательство;ISBN;ГодИздания;
# ISBN в формате EAN-13 имеет вид: 978-N-NNN-NNNNN-N, где N - цифра
# при этом число цифр в каждом разряде может отличаться, но общая
# их сумма должна быть 10, а кол-во сегментов - 5 (с учётом заголовка - 978)
# Вместо 978 может быть 979
def CheckBookCSV(s):
    return re.fullmatch(r'^\d+;\w+;\d+;\w+;\b(978|979)-\d+-\d+-\d+-\d+\b;\d+$',s) != None

#print(CheckDecimal("abc"))
