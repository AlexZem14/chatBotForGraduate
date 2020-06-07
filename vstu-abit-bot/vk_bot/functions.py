import json
from db import get_old_loc, add_achievement, add_exam
from points import *


def nextNode(location, message, connect = None, vk_id=None):
    """
    Ответная реакция на сообщение пользователя
    :param location: позиция пользователя
    :param message: сообщение пользователя
    :param connect: соединениие с БД
    :param vk_id: идентификатор пользователя в вк
    :return: вернуть следующую позицию пользователя
    """
    # Если тип узла означает начало работы
    if location == 501:
        # Действия, при сообщении
        if message.lower() == "понял. продолжим!":
            # Записать новую позицию
            next_loc = 0
        else:
            print("Error in nextNode")
            # При ошибке указать прежнюю позицию
            next_loc = location

    # if	location == 5010:
    #     if message == "Привет":
    #         next_loc = 0
    #     else:
    #         next_loc = location

    if location == 0:
        if message == "Информационный режим":
            next_loc = 1
        elif message == "Интерактивный режим":
            next_loc = 10
        else:
            next_loc = location

    # Информационный режим
    if location == 1:
        if message == "Об университете":
            next_loc = 101
        elif message == "Абитуриентам":
           next_loc = 20
        elif message == "Интерактивный режим":
            next_loc = 10
        else:
            next_loc = location

    if location == 20:
        if message == "Проходные баллы прошлых лет":
            next_loc = 21
        elif message == "Индивидуальные достижения":
            next_loc = 22
        elif message == "Документы для поступления":
            next_loc = 23
        elif message == "Стоимость обучения":
            next_loc = 24
        elif message == "Сведения о льготах":
            next_loc = 25
        elif message == "Подготовка к поступлению":
            next_loc = 26
        elif message == "Календарь абитуриента":
            next_loc = 27
        elif message == "Общежитие":
            next_loc = 28
        elif message == "Количество мест":
            next_loc = 29
        elif message == "Вступительные испытания":
            next_loc = 30
        elif message == "Назад":
            next_loc = 1
        elif message == "Интерактивный режим":
            next_loc = 10
        else:
            next_loc = location

    if location == 21:
        if message == "Назад":
            next_loc = 20
        elif message == "Интерактивный режим":
            next_loc = 10
        else:
            next_loc = location
    
    if location == 22:
        if message == "Назад":
            next_loc = 20
        elif message == "Интерактивный режим":
            next_loc = 10
        else:
            next_loc = location

    if location == 23:
        if message == "Назад":
            next_loc = 20
        elif message == "Интерактивный режим":
            next_loc = 10
        else:
            next_loc = location

    if location == 24:
        if message == "Назад":
            next_loc = 20
        elif message == "Интерактивный режим":
            next_loc = 10
        else:
            next_loc = location

    if location == 25:
        if message == "Назад":
            next_loc = 20
        elif message == "Интерактивный режим":
            next_loc = 10
        else:
            next_loc = location

    if location == 26:
        if message == "Назад":
            next_loc = 20
        elif message == "Интерактивный режим":
            next_loc = 10
        else:
            next_loc = location
    
    if location == 27:
        if message == "Назад":
            next_loc = 20
        elif message == "Интерактивный режим":
            next_loc = 10
        else:
            next_loc = location

    if location == 28:
        if message == "Назад":
            next_loc = 20
        elif message == "Интерактивный режим":
            next_loc = 10
        else:
            next_loc = location

    if location == 29:
        if message == "Назад":
            next_loc = 20
        elif message == "Интерактивный режим":
            next_loc = 10
        else:
            next_loc = location

    if location == 30:
        if message == "Назад":
            next_loc = 20
        elif message == "Интерактивный режим":
            next_loc = 10
        else:
            next_loc = location

    if location == 101:
        if message == "Направления":
            next_loc = 110
        elif message == "Подробнее об университете":
            next_loc = 120
        elif message == "Контакты и структура":
            next_loc = 130
        elif message == "Назад":
            next_loc = 1
        elif message == "Интерактивный режим":
            next_loc = 10
        else:
            next_loc = location
    
    if location == 110:
        if message == "Информатика и вычислительная техника":
            next_loc = 1110
        elif message == "Программная инженерия":
            next_loc = 1120
        elif message == "Физика":
            next_loc = 1130
        elif message == "Приборостроение":
            next_loc = 1140
        elif message == "Назад":
            next_loc = 101
        elif message == "Интерактивный режим":
            next_loc = 10
        else:
            next_loc = location

    if location == 120:
        if message == "Назад":
            next_loc = 101
        elif message == "Интерактивный режим":
            next_loc = 10
        else:
            next_loc = location

    if location == 130:
        if message == "Назад":
            next_loc = 101
        elif message == "Интерактивный режим":
            next_loc = 10
        else:
            next_loc = location

    if location == 1110:
        if message == "Назад":
            next_loc = 110
        elif message == "Интерактивный режим":
            next_loc = 10
        else:
            next_loc = location

    if location == 1120:
        if message == "Назад":
            next_loc = 110
        elif message == "Интерактивный режим":
            next_loc = 10
        else:
            next_loc = location

    if location == 1130:
        if message == "Назад":
            next_loc = 110
        elif message == "Интерактивный режим":
            next_loc = 10
        else:
            next_loc = location

    if location == 1140:
        if message == "Назад":
            next_loc = 110
        elif message == "Интерактивный режим":
            next_loc = 10
        else:
            next_loc = location
    
    # Интерактивный режим
    elif location == 10:
        if message == "Выпускник школы":
            next_loc = 221
        elif message == "Студент другого вуза":
            next_loc = 30
        elif message == "Выпускник коледжа":
            next_loc = 40
        elif message == "Выпускник вуза":
            next_loc = 50
        elif message == "Ученик школы":
            next_loc = 60
        else:
            next_loc = location

    elif location == 50:
        if message == "Факультет послевузовского образования":
            next_loc = 747
        else:
            next_loc = location

    elif location == 747:
        if message == "Главное меню":
            next_loc = 0
        else:
            next_loc = location

    elif location == 221:
        if message == "Да":
            next_loc = 241
        elif message == "Нет":
            next_loc = 222
        else:
            next_loc = location

    elif location == 30:
        if message == "Информация о переводе":
            next_loc = 2116
        else:
            next_loc = location

    elif location == 2116:
        if message == "Понял. Продолжим!":
            next_loc = 2118
        else:
            next_loc = location
    
    elif location == 40:
        if message == "Да":
            next_loc = 1447
        elif message == "Нет":
            next_loc = 4117
        else:
            next_loc = location
    
    elif location == 1447:
        if message == "Информация о вступительных испытаниях":
            next_loc = 742
        elif message == "Я сдавал ЕГЭ по профильным предметам":
            next_loc = 241
        else:
            next_loc = location

    elif location == 4117:
        if message == "Информация о вступительных испытаниях":
            next_loc = 742
        elif message == "Я сдавал ЕГЭ по профильным предметам":
            next_loc = 241
        else:
            next_loc = location

    # elif location == 741:
    #     if message == "Информация о вступительных испытаниях":
    #         next_loc = 742
    #     else:
    #         next_loc = location


    elif location == 742:
        if message == "Понял. Продолжим!":
            next_loc = 2118
        else:
            next_loc = location
    # elif location == 40:
    #     if message == "Информация о вступительных испытаниях":
    #         next_loc = 2117
    #     elif message == "Информация о довузовской подготовке":
    #         next_loc = 1447
    #     elif message == "Я сдавал ЕГЭ по профильным предметам":
    #         next_loc = 241
    #     else:
    #         next_loc = location

    elif location == 60:
        if message == "Да":
            next_loc = 621
        elif message == "Нет":
            next_loc = 222
        else:
            next_loc = location

    # elif location == 221:
    #     if message == "Да":
    #         next_loc = 241
    #     elif message == "Нет":
    #         next_loc = 2118
    #     else:
    #         next_loc = location

    elif location == 222:
        if message == "Назад":
            next_loc = get_old_loc(vk_id, connect)
        else:
            next_loc = location

    elif location == 621:
        if message == "Да":
            next_loc = 641
        elif message == "Нет":
            next_loc = 2118
        else:
            next_loc = location

    elif location == 241:
        deleteAllPoints(vk_id,connect)
        if message == "Да":
            add_achievement(vk_id, "Золотая медаль", 10, connect)
            next_loc = 2111
        elif message == "Нет":
            next_loc = 272
        else:
            next_loc = location

    elif location == 641:
        if message == "Понял. Продолжим!":
            next_loc = 2118
        else:
            next_loc = location

    elif location == 272:
        if message == "Да":
            add_achievement(vk_id, "Диплом", 5, connect)
            next_loc = 291
        elif message == "Нет":
            next_loc = 291
        else:
            next_loc = location

    elif location == 291:
        if message == "Да":
            add_achievement(vk_id, "ГТО", 3, connect)
            next_loc = 2111
        elif message == "Нет":
            next_loc = 2111
        else:
            next_loc = location

    elif location == 2111:
        sumAchPoints(vk_id,connect)
        if message.isdigit() is True:
            if 27 <= int(message) <= 100:
                add_exam(vk_id, "Математика", int(message), connect)
                next_loc = 2113
            else:
                next_loc = location
        else:
            next_loc = location

    elif location == 2113:
        if message.isdigit() is True:
            if 36 <= int(message) <= 100:
                add_exam(vk_id, "Физика", int(message), connect)
                next_loc = 2115
            else:
                next_loc = location
        else:
            next_loc = location

    elif location == 2115:
        if message.isdigit() is True:
            if 36 <= int(message) <= 100:
                add_exam(vk_id, "Русский", int(message), connect)
                sumEgePoints(vk_id,connect)
                next_loc = 2117
            else:
                next_loc = location
        else:
            next_loc = location

    elif location == 2117:
        if message == "Понял. Продолжим!":
            next_loc = 2118
        else:
            next_loc = location

    elif location == 2118:
        if message == "Подробнее о направлениях":
            next_loc = 2121
        elif message == "Подробнее об стоимости обучения":
            next_loc = 2122
        elif message == "Не хочу":
            next_loc = 2135
        else:
            next_loc = location

    elif location == 2121:
        if message == "ПрИн":
            next_loc = 2131
        elif message == "ИВТ":
            next_loc = 2132
        elif message == "Физика":
            next_loc = 2133
        elif message == "Приборостроение":
            next_loc = 2134
        else:
            next_loc = location

    elif location == 2122:
        if message == "Подробнее о направлениях":
            next_loc = 2121
        elif message == "Да":
            next_loc = 2151
        elif message == "Нет, я уже узнал все что хотел":
            next_loc = 0
        # elif message == "Назад":
        #     next_loc = 2117
        else:
            next_loc = location

    elif location == 2131:
        if message == "Да":
            next_loc = 2151
        elif message == "Нет, я уже узнал все что хотел":
            next_loc = 0
        elif message == "Назад":
            next_loc = 2121
        elif message == "Подробнее об стоимости обучения":
            next_loc = 2122
        else:
            next_loc = location

    elif location == 2132:
        if message == "Да":
            next_loc = 2151
        elif message == "Нет, я уже узнал все что хотел":
            next_loc = 0
        elif message == "Назад":
            next_loc = 2121
        elif message == "Подробнее об стоимости обучения":
            next_loc = 2122
        else:
            next_loc = location

    elif location == 2133:
        if message == "Да":
            next_loc = 2151
        elif message == "Нет, я уже узнал все что хотел":
            next_loc = 0
        elif message == "Назад":
            next_loc = 2121
        elif message == "Подробнее об стоимости обучения":
            next_loc = 2122
        else:
            next_loc = location

    elif location == 2134:
        if message == "Да":
            next_loc = 2151
        elif message == "Нет, я уже узнал все что хотел":
            next_loc = 0
        elif message == "Назад":
            next_loc = 2121
        elif message == "Подробнее об стоимости обучения":
            next_loc = 2122
        else:
            next_loc = location

    elif location == 2135:
        if message == "Да":
            next_loc = 2151
        elif message == "Нет, я уже узнал все что хотел":
            next_loc = 0
        elif message == "Назад":
            next_loc = 2121
        elif message == "Подробнее об стоимости обучения":
            next_loc = 2122
        else:
            next_loc = location

    elif location == 2151:
        if message == "Документы для поступления":
            next_loc = 2161
        elif message == "Сведения о льготах":
            next_loc = 2162
        elif message == "Календарь абитуриента":
            next_loc = 2163
        elif message == "Общежитие":
            next_loc = 2164
        elif message == "Количество мест":
            next_loc = 2165
        else:
            next_loc = location

    elif location == 2161:
        if message == "Назад":
            next_loc = 2151
        elif message == "Главное меню":
            next_loc = 0
        else:
            next_loc = location

    elif location == 2162:
        if message == "Назад":
            next_loc = 2151
        elif message == "Главное меню":
            next_loc = 0
        else:
            next_loc = location

    elif location == 2163:
        if message == "Назад":
            next_loc = 2151
        elif message == "Главное меню":
            next_loc = 0
        else:
            next_loc = location

    elif location == 2164:
        if message == "Назад":
            next_loc = 2151
        elif message == "Главное меню":
            next_loc = 0
        else:
            next_loc = location

    elif location == 2165:
        if message == "Назад":
            next_loc = 2151
        elif message == "Главное меню":
            next_loc = 0
        else:
            next_loc = location

    return next_loc

def newMess(loc_type,vk_id,connect):
    """
    Создать сообщение для пользователя
    :param location: новая позиция пользователя
    :param connect: соединение с БД
    :param vk_id: идентификатор пользователя в вк
    :param message: сообщение пользователя
    :return: вернуть список, содержащий текст и клавиатуру вк
    """
    # Переменная для хранения текста
    text = ""

    # Если тип узла относится к началу работы с программой
    # if loc_type == 5010:
    #     text = "Привет"

    #     startKeyboard = None

    if loc_type == 501:
        text = "Здесь есть 2 режима"
        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Понял. Продолжим!", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    if loc_type == 0:
        text = "Добрый день, что вас интересует"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Информационный режим", color="primary")],
                [getButton("Интерактивный режим", color="primary")]

            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))
    
    # Информационный режим
    if loc_type == 1:
        text = "Что вас интересует?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Об университете", color="primary")],
                [getButton("Абитуриентам", color="primary")],
                [getButton("Интерактивный режим", color="secondary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    if loc_type == 20:
        text = "Что вас интересует?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
            [getButton("Проходные баллы прошлых лет", color="primary")],
            [getButton("Индивидуальные достижения", color="primary")],
            [
                getButton("Документы для поступления", color="primary"),
                getButton("Стоимость обучения", color="primary")
            ],
            [
                getButton("Сведения о льготах", color="primary"),
                getButton("Подготовка к поступлению", color="primary")
            ],
            [
                getButton("Календарь абитуриента", color="primary"),
                getButton("Общежитие", color="primary")
            ],
            [getButton("Количество мест", color="primary")],
            [getButton("Вступительные испытания", color="primary")],
            [
                getButton("Назад", color="secondary"),
                getButton("Интерактивный режим", color="secondary")
            ]
        ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    if loc_type == 21:
        text = "Проходные баллы прошлых лет"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Назад", color="secondary")],
                [getButton("Интерактивный режим", color="secondary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    if loc_type == 22:
        text = "Индивидуальные достижения"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Назад", color="secondary")],
                [getButton("Интерактивный режим", color="secondary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    if loc_type == 23:
        text = "Документы для поступления"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Назад", color="secondary")],
                [getButton("Интерактивный режим", color="secondary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    if loc_type == 24:
        text = "Стоимость обучения"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Назад", color="secondary")],
                [getButton("Интерактивный режим", color="secondary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    if loc_type == 25:
        text = "Сведения о льготах"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Назад", color="secondary")],
                [getButton("Интерактивный режим", color="secondary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    if loc_type == 26:
        text = "Подготовка к поступлению"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Назад", color="secondary")],
                [getButton("Интерактивный режим", color="secondary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    if loc_type == 27:
        text = "Календарь абитуриента"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Назад", color="secondary")],
                [getButton("Интерактивный режим", color="secondary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    if loc_type == 28:
        text = "Общежитие"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Назад", color="secondary")],
                [getButton("Интерактивный режим", color="secondary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    if loc_type == 29:
        text = "Количество мест"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Назад", color="secondary")],
                [getButton("Интерактивный режим", color="secondary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    if loc_type == 30:
        text = "Вступительные испытания"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Назад", color="secondary")],
                [getButton("Интерактивный режим", color="secondary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    if loc_type == 101:
        text = "Что интересует?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Направления", color="primary")],
                [getButton("Подробнее об университете", color="primary")],
                [getButton("Контакты и структура", color="primary")],
                [getButton("Назад", color="secondary")],
                [getButton("Интерактивный режим", color="secondary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    if loc_type == 110:
        text = "Направления"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Информатика и вычислительная техника", color="primary")],
                [getButton("Программная инженерия", color="primary")],
                [getButton("Физика", color="primary")],
                [getButton("Приборостроение", color="primary")],
                [getButton("Назад", color="secondary")],
                [getButton("Интерактивный режим", color="secondary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    if loc_type == 120:
        text = "Подробнее об университете"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Назад", color="secondary")],
                [getButton("Интерактивный режим", color="secondary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    if loc_type == 130:
        text = "Контакты и структура"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Назад", color="secondary")],
                [getButton("Интерактивный режим", color="secondary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    if loc_type == 1110:
        text = "Информатика и вычислительная техника"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Назад", color="secondary")],
                [getButton("Интерактивный режим", color="secondary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    if loc_type == 1120:
        text = "Программная инженерия"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Назад", color="secondary")],
                [getButton("Интерактивный режим", color="secondary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    if loc_type == 1130:
        text = "Физика"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Назад", color="secondary")],
                [getButton("Интерактивный режим", color="secondary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    if loc_type == 1140:
        text = "Приборостроение"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Назад", color="secondary")],
                [getButton("Интерактивный режим", color="secondary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    # Интерактивный режим
    elif loc_type == 10:
        text = "Кем вы являетесь?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Выпускник школы", color="primary")],
                [getButton("Студент другого вуза", color="primary")],
                [getButton("Выпускник коледжа", color="primary")],
                [getButton("Выпускник вуза", color="primary")],
                [getButton("Ученик школы", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 221:
        text = "Вы сдавали/будете сдавать в качестве экзаменов ЕГЭ профильную математику и физику?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Да", color="primary")],
                [getButton("Нет", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 30:
        text = "Что вас интересует?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Информация о переводе", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 50:
        text = "Что вас интересует?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Факультет послевузовского образования", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 747:
        text = "Что вы хотите?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Главное меню", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    # elif loc_type == 40:
    #     text = "Что вас интересует?"

    #     startKeyboard = {
    #         "one_time": True,
    #         "buttons": [
    #             [getButton("Информация о вступительных испытаниях", color="primary")],
    #             [getButton("Информация о довузовской подготовке", color="primary")],
    #             [getButton("Я сдавал ЕГЭ по профильным предметам", color="primary")]
    #         ]
    #     }

    #     startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
    #     startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 60:
        text = "Вы собираетесь сдавать в качестве экзаменов ЕГЭ профильную математику и физику?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Да", color="primary")],
                [getButton("Нет", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    # elif loc_type == 221:
    #     text = "Вы уже сдали ЕГЭ?"

    #     startKeyboard = {
    #         "one_time": True,
    #         "buttons": [
    #             [getButton("Да", color="primary")],
    #             [getButton("Нет", color="primary")]
    #         ]
    #     }

    #     startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
    #     startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 222:
        text = "Извините, вам не подходит наш факультет"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Назад", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 621:
        text = "Вас интересует информация о довузовской подготовке?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Да", color="primary")],
                [getButton("Нет", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    # elif loc_type == 6411:
    #     text = "Да"

    #     startKeyboard = {
    #         "one_time": True,
    #         "buttons": [
    #             [getButton("Да", color="primary")],
    #             [getButton("Нет", color="primary")]
    #         ]
    #     }

        # startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        # startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 241:
        text = "У вас есть аттестат с отличием (золотая медаль)?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Да", color="primary")],
                [getButton("Нет", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 641:
        text = "Информация о довузовской подготовке"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Понял. Продолжим!", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    # elif loc_type == 741:
    #     text = "Информация о вступительных испытаниях"

    #     startKeyboard = {
    #         "one_time": True,
    #         "buttons": [
    #             [getButton("Информация о вступительных испытаниях", color="primary")]
    #         ]
    #     }

    #     startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
    #     startKeyboard = str(startKeyboard.decode("utf-8"))
    
    elif loc_type == 742:
        text = "Информация о вступительных испытаниях"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Понял. Продолжим!", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 2116:
        text = "Информация о переводе"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Понял. Продолжим!", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))


    elif loc_type == 272:
        text = "У вас есть диплом победителя регионального этапа Всероссийской олимпиады школьников или диплом " \
               "победителя олимпиады ВолгГТУ?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Да", color="primary")],
                [getButton("Нет", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 291:
        text = "У вас есть золотой значок ГТО?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Да", color="primary")],
                [getButton("Нет", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 2111:
        text = "Введите баллы ЕГЭ, готорые вы получили по профильной математике"

        startKeyboard = None

    elif loc_type == 2113:
        text = "Введите баллы ЕГЭ, готорые вы получили по физике"

        startKeyboard = None

    elif loc_type == 2115:
        text = "Введите баллы ЕГЭ, готорые вы получили по русскому языку"

        startKeyboard = None

    elif loc_type == 2117:
        text = "У вас " + str(get_all_points(vk_id, connect)) + " баллов."

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Понял. Продолжим!", color="primary")],
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 2118:
        text = "Хотите узнать подробней об одном из направлений/стоимости обучения?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Подробнее о направлениях", color="primary")],
                [getButton("Подробнее об стоимости обучения", color="primary")],
                [getButton("Не хочу", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 2122:
        text = "Инфо о стоимости обучения\nВам что-то еще хотелось бы узнать?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Подробнее о направлениях", color="primary")],
                [getButton("Да", color="primary")],
                [getButton("Нет, я уже узнал все что хотел", color="primary")]
                #[getButton("Назад", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 2121:
        text = "О каких направлениях вы хотели бы узнать?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("ПрИн", color="primary")],
                [getButton("ИВТ", color="primary")],
                [getButton("Физика", color="primary")],
                [getButton("Приборостроение", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 2131:
        text = "Информация о ПрИн\nВам что-то еще хотелось бы узнать?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Да", color="primary")],
                [getButton("Нет, я уже узнал все что хотел", color="primary")],
                [getButton("Подробнее об стоимости обучения", color="primary")],
                [getButton("Назад", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 2132:
        text = "Информация о ИВТ\nВам что-то еще хотелось бы узнать?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Да", color="primary")],
                [getButton("Нет, я уже узнал все что хотел", color="primary")],
                [getButton("Подробнее об стоимости обучения", color="primary")],
                [getButton("Назад", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 2133:
        text = "Информация о Физике\nВам что-то еще хотелось бы узнать?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Да", color="primary")],
                [getButton("Нет, я уже узнал все что хотел", color="primary")],
                [getButton("Подробнее об стоимости обучения", color="primary")],
                [getButton("Назад", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 2134:
        text = "Информация о Приборостроении\nВам что-то еще хотелось бы узнать?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Да", color="primary")],
                [getButton("Нет, я уже узнал все что хотел", color="primary")],
                [getButton("Подробнее об стоимости обучения", color="primary")],
                [getButton("Назад", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 2135:
        text = "Вам что-то еще хотелось бы узнать?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Да", color="primary")],
                [getButton("Нет, я уже узнал все что хотел", color="primary")],
                [getButton("Подробнее об стоимости обучения", color="primary")],
                [getButton("Назад", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 2151:
        text = "Что именно вам хотелось бы узнать?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Документы для поступления", color="primary")],
                [getButton("Сведения о льготах", color="primary")],
                [getButton("Календарь абитуриента", color="primary")],
                [getButton("Общежитие", color="primary")],
                [getButton("Количество мест", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 2161:
        text = "Документы для поступления"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Назад", color="primary")],
                [getButton("Главное меню", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 2162:
        text = "Сведения о льготах"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Назад", color="primary")],
                [getButton("Главное меню", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 2163:
        text = "Календарь абитуриента"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Назад", color="primary")],
                [getButton("Главное меню", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 2164:
        text = "Общежитие"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Назад", color="primary")],
                [getButton("Главное меню", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))
    
    elif loc_type == 1447:
        text = "Информация о довузовской подготовке\nЧто еще хотите узнать?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Информация о вступительных испытаниях", color="primary")],
                [getButton("Я сдавал ЕГЭ по профильным предметам", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 4117:
        text = "Что хотите узнать?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Информация о вступительных испытаниях", color="primary")],
                [getButton("Я сдавал ЕГЭ по профильным предметам", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 40:
        text = "Вас интересует информация о довузовской подготовке?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Да", color="primary")],
                [getButton("Нет", color="primary")]
            ]
        }
        
        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 2165:
        text = "Количество мест"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Назад", color="primary")],
                [getButton("Главное меню", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    return [text, startKeyboard]
    
def getButton(label, color, payload=''):
    """
    Создать кнопку
    :param label: текст
    :param color: цвет
    :param payload: дополнительная информация
    :return: вернуть кнопку
    """
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }
