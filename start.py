import os
import datetime

now = datetime.datetime.now()
start_date = now.strftime('%Y-%m-%d')

# Markdown 파일 생성
til_file_name = f"{start_date}.md"
with open(til_file_name, 'w') as til_file:
    pass  # 아무 내용 없이 빈 파일 생성
