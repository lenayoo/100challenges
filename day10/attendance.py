import argparse
import csv
import os
from datetime import datetime

FILENAME = "attendance.csv"
USERNAME = os.getenv("USER", "Lena")

def log_action(action):
    now = datetime.now()
    date = now.date().isoformat()
    time = now.strftime("%H:%M")

    # CSV 파일 없으면 헤더 추가
    file_exists = os.path.isfile(FILENAME)
    with open(FILENAME, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["date", "name", "action", "time"])
        writer.writerow([date, USERNAME, action, time])
    print(f"{action} 기록 완료 ({time})")

def report():
    if not os.path.isfile(FILENAME):
        print("기록이 없습니다.")
        return
    with open(FILENAME, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"{row['date']} - {row['name']} - {row['action']} at {row['time']}")

def main():
    parser = argparse.ArgumentParser(description="근태관리 시스템")
    parser.add_argument("command", choices=["checkin", "checkout", "report"], help="명령 선택")
    args = parser.parse_args()

    if args.command == "checkin":
        log_action("checkin")
    elif args.command == "checkout":
        log_action("checkout")
    elif args.command == "report":
        report()

if __name__ == "__main__":
    main()
