import tkinter as tk
from tkinter import ttk
import requests
from io import BytesIO
from PIL import Image, ImageTk
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)


CITY="Seoul"
api_key = os.getenv("OPENWEATHER_API_KEY")

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={api_key}"
res = requests.get(url)

data = res.json()
name = data["name"]        #seoul
weather = data["weather"][0]["main"]  #날씨
description = data["weather"][0]["description"] #전체적인 날씨
icon_code = data["weather"][0]["icon"]  #아이콘

icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
print(icon_url)

# pretty_json = json.dumps(data, indent=4, ensure_ascii=False)

# ---- Tkinter UI ----
root = tk.Tk()
root.title("Weather")
root.geometry("360x220")
root.configure(bg="white")

style = ttk.Style()
# 일부 테마는 배경 반영이 약해서 'clam' 같은 테마가 반응이 좋음
try:
    style.theme_use("clam")
except:
    pass

container = ttk.Frame(root, padding=16)
container.pack(fill="both", expand=True)

title = ttk.Label(container, text=f"{name}", font=("Arial", 18, "bold"))
title.grid(row=0, column=0, columnspan=2, sticky="w")

sub = ttk.Label(container, text=f"{weather} · {description}", font=("Arial", 12))
sub.grid(row=1, column=0, columnspan=2, sticky="w", pady=(4, 12))

icon_lbl = ttk.Label(container, text="(loading icon...)")
icon_lbl.grid(row=0, column=2, rowspan=3, padx=(12, 0))

def load_icon():
    try:
        r = requests.get(icon_url, timeout=8)
        r.raise_for_status()
        img = Image.open(BytesIO(r.content))
        photo = ImageTk.PhotoImage(img)
        icon_lbl.configure(image=photo, text="")
        # 참조 유지(안 하면 가비지 컬렉션으로 이미지가 사라짐)
        icon_lbl.image = photo
    except Exception as e:
        icon_lbl.configure(text=f"icon load failed\n{e}")

load_icon()

# 추가 정보 영역(필요하면 확장)
info = ttk.Label(container, text="Data source: OpenWeather", font=("Arial", 10))
info.grid(row=2, column=0, columnspan=2, sticky="w", pady=(12, 0))

root.mainloop()