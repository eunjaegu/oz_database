import pymysql

# (1) db connection

# 데이터베이스 연결 설정
connection = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '0000',
    db = 'classicmodels',
    charset='utf8mb4',  # 이모지르 포함한 모든 유니코드 문지를 지원 
    # 딕셔너리 형태 : 이 코드 없으면 아래 튜플형태로 반환함. 이럴 경우 values값 넣기 코드 추가
    cursorclass=pymysql.cursors.DictCursor
)

# (2) CURD

## 1. SELECT * FROM

# 데이터베이스 연결 
def get_customers():
    cursor = connection.cursor()

    sql = "select * from customers"
    cursor.execute(sql)

    customers = cursor.fetchone()
    # 딕셔너리 형태일 때
    print('customer:', customers)
    print('customer:', customers['customerNumber'])
    print('customer:', customers['country'])
    print('customer:', customers['customerName'])
    cursor.close

# 튜플형태 시 values값 넣기
# print('customer:', customers[0] )  
# print('customer:', customers[1] )
# print('customer:', customers[2] )
# print('customer:', customers[3] )

## 2. INSERT INTO
def add_customer():
    cursor = connection.cursor()
    name = 'inseop'
    family_name = 'kim'
    sql = "INSERT INTO customers(customerNumber, customerName, contactLastName) VALUES (1005, '{name}', '{family_name}')"
    cursor.execute(sql)
    connection.commit()
    cursor.close

add_customer()    

## 3. UPDATE INTO
def uqdate_customer():
    cursor = connection.cursor()
    update_name = 'update_inseop'
    contactLastName = 'update_kim'

    sql = f"UPDATE customers SET customerName = '{update_name}', contactLastName = '{contactLastName}' WHERE customerNumber = 1000"
    cursor.execute(sql)
    connection.commit()
    cursor.close()

## 4. DELETE FROM
def delete_customer():
    cursor = connection.cursor()
    sql = "DELETE FROM customers WHERE customerNumber = 1000"
    cursor.execute(sql)
    connection.commit()
    cursor.close()

delete_customer()


