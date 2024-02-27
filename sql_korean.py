import sqlite3

connection = sqlite3.connect('netflixTest.db')
cursor = connection.cursor()

cursor.execute("SELECT * FROM netflix_title WHERE country = 'South Korea'")

rows = cursor.fetchall()

# for row in rows :
#     print(row)


# 1. txt 파일을 만든다.
with open('korean_movies.txt', 'w') as file:
    # 2. txt 파일에 한국 영화만 저장한다.
    for row in rows:
        file.write(row[2] + '\n')
        
connection.close()