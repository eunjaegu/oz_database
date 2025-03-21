import pymysql

# 데이터베이스 쿼리 실행 함수 (연결)
def execute_query(connection, query, args=None):
    # 커서 객체 생성 및 궈리 실행
    with connection.cursor() as cursor:
        cursor.execute(query, args or ())   # 쿼리 실행, 인자가 없으면 빈 튜플 사용
        # SELECT 쿼리일 경우 결과를 반환, 그렇지 않으면 변경 사항을 커밋
        if query.strip().upper().startswith('SELECT'):
            return cursor.fetchall() # SELECT 쿼리 결과 반환
        else:
            connection.commit() # INSERT, UPDATE, DELETE 등의 쿼리 실행 후 커밋

#메인 함수 
def main():
    # 데이터베이스 연결 설정
    connection = pymysql.connect(host='localhost',
                                 user='username',
                                 password='password',
                                 db='database_name',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        # SELECT 쿼리 실행
        result = execute_query(connection, "SELECT * FROM table_name")
        print("SELECT 연산 결과:")
        # 쿼리 결과 출력(사용자에게 조회)
        for row in result:
            print(row)

        # INSERT 연산
        execute_query(connection, "INSERT INTO table_name (column1, column2) VALUES (%s, %s)", ('data1', 'data2'))
        print("INSERT 연산 수행됨.")

        # UPDATE 연산
        execute_query(connection, "UPDATE table_name SET column1=%s WHERE column2=%s", ('new_data', 'criteria'))
        print("UPDATE 연산 수행됨.")

        # DELETE 연산
        execute_query(connection, "DELETE FROM table_name WHERE column_name=%s", ('criteria',))
        print("DELETE 연산 수행됨.")

    finally:
        # DB 연결 종료
        connection.close()

# 메인 함수 호출
if __name__ == "__main__":
    main()