import os
import datetime

# 현재 날짜와 시간
now = datetime.datetime.now()

# 시작 시간 업데이트
start_time = now.strftime("%H:%M")
start_date = now.strftime('%Y-%m-%d')
start_time_line = f"| [{start_date}](./{start_date}.md) | {start_time} |"

# README 파일 열기
readme_file = 'README.md'
with open(readme_file, 'r') as file:
    lines = file.readlines()

# README 파일 업데이트
for i, line in enumerate(reversed(lines)):
    if line.strip():
        # 파일의 마지막 줄을 찾아서 종료 시간 업데이트
        lines.append("\n")
        lines.append(f"| [{start_date}](./{start_date}.md) | {start_time} | |")
        break

# README 파일 저장
with open(readme_file, 'w') as file:
    file.writelines(lines)

# 날짜별 파일 생성 (빈 파일 생성)
til_file_name = f"{start_date}.md"
with open(til_file_name, 'w') as til_file:
    pass  # 아무 내용 없이 빈 파일 생성

# 커밋 및 푸시
commit_message = f":book: {start_date} 공부 시작"
os.system(f"git add {readme_file} {til_file_name}")
os.system(f"git commit -m '{commit_message}'")
os.system("git push origin main")