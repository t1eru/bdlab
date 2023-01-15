import sqlalchemy
import random
from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, Boolean, update
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from view import view
import self
import psycopg2
import time

user = 'postgres'
password = 'Kjujc329!'
host = 'localhost'
port = 5432
database = 'lab1'

Base = declarative_base()

def current_milli_time():
    return round(time.time() * 1000)

def get_engine():
    return create_engine(url=f"postgresql://{user}:{password}@{host}:{port}/{database}")


def connect():
    try:
        _engine = get_engine()
        Base.metadata.create_all(_engine)
        print(f"Connection to the {host} for user {user} created successfully.")
        return sessionmaker(bind=_engine)()
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)


session = connect()

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




class internet_cafe(Base):
    __tablename__ = 'internet_cafe'
    id = Column(Integer, primary_key=True,)
    name = Column(String)
    location = Column(String)

    def __init__(self, name, location):
        self.name = name
        self.location = location
        super(internet_cafe, self).__init__()

class employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    cafe_id = Column(Integer, ForeignKey('internet_cafe.id'))
    surname = Column(String)
    age = Column(Integer)
    phone = Column(String)

    def __init__(self, cafe_id, surname, age, phone):
        self.cafe_id = cafe_id
        self.surname = surname
        self.age = age
        self.phone = phone
        super(employee, self).__init__()

class computer(Base):
    __tablename__ = 'computer'
    id = Column(Integer, primary_key=True)
    cafe_id = Column(Integer, ForeignKey('internet_cafe.id'))
    model = Column(String)
    isbusy = Column(Boolean)

    def __init__(self, cafe_id, model, isbusy):
        self.cafe_id = cafe_id
        self.model = model
        self.isbusy = isbusy
        super(computer, self).__init__()

class application(Base):
    __tablename__ = 'application'
    id = Column(Integer, primary_key=True)
    computer_id = Column(Integer, ForeignKey('computer.id'))
    name = Column(String)

    def __init__(self, computer_id, name):
        self.computer_id = computer_id
        self.name = name
        super(application, self).__init__()

class attendee_card_internet_cafe(Base):
    __tablename__ = 'attendee_card_internet_cafe'
    id = Column(Integer, primary_key=True)
    internet_cafe_id = Column(Integer, ForeignKey('internet_cafe.id'))
    attendee_card_id = Column(Integer, ForeignKey('attendee_card.id'))

    def __init__(self, internet_cafe_id, attendee_card_id):
        self.internet_cafe_id = internet_cafe_id
        self.attendee_card_id = attendee_card_id
        super(attendee_card_internet_cafe, self).__init__()

class attendee_card(Base):
    __tablename__ = 'attendee_card'
    id = Column(Integer, primary_key=True)
    internet_cafe_id = Column(Integer, ForeignKey('internet_cafe.id'))
    owner_surname = Column(String)
    owner_age = Column(Integer)
    owner_phone = Column(String)

    def __init__(self, internet_cafe_id, owner_surname, owner_age, owner_phone):
        self.internet_cafe_id = internet_cafe_id
        self.owner_surname = owner_surname
        self.owner_age = owner_age
        self.owner_phone = owner_phone
        super(attendee_card, self).__init__()

def get_active_column_names(row):
    columns = [col for col in row.__table__.columns.keys()]
    columns.pop(0)  # delete ID column
    return columns

def set_new_attr_values(row, data):
    columns = get_active_column_names(row)

    for column, d in zip(columns, data):
        row.__setattr__(column, d)

def update_internet_cafe_table(_data: data):
    values = [_data.internet_cafe_id, _data.internet_cafe_location, _data.internet_cafe_name]
    _row = session.query(internet_cafe).filter(internet_cafe.id == int(_data.internet_cafe_id)).first()
    set_new_attr_values(_row, values)
    session.commit()

def update_employee_table(_data: data):
    values = [_data.internet_cafe_id, _data.employee_surname, _data.employee_age, _data.employee_phone]
    _row = session.query(employee).filter(employee.id == int(_data.employee_id)).first()
    set_new_attr_values(_row, values)
    session.commit()

def update_computer_table(_data: data):
    values = [_data.internet_cafe_id, _data.computer_model, _data.computer_isbusy]
    _row = session.query(computer).filter(computer.id == int(_data.computer_id)).first()
    set_new_attr_values(_row, values)
    session.commit()

def update_application_table(_data: data):
    values = [_data.computer_id, _data.application_name]
    _row = session.query(application).filter(application.id == int(_data.application_id)).first()
    set_new_attr_values(_row, values)
    session.commit()

def update_attendee_card(_data: data):
    values = [_data.internet_cafe_id, _data.attendee_card_owner_surname, _data.attendee_card_owner_age, _data.attendee_card_owner_phone]
    _row = session.query(attendee_card).filter(attendee_card.id == int(_data.attendee_card_owner_id)).first()
    set_new_attr_values(_row, values)
    session.commit()
    update_attendee_card_internet_cafe(_data)

def update_attendee_card_internet_cafe(_data: data):
    values = [_data.internet_cafe_id, _data.attendee_card_owner_id]
    _row = session.query(attendee_card_internet_cafe).filter(attendee_card_internet_cafe.attendee_card_id == int(_data.attendee_card_owner_id)).first()
    set_new_attr_values(_row, values)
    session.commit()

def delete_from_internet_cafe_table(_data: data):
    _row = session.query(internet_cafe).filter(internet_cafe.id == int(_data.internet_cafe_id)).first()
    session.delete(_row)
    session.commit()

def delete_from_employee_table(_data: data):
    _row = session.query(employee).filter(employee.id == int(_data.employee_id)).first()
    session.delete(_row)
    session.commit()

def delete_from_computer_table(_data: data):
    _row = session.query(computer).filter(computer.id == int(_data.computer_id)).first()
    session.delete(_row)
    session.commit()

def delete_from_application_table(_data: data):
    _row = session.query(application).filter(application.id == int(_data.application_id)).first()
    session.delete(_row)
    session.commit()

def delete_from_attendee_card(_data: data):
    _row = session.query(attendee_card).filter(attendee_card.id == int(_data.attendee_card_owner_id)).first()
    session.delete(_row)
    session.commit()


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