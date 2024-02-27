import csv
import sqlite3

# CSV 파일 경로
csv_file_path = './netflix_titles.csv'

# SQLite 데이터베이스 연결
connection = sqlite3.connect('netflixTest.db')
cursor = connection.cursor()

# 테이블 생성 쿼리
create_table_query = '''CREATE TABLE IF NOT EXISTS netflix_title (
            show_id TEXT,
            type TEXT,
            title TEXT,
            director TEXT,
            cast TEXT,
            country TEXT,
            date_added TEXT,
            release_year INTEGER,
            rating TEXT,
            duration TEXT,
            listed_in TEXT,
            description TEXT
            )'''
cursor.execute(create_table_query)



# CSV 파일 읽기 및 데이터 삽입
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # 헤더 건너뛰기
    for row in csv_reader:
        insert_query = '''INSERT INTO netflix_title (
              show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description) 
              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        data = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], int(row[7]), row[8], row[9], row[10], row[11])
        cursor.execute(insert_query, data)

# 변경 사항 커밋
connection.commit()

# 연결 종료
connection.close()
