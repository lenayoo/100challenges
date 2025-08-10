import random
import tkinter as tk
import pandas as pd

df = pd.read_csv("quotes-500k/quotes.csv")

#TODO: category에 따라서 이모티콘 다르게 표현하기 
emojis = ["🌞", "🌙", "⭐", "💡", "🌸", "🔥", "💎", "🎯", "🚀", "🌈", "☁️"]

# 랜덤 데이터 설정 함수
def update_quote():
  random_quote = df.sample(1).iloc[0]
  emoji_label.config(text=random.choice(emojis))
  quote_label.config(text=f'{random_quote["quote"]}')
  author_label.config(text=f'— {random_quote["author"]}')


# Tkinter 윈도우 생성
root = tk.Tk()
root.title("Random Quote")
root.geometry("500x200")
root.configure(bg="white")

# 이모지 라벨
emoji_label = tk.Label(root, text="", font=("Arial", 30), bg="white")
emoji_label.pack(pady=(20, 0))

# 명언 내용
quote_label = tk.Label(
    root,
    text="",
    wraplength=450,
    justify="center",
    font=("Arial", 12),
    bg="white"
)
quote_label.pack(expand=True, fill="both", padx=20, pady=(0, 5))

# 저자
author_label = tk.Label(
    root,
    text="",
    justify="center",
    font=("Arial", 10, "italic"),
    bg="white",
    fg="gray"
)
author_label.pack(pady=(0, 20))

update_quote()

root.mainloop()