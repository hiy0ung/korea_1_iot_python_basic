import pymysql

def saveCoupangData(coupangData: list):
    try:
        connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='gkdud989898!!!!', db='coupang_db')
        # save는 insert라 굳이 cursor=cursors.DictCursor를 쓸 필요 없음!
        try:
            cursor = connection.cursor()
            # category 1개랑 product들이 들어있음
            for data in coupangData:
                sql = "insert into category_tb values(default, %s)"
                cursor.execute(sql, data["category"])
                category_id = cursor.lastrowid

                # SQL에서 짜는 형태에 맞춰서 쿼리문 만들어 줘야 함
                # 제일 처음과 끝 빼고 ","로 다 나눠져있음
                # \ 이스케이프문 >> 문자열로 만들기 위해? 문자열에 ''를 썼는데 안에 또 ''를 쓰고 있어서 구분 해주기 위해 (int 타입인 price는 안 써도 됨)
                # values = ",\n".join(list(map(lambda product: f"(default, \'{product['productName']}\', {product['price'].replace(',', '')}, \'{product['productImgUrl']}\', '{category_id}')", data['products'])))
                values = ",\n".join(list(map(lambda product: "(default, %s, %s, %s, %s)", data['products'])))
                sql = "insert into product_tb values" + values
                valueDatas = []
                for value in list(map(lambda product: [product["productName"], product["price"], product["productImgUrl"], category_id], data["products"])):
                    # 리스트들끼리 합쳐줌 (확장해줌)
                    valueDatas.extend(value)
                cursor.execute(sql, value)
            connection.commit()

        except Exception as e:
            print(e) #SQL 오류
        finally:
            connection.close()

    except Exception as e:
        print("데이터베이스 연결 실패")