import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

def do_translate():
    src = input_box.get("1.0", "end").strip()
    if not src:
        messagebox.showwarning("입력 필요", "번역할 한국어 문장을 입력하세요.")
        return
    try:
        translated = GoogleTranslator(source="ko", target="ja").translate(src)
        output_box.config(state="normal")
        output_box.delete("1.0", "end")
        output_box.insert("1.0", translated)
        output_box.config(state="disabled")
        status_var.set("번역 완료 ✅")
    except Exception as e:
        status_var.set("번역 실패 ❌")
        messagebox.showerror("오류", f"번역 중 오류가 발생했습니다.\n{e}")

def copy_output():
    txt = output_box.get("1.0", "end").strip()
    if not txt:
        return
    root.clipboard_clear()
    root.clipboard_append(txt)
    status_var.set("복사 완료 📋")

def clear_all():
    input_box.delete("1.0", "end")
    output_box.config(state="normal")
    output_box.delete("1.0", "end")
    output_box.config(state="disabled")
    status_var.set("")

root = tk.Tk()
root.title("한→일 번역기")
root.geometry("640x420")
root.configure(bg="white")

style = ttk.Style()
try:
    style.theme_use("clam")
except:
    pass

title = ttk.Label(root, text="한국어 → 日本語 번역", font=("Arial", 16, "bold"))
title.pack(pady=(12, 6))

frame = ttk.Frame(root, padding=12)
frame.pack(fill="both", expand=True)

left = ttk.LabelFrame(frame, text="입력(한국어)")
left.pack(side="left", fill="both", expand=True, padx=(0, 6))
input_box = tk.Text(left, height=10, wrap="word")
input_box.pack(fill="both", expand=True, padx=8, pady=8)

right = ttk.LabelFrame(frame, text="출력(日本語)")
right.pack(side="left", fill="both", expand=True, padx=(6, 0))
output_box = tk.Text(right, height=10, wrap="word", state="disabled")
output_box.pack(fill="both", expand=True, padx=8, pady=8)

btns = ttk.Frame(root)
btns.pack(pady=6)
ttk.Button(btns, text="번역", command=do_translate).grid(row=0, column=0, padx=6)
ttk.Button(btns, text="복사", command=copy_output).grid(row=0, column=1, padx=6)
ttk.Button(btns, text="지우기", command=clear_all).grid(row=0, column=2, padx=6)

status_var = tk.StringVar()
status = ttk.Label(root, textvariable=status_var, foreground="#666")
status.pack(pady=(2, 10))

# 단축키: ⌘/Ctrl + Enter 로 번역
root.bind("<Command-Return>", lambda e: do_translate())
root.bind("<Control-Return>", lambda e: do_translate())

root.mainloop()
