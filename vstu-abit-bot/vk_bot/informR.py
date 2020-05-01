from vk_api.longpoll import VkLongPoll, VkEventType
import json
import time


def getButton(label, color, payload=''):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }


def testdef(vk, longpoll, event, inID = ""):
    flag = 0
    a = "0"
    transitionFlag = 0.0
    startKeyboard = {
        "one_time": True,
        "buttons": [
            [getButton("Информационный режим", color="primary")]#,
         #   [getButton("Интерактивный режим", color="primary")]
        ]
    }

    startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
    startKeyboard = str(startKeyboard.decode("utf-8"))

    informKeyboard = {
        "one_time": True,
        "buttons": [
            [getButton("Об университете", color="primary")],
            [getButton("Абитуриентам", color="primary")],
            #[getButton("Наиболее популярные вопросы", color="primary")],
            [
                getButton("Интерактивный режим", color="secondary")
            ]
        ]
    }

    informKeyboard = json.dumps(informKeyboard, ensure_ascii=False).encode("utf-8")
    informKeyboard = str(informKeyboard.decode("utf-8"))

    universityKeyboard = {
        "one_time": True,
        "buttons": [
            [getButton("Направления", color="primary")],
            [getButton("Подробнее об университете", color="primary")],
            [getButton("Контакты и структура", color="primary")],
            [
                getButton("Назад", color="secondary"),
                getButton("Интерактивный режим", color="secondary")
            ]
        ]
    }

    universityKeyboard = json.dumps(universityKeyboard, ensure_ascii=False).encode("utf-8")
    universityKeyboard = str(universityKeyboard.decode("utf-8"))

    abbKeyboard = {
        "one_time": True,
        "buttons": [
            [getButton("Проходные баллы прошлых лет", color="primary")],
            [getButton("Индивидуальные достижения", color="primary")],
            [
                getButton("Документы для поступления", color="primary"),
                getButton("Сведения о льготах", color="primary")
            ],
            [
                getButton("Стоимость обучения", color="primary"),
                getButton("Подготовка к поступлению", color="primary")
            ],
            [
                getButton("Общежитие", color="primary"),
                getButton("Календарь абитуриента", color="primary")
            ],
            [getButton("Количество мест", color="primary")],
            [getButton("Вступительные испытания", color="primary")],
            [
                getButton("Назад", color="secondary"),
                getButton("Интерактивный режим", color="secondary")
            ]
        ]
    }

    abbKeyboard = json.dumps(abbKeyboard, ensure_ascii=False).encode("utf-8")
    abbKeyboard = str(abbKeyboard.decode("utf-8"))

    naprKeyboard = {
        "one_time": True,
        "buttons": [
            [getButton("Информатика и вычислительная техника", color="primary")],
            [getButton("Программная инженерия", color="primary")],
            [getButton("Физика", color="primary")],
            [getButton("Приборостроение", color="primary")],
            [
                getButton("Назад", color="secondary"),
                getButton("Интерактивный режим", color="secondary")
            ]
        ]
    }

    naprKeyboard = json.dumps(naprKeyboard, ensure_ascii=False).encode("utf-8")
    naprKeyboard = str(naprKeyboard.decode("utf-8"))

    #longpoll = VkLongPoll(vk)
    if inID == "":
        vk.method("messages.send",
                  {"peer_id": event.peer_id, "message": "Нажмите на одну из кнопок, чтобы узнать интересующую вас\n"
                                                        "информацию",
                   "random_id": 0, "keyboard": informKeyboard})
    elif inID == "start":
        vk.method("messages.send", {"peer_id": event.peer_id, "message": "Нажмите на одну из кнопок, чтобы узнать интересующую вас\n"
                                                                         "информацию",
                                    "random_id": 0, "keyboard": informKeyboard})
    elif inID == "a":
        vk.method("messages.send",
                  {"peer_id": event.peer_id, "message": "Нажмите на одну из кнопок, чтобы узнать интересующую вас\n"
                                                        "информацию",
                   "random_id": 0, "keyboard": universityKeyboard})
    elif inID == "aa":
        vk.method("messages.send",
                  {"peer_id": event.peer_id, "message": "Какое направление вас интересует?",
                   "random_id": 0, "keyboard": naprKeyboard})
        transitionFlag = 113
    elif inID == "b":
        vk.method("messages.send",
                  {"peer_id": event.peer_id, "message": "Стоимость обучения:\n"
                                                        "http://welcome.vstu.ru/acceptance/platnoe-obrazovanie/",
                   "random_id": 0, "keyboard": abbKeyboard})
        transitionFlag = 12

    while flag == 0:
        for event in longpoll.listen():
            if event.to_me:
                if event.type == VkEventType.MESSAGE_NEW:
                    if event.text.lower() == "0":
                        vk.method("messages.send",
                                                {"peer_id": event.peer_id, "message": "Какая информация вас интересует?",
                                                 "random_id": 0, "keyboard": informKeyboard})
                    #if event.text.lower() == "старт":
                    #    vk.method("messages.send",
                    #              {"peer_id": event.peer_id, "message": "Выберите необходимый режим работы",
                    #               "random_id": 0, "keyboard": startKeyboard})

                    elif "Информационный режим" in event.text:
                        vk.method("messages.send", {"peer_id": event.peer_id, "message": "Нажмите на одну из кнопок, чтобы узнать интересующую вас\n"
                                                                                         "информацию",
                                                    "random_id": 0, "keyboard": informKeyboard})

                    elif "Об университете" in event.text:
                        vk.method("messages.send",
                                  {"peer_id": event.peer_id, "message": "Какая информация вас интересует?",
                                   "random_id": 0, "keyboard": universityKeyboard})
                        transitionFlag = 11

                    elif "Абитуриентам" in event.text:
                        vk.method("messages.send",
                                  {"peer_id": event.peer_id, "message": "Какая информация вас интересует?",
                                   "random_id": 0, "keyboard": abbKeyboard})
                        transitionFlag = 12

                    elif "Наиболее популярные вопросы" in event.text:
                        vk.method("messages.send",
                                  {"peer_id": event.peer_id, "message": "Наиболее популярные вопросы:"
                                                            "\n У вас есть военная кафедра?"
                                                            "\n Нет"
                                                            "\n У вас есть стипендия?"
                                                            "\n Да",        
                                   "random_id": 0, "keyboard": informKeyboard})

                    elif "Подробнее об университете" in event.text:
                        vk.method("messages.send",
                                  {"peer_id": event.peer_id, "message": "Информация об университете: "
                                                                        "\n http://www.vstu.ru/university/", "random_id": 0,
                                   "keyboard": universityKeyboard})

                    elif "Контакты и структура" in event.text:
                        vk.method("messages.send",
                                  {"peer_id": event.peer_id, "message": "Контакты:"
                                                                        "\n http://welcome.vstu.ru/contact/"
                                                                        "\n Структура:"
                                                                        "\n http://www.vstu.ru/university/structure/",
                                   "random_id": 0, "keyboard": universityKeyboard})

                    elif "Направления" in event.text:
                        vk.method("messages.send",
                                  {"peer_id": event.peer_id, "message": "Какое направление вас интересует?",
                                   "random_id": 0, "keyboard": naprKeyboard})
                        transitionFlag = 113

                    elif "Информатика и вычислительная техника" in event.text:
                        vk.method("messages.send",
                                  {"peer_id": event.peer_id, "message": "Существует три поднаправления на этом "
                                                                        "направлении\n"
                                                                        "Автоматизированное проектирование "
                                                                        "киберфизических систем\n"
                                                                        "http://welcome.vstu.ru/specialty-choice/vse-spetsialnosti/avtomatizirovannoe-proektirovanie-kiberfizicheskih-sistem/\n"
                                                                        "Вычислительные машины, комплексы, системы и "
                                                                        "сети\n"
                                                                        "http://welcome.vstu.ru/specialty-choice/vse-spetsialnosti/vychislitelnye-mashiny-kompleksy-sistemy-i-seti/\n"
                                                                        "Системная инженерия\n"
                                                                        "http://welcome.vstu.ru/specialty-choice/vse-spetsialnosti/sistemnaya-inzheneriya/",
                                   "random_id": 0, "keyboard": naprKeyboard})
                        transitionFlag = 1131

                    elif "Программная инженерия" in event.text:
                        vk.method("messages.send",
                                  {"peer_id": event.peer_id, "message": "Направление \"Программная инженерия\":\n"
                                                                        "http://welcome.vstu.ru/specialty-choice/vse-spetsialnosti/programmnaya-inzheneriya/ ",
                                   "random_id": 0, "keyboard": naprKeyboard})
                        transitionFlag = 1132

                    elif "Физика" in event.text:
                        vk.method("messages.send",
                                  {"peer_id": event.peer_id, "message": "Направление \"Физика\":\n"
                                                                        "http://welcome.vstu.ru/specialty-choice/vse-spetsialnosti/fizika/",
                                   "random_id": 0, "keyboard": naprKeyboard})
                        transitionFlag = 1133

                    elif "Приборостроение" in event.text:
                        vk.method("messages.send",
                                  {"peer_id": event.peer_id, "message": "Направление \"Приборостроение\":\n"
                                                                        "http://welcome.vstu.ru/specialty-choice/vse-spetsialnosti/priborostroenie/",
                                   "random_id": 0, "keyboard": naprKeyboard})
                        transitionFlag = 1134

                    elif "Проходные баллы прошлых лет" in event.text:
                        vk.method("messages.send",
                                  {"peer_id": event.peer_id, "message": "Проходные баллы прошлых лет на направлениях факультета:\n"
                                                                        "http://welcome.vstu.ru/acceptance/statistika-priyema/",
                                   "random_id": 0, "keyboard": abbKeyboard})

                    elif "Индивидуальные достижения" in event.text:
                        vk.method("messages.send",
                                  {"peer_id": event.peer_id, "message": "Индивидуальные достижения:\n"
                                                                        "http://welcome.vstu.ru/%D0%9F%D1%80%D0%B8%D0%B5%D0%BC%202020/1%20%D0%BE%D0%BA%D1%82%D1%8F%D0%B1%D1%80%D1%8F/07_ID.pdf",
                                   "random_id": 0, "keyboard": abbKeyboard})

                    elif "Документы для поступления" in event.text:
                        vk.method("messages.send",
                                  {"peer_id": event.peer_id, "message": "Документы для поступления:\n"
                                                                        "http://welcome.vstu.ru/acceptance/",
                                   "random_id": 0, "keyboard": abbKeyboard})

                    elif "Сведения о льготах" in event.text:
                        vk.method("messages.send",
                                  {"peer_id": event.peer_id, "message": "Сведения о льготах:\n"
                                                                        "http://welcome.vstu.ru/%D0%9F%D1%80%D0%B8%D0%B5%D0%BC%202020/1%20%D0%BE%D0%BA%D1%82%D1%8F%D0%B1%D1%80%D1%8F/04_4_Osobye%20prava.pdf",
                                   "random_id": 0, "keyboard": abbKeyboard})

                    elif "Стоимость обучения" in event.text:
                        vk.method("messages.send",
                                  {"peer_id": event.peer_id, "message": "Стоимость обучения:\n"
                                                                        "http://welcome.vstu.ru/acceptance/platnoe-obrazovanie/",
                                   "random_id": 0, "keyboard": abbKeyboard})

                    elif "Подготовка к поступлению" in event.text:
                        vk.method("messages.send",
                                  {"peer_id": event.peer_id, "message": "Подготовка к поступлению:\n"
                                                                        "http://welcome.vstu.ru/preparation/",
                                   "random_id": 0, "keyboard": abbKeyboard})

                    elif "Общежитие" in event.text:
                        vk.method("messages.send",
                                  {"peer_id": event.peer_id, "message": "Общежитие:\n"
                                                                        "http://welcome.vstu.ru/%D0%9F%D1%80%D0%B8%D0%B5%D0%BC%202020/1%20%D0%BE%D0%BA%D1%82%D1%8F%D0%B1%D1%80%D1%8F/18_Obchaga.pdf",
                                   "random_id": 0, "keyboard": abbKeyboard})

                    elif "Календарь абитуриента" in event.text:
                        vk.method("messages.send",
                                  {"peer_id": event.peer_id, "message": "Календарь абитуриента:\n"
                                                                        "http://welcome.vstu.ru/acceptance/kalendar-abiturienta/",
                                   "random_id": 0, "keyboard": abbKeyboard})

                    elif "Количество мест" in event.text:
                        vk.method("messages.send",
                                  {"peer_id": event.peer_id, "message": "Количество мест:\n"
                                                                        "http://welcome.vstu.ru/acceptance/Abitur/#kolmest",
                                   "random_id": 0, "keyboard": abbKeyboard})

                    elif "Вступительные испытания" in event.text:
                        vk.method("messages.send",
                                  {"peer_id": event.peer_id, "message": "Вступительные испытания:\n"
                                                                        "http://welcome.vstu.ru/acceptance/vstupitelnye-ispytaniya/",
                                   "random_id": 0, "keyboard": abbKeyboard})

                    elif "Интерактивный режим" in event.text:
                        return 1

                    elif "Назад" in event.text:
                        if transitionFlag == 0:
                            vk.method("messages.send",
                                      {"peer_id": event.peer_id, "message": "Нажмите на одну из кнопок, чтобы узнать интересующую вас\n"
                                                                            "информацию",
                                       "random_id": 0, "keyboard": informKeyboard})
                        if 10 < transitionFlag < 20:
                            vk.method("messages.send",
                                      {"peer_id": event.peer_id, "message": "Нажмите на одну из кнопок, чтобы узнать интересующую вас\n"
                                                                            "информацию",
                                       "random_id": 0, "keyboard": informKeyboard})
                            transitionFlag = 0

                        if 110 < transitionFlag < 120:
                            vk.method("messages.send",
                                      {"peer_id": event.peer_id, "message": "Нажмите на одну из кнопок, чтобы узнать интересующую вас\n"
                                                                            "информацию",
                                       "random_id": 0, "keyboard": universityKeyboard})
                            transitionFlag = 11


                        if 1130 < transitionFlag < 1140:
                            vk.method("messages.send",
                                      {"peer_id": event.peer_id, "message": "Нажмите на одну из кнопок, чтобы узнать интересующую вас\n"
                                                                            "информацию",
                                       "random_id": 0, "keyboard": universityKeyboard})
                            transitionFlag = 113
                    else:
                        if transitionFlag == 0:
                            vk.method("messages.send",
                                      {"peer_id": event.peer_id, "message": "Я вас не понимаю.\n"
                                                                            "Нажмите на одну из кнопок, чтобы узнать интересующую вас\n"
                                                                            "информацию",
                                       "random_id": 0, "keyboard": informKeyboard})
                        if 10 < transitionFlag < 20:
                            vk.method("messages.send",
                                      {"peer_id": event.peer_id, "message": "Я вас не понимаю.\n"
                                                                            "Нажмите на одну из кнопок, чтобы узнать интересующую вас\n"
                                                                            "информацию",
                                       "random_id": 0, "keyboard": informKeyboard})
                            transitionFlag = 0

                        if 110 < transitionFlag < 120:
                            vk.method("messages.send",
                                      {"peer_id": event.peer_id, "message": "Я вас не понимаю.\n"
                                                                            "Нажмите на одну из кнопок, чтобы узнать интересующую вас\n"
                                                                            "информацию",
                                       "random_id": 0, "keyboard": universityKeyboard})
                            transitionFlag = 11

                        if 1130 < transitionFlag < 1140:
                            vk.method("messages.send",
                                      {"peer_id": event.peer_id, "message": "Я вас не понимаю.\n"
                                                                            "Какое направление вас интересует?",
                                       "random_id": 0, "keyboard": universityKeyboard})
                            transitionFlag = 113
                        time.sleep(1)

