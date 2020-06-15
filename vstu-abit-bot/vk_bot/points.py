def sumEgePoints(vk_id, connect):
    """
    Подсчет баллов ЕГЭ пользователя
    :param vk_id: идентификатор пользователя в вк
    :param connect: соединение с БД
    """
    sumP = 0
    # Подготавливаем SQL запросы для передачи их базе данных
    bdSelectExam1 = """select * from exam where id_user = %s and name = \"Математика\";"""
    bdSelectExam2 = """select * from exam where id_user = %s and name = \"Физика\";"""
    bdSelectExam3 = """select * from exam where id_user = %s and name = \"Русский\";"""
    bdSelectUser = """select * from user where id = %s;"""
    updateUserPoints = """update user set ege_points = %s where id = %s;"""

    # Передаем запросы на добавление элемента и фиксируем в БД
    try:
        with connect.cursor() as cursor:
            cursor.execute(bdSelectExam1, str(vk_id))
            sumP = sumP + cursor.fetchall()[0]["points"]
            cursor.execute(bdSelectExam2, str(vk_id))
            sumP = sumP + cursor.fetchall()[0]["points"]
            cursor.execute(bdSelectExam3, str(vk_id))
            sumP = sumP + cursor.fetchall()[0]["points"]
            cursor.execute(bdSelectUser, str(vk_id))
            sumP = sumP + cursor.fetchall()[0]["ege_points"]
            cursor.execute(updateUserPoints, (str(sumP), vk_id))
            connect.commit()
    # В случае неудачи оповещаем об ошибке
    except:
        print("Ошибка в подсчете баллов ЕГЭ")


def sumAchPoints(vk_id, connect):
    """
    Подсчет баллов за индивидуальные достижения пользователя
    :param vk_id: идентификатор пользователя в вк
    :param connect: соединение с БД
    :return:
    """
    sumP = 0
    storePoints = 0
    # Подготавливаем SQL запросы для передачи их базе данных
    bdSelectAch1 = """select * from achievement where id_user = %s and name = %s;"""
    bdSelectAch2 = """select * from achievement where id_user = %s and name = %s;"""
    bdSelectAch3 = """select * from achievement where id_user = %s and name = %s;"""
    bdSelectUser = """select * from user where id = %s;"""
    updateUserPoints = """update user set ege_points = %s where id = %s;"""

    # Передаем запросы на добавление элемента и фиксируем в БД
    try:
        with connect.cursor() as cursor:
            cursor.execute(bdSelectAch1, (str(vk_id),"Золотая медаль"))
            storePoints = cursor.fetchall()
            if len(storePoints) > 0:
                sumP = sumP + storePoints[0]["points"]
            cursor.execute(bdSelectAch2, (str(vk_id),"Диплом"))
            storePoints = cursor.fetchall()
            if len(storePoints) > 0:
                sumP = sumP + storePoints[0]["points"]
            cursor.execute(bdSelectAch3, (str(vk_id),"ГТО"))
            storePoints = cursor.fetchall()
            if len(storePoints) > 0:
                sumP = sumP + storePoints[0]["points"]
            cursor.execute(bdSelectUser, str(vk_id))
            sumP = sumP + cursor.fetchall()[0]["ege_points"]
            cursor.execute(updateUserPoints, (str(sumP), vk_id))
            connect.commit()
    # В случае неудачи оповещаем об ошибке
    except:
        print("Ошибка в подсчете баллов за индивидуальные достижения")


def deleteAllPoints(vk_id, connect):
    """
    Удалить все баллы пользователя
    :param vk_id: идентификатор пользователя в вк
    :param connect: соединение с БД
    :return:
    """
    # Подготавливаем SQL запросы для передачи их базе данных
    deleteAch = """delete from achievement where id_user = %s;"""
    deleteEx = """delete from exam where id_user = %s;"""
    updatePoints = """update user set ege_points = 0 where id = %s;"""

    # Передаем запросы на добавление элемента и фиксируем в БД
    try:
        with connect.cursor() as cursor:
            cursor.execute(deleteAch, str(vk_id))
            cursor.execute(deleteEx, str(vk_id))
            cursor.execute(updatePoints, str(vk_id))
            connect.commit()
    # В случае неудачи оповещаем об ошибке
    except:
        print("Ошибка при удалении баллов")


def getAllPoints(vk_id, connect):
    """
    Получить все баллы пользователя
    :param vk_id: идентификатор пользователя в вк
    :param connect: соединение с БД
    :return: вернуть все баллы пользователя
    """
    points = 0
    # Подготавливаем SQL запрос для передачи его базе данных
    selectDB = """select * from user where id = %s"""

    # Передаем запрос на добавление элемента и фиксируем в БД
    try:
        with connect.cursor() as cursor:
            cursor.execute(selectDB, str(vk_id))
            points = cursor.fetchall()[0]["ege_points"]
    # В случае неудачи оповещаем об ошибке
    except:
        print("Ошибка при получении баллов ЕГЭ")
    return int(points)

def maxPointsSpeciality(connect):
    """
    Получить максимальный проходной балл среди всех направлений
    :param connect: соединение с БД
    :return: максимальный проходной балл среди всех направлений
    """
    maxPoints = 0
    # Подготавливаем SQL запрос для передачи его базе данных
    selectDB = """select max(min_points) from speciality;"""
    try:
        with connect.cursor() as cursor:
            cursor.execute(selectDB)
            maxPoints = cursor.fetchall()[0]["max(min_points)"]
    # В случае неудачи оповещаем об ошибке
    except:
        print("Ошибка при получении проходных баллов")
    return int(maxPoints)

def choiceSpeciality(vk_id, connect):
    """
    Определить по баллам пользователя на какой основе он может обучаться
    :param vk_id: идентификатор пользователя в вк
    :param connect: соединение с БД
    :return: вернуть текст
    """
    # Подготавливаем SQL запрос для передачи его базе данных
    selectDB = """select * from speciality"""
    allPoints = getAllPoints(vk_id, connect)
    budgetList = []
    contractList = []
    text = ""
    # Передаем запрос на добавление элемента и фиксируем в БД
    try:
        with connect.cursor() as cursor:
            cursor.execute(selectDB)
            spec = cursor.fetchall()
            for i in range(len(spec)):
                if allPoints >= spec[i]["min_points"]:
                    budgetList.append(spec[i]["name"])
                else:
                    contractList.append(spec[i]["name"])
            # Записываем в сообщение сумму баллов
            #text = "Сумма: " + str(allPoints)
            # Если сумма баллов больше, чем максимум баллов среди направлений
            if len(contractList) == 0:
                text = text + "\nОсновываясь на данных приемной комиссии за прошлый год, вы можете поступить на нашем " \
                                    "факультете на все направления на бюджетной основе"
            # Если сумма баллов меньше, чем минимум баллов среди направлений
            elif len(budgetList) == 0:
                text = text + "\nОсновываясь на данных приемной комиссии за прошлый год, вы можете поступить на наш " \
                                    "факультет только на контрактной основе"
            else:
                text = text + "\nОсновываясь на данных приемной комиссии за прошлый год, вы можете поступить на нашем " \
                                    "факультете на следующие направления на бюджетной основе:"
                # Для всех направлений
                # Сравниваем сумму баллов со значениями направлений
                # Для распределений на бюджетные и контрактные основы
                for i in range(len(budgetList)):
                    text = text + "\n" + budgetList[i]
                text = text + "\n\nНа контрактной основе:"
                for i in range(len(contractList)):
                    text = text + "\n" + contractList[i]

            return text
    # В случае неудачи оповещаем об ошибке
    except:
        print("Ошибка при получении данных для выбора доступных направлений")