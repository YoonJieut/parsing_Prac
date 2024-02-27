import csv



csv_file_path = './netflix_titles.csv'
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        # 각 행의 데이터 처리 작업 수행  
        print(row) 
    # 반복문 종료
    # with 블록 종료 후 자동으로 파일이 닫힙니다.
