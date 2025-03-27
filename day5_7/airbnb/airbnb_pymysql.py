import pymysql

# 데이터베이스 연결 설ㅓ
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='0000',
    db='airbnb',
    charset='utf8mb4',
    # pymysql라이브러리에서 데이터베이스 쿼리 결과를 처리할 때 딕셔너리 형태로 받기
    # 딕셔너리 형태로 받으면 컬럼 이름을 키로 하여 값에 접근할 수 있어 직관적이고 편리
    cursorclass=pymysql.cursors.DictCursor
)

# with문으로 커서 자동 관리
# 커서를 사용하여 쿼리 실행
with connection.cursor() as cursor:
    
    # # 1. 새로운 제품 추가
    # sql = "INSERT INTO Products(productName, price, stockQuantity) VALUES (%s, %s, %s)"
    # cursor.execute(sql, ('python Book', 10000, 10))
    # connection.commit()

    # # 2. 고객 목록 조회
    # cursor.execute("SELECT * FROM Products")
    # for book in cursor.fetchall():
    #     print(book)

    # # 3. 제품 제고 업데이터
    # sql = "UPDATE Products SET stockQuantity = stockQuantity - %s WHERE productID = %s"
    # # (차감할 값, ID 값)
    # cursor.execute(sql, (1, 1))
    # connection.commit()

    # # 4. 고객별 총 주문 금액
    # sql = "SELECT customerID, SUM(totalAmount) AS totalAmount FROM Orders GROUP BY customerID"
    # cursor.execute(sql)
    # datas = cursor.fetchall()
    # print(datas)

    # # 5. 고객 이메일 업데이트
    # sql = "UPDATE Customers SET email=%s WHERE customerID = %s"
    # cursor.execute(sql, ('update@update.com', 1))
    # connection.commit()
    

    # # 6. 주문 취소
    # sql = "DELETE FROM Orders WHERE orderID = %s"
    # cursor.execute(sql, (15,))
    # connection.commit()
    
    # 7. 특정 제품 검색
    # sql = "SELECT * FROM Products WHERE ProductName LIKE %s"
    # cursor.execute(sql, ('%Book%',))
    # datas = cursor.fetchall()

    # print(datas[0].keys())

    # for data in datas:
    #     print(data['productName'])
     
    # 8. 특정 고객의 모든 주문 조회
    sql = "SELECT * FROM Orders WHERE customerID = %s"
    cursor.execute(sql, (1))
    datas = cursor.fetchall()

    for data in datas:
        print(data)

    # 9. 가장 많이 주문한 고객 (주문 횟수가 가장 많은 고객을 뽑아라)
    sql = """ 
        SELECT customerID, COUNT(*) as orderCount 
        FROM Orders GROUP BY customerID 
        ORDER BY orderCount DESC LIMIT 1
        """
    cursor.execute(sql)
    datas = cursor.fetchall()
    print(data)



cursor.close()      



