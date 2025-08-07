import tkinter as tk

def check_word():
    word = entry.get()
    if word == "apple":
        result.config(text="정답!")
    else:
        result.config(text="틀렸어!")

root = tk.Tk()
entry = tk.Entry(root)
entry.pack()
btn = tk.Button(root, text="제출", command=check_word)
btn.pack()
result = tk.Label(root)
result.pack()
root.mainloop()


