import pymysql
from dbConnect import *

# def add_dot(id1, description, buttons):
#     """ Добавить узел в таблицу узлов БД

#     Аргументы:
#     id1 - идентификатор узла
#     description - описание кнопки
#     buttons - название кнопки
#     """
#     # Подготавливаем SQL запрос для передачи его базе данных
#     dbInject = """insert into dot (id, description, buttons) values (%s, %s, %s);"""
#     # Соединяемся с базой данных
#     connect = getConnection()
#     # Передаем запрос на добавление элемента, выводим его в терминал и фиксируем в бд
#     try:
#         with connect.cursor() as cursor:
#             cursor.execute(dbInject, (id1, description, buttons))
#             cursor.execute("""select * from dot;""")
#             print(cursor.fetchall())
#             connect.commit()
#     # В случае неудачи оповещаем об ошибке
#     except:
#         print("Ошибка")
#     # Отсоединяемся от базы данных
#     connect.close()

def add_user(id1, status, ege_points, position, old_position):
    """ Добавить пользователя в таблицу пользователей в БД

    Аргументы:
    id1 - идентификатор пользователя в вк
    status - категория пользователя
    ege_points - баллы ЕГЭ пользователя
    position - нынешняя позиция пользователя
    old_position - позиция, в которой находился пользователь на прошлом шаге
    """
    # Подготавливаем SQL запрос для передачи его базе данных
    dbInject = """insert into user (id, status, ege_points, position, old_position) values (%s, %s, %s, %s, %s);"""
    # Соединяемся с базой данных
    connect = getConnection()

    # Передаем запрос на добавление элемента, выводим его в терминал и фиксируем в бд
    try:
        with connect.cursor() as cursor:
            cursor.execute(dbInject, (id1, status, ege_points, position, old_position))
            cursor.execute("""select * from user;""")
            print(cursor.fetchall())
            connect.commit()
    # В случае неудачи оповещаем об ошибке
    except:
        print("Ошибка")
    # Отсоединяемся от базы данных
    connect.close()

def add_exam(id1, id_user, name, points):
    """ Добавить экзамен в таблицу экзаменов в БД

    Аргументы:
    id1 - идентификатор экзамена
    id_user - идентификатор пользователя в вк
    name - название экзамена
    points - баллы за экзамен
    """
    # Подготавливаем SQL запрос для передачи его базе данных
    dbInject = """insert into exam (id, id_user, name, points) values (%s, %s, %s, %s);"""
    # Соединяемся с базой данных
    connect = getConnection()

    # Передаем запрос на добавление элемента, выводим его в терминал и фиксируем в бд
    try:
        with connect.cursor() as cursor:
            cursor.execute(dbInject, (id1, id_user, name, points))
            cursor.execute("""select * from exam;""")
            print(cursor.fetchall())
            connect.commit()
    # В случае неудачи оповещаем об ошибке
    except:
        print("Ошибка")
    # Отсоединяемся от базы данных
    connect.close()

def add_achievement(id1, id_user, name, points):
    """ Добавить индивидуальное достижение в таблицу индивидуальных достижений в БД

    Аргументы:
    id1 - идентификатор индивидуального достижения
    id_user - идентификатор пользователя в вк
    name - название индивидуального достижения
    points - баллы за индивидуальное достижение
    """
    # Подготавливаем SQL запрос для передачи его базе данных
    dbInject = """insert into achievement (id, id_user, name, points) values (%s, %s, %s, %s);"""
    # Соединяемся с базой данных
    connect = getConnection()

    # Передаем запрос на добавление элемента, выводим его в терминал и фиксируем в бд
    try:
        with connect.cursor() as cursor:
            cursor.execute(dbInject, (id1, id_user, name, points))
            cursor.execute("""select * from achievement;""")
            print(cursor.fetchall())
            connect.commit()
    # В случае неудачи оповещаем об ошибке
    except:
        print("Ошибка")
    # Отсоединяемся от базы данных
    connect.close()

def add_speciality(id1, name, min_points):
    """ Добавить направление в таблицу направлений в БД

    Аргументы:
    id1 - идентификатор направления
    name - название направления
    min_points - минимальное кол-во баллов для поступление на направление
    """
    # Подготавливаем SQL запрос для передачи его базе данных
    dbInject = """insert into speciality (id, name, min_points) values (%s, %s, %s);"""
    # Соединяемся с базой данных
    connect = getConnection()

    # Передаем запрос на добавление элемента, выводим его в терминал и фиксируем в бд
    try:
        with connect.cursor() as cursor:
            cursor.execute(dbInject, (id1, name, min_points))
            cursor.execute("""select * from speciality;""")
            print(cursor.fetchall())
            connect.commit()
    # В случае неудачи оповещаем об ошибке
    except:
        print("Ошибка")
    # Отсоединяемся от базы данных
    connect.close()

def update_user_ege_points(ege_points, id1):
    """Обновить баллы ЕГЭ пользователя в БД

    Аргументы:
    ege_points - нынешнее баллы ЕГЭ пользователя
    id1 - идентификатор пользователя в вк
    """
    # Подготавливаем SQL запрос для передачи его базе данных
    dbUpdate = """update user set ege_points = %s where id = %s;"""
    # Соединяемся с базой данных
    connect = getConnection()

    # Передаем запрос на изменение элемента, выводим его в терминал и фиксируем в бд
    try:
        with connect.cursor() as cursor:
            cursor.execute(dbUpdate, (ege_points, id1))
            cursor.execute("""select * from user;""")
            print(cursor.fetchall())
            connect.commit()
    # В случае неудачи оповещаем об ошибке
    except:
        print("Ошибка")
    # Отсоединяемся от базы данных
    connect.close()

def update_exam_points(points, id1):
    """Обновить баллы за индивидуальное достижение пользователя в БД

    Аргументы:
    ege_points - нынешнее баллы за индивидуальное достижение пользователя
    id1 - идентификатор пользователя в вк
    """
    # Подготавливаем SQL запрос для передачи его базе данных
    dbUpdate = """update exam set points = %s where id = %s;"""
    # Соединяемся с базой данных
    connect = getConnection()

    # Передаем запрос на изменение элемента, выводим его в терминал и фиксируем в бд
    try:
        with connect.cursor() as cursor:
            cursor.execute(dbUpdate, (points, id1))
            cursor.execute("""select * from exam;""")
            print(cursor.fetchall())
            connect.commit()
    # В случае неудачи оповещаем об ошибке
    except:
        print("Ошибка")
    # Отсоединяемся от базы данных
    connect.close()

def delete_exam(user_exam, user_id):
    """Удалить экзамен пользователя из БД

    Аргументы:
    user_exam - экзамен пользователя
    user_id - идентификатор пользователя в вк
    """
    # Подготавливаем SQL запрос для передачи его базе данных
    dbDelete = """delete from exam where name = %s and id_user = %s;"""
    # Соединяемся с базой данных
    connect = getConnection()

    # Передаем запрос на изменение элемента, выводим его в терминал и фиксируем в бд
    try:
        with connect.cursor() as cursor:
            cursor.execute(dbDelete, (user_exam, user_id))
            cursor.execute("""select * from exam;""")
            print(cursor.fetchall())
            connect.commit()
    # В случае неудачи оповещаем об ошибке
    except:
        print("Ошибка")
    # Отсоединяемся от базы данных
    connect.close()

def delete_achievement(user_achievement, user_id):
    """Удалить индивидуальное достижение пользователя из БД

    Аргументы:
    user_achievement - индивидуальное достижение пользователя
    user_id - идентификатор пользователя в вк
    """
    # Подготавливаем SQL запрос для передачи его базе данных
    dbDelete = """delete from achievement where name = %s and id_user = %s;"""
    # Соединяемся с базой данных
    connect = getConnection()
    
    # Передаем запрос на изменение элемента, выводим его в терминал и фиксируем в бд
    try:
        with connect.cursor() as cursor:
            cursor.execute(dbDelete, (user_achievement, user_id))
            cursor.execute("""select * from achievement;""")
            print(cursor.fetchall())
            connect.commit()
    # В случае неудачи оповещаем об ошибке
    except:
        print("Ошибка")
    # Отсоединяемся от базы данных
    connect.close()

# def delete_user(user, user_id):
#     """Удалить пользователя из БД ctrl+/

#     Аргументы:
#     user - пользователь
#     user_id - идентификатор пользователя в вк
#     """
#     # Подготавливаем SQL запрос для передачи его базе данных
#     dbDelete = """delete from user where ege_points = %s and id = %s;"""
#     # Соединяемся с базой данных
#     connect = getConnection()

#     # Передаем запрос на изменение элемента, выводим его в терминал и фиксируем в бд
#     try:
#         with connect.cursor() as cursor:
#             cursor.execute(dbDelete, (user, user_id))
#             cursor.execute("""select * from user;""")
#             print(cursor.fetchall())
#             connect.commit()
#     # В случае неудачи оповещаем об ошибке
#     except:
#         print("Ошибка")
#     # Отсоединяемся от базы данных
#     connect.close()
    
