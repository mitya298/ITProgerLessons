# base operations
# ** - возведение в квадрат, // - округление к целому числу (к меньшему)
# min(), max(), pow(), round() - округление к ближайшему, abs() - значение по модулю
def operator_print():
    # sep - доплнительное свойство - разделитель, который разделяет каждый элемент
    # end - символ в конце строки \n - перевод на новую,\t - табуляция \' \" \\ - Сырые символы
    print("Результат: ", 7, 15, ".", sep="", end="!\n")
    print("Second \"line")
    print("Результат: ", 5 // 5)
    print("Результат: ", min(5, 4, 10, -5, -7, 154))
    # ввод данных от пользователя
    input("Введите свой возраст: \n")

# переменные (не используются спецсимволы, ) типы данных: int, float, boolean, string
def variable():
    number = 5 #int
    digit = 4.5465433 #float
    word = 'Resalt:' #string
    boolean = True #boolean
    digit2 = "5.6564556"# приведение к типу string
    digit3 = 45
    str_num = "5"
    #del number
    print(word, digit, boolean)
    #приведение типов данных

    print(number + int(str_num))
    print(word + str(number + int(str_num)))
    print(word + digit2)
    print(word + str(digit3))
    del number
    number = 7
    print(number)
    #string
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    # +=, -=, *=, /=, %=
    num1 +=5

    print(word, num1 + num2)
    print(word, num1 - num2)
    print(word, num1 * num2)
    print(word, num1 / num2)
    print(word, num1 ** num2)
    print(word, num1 // num2)

    word = "Hi"
    print(word*2)