# todays_word.py
import argparse, csv, datetime as dt, os, random, sys
from dataclasses import dataclass

import kagglehub, os

# 예시: 실제 슬러그로 바꿔 넣으세요 (owner/dataset-name)
slug = "robinpourtaud/jlpt-words-by-level"

path = kagglehub.dataset_download(slug)  # 캐시에 내려받고 경로 반환
print("Downloaded to:", path)
print("Files:", os.listdir(path))


# try:
#     import tkinter as tk  # --gui 옵션에서만 씀
# except Exception:
#     tk = None  # GUI 미사용 시 문제없음

# @dataclass
# class Entry:
#     lang: str
#     term: str
#     reading: str
#     meaning: str
#     example: str

# SAMPLE = [
#     Entry("ja", "挑戦", "ちょうせん", "도전", "新しい挑戦を始めよう。"),
#     Entry("ja", "習慣", "しゅうかん", "습관", "毎日の小さな習慣が力になる。"),
#     Entry("en", "resilience", "", "회복탄력성", "Build resilience through small wins."),
#     Entry("en", "iterate", "", "반복·개선하다", "We iterate and improve every day."),
# ]

# def load_entries(csv_path: str | None) -> list[Entry]:
#     if not csv_path:
#         return SAMPLE
#     if not os.path.exists(csv_path):
#         print(f"[info] CSV가 없어 내장 샘플로 진행합니다: {csv_path}", file=sys.stderr)
#         return SAMPLE

#     entries: list[Entry] = []
#     with open(csv_path, newline="", encoding="utf-8") as f:
#         reader = csv.DictReader(f)
#         # 기대 컬럼: lang,term,reading,meaning,example
#         for r in reader:
#             entries.append(Entry(
#                 r.get("lang","").strip() or "ja",
#                 r.get("term","").strip(),
#                 r.get("reading","").strip(),
#                 r.get("meaning","").strip(),
#                 r.get("example","").strip(),
#             ))
#     return entries or SAMPLE

# def pick_today(entries: list[Entry], shuffle: bool) -> Entry:
#     if shuffle:
#         return random.choice(entries)
#     # 날짜(현지) 기준 결정적 선택 → 오늘은 항상 같은 항목
#     today = dt.date.today().isoformat()  # 'YYYY-MM-DD'
#     rnd = random.Random(today)           # 날짜 문자열을 시드로 사용
#     return entries[rnd.randrange(len(entries))]

# def format_text(e: Entry) -> tuple[str, str]:
#     # 화면/콘솔 공용 표시 텍스트
#     if e.lang == "ja":
#         title = f"今日の単語: {e.term} ({e.reading}) - {e.meaning}"
#         detail = e.example
#     else:
#         title = f"Today's expression: {e.term} - {e.meaning}"
#         detail = e.example
#     return title, detail

# def show_cli(e: Entry):
#     title, detail = format_text(e)
#     print(title)
#     if detail:
#         print(detail)

# def show_gui(e: Entry):
#     if tk is None:
#         print("[error] Tkinter를 사용할 수 없습니다. --gui 없이 실행하세요.", file=sys.stderr)
#         sys.exit(1)
#     title, detail = format_text(e)
#     root = tk.Tk()
#     root.title("오늘의 단어/문장")
#     root.configure(bg="white")
#     root.geometry("520x220")

#     emoji = tk.Label(root, text="📚", font=("Arial", 28), bg="white")
#     emoji.pack(pady=(10, 4))

#     lbl_title = tk.Label(root, text=title, font=("Arial", 14, "bold"),
#                          bg="white", wraplength=480, justify="center")
#     lbl_title.pack(padx=16)

#     if detail:
#         lbl_detail = tk.Label(root, text=detail, font=("Arial", 12),
#                               bg="white", fg="#555", wraplength=480, justify="center")
#         lbl_detail.pack(padx=16, pady=(6, 10))

#     btns = tk.Frame(root, bg="white")
#     btns.pack(pady=(0, 10))

#     def refresh():
#         # 날짜 고정 대신 즉시 랜덤(학습용)
#         new = pick_today(entries, shuffle=True)
#         t, d = format_text(new)
#         lbl_title.config(text=t)
#         if detail:
#             lbl_detail.config(text=d)

#     tk.Button(btns, text="랜덤", command=refresh, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=6)
#     tk.Button(btns, text="닫기", command=root.destroy).grid(row=0, column=1, padx=6)

#     root.mainloop()

# def main():
#     ap = argparse.ArgumentParser(description="오늘의 단어/문장 학습기")
#     ap.add_argument("--csv", help="학습용 CSV 경로 (컬럼: lang,term,reading,meaning,example)")
#     ap.add_argument("--gui", action="store_true", help="Tk 창으로 표시")
#     ap.add_argument("--shuffle", action="store_true", help="오늘 날짜 고정 대신 매 실행 랜덤")
#     args = ap.parse_args()

#     global entries
#     entries = load_entries(args.csv)
#     entry = pick_today(entries, shuffle=args.shuffle)

#     if args.gui:
#         show_gui(entry)
#     else:
#         show_cli(entry)

# if __name__ == "__main__":
#     main()

