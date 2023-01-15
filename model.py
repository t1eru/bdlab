import psycopg2
import random
import self
import time
from view import view

def current_milli_time():
    return round(time.time() * 1000)

class data:
    tableName = "attendee_card"
    internet_cafe_name = "Veselyy Gorikh"
    internet_cafe_location = "Irpin"
    internet_cafe_id = 2
    employee_id = 2
    employee_surname = "Bateman"
    employee_age = 22
    employee_phone = "+479218865456"
    computer_id = 1
    computer_model = "Gaming"
    computer_isbusy = False
    application_id = 3
    application_name = "Earthworm Jim"
    attendee_card_owner_id = 2
    attendee_card_owner_phone = "+380943523872"
    attendee_card_owner_surname = "Kuro"
    attendee_card_owner_age = 33
    quant = 4

def checkTable():
    try:
        connection = psycopg2.connect(host="localhost", port="5432", database="lab1", user="postgres", password="Kjujc329!")
        cursor = connection.cursor()
    except (Exception, psycopg2.Error) as error:
        view.errorMessage(self, error)
    try:
        # створення та виконання запиту
        cursor.execute(f"SELECT *FROM {data.tableName}")
        # отримання результату запиту
        row = cursor.fetchone()
        # обробка результату запиту
        while row is not None:
            print(row)
            row = cursor.fetchone()
    except (Exception, psycopg2.Error) as error:
        view.errorMessage(self, error)
        # Закриття з'єднання з БД.
    finally:
        if connection:
            cursor.close()
            connection.close()
            view.connectionClose(self)

def insertIntoTable(validation_status=False):
    try:
        connection = psycopg2.connect(host="localhost", port="5432", database="lab1", user="postgres", password="Kjujc329!")
        cursor = connection.cursor()
    except (Exception, psycopg2.Error) as error:
        view.errorMessage(self, error)

    if data.tableName == "internet_cafe":
        try:
            cursor.execute("INSERT INTO internet_cafe (name,location) VALUES (%s,%s)", (data.internet_cafe_name, data.internet_cafe_location))
            connection.commit()
        except (Exception, psycopg2.Error) as error:
            view.errorMessage(self, error)
        # Закриття з'єднання з БД.
        finally:
            if connection:
                cursor.close()
                connection.close()
                view.connectionClose(self)

    elif data.tableName == "employee":
        try:
            cursor.execute(f"SELECT *FROM internet_cafe")
            row = cursor.fetchone()
            while row is not None:
                if len(data.employee_phone) == 13:
                    if row[0] == data.internet_cafe_id:
                        validation_status = True
                        break
                else:
                    view.incorrectData(self)
                    break
                row = cursor.fetchone()
            if validation_status == False:
                view.incorrectData(self)
        except (Exception, psycopg2.Error) as error:
            view.errorMessage(self, error)
        if validation_status == True:
            try:
                cursor.execute("INSERT INTO employee (cafe_id,surname,age,phone) VALUES (%s,%s,%s,%s)", (data.internet_cafe_id, data.employee_surname, data.employee_age, data.employee_phone))
                connection.commit()
            except (Exception, psycopg2.Error) as error:
                view.errorMessage(self, error)
            finally:
                if connection:
                    cursor.close()
                    connection.close()
                    view.connectionClose(self)

    elif data.tableName == "computer":
        try:
            cursor.execute(f"SELECT *FROM internet_cafe")
            row = cursor.fetchone()
            while row is not None:
                if len(data.computer_model) == 6:
                    if row[0] == data.internet_cafe_id:
                        validation_status = True
                        break
                else:
                    view.incorrectData(self)
                    break
                row = cursor.fetchone()
            if validation_status == False:
                view.incorrectData(self)
        except (Exception, psycopg2.Error) as error:
            view.errorMessage(self, error)
        if validation_status == True:
            try:
                cursor.execute("INSERT INTO computer (cafe_id,model,isbusy) VALUES (%s,%s,%s)", (data.internet_cafe_id, data.computer_model, data.computer_isbusy))
                connection.commit()
            except (Exception, psycopg2.Error) as error:
                view.errorMessage(self, error)
            finally:
                if connection:
                    cursor.close()
                    connection.close()
                    view.connectionClose(self)

    elif data.tableName == "application":
        try:
            cursor.execute(f"SELECT *FROM computer")
            row = cursor.fetchone()
            while row is not None:
                if row[0] == data.computer_id:
                    validation_status = True
                    break
                row = cursor.fetchone()
            if validation_status == False:
                view.incorrectData(self)
        except (Exception, psycopg2.Error) as error:
            view.errorMessage(self, error)
        if validation_status == True:
            try:
                cursor.execute("INSERT INTO application (computer_id,name) VALUES (%s,%s)", (data.computer_id, data.application_name))
                connection.commit()
            except (Exception, psycopg2.Error) as error:
                view.errorMessage(self, error)
            finally:
                if connection:
                    cursor.close()
                    connection.close()
                    view.connectionClose(self)

    elif data.tableName == "attendee_card":
        try:
            cursor.execute(f"SELECT *FROM internet_cafe")
            row = cursor.fetchone()
            while row is not None:
                if len(data.attendee_card_owner_phone) == 13:
                    if row[0] == data.internet_cafe_id:
                        validation_status = True
                        break
                else:
                    view.incorrectData(self)
                    break
                row = cursor.fetchone()
            if validation_status == False:
                view.incorrectData(self)
        except (Exception, psycopg2.Error) as error:
            view.errorMessage(self, error)
        if validation_status == True:
             try:
                cursor.execute("INSERT INTO attendee_card (internet_cafe_id,owner_surname,owner_age,owner_phone) VALUES (%s,%s,%s,%s)", (data.internet_cafe_id, data.attendee_card_owner_surname, data.attendee_card_owner_age, data.attendee_card_owner_phone))
                cursor.execute("SELECT *FROM attendee_card_internet_cafe")
                row = cursor.fetchone()
                cnt = 1
                while row is not None:
                    cnt = cnt+1
                    row = cursor.fetchone()
                cursor.execute("INSERT INTO attendee_card_internet_cafe (internet_cafe_id,attendee_card_id) VALUES (%s,%s)", (data.internet_cafe_id, cnt))
                connection.commit()
             except (Exception, psycopg2.Error) as error:
                view.errorMessage(self, error)
             finally:
                if connection:
                    cursor.close()
                    connection.close()
                    view.connectionClose(self)

    else:
        view.incorrectTableName(self)

def updateTable(validation_status=False):
    try:
        connection = psycopg2.connect(host="localhost", port="5432", database="lab1", user="postgres", password="Kjujc329!")
        cursor = connection.cursor()
    except (Exception, psycopg2.Error) as error:
        view.errorMessage(self, error)

    if data.tableName == "internet_cafe":
        try:
            cursor.execute("SELECT *FROM internet_cafe")
            row = cursor.fetchone()
            while row is not None:
                if row[0] == data.internet_cafe_id:
                    validation_status = True
                    break
                row = cursor.fetchone()
        except (Exception, psycopg2.Error) as error:
            view.errorMessage(self, error)
        if validation_status == False:
            view.incorrectData(self)
        if validation_status == True:
            try:
                cursor.execute("UPDATE internet_cafe SET name =%s,location=%s WHERE id=%s ", (data.internet_cafe_name, data.internet_cafe_location, data.internet_cafe_id))
                connection.commit()
            except (Exception, psycopg2.Error) as error:
                view.errorMessage(self, error)
            # Закриття з'єднання з БД.
            finally:
                if connection:
                    cursor.close()
                    connection.close()
                    view.connectionClose(self)

    elif data.tableName == "employee":
        try:
            cursor.execute("SELECT *FROM employee")
            row = cursor.fetchone()
            while row is not None:
                if len(data.employee_phone) == 13:
                    if row[0] == data.employee_id:
                        validation_status = True
                        break
                else:
                    view.incorrectData(self)
                    break
                row = cursor.fetchone()
            if validation_status == False:
                view.incorrectData(self)
        except (Exception, psycopg2.Error) as error:
            view.errorMessage(self, error)
        if validation_status == True:
            try:
                cursor.execute("Update employee SET  cafe_id =%s, surname =%s, age = %s, phone = %s WHERE id = %s", (data.internet_cafe_id, data.employee_surname, data.employee_age, data.employee_phone, data.employee_id))
                connection.commit()
            except (Exception, psycopg2.Error) as error:
                view.errorMessage(self, error)
            finally:
                if connection:
                    cursor.close()
                    connection.close()
                    view.connectionClose(self)

    elif data.tableName == "computer":
        try:
            cursor.execute("SELECT *FROM computer")
            row = cursor.fetchone()
            while row is not None:
                if len(data.computer_model) == 6:
                    if row[0] == data.computer_id:
                        validation_status = True
                        break
                else:
                    view.incorrectData(self)
                    break
                row = cursor.fetchone()
            if validation_status == False:
                view.incorrectData(self)
        except (Exception, psycopg2.Error) as error:
            view.errorMessage(self, error)
        if validation_status == True:
            try:
                cursor.execute("UPDATE computer SET cafe_id =%s, model =%s, isbusy =%s WHERE id =%s ", (data.internet_cafe_id, data.computer_model, data.computer_isbusy, data.computer_id))
                connection.commit()
            except (Exception, psycopg2.Error) as error:
                view.errorMessage(self, error)
            finally:
                if connection:
                    cursor.close()
                    connection.close()
                    view.connectionClose(self)

    elif data.tableName == "application":
        try:
            cursor.execute("SELECT *FROM application")
            row = cursor.fetchone()
            while row is not None:
                if row[0] == data.application_id:
                    validation_status = True
                    break
                row = cursor.fetchone()
            if validation_status == False:
                view.incorrectData(self)
        except (Exception, psycopg2.Error) as error:
            view.errorMessage(self, error)
        if validation_status == True:
            try:
                cursor.execute("UPDATE application SET computer_id =%s, name =%s WHERE id =%s", (data.computer_id, data.application_name, data.application_id))
                connection.commit()
            except (Exception, psycopg2.Error) as error:
                view.errorMessage(self, error)
            finally:
                if connection:
                    cursor.close()
                    connection.close()
                    view.connectionClose(self)

    elif data.tableName == "attendee_card":
        try:
            cursor.execute("SELECT *FROM attendee_card")
            row = cursor.fetchone()
            while row is not None:
                if len(data.attendee_card_owner_phone) == 13:
                    if row[0] == data.attendee_card_owner_id:
                        validation_status = True
                        break
                else:
                    view.incorrectData(self)
                    break
                row = cursor.fetchone()
            if validation_status == False:
                view.incorrectData(self)
        except (Exception, psycopg2.Error) as error:
            view.errorMessage(self, error)
        if validation_status == True:
            try:
                cursor.execute("UPDATE attendee_card SET internet_cafe_id =%s, owner_surname =%s ,owner_age =%s ,owner_phone =%s WHERE id = %s", (data.internet_cafe_id, data.attendee_card_owner_surname, data.attendee_card_owner_age, data.attendee_card_owner_phone, data.attendee_card_owner_id))
                cursor.execute("SELECT *FROM attendee_card_internet_cafe")
                row = cursor.fetchone()
                while row is not None:
                    row = cursor.fetchone()
                cursor.execute("UPDATE attendee_card_internet_cafe SET internet_cafe_id=%s WHERE id= %s", (data.internet_cafe_id, data.attendee_card_owner_id))
                connection.commit()
            except (Exception, psycopg2.Error) as error:
                view.errorMessage(self, error)
            finally:
                if connection:
                    cursor.close()
                    connection.close()
                    view.connectionClose(self)

    else:
        view.incorrectTableName(self)

def deleteFromTable(validation_status=False):
    try:
        connection = psycopg2.connect(host="localhost", port="5432", database="lab1", user="postgres", password="Kjujc329!")
        cursor = connection.cursor()
    except (Exception, psycopg2.Error) as error:
        view.errorMessage(self, error)

    if data.tableName == "internet_cafe":
        try:
            cursor.execute("SELECT *FROM internet_cafe")
            row = cursor.fetchone()
            while row is not None:
                if row[0] == data.internet_cafe_id:
                    validation_status = True
                    break
                row = cursor.fetchone()
        except (Exception, psycopg2.Error) as error:
            view.errorMessage(self, error)
        if validation_status == False:
            view.incorrectData(self)
        if validation_status == True:
            try:
                cursor.execute("DELETE FROM internet_cafe WHERE id =%s", [data.internet_cafe_id])
                connection.commit()
            except (Exception, psycopg2.Error) as error:
                view.errorMessage(self, error)
            finally:
                if connection:
                    cursor.close()
                    connection.close()
                    view.connectionClose(self)

    elif data.tableName == "employee":
        try:
            cursor.execute("SELECT *FROM employee")
            row = cursor.fetchone()
            while row is not None:
                if len(data.employee_phone) == 13:
                    if row[0] == data.employee_id:
                        validation_status = True
                        break
                else:
                    view.incorrectData(self)
                    break
                row = cursor.fetchone()
            if validation_status == False:
                view.incorrectData(self)
        except (Exception, psycopg2.Error) as error:
            view.errorMessage(self, error)
        if validation_status == True:
            try:
                cursor.execute("DELETE FROM employee WHERE id = %s", [data.employee_id])
                connection.commit()
            except (Exception, psycopg2.Error) as error:
                view.errorMessage(self, error)
            finally:
                if connection:
                    cursor.close()
                    connection.close()
                    view.incorrectData(self)

    elif data.tableName == "computer":
        try:
            cursor.execute("SELECT *FROM computer")
            row = cursor.fetchone()
            while row is not None:
                if len(data.computer_model) == 6:
                    if row[0] == data.computer_id:
                        validation_status = True
                        break
                else:
                    view.incorrectData(self)
                    break
                row = cursor.fetchone()
            if validation_status == False:
                view.incorrectData(self)
        except (Exception, psycopg2.Error) as error:
            view.errorMessage(self, error)
        if validation_status == True:
            try:
                cursor.execute("DELETE FROM computer WHERE id =%s ", [data.computer_id])
                connection.commit()
            except (Exception, psycopg2.Error) as error:
                view.errorMessage(self, error)
            finally:
                if connection:
                    cursor.close()
                    connection.close()
                    view.connectionClose(self)

    elif data.tableName == "application":
        try:
            cursor.execute("SELECT *FROM application")
            row = cursor.fetchone()
            while row is not None:
                if row[0] == data.application_id:
                    validation_status = True
                    break
                row = cursor.fetchone()
            if validation_status == False:
                view.incorrectData(self)
        except (Exception, psycopg2.Error) as error:
            view.errorMessage(self, error)
        if validation_status == True:
            try:
                cursor.execute("DELETE FROM application WHERE id =%s", [data.application_id])
                connection.commit()
            except (Exception, psycopg2.Error) as error:
                view.errorMessage(self, error)
            finally:
                if connection:
                    cursor.close()
                    connection.close()
                    view.connectionClose(self)

    elif data.tableName == "attendee_card":
        try:
            cursor.execute("SELECT *FROM attendee_card")
            row = cursor.fetchone()
            while row is not None:
                if row[0] == data.attendee_card_owner_id:
                    validation_status = True
                    break
                row = cursor.fetchone()
            if validation_status == False:
                view.incorrectData(self)
        except (Exception, psycopg2.Error) as error:
            view.errorMessage(self, error)
        if validation_status == True:
            try:
                cursor.execute("DELETE FROM attendee_card S WHERE id = %s", [data.attendee_card_owner_id])
                connection.commit()
            except (Exception, psycopg2.Error) as error:
                view.errorMessage(self, error)
            finally:
                if connection:
                    cursor.close()
                    connection.close()
                    view.connectionClose(self)
    else:
        view.incorrectTableName(self)

def genRandIntoTable(quant):
    try:
        connection = psycopg2.connect(host="localhost", port="5432", database="lab1", user="postgres", password="Kjujc329!")
        cursor = connection.cursor()
    except (Exception, psycopg2.Error) as error:
        view.errorMessage(self, error)

    if data.tableName == "internet_cafe":
        try:
            length = 7
            uppercase_letter = "chr(ascii('A') + (random() * 25)::int)"
            lowercase_letter = "chr(ascii('a') + (random() * 25)::int)"
            for i in range(0, quant):
                cursor.execute(f"""INSERT INTO internet_cafe (name,location) 
                VALUES ({uppercase_letter}{(" || " + lowercase_letter) * (length - 1)},
                {uppercase_letter}{(" || " + lowercase_letter) * (length - 3)})""")
            connection.commit()
        except (Exception, psycopg2.Error) as error:
            view.errorMessage(self, error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                view.connectionClose(self)

    elif data.tableName == "employee":
        try:
            cursor.execute("select id from internet_cafe ORDER BY id DESC limit 1")
            maxCafeId = cursor.fetchone()[0]
            length = 7
            uppercase_letter = "chr(ascii('A') + (random() * 25)::int)"
            lowercase_letter = "chr(ascii('a') + (random() * 25)::int)"
            digit = "chr(ascii('0') + (random() * 9)::int)"
            for i in range(0, quant):
                cursor.execute(f"""INSERT INTO employee (cafe_id,surname,age,phone) 
                VALUES(random()*{maxCafeId-1}+1, 
                {uppercase_letter}{(" || " + lowercase_letter) * (length - 1)},
                random()*100::int,
                '+380'{(" || "+digit)*9})""")
            connection.commit()
        except (Exception, psycopg2.Error) as error:
            view.errorMessage(self, error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                view.connectionClose(self)

    elif data.tableName == "computer":
        try:
            cursor.execute("select id from internet_cafe ORDER BY id DESC limit 1")
            maxCafeId = cursor.fetchone()[0]
            length = 7
            uppercase_letter = "chr(ascii('A') + (random() * 25)::int)"
            lowercase_letter = "chr(ascii('a') + (random() * 25)::int)"
            digit = "chr(ascii('0') + (random() * 9)::int)"
            for i in range(0, quant):
                cursor.execute(f"""INSERT INTO computer (cafe_id,model,isbusy) 
                VALUES (random()*{maxCafeId-1}+1,
                {uppercase_letter}{(" || " + lowercase_letter) * 5},
                {bool(random.randint(0,2))})""")
            connection.commit()
        except (Exception, psycopg2.Error) as error:
            view.errorMessage(self, error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                view.connectionClose(self)

    elif data.tableName == "application":
        try:
            cursor.execute("select id from computer ORDER BY id DESC limit 1")
            maxComputerId = cursor.fetchone()[0]
            length = 10
            uppercase_letter = "chr(ascii('A') + (random() * 25)::int)"
            lowercase_letter = "chr(ascii('a') + (random() * 25)::int)"
            for i in range(0, quant):
                cursor.execute(f"""INSERT INTO application (computer_id,name) 
                VALUES (random()*{maxComputerId-1}+1,
                {uppercase_letter}{(" || " + lowercase_letter) * (length - 1)})""")
            connection.commit()
        except (Exception, psycopg2.Error) as error:
            view.errorMessage(self, error)
        # Закриття з'єднання з БД.
        finally:
            if connection:
                cursor.close()
                connection.close()
                view.connectionClose(self)

    elif data.tableName == "attendee_card":
        try:
            cursor.execute("select id from internet_cafe ORDER BY id DESC limit 1")
            maxCafeId = cursor.fetchone()[0]
            length = 7
            uppercase_letter = "chr(ascii('A') + (random() * 25)::int)"
            lowercase_letter = "chr(ascii('a') + (random() * 25)::int)"
            digit = "chr(ascii('0') + (random() * 9)::int)"
            for i in range(0, quant):
                var = random.randint(0, maxCafeId-1) + 1
                cursor.execute(f"""INSERT INTO attendee_card (internet_cafe_id,owner_surname,owner_age,owner_phone) 
                VALUES ({var},
                {uppercase_letter}{(" || " + lowercase_letter) * (length - 1)},
                random()*100::int,
                '+380'{(" || "+digit)*9})""")
                cursor.execute("SELECT *FROM attendee_card_internet_cafe")
                row = cursor.fetchone()
                cnt = 1
                while row is not None:
                    row = cursor.fetchone()
                    cnt = cnt + 1
                cursor.execute(f"""INSERT INTO attendee_card_internet_cafe (internet_cafe_id,attendee_card_id) 
                VALUES ({var},
                {cnt})""")
            connection.commit()
        except (Exception, psycopg2.Error) as error:
            view.errorMessage(self, error)
        # Закриття з'єднання з БД.
        finally:
            if connection:
                cursor.close()
                connection.close()
                view.connectionClose(self)
    else:
        view.incorrectTableName(self)

def atrSearch1():
    try:
        connection = psycopg2.connect(host="localhost", port="5432", database="lab1", user="postgres",
                                      password="Kjujc329!")
        cursor = connection.cursor()
        time_start = current_milli_time()
        cursor.execute(f"""select * from internet_cafe INNER JOIN computer ON computer.cafe_id = internet_cafe.id 
        WHERE internet_cafe.id <= 20 AND internet_cafe.id > 3""")
        row = cursor.fetchone()
        while row is not None:
            print(row)
            row = cursor.fetchone()
        time_end = current_milli_time()
        print(f"Час виконання запиту: {time_end - time_start} ms ")
    except (Exception, psycopg2.Error) as error:
        view.errorMessage(self, error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            view.connectionClose(self)

def atrSearch2():
    try:
        connection = psycopg2.connect(host="localhost", port="5432", database="lab1", user="postgres", password="Kjujc329!")
        cursor = connection.cursor()
        time_start = current_milli_time()
        cursor.execute(f"""select * from internet_cafe INNER JOIN attendee_card_internet_cafe ON internet_cafe.id = attendee_card_internet_cafe.internet_cafe_id 
        WHERE internet_cafe.id <= 10 AND internet_cafe.id >2""")
        row = cursor.fetchone()
        while row is not None:
            print(row)
            row = cursor.fetchone()
        time_end = current_milli_time()
        print(f"Час виконання запиту: {time_end-time_start} ms ")
    except (Exception, psycopg2.Error) as error:
        view.errorMessage(self, error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            view.connectionClose(self)

def atrSearch3():
    try:
        connection = psycopg2.connect(host="localhost", port="5432", database="lab1", user="postgres", password="Kjujc329!")
        cursor = connection.cursor()
        time_start = current_milli_time()
        cursor.execute(f"""select * from internet_cafe INNER JOIN employee ON employee.cafe_id = internet_cafe.id 
        WHERE internet_cafe.id <= 200 AND internet_cafe.id >3""")
        row = cursor.fetchone()
        while row is not None:
            print(row)
            row = cursor.fetchone()
        time_end = current_milli_time()
        print(f"Час виконання запиту: {time_end-time_start} ms ")
    except (Exception, psycopg2.Error) as error:
        view.errorMessage(self, error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            view.connectionClose(self)


# checkTable()
# deleteFromTable()
# updateTable()
# insertIntoTable()
# checkTable()
# genRandIntoTable(15)
# checkTable()
# atrSearch()
