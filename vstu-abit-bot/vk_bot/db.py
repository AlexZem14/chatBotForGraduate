import pymysql
from dbConnect import *

def add_user(vk_id, status, ege_points, position, old_position, connect):
    """ Добавить пользователя в таблицу пользователей в БД

    Аргументы:
    vk_id - идентификатор пользователя в вк
    status - категория пользователя
    ege_points - баллы ЕГЭ пользователя
    position - нынешняя позиция пользователя
    old_position - позиция, в которой находился пользователь на прошлом шаге
    connect - соединение с БД
    """
    # Подготавливаем SQL запрос для передачи его базе данных
    dbInject = """insert into user (id, status, ege_points, position, old_position) values (%s, %s, %s, %s, %s);"""

    # Передаем запрос на добавление элемента, выводим его в терминал и фиксируем в бд
    try:
        with connect.cursor() as cursor:
            cursor.execute(dbInject, (vk_id, status, ege_points, position, old_position))
            cursor.execute("""select * from user;""")
            print(cursor.fetchall())
            connect.commit()
    # В случае неудачи оповещаем об ошибке
    except:
        print("Ошибка")

def add_exam(vk_id, name, points, connect):
    """ Добавить экзамен в таблицу экзаменов в БД

    Аргументы:
    vk_id - идентификатор пользователя в вк
    name - название экзамена
    points - баллы за экзамен
    connect - соединение с БД
    """
    # Подготавливаем SQL запрос для передачи его базе данных
    dbInject = """insert into exam (id_user, name, points) values (%s, %s, %s);"""

    # Передаем запрос на добавление элемента, выводим его в терминал и фиксируем в бд
    try:
        with connect.cursor() as cursor:
            cursor.execute(dbInject, (str(vk_id), name, str(points)))
            cursor.execute("""select * from exam;""")
            print(cursor.fetchall())
            connect.commit()
    # В случае неудачи оповещаем об ошибке
    except:
        print("Ошибка")

def add_achievement(vk_id, name, points, connect):
    """ Добавить индивидуальное достижение в таблицу индивидуальных достижений в БД

    Аргументы:
    vk_id - идентификатор пользователя в вк
    name - название индивидуального достижения
    points - баллы за индивидуальное достижение
    connect - соединение с БД
    """
    # Подготавливаем SQL запрос для передачи его базе данных
    dbInject = """insert into achievement (id_user, name, points) values (%s, %s, %s);"""

    # Передаем запрос на добавление элемента, выводим его в терминал и фиксируем в бд
    try:
        with connect.cursor() as cursor:
            cursor.execute(dbInject, (str(vk_id), name, str(points)))
            cursor.execute("""select * from achievement;""")
            print(cursor.fetchall())
            connect.commit()
    # В случае неудачи оповещаем об ошибке
    except:
        print("Ошибка")

def add_speciality(id_spec, name, min_points, connect):
    """ Добавить направление в таблицу направлений в БД

    Аргументы:
    id_spec - идентификатор направления
    name - название направления
    min_points - минимальное кол-во баллов для поступление на направление
    connect - соединение с БД
    """
    # Подготавливаем SQL запрос для передачи его базе данных
    dbInject = """insert into speciality (id, name, min_points) values (%s, %s, %s);"""

    # Передаем запрос на добавление элемента, выводим его в терминал и фиксируем в бд
    try:
        with connect.cursor() as cursor:
            cursor.execute(dbInject, (vk_id, name, min_points))
            cursor.execute("""select * from speciality;""")
            print(cursor.fetchall())
            connect.commit()
    # В случае неудачи оповещаем об ошибке
    except:
        print("Ошибка")

def update_user_ege_points(ege_points, vk_id, connect):
    """Обновить баллы ЕГЭ пользователя в БД

    Аргументы:
    ege_points - нынешнее баллы ЕГЭ пользователя
    vk_id - идентификатор пользователя в вк
    connect - соединение с БД
    """
    # Подготавливаем SQL запрос для передачи его базе данных
    dbUpdate = """update user set ege_points = %s where id = %s;"""

    # Передаем запрос на изменение элемента, выводим его в терминал и фиксируем в бд
    try:
        with connect.cursor() as cursor:
            cursor.execute(dbUpdate, (ege_points, vk_id))
            cursor.execute("""select * from user;""")
            print(cursor.fetchall())
            connect.commit()
    # В случае неудачи оповещаем об ошибке
    except:
        print("Ошибка")

def update_user_status(status, vk_id, connect):
    """Обновить категорию пользователя в БД

    Аргументы:
    status - категория пользователя
    vk_id - идентификатор пользователя в вк
    connect - соединение с БД
    """
    # Подготавливаем SQL запрос для передачи его базе данных
    dbUpdate = """update user set status = %s where id = %s;"""

    # Передаем запрос на изменение элемента, выводим его в терминал и фиксируем в бд
    try:
        with connect.cursor() as cursor:
            cursor.execute(dbUpdate, (status, vk_id))
            cursor.execute("""select * from user;""")
            print(cursor.fetchall())
            connect.commit()
    # В случае неудачи оповещаем об ошибке
    except:
        print("Ошибка")

def update_exam_points(points, vk_id, connect):
    """Обновить баллы за индивидуальное достижение пользователя в БД

    Аргументы:
    points - нынешнее баллы за индивидуальное достижение пользователя
    vk_id - идентификатор пользователя в вк
    connect - соединение с БД
    """
    # Подготавливаем SQL запрос для передачи его базе данных
    dbUpdate = """update exam set points = %s where id = %s;"""

    # Передаем запрос на изменение элемента, выводим его в терминал и фиксируем в бд
    try:
        with connect.cursor() as cursor:
            cursor.execute(dbUpdate, (points, vk_id))
            cursor.execute("""select * from exam;""")
            print(cursor.fetchall())
            connect.commit()
    # В случае неудачи оповещаем об ошибке
    except:
        print("Ошибка")

def delete_exam(user_exam, user_id, connect):
    """Удалить экзамен пользователя из БД

    Аргументы:
    user_exam - экзамен пользователя
    user_id - идентификатор пользователя в вк
    connect - соединение с БД
    """
    # Подготавливаем SQL запрос для передачи его базе данных
    dbDelete = """delete from exam where name = %s and id_user = %s;"""

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

def delete_achievement(user_achievement, user_id, connect):
    """Удалить индивидуальное достижение пользователя из БД

    Аргументы:
    user_achievement - индивидуальное достижение пользователя
    user_id - идентификатор пользователя в вк
    connect - соединение с БД
    """
    # Подготавливаем SQL запрос для передачи его базе данных
    dbDelete = """delete from achievement where name = %s and id_user = %s;"""
    
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

def user_update_position(vk_id, location, connect):
    """Обновить позицию пользователя

    Аргументы:
    vk_id - идентификатор пользователя в вк
    location - позиция пользователя 
    connect - соединение с БД
    """
    dbUpdate = """update user set position = %s where id = %s;"""

    try:
        with connect.cursor() as cursor:
            cursor.execute(dbUpdate, (location, str(vk_id)))
            connect.commit()
    except:
        print("Ошибка при обновлении позиции пользователя")


def user_update_old_position(vk_id, old_location, connect):
    """Обновить прежнюю позицию пользователя

    Аргументы:
    vk_id - идентификатор пользователя в вк
    old_location - прежняя позиция пользователя 
    connect - соединение с БД
    """
    dbUpdate = """update user set old_position = %s where id = %s;"""

    try:
        with connect.cursor() as cursor:
            cursor.execute(dbUpdate, (old_location, str(vk_id)))
            connect.commit()
    except:
        print("Ошибка при обновлении прежней позиции пользователя")


def get_old_loc(vk_id, connect):
    """Получить прежнюю позицию пользователя

    Аргументы:
    vk_id - идентификатор пользователя в вк
    connect - соединение с БД
    """
    dbSelect = """select * from user where id = %s"""

    try:
        with connect.cursor() as cursor:
            cursor.execute(dbSelect, str(vk_id))
            return cursor.fetchall()[0]["old_position"]
    except:
        print("Ошибка при получении прежней позиции пользователя")
    return 0

def delete_user(vk_id, connect):
    """Удалить пользователя из БД

    Аргументы:
    user_id - идентификатор пользователя в вк
    connect - соединение с БД
    """
    # Подготавливаем SQL запрос для передачи его базе данных
    dbDelete = """delete from user where id = %s;"""

    # Передаем запрос на изменение элемента, выводим его в терминал и фиксируем в бд
    try:
        with connect.cursor() as cursor:
            cursor.execute(dbDelete, (vk_id))
            cursor.execute("""select * from user;""")
            print(cursor.fetchall())
            connect.commit()
    # В случае неудачи оповещаем об ошибке
    except:
        print("Ошибка")
    
