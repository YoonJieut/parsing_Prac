import sqlite3

# SQLite 데이터베이스 연결
connection = sqlite3.connect('netflixTest.db')
cursor = connection.cursor()

# SQL 쿼리 실행
cursor.execute('SELECT * FROM netflix_title')

# 조회 결과 가져오기
rows = cursor.fetchall()

# 결과 출력
for row in rows:
    print(row)

# 연결 종료
connection.close()
