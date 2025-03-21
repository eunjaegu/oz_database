import mysql.connector
from faker import Faker
import random

# 1. MYSQL 연결 설정
db_connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '0000',
    database = 'testdatabase'
)

# 2. MYSQL 연결
cursor = db_connection.cursor()
faker = Faker()

# users 데이터 생성 (더미데이터)
for _ in range(100):
    username = faker.user_name()
    email = faker.email()

    sql = "INSERT INTO users(username, email) VALUES(%s, %s)"
    values = (username, email)
    # print(sql)
    cursor.execute(sql, values)

# user_id 불러오기
cursor.execute("SELECT user_id FROM users")
valid_user_id = [row[0] for row in cursor.fetchall()]
# print(valid_user_id)

# 100개의 주문 더미 데이터 생성
for _ in range(100):
    user_id = random.choice(valid_user_id)
    product_name = faker.word()
    quantity = random.randint(1, 10)

    try:
        sql = "INSERT INTO orders(user_id, product_name, quantity) VALUES(%s, %s, %s)"
        values = (user_id, product_name, quantity)
        #print(sql, values)

        cursor.execute(sql, values)
    except:
        pass

db_connection.commit()   

# 쿼리 실행 및 결과처리 종료
cursor.close()

# 물리적 연결 종료
db_connection.close()

