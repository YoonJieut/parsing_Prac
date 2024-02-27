# import mysql.connector

# MySQL 서버 연결 정보
config = {
    'host': 'localhost',
    'user': 'root',
    'password': '0000',
    'database': 'blog_db'
}

# MySQL 데이터베이스 연결
connection = mysql.connector.connect(**config)
cursor = connection.cursor()

# SQL 쿼리 실행
cursor.execute('SELECT * FROM netflix_title') # MySQL에서는 테이블 이름을 대소문자 구분함. 'netflix_title'과 'Netflix_title'은 다른 테이블로 인식됨.

# 조회 결과 가져오기
rows = cursor.fetchall()

# 결과 출력
for row in rows:
    print(row)

# 연결 종료
connection.close()
