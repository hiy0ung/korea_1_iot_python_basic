import pymysql

def saveCoupangData(coupangData: list):
    try:
        connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='gkdud989898!!!!', db='coupang_db')
        # save는 insert라 굳이 dictionary cursor를 쓸 필요 없음!
        try:
            cursor = connection.cursor()
        except Exception as e:
            print(e) #SQL 오류
        finally:
            connection.close()

    except Exception as e:
        print("데이터베이스 연결 실패")