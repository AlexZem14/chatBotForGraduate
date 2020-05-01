from informR import getButton
from vk_api.longpoll import VkEventType
import time
import json


# Функция для выбора доступных направлений на ФЭВТ
# sumPoints - кол-во набранных абитуриентам баллов
# return - sumVivod Сообщение о возможностях поступления
# return - minPoints Минимальные баллы для поступления
# return - maxPoints Максимальные баллы для поступления
def choiceOfDirection(sumPoints):
    minPoints = 0
    maxPoints = 0
    flag = 0
    # Массив напралений и баллов
    directions = [
        ["Программная инженерия", 235],
        ["Информатика и вычислительная техника", 204],
        ["Приборостроение", 178],
        ["Физика", 175]
    ]

    # Для всех направлений
    for i in range(len(directions)):
        # Если начали с первого направления
        if i == 0:
            # То устанавливливаем его баллы для максимума и минимума
            maxPoints = directions[i][1]
            minPoints = maxPoints
        # Иначе
        else:
            # Если баллы данного факультета больше максимальных баллов
            if directions[i][1] > maxPoints:
                # То записываем баллы данного факультета в максимум
                maxPoints = directions[i][1]
            # Если баллы данного факультета меньше минимальных баллов
            if directions[i][1] < minPoints:
                # То записываем баллы данного факультета в минимум
                minPoints = directions[i][1]

    # Записываем в сообщение сумму баллов
    sumVivod = "Сумма: " + str(sumPoints)
    # Если сумма баллов больше, чем максимум баллов среди направлений
    if sumPoints > maxPoints:
        sumVivod = sumVivod + "\nОсновываясь на данных приемной комиссии за прошлый год, вы можете поступить на нашем " \
                              "факультете на все направления на бюджетной основе"
    # Если сумма баллов меньше, чем минимум баллов среди направлений
    elif sumPoints < minPoints:
        sumVivod = sumVivod + "\nОсновываясь на данных приемной комиссии за прошлый год, вы можете поступить на наш " \
                              "факультет только на контрактной основе"
    else:
        sumVivod = sumVivod + "\nОсновываясь на данных приемной комиссии за прошлый год, вы можете поступить на нашем " \
                              "факультете на следующие направления на бюджетной основе:"
        # Для всех направлений
        # Сравниваем сумму баллов со значениями направлений
        # Для распределений на бюджетные и контрактные основы
        for i in range(len(directions)):
            if directions[i][1] <= sumPoints:
                sumVivod = sumVivod + "\n" + directions[i][0]
        for i in range(len(directions)):
            if flag == 0:
                sumVivod = sumVivod + "\nНа контрактной основе:"
                flag = 1
            if directions[i][1] > sumPoints:
                sumVivod = sumVivod + "\n" + directions[i][0]

    return sumVivod, minPoints, maxPoints


# Функция для проверки введенных баллов абитуриентов по предметам
# stroka - переменная для введенных баллов
# minPoints - переменная для минимальных баллов
# return -  возвращает True, если баллы введены верно
#           возвращает False, если баллы введены неверно
def numberCheck(stroka, minPoints=0):
    # Строка чисел
    cfr = "0123456789"
    cfr10 = "123456789"
    # Если введенная строка длинее 3 символов или не имеет символов
    if len(stroka) > 3 or len(stroka) == 0:
        return False
    # Если введенная строка 3 символа в длину
    elif len(stroka) == 3:
        # Если введенная строка не равна 100
        if stroka != "100":
            return False
        else:
            return True
    # Если введенная строка длиннее 1 символа
    elif len(stroka) > 1:
        # Для всех цифр кроме 0
        for i in range(len(cfr10)):
            # Если цифра десяток введенной строки есть цифра
            if stroka[0] == cfr10[i]:
                # Для всех цифр
                for j in range(len(cfr)):
                    # Если цифра введенной строки есть цифра
                    if stroka[1] == cfr[j]:
                        # Если введенное число не меньше минимума
                        if int(stroka) >= minPoints:
                            return True
                        else:
                            return False
        return False
    else:
        # Для всех цифр
        for j in range(len(cfr)):
            # Если цифра введенной строки есть цифра
            if stroka == cfr[j]:
                # Если введенное число не меньше минимума
                if int(stroka) >= minPoints:
                    return True
                else:
                    return False
        return False


# Функция для вычисления дополнительных баллов за индивидуальные достижения
def individAchievements(vk, longpoll, event):
    # Дополнитеьлные баллы
    dopPoints = 0
    flag = 0

    daNetKeyboard = {
        "one_time": True,
        "buttons": [
            [
                getButton("Да, у меня есть золотая медаль", color="positive"),
                getButton("Нет, у меня отсутствует золотая медаль", color="negative")
            ]
        ]
    }

    daNetKeyboard = json.dumps(daNetKeyboard, ensure_ascii=False).encode("utf-8")
    daNetKeyboard = str(daNetKeyboard.decode("utf-8"))

    daNet1Keyboard = {
        "one_time": True,
        "buttons": [
            [
                getButton("Да, у меня есть значок", color="positive"),
                getButton("Нет, у меня отсутствует значок", color="negative")
            ]
        ]
    }

    daNet1Keyboard = json.dumps(daNet1Keyboard, ensure_ascii=False).encode("utf-8")
    daNet1Keyboard = str(daNet1Keyboard.decode("utf-8"))

    # Вызываем начальную клавиатуру
    vk.method("messages.send",
              {"peer_id": event.peer_id, "message": "У вас есть аттестат с отличием (золотая медаль)?",
               "random_id": 0, "keyboard": daNetKeyboard})

    while True:
        for event in longpoll.listen():
            if event.to_me:
                if event.type == VkEventType.MESSAGE_NEW:
                    # Если у абитуриента есть золотая медаль
                    if "Да, у меня есть золотая медаль" in event.text:
                        # + 10 дополнительных баллов
                        dopPoints = dopPoints + 10
                        return dopPoints
                    # Если у абитуриента нет золотой медали
                    elif "Нет, у меня отсутствует золотая медаль" in event.text:
                        flag = 1
                        # Спрашиваем про значок ГТО
                        vk.method("messages.send",
                                  {"peer_id": event.peer_id,
                                   "message": "У вас есть золотой значок ГТО?",
                                   "random_id": 0, "keyboard": daNet1Keyboard})
                    # Если есть значок ГТО
                    elif "Да, у меня есть значок" in event.text:
                        # + 3 дополнительных балла
                        dopPoints = dopPoints + 3
                        return dopPoints
                    elif "Нет, у меня отсутствует значок" in event.text:
                        return dopPoints
                    else:
                        if flag == 0:
                            vk.method("messages.send",
                                        {"peer_id": event.peer_id,
                                        "message": "Я вас не понимаю. Нажмите на одну из кнопок ниже.\n "
                                                   "У вас есть аттестат с отличием (золотая медаль)?",
                                        "random_id": 0, "keyboard": daNetKeyboard})
                        else:
                            vk.method("messages.send",
                                        {"peer_id": event.peer_id,
                                        "message": "Я вас не понимаю. Нажмите на одну из кнопок ниже.\n "
                                                   "У вас есть золотой значок ГТО?",
                                        "random_id": 0, "keyboard": daNet1Keyboard})


def EGPoints(vk, longpoll, event):
    exam = 0
    sumPoints = 0
    flag = 0

    vk.method("messages.send",
              {"peer_id": event.peer_id, "message": "Введите баллы ЕГЭ, которые вы получили по профильной математике."
                                                    "\nВводимое значение - число от 27 до 100:",
               "random_id": 0})

    while flag == 0:
        for event in longpoll.listen():
            if event.to_me:
                if event.type == VkEventType.MESSAGE_NEW:
                    if exam == 0:
                        if numberCheck(event.text.lower(), 27) is True:
                            sumPoints = sumPoints + int(event.text.lower())
                            exam = exam + 1
                            vk.method("messages.send",
                                      {"peer_id": event.peer_id,
                                       "message": "Введите баллы ЕГЭ, которые вы получили по физике.\nВводимое значение"
                                                  " - число от 36 до 100:",
                                       "random_id": 0})
                        else:
                            vk.method("messages.send",
                                      {"peer_id": event.peer_id,
                                       "message": "Вы ввели некорректное значение. Повторите попытку."
                                                  "\nВводимое значение - число от 27 до 100:",
                                       "random_id": 0})
                    elif exam == 1:
                        if numberCheck(event.text.lower(), 36) is True:
                            sumPoints = sumPoints + int(event.text.lower())
                            exam = exam + 1
                            vk.method("messages.send",
                                      {"peer_id": event.peer_id,
                                       "message": "Введите баллы ЕГЭ, которые вы получили по русскому языку."
                                                  "\nВводимое значение - число от 36 до 100:",
                                       "random_id": 0})
                        else:
                            vk.method("messages.send",
                                      {"peer_id": event.peer_id,
                                       "message": "Вы ввели некорректное значение. Повторите попытку."
                                                  "\nВводимое значение - число от 36 до 100:",
                                       "random_id": 0})
                    elif exam == 2:
                        if numberCheck(event.text.lower(), 36) is True:
                            sumPoints = sumPoints + int(event.text.lower())
                            exam = exam + 1
                            return sumPoints
                        else:
                            vk.method("messages.send",
                                      {"peer_id": event.peer_id,
                                       "message": "Вы ввели некорректное значение. Повторите попытку."
                                                  "\nВводимое значение - число от 36 до 100:",                                   
                                       "random_id": 0})


# Функция для обработки интерактивного режима
def interactR(vk, longpoll, event):
    flag = 0
    pointsFlag = 0
    inID = ""
    outID = ""
    royal = 0

    daNetKeyboard = {
        "one_time": True,
        "buttons": [
            [
                getButton("Да", color="positive"),
                getButton("Нет", color="negative")
            ]
        ]
    }

    daNetKeyboard = json.dumps(daNetKeyboard, ensure_ascii=False).encode("utf-8")
    daNetKeyboard = str(daNetKeyboard.decode("utf-8"))

    budgetKeyboard = {
        "one_time": True,
        "buttons": [
            [getButton("Подробнее о направлениях", color="primary")],
            [getButton("Информационный режим", color="secondary")]
        ]
    }

    budgetKeyboard = json.dumps(budgetKeyboard, ensure_ascii=False).encode("utf-8")
    budgetKeyboard = str(budgetKeyboard.decode("utf-8"))

    contractKeyboard = {
        "one_time": True,
        "buttons": [
            [getButton("Подробнее о направлениях", color="primary")],
            [getButton("Подробнее о стоимости обучения", color="primary")],
            [getButton("Информационный режим", color="secondary")]
        ]
    }

    contractKeyboard = json.dumps(contractKeyboard, ensure_ascii=False).encode("utf-8")
    contractKeyboard = str(contractKeyboard.decode("utf-8"))

    sbrosKeyboard = {
        "one_time": True,
        "buttons": [
            [getButton("Назад", color="secondary")],
            [getButton("Информационный режим", color="secondary")]
        ]
    }

    sbrosKeyboard = json.dumps(sbrosKeyboard, ensure_ascii=False).encode("utf-8")
    sbrosKeyboard = str(sbrosKeyboard.decode("utf-8"))

    sbros1Keyboard = {
        "one_time": True,
        "buttons": [
            [getButton("Назад", color="secondary")],
            [getButton("Информационный режим", color="secondary")]
        ]
    }

    sbros1Keyboard = json.dumps(sbros1Keyboard, ensure_ascii=False).encode("utf-8")
    sbros1Keyboard = str(sbros1Keyboard.decode("utf-8"))

    vk.method("messages.send",
              {"peer_id": event.peer_id, "message": "Вы являетесь выпускником школы?",
               "random_id": 0, "keyboard": daNetKeyboard})

    while flag == 0:
        for event in longpoll.listen():
            if event.to_me:
                if event.type == VkEventType.MESSAGE_NEW:
                    if "Да" in event.text or royal == 1:
                        if royal == 0:
                            event.text = ""
                            vk.method("messages.send",
                                      {"peer_id": event.peer_id, "message": "Вы сдавали в качестве экзаменов ЕГЭ профильную \n"
                                                                            "математику и физику?",
                                       "random_id": 0, "keyboard": daNetKeyboard})
                        if "Да" in event.text and royal == 1:
                            ############################################################
                            event.text = ""
                            dopPints = individAchievements(vk, longpoll, event)
                            ############################################################
                            sumPoints = EGPoints(vk, longpoll, event)
                            sumPoints = sumPoints + dopPints
                            sumVivod, minPoints, maxPoints = choiceOfDirection(sumPoints)
                            if sumPoints >= maxPoints:
                                vk.method("messages.send",
                                          {"peer_id": event.peer_id, "message": sumVivod,
                                           "random_id": 0, "keyboard": budgetKeyboard})
                                royal = 0
                            elif sumPoints <= minPoints:
                                vk.method("messages.send",
                                          {"peer_id": event.peer_id, "message": sumVivod,
                                           "random_id": 0, "keyboard": contractKeyboard})
                                royal = 0
                            else:
                                vk.method("messages.send",
                                          {"peer_id": event.peer_id, "message": sumVivod,
                                           "random_id": 0, "keyboard": contractKeyboard})
                        elif "Нет" in event.text:
                            vk.method("messages.send",
                                      {"peer_id": event.peer_id,
                                       "message": "Извините, вам не подходит наш факультет", "random_id": 0,
                                       "keyboard": sbrosKeyboard})
                        elif "Назад" in event.text:
                            vk.method("messages.send",
                                      {"peer_id": event.peer_id, "message": "Вы сдавали в качестве экзаменов ЕГЭ профильную \n"
                                                                            "математику и физику?",
                                       "random_id": 0, "keyboard": daNetKeyboard})
                        elif "Информационный режим" in event.text:
                            inID = "start"
                            return inID
                        elif "Подробнее о направлениях" in event.text:
                            inID = "aa"
                            return inID
                        elif "Подробнее о стоимости обучения" in event.text:
                            inID = "b"
                            return inID
                        elif "Интерактивный режим" in event.text:
                            royal = 0
                            vk.method("messages.send",
                                      {"peer_id": event.peer_id, "message": "Вы являетесь выпускником школы?",
                                       "random_id": 0, "keyboard": daNetKeyboard})
                        else:
                            if royal != 0:
                                vk.method("messages.send",
                                          {"peer_id": event.peer_id, "message": "Я вас не понимаю. Нажмите на одну из кнопок ниже.\n"
                                                                                "Вы сдавали в качестве экзаменов ЕГЭ профильную \n"
                                                                                "математику и физику?",
                                           "random_id": 0, "keyboard": daNetKeyboard})
                            royal = 1

                    elif "Нет" in event.text:
                        vk.method("messages.send",
                                  {"peer_id": event.peer_id, "message": "Извините, в данной версии чат-бота доступен "
                                                                        "функционал только для выпускников школ",
                                   "random_id": 0, "keyboard": sbros1Keyboard})
                        #event.text = ""
                        #vk.method("messages.send",
                                  #{"peer_id": event.peer_id, "message": "Что вас интересует?",
                                   #"random_id": 0, "keyboard": sbros1Keyboard})
                    elif "Подробнее о направлениях" in event.text:
                        inID = "aa"
                        return inID
                    elif "Подробнее о стоимости обучения" in event.text:
                        inID = "b"
                        return inID
                    elif "Информационный режим" in event.text:
                        inID = "start"
                        return inID
                    elif "Назад" in event.text:
                        vk.method("messages.send",
                                  {"peer_id": event.peer_id, "message": "Вы являетесь выпускником школы?",
                                   "random_id": 0, "keyboard": daNetKeyboard})
                    else:
                        event.text = ""
                        vk.method("messages.send",
                                  {"peer_id": event.peer_id, "message": "Я вас не понимаю. Нажмите на одну из кнопок ниже.\n"
                                                                        "Вы являетесь выпускником школы?",
                                   "random_id": 0, "keyboard": daNetKeyboard})
