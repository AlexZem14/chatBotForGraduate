def sumEgePoints(vk_id, connect):
    sumP = 0
    bdSelectExam1 = """select * from exam where id_user = %s and name = \"Математика\";"""
    bdSelectExam2 = """select * from exam where id_user = %s and name = \"Физика\";"""
    bdSelectExam3 = """select * from exam where id_user = %s and name = \"Русский\";"""
    bdSelectUser = """select * from user where id = %s;"""
    updateUserPoints = """update user set ege_points = %s where id = %s;"""

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
    except:
        print("Ошибка в подсчете баллов ЕГЭ")


def sumAchPoints(vk_id, connect):
    sumP = 0
    storePoints = 0
    bdSelectExam1 = """select * from achievement where id_user = %s and name = %s;"""
    bdSelectExam2 = """select * from achievement where id_user = %s and name = %s;"""
    bdSelectExam3 = """select * from achievement where id_user = %s and name = %s;"""
    bdSelectUser = """select * from user where id = %s;"""
    updateUserPoints = """update user set ege_points = %s where id = %s;"""
    try:
        with connect.cursor() as cursor:
            cursor.execute(bdSelectExam1, (str(vk_id),"Золотая медаль"))
            storePoints = cursor.fetchall()
            if len(storePoints) > 0:
                sumP = sumP + storePoints[0]["points"]
            cursor.execute(bdSelectExam2, (str(vk_id),"Диплом"))
            storePoints = cursor.fetchall()
            if len(storePoints) > 0:
                sumP = sumP + storePoints[0]["points"]
            cursor.execute(bdSelectExam3, (str(vk_id),"ГТО"))
            storePoints = cursor.fetchall()
            if len(storePoints) > 0:
                sumP = sumP + storePoints[0]["points"]
            cursor.execute(bdSelectUser, str(vk_id))
            sumP = sumP + cursor.fetchall()[0]["ege_points"]
            cursor.execute(updateUserPoints, (str(sumP), vk_id))
            connect.commit()
    except:
        print("Ошибка в подсчете баллов за индивидуальные достижения")


def deleteAllPoints(vk_id, connect):
    deleteAch = """delete from achievement where id_user = %s;"""
    deleteEx = """delete from exam where id_user = %s;"""
    updatePoints = """update user set ege_points = 0 where id = %s;"""

    try:
        with connect.cursor() as cursor:
            cursor.execute(deleteAch, str(vk_id))
            cursor.execute(deleteEx, str(vk_id))
            cursor.execute(updatePoints, str(vk_id))
            connect.commit()
    except:
        print("Ошибка при удалении баллов")


def get_all_points(vk_id, connect):
    points = 0
    selectDB = """select * from user where id = %s"""
    try:
        with connect.cursor() as cursor:
            cursor.execute(selectDB, str(vk_id))
            points = cursor.fetchall()[0]["ege_points"]
    except:
        print("Ошибка при получении баллов ЕГЭ")
    return int(points)
