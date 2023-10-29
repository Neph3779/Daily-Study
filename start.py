import os
import datetime
import subprocess

now = datetime.datetime.now()
start_date = now.strftime('%Y-%m-%d')

# Markdown 파일 생성
til_file_name = f"{start_date}.md"
with open(til_file_name, 'w') as til_file:
    pass  # 아무 내용 없이 빈 파일 생성

# 파일 열기 (Mac OS에서는 open 명령 사용)
subprocess.call(['open', til_file_name])
