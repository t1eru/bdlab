class view:

    def menuView(self):
        print("==========================================")
        print("Введіть символ для вибору опції з меню:")
        print("1. Переглянути вміст таблиці")
        print("2. Вставити дані в таблицю")
        print("3. Змінити дані в таблиці по id")
        print("4. Видалити дані з таблиці по id")
        print("5. Згенерувати рандомні дані в таблицю")
        print("6. Перевірка пошукових запитів ")
        print("0. Для виходу з програми ")
        print("==========================================")

    def connectionClose(self):
        print("З'єднання з PostgreSQL закрите")

    def incorrectData(self):
        print("Введено некоректні дані")

    def incorrectTableName(self):
        print("Введено некоректну назву таблиці")

    def errorMessage(self, error):
        print("Виникла помилка при виконанні запиту", error)

    def insertTableName(self):
        print("==========================================")
        print("Введіть символ для вибору таблиці з меню:")
        print("1. Таблиця internet_cafe")
        print("2. Таблиця employee")
        print("3. Таблиця computer")
        print("4. Таблиця application")
        print("5. Таблиця attendee_card")

    def uncorrectSymbol(self):
        print("Невірно введений символ")

    def insertInto_internet_cafe_name(self):
        print("Введіть параметр internet_cafe_name:")

    def insertInto_internet_cafe_location(self):
        print("Введіть параметр internet_cafe_location:")

    def insertInto_internet_cafe_id(self):
        print("Введіть параметр internet_cafe_id:")

    def insertInto_employee_id(self):
        print("Введіть параметр employee_id:")

    def insertInto_employee_surname(self):
        print("Введіть параметр employee_surname:")

    def insertInto_employee_age(self):
        print("Введіть параметр employee_age:")

    def insertInto_employee_phone(self):
        print("Введіть параметр employee_phone починаючи з +:")

    def insertInto_computer_model(self):
        print("Введіть параметр computer_model:")

    def insertInto_computer_isbusy(self):
        print("Введіть параметр computer_isbusy(0=False,1=True):")

    def insertInto_computer_id(self):
        print("Введіть параметр computer_id:")

    def insertInto_application_id(self):
        print("Введіть параметр application_id:")

    def insertInto_application_name(self):
        print("Введіть параметр application_name:")

    def insertInto_attendee_card_owner_id(self):
        print("Введіть параметр owner_id:")

    def insertInto_attendee_card_owner_surname(self):
        print("Введіть параметр owner_surname:")

    def insertInto_attendee_card_owner_age(self):
        print("Введіть параметр owner_age:")

    def insertInto_attendee_card_owner_phone(self):
        print("Введіть параметр owner_phone починаючи з +:")

    def insertQuantityOfRandomValues(self):
        print("Введіть кількість випадково-генерованих значень:")

    def waitingButtonToPress(self):
        print("Для повернення в меню введіть будь-яке значення:")
