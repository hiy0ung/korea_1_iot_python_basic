from pymysql import connect
class DatabaseConfig:

    @staticmethod
    def getConnection():
        host: str = 'localhost'
        port: int = 3306
        user: str = 'root'
        password: str = 'gkdud989898!!!!'
        database: str = 'pymysql_study'

        return connect(host=host, user=user, password=password, database=database, port=port)