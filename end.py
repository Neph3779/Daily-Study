import os
import datetime

now = datetime.datetime.now()
end_date = now.strftime('%Y-%m-%d')

# 커밋 및 푸시
commit_message = f":book: {end_date} 공부 종료"
os.system(f"git add .")
os.system(f"git commit -m '{commit_message}'")
os.system("git push origin main")
