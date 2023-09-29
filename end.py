import os
import datetime

# 현재 날짜와 시간
now = datetime.datetime.now()

# 종료 시간 업데이트
end_time = now.strftime("%H:%M")
end_date = now.strftime('%Y-%m-%d')

# README 파일 열기
readme_file = 'README.md'
with open(readme_file, 'r') as file:
    lines = file.readlines()

# README 파일 업데이트
split_result = lines[-1].split('|')
split_result[-2] = f" {end_time} "
lines[-1] = '|'.join(split_result)

# README 파일 저장
with open(readme_file, 'w') as file:
    file.writelines(lines)

# 커밋 및 푸시
commit_message = f":book: {end_date} 공부 종료"
os.system(f"git add .")
os.system(f"git commit -m '{commit_message}'")
os.system("git push origin main")