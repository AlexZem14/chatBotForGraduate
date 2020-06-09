import json
from db import get_old_loc, add_achievement, add_exam, update_user_status
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
        if message.lower() == "понятно. продолжим!":
            # Записать новую позицию
            next_loc = 0
        else:
            print("Error in nextNode")
            # При ошибке указать прежнюю позицию
            next_loc = location

    if location == 0:
        if message == "Информационный режим":
            next_loc = 1
        elif message == "Интерактивный режим":
            next_loc = 10
        else:
            next_loc = location

    # Информационный режим
    if location == 1:
        if message == "Об университете и факультете":
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
        elif message == "Подробнее об университете и факультете":
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
            update_user_status('school_grad', vk_id, connect)
            next_loc = 221
        elif message == "Студент другого вуза":
            update_user_status('each_univer_stud', vk_id, connect)
            next_loc = 230
        elif message == "Студент колледжа":
            update_user_status('college_grad', vk_id, connect)
            next_loc = 40
        elif message == "Выпускник вуза":
            update_user_status('student_bach', vk_id, connect)
            next_loc = 50
        elif message == "Ученик школы":
            update_user_status('school', vk_id, connect)
            next_loc = 60
        else:
            next_loc = location

    elif location == 50:
        if message == "Факультет послевузовского образования":
            next_loc = 747
        else:
            next_loc = location

    elif location == 747:
        if message == "Информационный режим":
            next_loc = 1
        else:
            next_loc = location

    elif location == 221:
        if message == "Да":
            next_loc = 241
        elif message == "Нет":
            next_loc = 222
        else:
            next_loc = location

    elif location == 230:
        if message == "Информация о переводе":
            next_loc = 2116
        else:
            next_loc = location

    elif location == 2116:
        if message == "Понятно. Продолжим!":
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
        elif message == "Я сдавал ЕГЭ по проф. матем. и по физике":
            next_loc = 241
        else:
            next_loc = location

    elif location == 4117:
        if message == "Информация о вступительных испытаниях":
            next_loc = 742
        elif message == "Я сдавал ЕГЭ по проф. матем. и по физике":
            next_loc = 241
        else:
            next_loc = location

    elif location == 742:
        if message == "Понятно. Продолжим!":
            next_loc = 2118
        else:
            next_loc = location

    elif location == 60:
        if message == "Да":
            next_loc = 621
        elif message == "Нет":
            next_loc = 622
        else:
            next_loc = location

    elif location == 222:
        if message == "Назад":
            next_loc = get_old_loc(vk_id, connect)
        elif message == "Информационный режим":
            next_loc = 1
        else:
            next_loc = location

    elif location == 622:
        if message == "Назад":
            next_loc = get_old_loc(vk_id, connect)
        elif message == "Информационный режим":
            next_loc = 1
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
        if message == "Понятно. Продолжим!":
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
        if message.isdigit() is True:
            if 27 <= int(message) <= 100:
                sumAchPoints(vk_id, connect)
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
        if message == "Понятно. Продолжим!":
            next_loc = 2118
        else:
            next_loc = location

    elif location == 2118:
        if message == "Подробнее о направлениях":
            next_loc = 2121
        elif message == "Подробнее о стоимости обучения":
            next_loc = 2122
        elif message == "Не хочу":
            next_loc = 2141
        else:
            next_loc = location

    elif location == 2121:
        if message == "Программная инженерия":
            next_loc = 2131
        elif message == "Информатика и вычислительная техника":
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
        else:
            next_loc = location

    elif location == 2131:
        if message == "Понятно. Продолжим!":
            next_loc = 2141
        elif message == "Подробнее о стоимости обучения":
            next_loc = 2122
        elif message == "Назад":
            next_loc = 2121
        else:
            next_loc = location

    elif location == 2132:
        if message == "Понятно. Продолжим!":
            next_loc = 2141
        elif message == "Подробнее о стоимости обучения":
            next_loc = 2122
        elif message == "Назад":
            next_loc = 2121
        else:
            next_loc = location

    elif location == 2133:
        if message == "Понятно. Продолжим!":
            next_loc = 2141
        elif message == "Подробнее о стоимости обучения":
            next_loc = 2122
        elif message == "Назад":
            next_loc = 2121
        else:
            next_loc = location
    
    elif location == 2134:
        if message == "Понятно. Продолжим!":
            next_loc = 2141
        elif message == "Подробнее о стоимости обучения":
            next_loc = 2122
        elif message == "Назад":
            next_loc = 2121
        else:
            next_loc = location

    elif location == 2141:
        if message == "Да":
            next_loc = 2151
        elif message == "Нет, я уже узнал все что хотел":
            next_loc = 0
        else:
            next_loc = location

    elif location == 2132:
        if message == "Да":
            next_loc = 2151
        elif message == "Нет, я уже узнал все что хотел":
            next_loc = 0
        elif message == "Назад":
            next_loc = 2121
        elif message == "Подробнее о стоимости обучения":
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
        elif message == "Подробнее о стоимости обучения":
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
        elif message == "Подробнее о стоимости обучения":
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
        elif message == "Информационный режим":
            next_loc = 1
        else:
            next_loc = location

    elif location == 2162:
        if message == "Назад":
            next_loc = 2151
        elif message == "Информационный режим":
            next_loc = 1
        else:
            next_loc = location

    elif location == 2163:
        if message == "Назад":
            next_loc = 2151
        elif message == "Информационный режим":
            next_loc = 1
        else:
            next_loc = location

    elif location == 2164:
        if message == "Назад":
            next_loc = 2151
        elif message == "Информационный режим":
            next_loc = 1
        else:
            next_loc = location

    elif location == 2165:
        if message == "Назад":
            next_loc = 2151
        elif message == "Информационный режим":
            next_loc = 1
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
    if loc_type == 501:
        text = "Чат-бот имеет два режима – информационный и интерактивный. Информационный режим оформлен в форме справки для абитуриентов. В интерактивном режиме общение бота похоже на диалог с пользователем с выбором вариантов ответа и вводом данных.\nВвод данных осуществляется только там, где необходимо указать баллы ЕГЭ. В остальных местах взаимодействие с чат-ботом происходит с помощью кнопок.\nЕсли вы вводите некорректное значение в поле ввода, то дублируется последнее сообщение бота"
        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Понятно. Продолжим!", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    if loc_type == 0:
        text = "Выберите режим работы"

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
        text = "Нажмите на одну из кнопок, чтобы узнать интересующую вас информацию"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Об университете и факультете", color="primary")],
                [getButton("Абитуриентам", color="primary")],
                [getButton("Интерактивный режим", color="secondary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    if loc_type == 20:
        text = "Какая информация вас интересует?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
            [getButton("Проходные баллы прошлых лет", color="primary")],
            [getButton("Индивидуальные достижения", color="primary")],
            [
                getButton("Количество мест", color="primary"),
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
            [getButton("Документы для поступления", color="primary")],
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
        text = "Проходные баллы прошлых лет на направлениях факультета:\nhttp://welcome.vstu.ru/acceptance/statistika-priyema/"

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
        text = "Индивидуальные достижения:\nhttp://welcome.vstu.ru/%D0%9F%D1%80%D0%B8%D0%B5%D0%BC%202020/1%20%D0%BE%D0%BA%D1%82%D1%8F%D0%B1%D1%80%D1%8F/07_ID.pdf"

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
        text = "Документы для поступления:\nhttp://welcome.vstu.ru/acceptance/"

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
        text = "Стоимость обучения:\nhttp://welcome.vstu.ru/acceptance/platnoe-obrazovanie/"

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
        text = "Сведения о льготах:\nhttp://welcome.vstu.ru/%D0%9F%D1%80%D0%B8%D0%B5%D0%BC%202020/1%20%D0%BE%D0%BA%D1%82%D1%8F%D0%B1%D1%80%D1%8F/04_4_Osobye%20prava.pdf"

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
        text = "Подготовка к поступлению:\nhttp://welcome.vstu.ru/preparation/"

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
        text = "Календарь абитуриента:\nhttp://welcome.vstu.ru/acceptance/kalendar-abiturienta/"

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
        text = "Общежитие:\nhttp://welcome.vstu.ru/%D0%9F%D1%80%D0%B8%D0%B5%D0%BC%202020/1%20%D0%BE%D0%BA%D1%82%D1%8F%D0%B1%D1%80%D1%8F/18_Obchaga.pdf"

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
        text = "Количество мест:\nhttp://welcome.vstu.ru/acceptance/Abitur/#kolmest"

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
        text = "Вступительные испытания:\nhttp://welcome.vstu.ru/acceptance/vstupitelnye-ispytaniya/"

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
        text = "Какая информация вас интересует?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Направления", color="primary")],
                [getButton("Подробнее об университете и факультете", color="primary")],
                [getButton("Контакты и структура", color="primary")],
                [getButton("Назад", color="secondary")],
                [getButton("Интерактивный режим", color="secondary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    if loc_type == 110:
        text = "Нажмите на одну из кнопок, чтобы узнать интересующую вас информацию"

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
        text = "Информация об университете:\nhttp://www.vstu.ru/university/\nИнформация о факультете:\nhttp://www.vstu.ru/university/fakultety-i-kafedry/fakultet-elektroniki-i-vychislitelnoy-tekhniki/"

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
        text = "Контакты:\nhttp://welcome.vstu.ru/contact/ \nCтруктура:\nhttp://www.vstu.ru/university/structure/"

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
        text = "Существует три поднаправления на этом направлении.\nАвтоматизированное проектирование киберфизических систем:\nhttp://welcome.vstu.ru/specialty-choice/vse-spetsialnosti/avtomatizirovannoe-proektirovanie-kiberfizicheskih-sistem/\nВычислительные машины, комплексы, системы и сети:\nhttp://welcome.vstu.ru/specialty-choice/vse-spetsialnosti/vychislitelnye-mashiny-kompleksy-sistemy-i-seti/\nСистемная инженерия:\nhttp://welcome.vstu.ru/specialty-choice/vse-spetsialnosti/sistemnaya-inzheneriya/"

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
        text = "Программная инженерия:\nhttp://welcome.vstu.ru/specialty-choice/vse-spetsialnosti/programmnaya-inzheneriya/"

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
        text = "Физика:\nhttp://welcome.vstu.ru/specialty-choice/vse-spetsialnosti/fizika/"

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
        text = "Приборостроение:\nhttp://welcome.vstu.ru/specialty-choice/vse-spetsialnosti/priborostroenie/"

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
                [getButton("Студент колледжа", color="primary")],
                [getButton("Выпускник вуза", color="primary")],
                [getButton("Ученик школы", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 221:
        text = "Вы сдавали в качестве экзаменов ЕГЭ профильную математику и физику?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Да", color="positive")],
                [getButton("Нет", color="negative")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 230:
        text = "Вам необходимо узнать информацию о переводе"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Информация о переводе", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 50:
        text = "Вам необходимо узнать информацию факультете послевузовского образования"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Факультет послевузовского образования", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 747:
        text = "Факультет послевузовского образования:\nhttp://vstu.ru/university/fakultety-i-kafedry/fakultet-poslevuzovskogo-obrazovaniya/"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Информационный режим", color="secondary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 60:
        text = "Вы собираетесь сдавать в качестве экзаменов ЕГЭ профильную математику и физику?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Да", color="positive")],
                [getButton("Нет", color="negative")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 222:
        text = "Извините, в таком случае вам не подходит наш факультет. Для того чтобы поступить на него, необходимо сдать профильную математику и физику"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Назад", color="secondary")],
                [getButton("Информационный режим", color="secondary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 622:
        text = "Для того чтобы поступить на наш факультет, необходимо сдать профильную математику и физику"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Назад", color="secondary")],
                [getButton("Информационный режим", color="secondary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 621:
        text = "Вас интересует информация о довузовской подготовке?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Да", color="positive")],
                [getButton("Нет", color="negative")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 241:
        text = "У вас есть аттестат с отличием (золотая медаль) \nили диплом о среднем профессиональном образовании с отличием \nили статус победителя или призера крупных международных спортивных соревнований?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Да", color="positive")],
                [getButton("Нет", color="negative")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 641:
        text = "Информация о довузовской подготовке:\nhttp://welcome.vstu.ru/preparation/"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Понятно. Продолжим!", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 742:
        text = "Информация о вступительных испытаниях:\nhttp://welcome.vstu.ru/acceptance/vstupitelnye-ispytaniya/"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Понятно. Продолжим!", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 2116:
        text = "Информация о переводе: студент может перевестись в другой вуз только при условии, если он является студентом вуза, из которого он будет переводится. В августе по графику деканат факультета будет заниматься этим вопросом. При переводе учитывается разница в учебных планах.\nПоложение о переводе:\nhttp://umu.vstu.ru/files/umo/page/45/polozhenie_o_perevodah_otchisleniyah_i_vosstanovleniyah_31_08_2018.pdf"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Понятно. Продолжим!", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))


    elif loc_type == 272:
        text = "У вас есть диплом ПОБЕДИТЕЛЯ регионального этапа Всероссийской олимпиады школьников \nили диплом " \
               "ПОБЕДИТЕЛЯ олимпиады ВолгГТУ?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Да", color="positive")],
                [getButton("Нет", color="negative")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 291:
        text = "У вас есть золотой значок ГТО \nили диплом ПРИЗЕРА регионального этапа Всероссийской олимпиады школьников \nили диплом " \
               "ПРИЗЕРА олимпиады ВолгГТУ \nили вы являетесь участником заключительного этапа олимпиады 'Звезда'?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Да", color="positive")],
                [getButton("Нет", color="negative")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 2111:
        text = "Введите баллы ЕГЭ, которые вы получили по профильной математике.\nВводимое значение - число от 27 до 100:"

        startKeyboard = None

    elif loc_type == 2113:
        text = "Введите баллы ЕГЭ, которые вы получили по физике.\nВводимое значение - число от 36 до 100:"

        startKeyboard = None

    elif loc_type == 2115:
        text = "Введите баллы ЕГЭ, которые вы получили по русскому языку.\nВводимое значение - число от 36 до 100:"

        startKeyboard = None

    elif loc_type == 2117:
        text = "Сумма баллов: " + str(getAllPoints(vk_id, connect)) + "\n"
        text = text + choiceSpeciality(vk_id, connect)
        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Понятно. Продолжим!", color="primary")],
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 2118:
        text = "Хотите узнать подробней о направлениях или стоимости обучения?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Подробнее о направлениях", color="primary")],
                [getButton("Подробнее о стоимости обучения", color="primary")],
                [getButton("Не хочу", color="negative")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 2122:
        text = "Информация о стоимости обучения:\nhttp://welcome.vstu.ru/acceptance/platnoe-obrazovanie/ \nВам что-то еще хотелось бы узнать?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Подробнее о направлениях", color="primary")],
                [getButton("Да", color="positive")],
                [getButton("Нет, я уже узнал все что хотел", color="negative")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 2121:
        text = "О каком направлении вы хотели бы узнать?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Программная инженерия", color="primary")],
                [getButton("Информатика и вычислительная техника", color="primary")],
                [getButton("Физика", color="primary")],
                [getButton("Приборостроение", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 2131:
        text = "Программная инженерия:\nhttp://welcome.vstu.ru/specialty-choice/vse-spetsialnosti/programmnaya-inzheneriya/\nВам что-то еще хотелось бы узнать?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Понятно. Продолжим!", color="primary")],
                [getButton("Подробнее о стоимости обучения", color="primary")],
                [getButton("Назад", color="secondary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 2132:
        text = "Существует три поднаправления на этом направлении.\nАвтоматизированное проектирование киберфизических систем:\nhttp://welcome.vstu.ru/specialty-choice/vse-spetsialnosti/avtomatizirovannoe-proektirovanie-kiberfizicheskih-sistem/\nВычислительные машины, комплексы, системы и сети:\nhttp://welcome.vstu.ru/specialty-choice/vse-spetsialnosti/vychislitelnye-mashiny-kompleksy-sistemy-i-seti/\nСистемная инженерия:\nhttp://welcome.vstu.ru/specialty-choice/vse-spetsialnosti/sistemnaya-inzheneriya/\nВам что-то еще хотелось бы узнать?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Понятно. Продолжим!", color="primary")],
                [getButton("Подробнее о стоимости обучения", color="primary")],
                [getButton("Назад", color="secondary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 2133:
        text = "Физика:\nhttp://welcome.vstu.ru/specialty-choice/vse-spetsialnosti/fizika/\nВам что-то еще хотелось бы узнать?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Понятно. Продолжим!", color="primary")],
                [getButton("Подробнее о стоимости обучения", color="primary")],
                [getButton("Назад", color="secondary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 2134:
        text = "Приборостроение:\nhttp://welcome.vstu.ru/specialty-choice/vse-spetsialnosti/priborostroenie/\nВам что-то еще хотелось бы узнать?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Понятно. Продолжим!", color="primary")],
                [getButton("Подробнее о стоимости обучения", color="primary")],
                [getButton("Назад", color="secondary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 2141:
        text = "Вам бы хотелось узнать что-то еще?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Да", color="positive")],
                [getButton("Нет, я уже узнал все что хотел", color="negative")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))


    elif loc_type == 2151:
        text = "Нажмите на одну из кнопок, чтобы узнать интересующую вас информацию"

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
        text = "Документы для поступления:\nhttp://welcome.vstu.ru/acceptance/"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Назад", color="secondary")],
                [getButton("Информационный режим", color="secondary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 2162:
        text = "Сведения о льготах:\nhttp://welcome.vstu.ru/%D0%9F%D1%80%D0%B8%D0%B5%D0%BC%202020/1%20%D0%BE%D0%BA%D1%82%D1%8F%D0%B1%D1%80%D1%8F/04_4_Osobye%20prava.pdf"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Назад", color="secondary")],
                [getButton("Информационный режим", color="secondary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 2163:
        text = "Календарь абитуриента:\nhttp://welcome.vstu.ru/acceptance/kalendar-abiturienta/"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Назад", color="secondary")],
                [getButton("Информационный режим", color="secondary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 2164:
        text = "Общежитие:\nhttp://welcome.vstu.ru/%D0%9F%D1%80%D0%B8%D0%B5%D0%BC%202020/1%20%D0%BE%D0%BA%D1%82%D1%8F%D0%B1%D1%80%D1%8F/18_Obchaga.pdf"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Назад", color="secondary")],
                [getButton("Информационный режим", color="secondary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))
    
    elif loc_type == 1447:
        text = "Информация о довузовской подготовке:\nhttp://welcome.vstu.ru/preparation/\nВы собираетесь сдавать вступительные экзамены или вы сдавали ЕГЭ?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Информация о вступительных испытаниях", color="primary")],
                [getButton("Я сдавал ЕГЭ по проф. матем. и по физике", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 4117:
        text = "Вы собираетесь сдавать вступительные экзамены или вы сдавали ЕГЭ?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Информация о вступительных испытаниях", color="primary")],
                [getButton("Я сдавал ЕГЭ по проф. матем. и по физике", color="primary")]
            ]
        }

        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 40:
        text = "Вас интересует информация о довузовской подготовке?"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Да", color="positive")],
                [getButton("Нет", color="negative")]
            ]
        }
        
        startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
        startKeyboard = str(startKeyboard.decode("utf-8"))

    elif loc_type == 2165:
        text = "Количество мест:\nhttp://welcome.vstu.ru/acceptance/Abitur/#kolmest"

        startKeyboard = {
            "one_time": True,
            "buttons": [
                [getButton("Назад", color="secondary")],
                [getButton("Информационный режим", color="secondary")]
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
