import tkinter as tk

guess_words = ["ruby", "python", "javascript"]

def check_word():
    word = entry.get()
    if word in guess_words:
        result.config(text="리스트 안에 있습니다!")
    else:
        result.config(text="리스트 안에 없습니다!")

root = tk.Tk()
entry = tk.Entry(root)
entry.pack()
btn = tk.Button(root, text="제출", command=check_word)
btn.pack()
result = tk.Label(root)
result.pack()
root.mainloop()
