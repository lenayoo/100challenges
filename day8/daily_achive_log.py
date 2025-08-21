from datetime import datetime

def write_daily_reflection():
    today = datetime.now().strftime("%Y-%m-%d")
    print(f"\n📅 {today} - 오늘의 3줄 다독 루틴\n")

    learned = input("1. 오늘 내가 배운/시도한 것: ")
    postponed = input("2. 오늘 미뤘지만 다음에 할 수 있는 것: ")
    smile = input("3. 오늘 나를 웃게 만든 순간: ")

    entry = f"""
📅 {today}
1. 배운 것: {learned}
2. 미룬 것: {postponed}
3. 웃게 만든 것: {smile}
{"-"*40}
"""
    with open("daily_reflections.txt", "a", encoding="utf-8") as f:
        f.write(entry)

    print("\n✅ 저장 완료! 오늘도 기록했어.\n")

if __name__ == "__main__":
    write_daily_reflection()
