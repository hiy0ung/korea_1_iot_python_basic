'''
    1. console에서 input() webtoon 제목을 하나 입력 받는다.
    2. 해당 제목의 webtoon 정보를 DB에서 select한다.
    * 받아올 형태
    {
        webtoonId: 1,
        title: "참교육",
        author: "채용택 / 한가람",
        rating: 9.89,
        imgUrl: "https://~~~~",
        categoryName: "월"
    }
    3.  제목 -> 이름(웹툰 제목: 참교육)
        내용 -> 위에 받아온 내용 나열
'''
import pymysql
from pymysql import cursors

def findBoard(title:str):
    try:
        connection = pymysql.connect(host="localhost", port=3306, user="root", passwd="gkdud989898!!!!", db="naver_webtoon_db")
        try:
            cursor = connection.cursor(cursor=cursors.DictCursor)
            sql = '''
            select
            wt.webtoon_id,
            wt.title,
            group_concat(at.author_name separator' / ') as author,
            wt.rating,
            wt.img_url,
            ct.category_name
        from
            webtoon_tb wt
            left outer join author_group_tb agt on(agt.webtoon_id = wt.webtoon_id)
            left outer join author_tb at on(at.author_id = agt.author_id)
            left outer join category_tb ct on(ct.category_id = wt.category_id)
        where
            title = %s
        group by
            wt.webtoon_id,
            wt.title,
            wt.rating,
            wt.img_url,
            ct.category_name
            '''
            cursor.execute(query=sql, args=(title,))
            result = cursor.fetchone()
            result['rating'] = float(result['rating'])
        except Exception as e:
            print(e)
        finally:
            connection.close()
    except Exception as e:
        print(e)

    return result



