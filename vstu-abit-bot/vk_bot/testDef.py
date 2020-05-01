import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from interactR import interactR
# Для объявления клавиатуры, необходимо объявление JSON
import json
# Вызов моих функций
from informR import testdef
from informR import getButton

# Объявление vk
vk = vk_api.VkApi(token="f8212de39f245851308e939775829425b122217a207919f6ad1c7a87018059dd32bf90d3aed02db13e305")

vk._auth_token()
vk.get_api()

# Устройство клавиатуры
startKeyboard = {
    "one_time": True,
    "buttons": [
        [getButton("Информационный режим", color="primary")],
        [getButton("Интерактивный режим", color="primary")]
    ]
}

startKeyboard = json.dumps(startKeyboard, ensure_ascii=False).encode("utf-8")
startKeyboard = str(startKeyboard.decode("utf-8"))

# Объявляем longpool
longpoll = VkLongPoll(vk)

inID = ""
flag = 0

# Условие продолжения работы
while True:
    for event in longpoll.listen():
        if event.to_me:
            if event.type == VkEventType.MESSAGE_NEW:
                # Для запуска вводим "старт" или "привет"
                if event.text.lower() == "начать" or event.text.lower() == "привет":
                    vk.method("messages.send",
                              {"peer_id": event.peer_id, "message": "Выберите необходимый режим работы",
                               "random_id": 0, "keyboard": startKeyboard})
                    # Действия при выборе информационного режима
                elif "Информационный режим" in event.text:
                    while True:
                        if len(inID) == 0:
                            testdef(vk, longpoll, event)
                        inID = interactR(vk, longpoll, event)
                        if len(inID) != 0:
                            testdef(vk, longpoll, event, inID)
                    ''''''''''
                    # Вызов функции
                    testdef(vk, longpoll, event)
                    # Вызов клавиатуры обратно
                    #vk.method("messages.send",
                    #          {"peer_id": event.peer_id, "message": "Выберите необходимый режим работы",
                    #           "random_id": 0, "keyboard": startKeyboard})
                    inID = interactR(vk, longpoll, event)
                    if len(inID) == 0:
                        vk.method("messages.send",
                                  {"peer_id": event.peer_id, "message": "Выберите необходимый режим работы",
                                   "random_id": 0, "keyboard": startKeyboard})
                    else:
                        testdef(vk, longpoll, event, inID)
                    '''''
                elif "Интерактивный режим" in event.text:
                    while True:
                        inID = interactR(vk, longpoll, event)
                        if len(inID) != 0:
                            testdef(vk, longpoll, event, inID)
                        else:
                            flag = 0
                    '''''''''
                    inID = interactR(vk, longpoll, event)
                    if len(inID) == 0:
                        vk.method("messages.send",
                                  {"peer_id": event.peer_id, "message": "Выберите необходимый режим работы",
                                   "random_id": 0, "keyboard": startKeyboard})
                    else:
                        testdef(vk, longpoll, event, inID)
                        inID = interactR(vk, longpoll, event)
                        if len(inID) == 0:
                            vk.method("messages.send",
                                      {"peer_id": event.peer_id, "message": "Выберите необходимый режим работы",
                                       "random_id": 0, "keyboard": startKeyboard})
                        else:
                            testdef(vk, longpoll, event, inID)
                    '''
                else:
                    vk.method("messages.send",
                              {"peer_id": event.peer_id, "message": "Я вас не понимаю.",
                               "random_id": 0})
                    vk.method("messages.send",
                              {"peer_id": event.peer_id, "message": "Выберите необходимый режим работы",
                               "random_id": 0, "keyboard": startKeyboard})
