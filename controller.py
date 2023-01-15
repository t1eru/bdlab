from model import *
import self
from sqlalchemy import insert
from view import view

class controller:
    def menu(self):
        view.menuView(self)
        option = input()
        if option == '1':
            view.insertTableName(self)
            option = input()
            if option == '1':
                data.tableName = "internet_cafe"
                checkTable()
                view.waitingButtonToPress(self)
                option1 = input()
                controller.menu(self)
            elif option == '2':
                data.tableName = "employee"
                checkTable()
                view.waitingButtonToPress(self)
                option1 = input()
                controller.menu(self)
            elif option == '3':
                data.tableName = "computer"
                checkTable()
                view.waitingButtonToPress(self)
                option1 = input()
                controller.menu(self)
            elif option == '4':
                data.tableName = "application"
                checkTable()
                view.waitingButtonToPress(self)
                option1 = input()
                controller.menu(self)
            elif option == '5':
                data.tableName = "attendee_card"
                checkTable()
                view.waitingButtonToPress(self)
                option1 = input()
                controller.menu(self)
            else:
                view.uncorrectSymbol(self)
                controller.menu(self)
        elif option == '2':
            view.insertTableName(self)
            option = input()
            if option == '1':
                data.tableName = "internet_cafe"
                view.insertInto_internet_cafe_name(self)
                data.internet_cafe_name = str(input())
                view.insertInto_internet_cafe_location(self)
                data.internet_cafe_location = str(input())
                session.add(internet_cafe(data.internet_cafe_name, data.internet_cafe_location))
                session.commit()
                view.waitingButtonToPress(self)
                option1 = input()
                controller.menu(self)
            elif option == '2':
                data.tableName = "employee"
                view.insertInto_internet_cafe_id(self)
                data.internet_cafe_id = int(input())
                view.insertInto_employee_surname(self)
                data.employee_surname = str(input())
                view.insertInto_employee_age(self)
                data.employee_age = int(input())
                view.insertInto_employee_phone(self)
                data.employee_phone = str(input())
                session.add(employee(data.internet_cafe_id, data.employee_surname, data.employee_age, data.employee_phone))
                session.commit()
                view.waitingButtonToPress(self)
                option1 = input()
                controller.menu(self)
            elif option == '3':
                data.tableName = "computer"
                view.insertInto_internet_cafe_id(self)
                data.internet_cafe_id = int(input())
                view.insertInto_computer_model(self)
                data.computer_model = str(input())
                view.insertInto_computer_isbusy(self)
                data.computer_isbusy = bool(input())
                session.add(computer(data.internet_cafe_id, data.computer_model, data.computer_isbusy))
                session.commit()
                view.waitingButtonToPress(self)
                option1 = input()
                controller.menu(self)
            elif option == '4':
                data.tableName = "application"
                view.insertInto_computer_id(self)
                data.computer_id = int(input())
                view.insertInto_application_name(self)
                data.application_name = str(input())
                session.add(application(data.computer_id, data.application_name))
                session.commit()
                view.waitingButtonToPress(self)
                option1 = input()
                controller.menu(self)
            elif option == '5':
                data.tableName = "attendee_card"
                view.insertInto_internet_cafe_id(self)
                data.internet_cafe_id = int(input())
                view.insertInto_attendee_card_owner_surname(self)
                data.attendee_card_owner_surname = str(input())
                view.insertInto_attendee_card_owner_age(self)
                data.attendee_card_owner_age = int(input())
                view.insertInto_attendee_card_owner_phone(self)
                data.attendee_card_owner_phone = str(input())
                session.add(attendee_card(data.internet_cafe_id, data.attendee_card_owner_surname, data.attendee_card_owner_age, data.attendee_card_owner_phone))
                session.commit()
                attendee_card_id = session.query(attendee_card).order_by(attendee_card.id.desc()).first().id
                session.add(attendee_card_internet_cafe(data.internet_cafe_id, attendee_card_id))
                session.commit()
                view.waitingButtonToPress(self)
                option1 = input()
                controller.menu(self)
            else:
                view.uncorrectSymbol(self)
                controller.menu(self)
        elif option == '3':
            view.insertTableName(self)
            option = input()
            if option == '1':
                data.tableName = "internet_cafe"
                view.insertInto_internet_cafe_id(self)
                data.internet_cafe_id = int(input())
                view.insertInto_internet_cafe_name(self)
                data.internet_cafe_name = str(input())
                view.insertInto_internet_cafe_location(self)
                data.internet_cafe_location = str(input())
                update_internet_cafe_table(data)
                view.waitingButtonToPress(self)
                option1 = input()
                controller.menu(self)
            elif option == '2':
                data.tableName = "employee"
                view.insertInto_employee_id(self)
                data.employee_id = int(input())
                view.insertInto_internet_cafe_id(self)
                data.internet_cafe_id = int(input())
                view.insertInto_employee_surname(self)
                data.employee_surname = str(input())
                view.insertInto_employee_age(self)
                data.employee_age = int(input())
                view.insertInto_employee_phone(self)
                data.employee_phone = str(input())
                update_employee_table(data)
                view.waitingButtonToPress(self)
                option1 = input()
                controller.menu(self)
            elif option == '3':
                data.tableName = "computer"
                view.insertInto_computer_id(self)
                data.computer_id = int(input())
                view.insertInto_internet_cafe_id(self)
                data.internet_cafe_id = int(input())
                view.insertInto_computer_model(self)
                data.computer_model = str(input())
                view.insertInto_computer_isbusy(self)
                data.computer_isbusy = bool(input())
                update_computer_table(data)
                view.waitingButtonToPress(self)
                option1 = input()
                controller.menu(self)
            elif option == '4':
                data.tableName = "application"
                view.insertInto_application_id(self)
                data.application_id = int(input())
                view.insertInto_computer_id(self)
                data.computer_id = int(input())
                view.insertInto_application_name(self)
                data.application_name = str(input())
                update_application_table(data)
                view.waitingButtonToPress(self)
                option1 = input()
                controller.menu(self)
            elif option == '5':
                data.tableName = "attendee_card"
                view.insertInto_attendee_card_owner_id(self)
                data.attendee_card_owner_id = int(input())
                view.insertInto_internet_cafe_id(self)
                data.internet_cafe_id = int(input())
                view.insertInto_attendee_card_owner_surname(self)
                data.attendee_card_owner_surname = str(input())
                view.insertInto_attendee_card_owner_age(self)
                data.attendee_card_owner_age = int(input())
                view.insertInto_attendee_card_owner_phone(self)
                data.attendee_card_owner_phone = str(input())
                update_attendee_card(data)
                view.waitingButtonToPress(self)
                option1 = input()
                controller.menu(self)
            else:
                view.uncorrectSymbol(self)
                controller.menu(self)
        elif option == '4':
            view.insertTableName(self)
            option = input()
            if option == '1':
                data.tableName = "internet_cafe"
                view.insertInto_internet_cafe_id(self)
                data.internet_cafe_id = int(input())
                delete_from_internet_cafe_table(data)
                view.waitingButtonToPress(self)
                option1 = input()
                controller.menu(self)
            elif option == '2':
                data.tableName = "employee"
                view.insertInto_employee_id(self)
                data.employee_id = int(input())
                delete_from_employee_table(data)
                view.waitingButtonToPress(self)
                option1 = input()
                controller.menu(self)
            elif option == '3':
                data.tableName = "computer"
                view.insertInto_computer_id(self)
                data.computer_id = int(input())
                delete_from_computer_table(data)
                view.waitingButtonToPress(self)
                option1 = input()
                controller.menu(self)
            elif option == '4':
                data.tableName = "application"
                view.insertInto_application_id(self)
                data.application_id = int(input())
                delete_from_application_table(data)
                view.waitingButtonToPress(self)
                option1 = input()
                controller.menu(self)
            elif option == '5':
                data.tableName = "attendee_card"
                view.insertInto_attendee_card_owner_id(self)
                data.attendee_card_owner_id = int(input())
                delete_from_attendee_card(data)
                view.waitingButtonToPress(self)
                option1 = input()
                controller.menu(self)
            else:
                view.uncorrectSymbol(self)
                controller.menu(self)
        elif option == '5':
            view.insertTableName(self)
            option = input()
            if option == '1':
                data.tableName = "internet_cafe"
                view.insertQuantityOfRandomValues(self)
                data.quant = int(input())
                genRandIntoTable(data.quant)
                view.waitingButtonToPress(self)
                option1 = input()
                controller.menu(self)
            elif option == '2':
                data.tableName = "employee"
                view.insertQuantityOfRandomValues(self)
                data.quant = int(input())
                genRandIntoTable(data.quant)
                view.waitingButtonToPress(self)
                option1 = input()
                controller.menu(self)
            elif option == '3':
                data.tableName = "computer"
                view.insertQuantityOfRandomValues(self)
                data.quant = int(input())
                genRandIntoTable(data.quant)
                view.waitingButtonToPress(self)
                option1 = input()
                controller.menu(self)
            elif option == '4':
                data.tableName = "application"
                view.insertQuantityOfRandomValues(self)
                data.quant = int(input())
                genRandIntoTable(data.quant)
                view.waitingButtonToPress(self)
                option1 = input()
                controller.menu(self)
            elif option == '5':
                data.tableName = "attendee_card"
                view.insertQuantityOfRandomValues(self)
                data.quant = int(input())
                genRandIntoTable(data.quant)
                view.waitingButtonToPress(self)
                option1 = input()
                controller.menu(self)
            else:
                view.uncorrectSymbol(self)
                controller.menu(self)
        elif option == '6':
            atrSearch1()
            atrSearch2()
            atrSearch3()
            view.waitingButtonToPress(self)
            option1 = input()
            controller.menu(self)
        elif option == '0':
            return 0
        else:
            view.uncorrectSymbol(self)
            controller.menu(self)

controller.menu(self)
