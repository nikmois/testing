import calc

# Задание 1:
# * сделать списки со значениями a, b, expected
# * в цикле пройти по этим спискам и выполнить тесты
# * автоматически отмечать номер теста по счёту

# Задание 2:
# Доделать тесты для Mul(), Div()
# покрыть другие интересующие варианты (отрицательные числа, деление на 0)

# *** Задание 3:
# Реализовать функцию, которая будет считывать данные по тестам из CSV-файла
# У функции будет 1 аргумент: название файла
# Каждая строчка в файле - отдельный тест-кейс
# формат файла: первый_аргумент,второй_аргумент,ожидаемый_результат,ожидается_ли_исключение
# данные функция возвращает в виде списка словарей (или списка списков)

### Словари
#test = { "first_arg": 1, "second_arg": 2, "expected": 3, "exception":False }
#e = test["expected"]

### Схематически на выходе должно получиться:
#add_tests = FileReadTests("add.txt")

#add_test =
#[
#    { "first_arg": 1, "second_arg": 2, "expected": 3, "exception":False },
#    { "first_arg": 2, "second_arg": 4, "expected": 6, "exception":False },
#    { "first_arg": "abc", "second_arg": 1, "expected": None, "exception":True },
#    { "first_arg": [1,2,3], "second_arg": 0, "expected": None, "exception":True }
#]

#a = add_test[0][]
#add_tests = FileReadTests("add.txt")
#[
    #[1,2,3,False],
    #[2,4,6,False]
#]

#add_tests[1][1]

def FileReadTests_List(filename):
    tests = []

    lines = []
    with open(filename,"r") as file:
        lines=file.read().splitlines()

    for line in lines:
        fields = line.split(",")
        tests.append(fields)

    return tests

def FileReadTests_Dict(filename):
    tests = []

    lines = []
    with open(filename,"r") as file:
        lines=file.read().splitlines()

    for line in lines:
        fields = line.split(",")
        tests.append({ \
            "first_arg": int(fields[0]), \
            "second_arg": int(fields[1]), \
            "expected": int(fields[2]), \
            "exception": (True if fields[3]=="True" else False) \
        })

    return tests

def RunTestsDict(function, data):
    for i in range(0,len(data)):
        print(f"Test {i+1}: ", end="")
        try:
            r = function(data[i]["first_arg"],data[i]["second_arg"])
            if data[i]["exception"]:
                print(f"Failed (expected exception), actual: {r}")
                continue
            if r == data[i]["expected"]:
                print("Passed ", end="")
            else:
                print("Failed ", end="")
            print(f'Expected: {data[i]["expected"]}, Actual: {r}')
        except:
            if data[i]["exception"]:
                print("Passed (exception)")
            else:
                print("Failed (exception)")

def RunTests(function, first_arg,second_arg,expected,exception):
    for i in range(0,len(a)):
        print(f"Test {i+1}: ", end="")
        try:
            r = function(first_arg[i],second_arg[i])
            if exception[i]:
                print(f"Failed (expected exception), actual: {r}")
                continue
            if r == expected[i]:
                print("Passed ", end="")
            else:
                print("Failed ", end="")
            print(f'Expected: {expected[i]}, Actual: {r}')
        except:
            if exception[i]:
                print("Passed (exception)")
            else:
                print("Failed (exception)")

# Список первых аргументов к тестируемой функции
a = [1,2,"abc",[1,2,3]]

# Список вторых аргументов к тестируемой функции
b = [2,4,1,0]

# Список ожидаемых результатов
add_expected = [3,6,None,None]
# Пометка: ожидаем для данного тест-кейса исключение или нет
add_exception = [False,False,True,True]

sub_expected = [-1,-2, None, None]
sub_exception = [False,False,True,True]

print("Running tests")
print("===\nAdd()\n===")

# Запускаем тесты уже в отлаженном виде
RunTestsDict(calc.Add,FileReadTests_Dict("add.txt"))

print("===\nSub()\n===")
RunTestsDict(calc.Sub,FileReadTests_Dict("sub.txt"))

print("===\nMul()\n===")
RunTestsDict(calc.Mul,FileReadTests_Dict("mul.txt"))

print("===\nDiv()\n===")
RunTestsDict(calc.Div,FileReadTests_Dict("div.txt"))

#a.clear()
#b.clear()
#add_expected.clear()
#add_exception.clear()

# Формируем Structure of Arrays (находимся в плену своего неудобного программного интерфейса)
#for test in add_tests:
#    a.append(test["first_arg"])
#    b.append(test["second_arg"])
#    add_expected.append(test["expected"])
#    add_exception.append(test["exception"])

#RunTests(calc.Add,a,b,add_expected,add_exception)
#print("\n===\nSub()\n===")
#RunTests(calc.Sub,a,b,sub_expected,sub_exception)
#RunTests(calc.Mul,a,b,expected,exception)
#RunTests(calc.Div,a,b,expected,exception)
