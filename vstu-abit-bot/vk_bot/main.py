import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from config import *
from functions import *
from dbConnect import *
from db import *

# Объявление vk
vk = vk_api.VkApi(token=vk_api_token)

vk._auth_token()
vk.get_api()


# Подключаемся к БД
connect = getConnection()

# Объявляем longpool
longpoll = VkLongPoll(vk)

inID = ""
flag = 0

# Условие продолжения работы
while True:
    for event in longpoll.listen():
        if event.to_me:
            if event.type == VkEventType.MESSAGE_NEW:
                # Передать переменной сообщение пользователя в нижнем регистре
                message = event.text
                # Передать переменной идентификатор собеседника
                vk_id = event.peer_id
                # Подготовить SQL запрос для получения информации о пользователе
                messageDbBot = """select * from user where id = %s;"""
                try:
                    with connect.cursor() as cursor:
                        # Передать SQL запрос БД
                        cursor.execute(messageDbBot, str(vk_id))
                        # Передать информацию о пользователе переменной
                        loc = cursor.fetchall()
                        if len(loc) == 0:
                            add_user(vk_id, None, None, 501, 501, connect=connect)
                            new_loc = 501
                            loc = new_loc
                        else:
                            # Получить позицию пользователя
                            loc = loc[0]["position"]
                            # Вычислить новую позицию пользователя и среагировать на сообщение
                            new_loc = nextNode(loc, message, connect, vk_id)
                        # Вычислить сообщения для отправки пользователю
                        new_mess = newMess(new_loc,vk_id,connect)
                        # Обновить позицию пользователя
                        user_update_position( vk_id, new_loc, connect)
                        # Если значения прежней позиции и новой не совпадают
                        if loc != new_loc:
                            # Обновить прежнюю позицию
                            user_update_old_position(vk_id, loc, connect)
                        # Отправить пользователю сообщение
                        if new_mess[1] is not None:
                            vk.method("messages.send",
                                      {"peer_id": event.peer_id, "message": new_mess[0],
                                       "random_id": 0, "keyboard": new_mess[1]})
                        else:
                            vk.method("messages.send",
                                      {"peer_id": event.peer_id, "message": new_mess[0],
                                       "random_id": 0})
                # В случае неудачи оповестить об ошибке
                except:
                    vk.method("messages.send",
                              {"peer_id": event.peer_id, "message": "Ошибка",
                               "random_id": 0})
connect.close()


