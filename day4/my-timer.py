# pomodoro.py
import tkinter as tk
from tkinter import ttk

# --- 설정(분) ---
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15

# --- 상태 변수 ---
reps = 0                # 시작된 세션 수 (work/break 포함)
running = False         # 카운트다운 동작 여부
remaining = 0           # 남은 초
after_id = None         # after() 취소용

# 색상 테마
COLOR_BG = "#ffffff"
COLOR_WORK = "#2e7d32"        # 녹색
COLOR_BREAK = "#1565c0"       # 파랑
COLOR_LONG = "#a52714"        # 적색
COLOR_TEXT = "#222222"

def seconds(m): return int(m * 60)

def format_mmss(sec: int) -> str:
    m, s = divmod(max(0, sec), 60)
    return f"{m:02d}:{s:02d}"

def next_session():
    """다음 세션 타입/길이(초)/표시색 반환"""
    global reps
    reps += 1
    if reps % 8 == 0:
        return ("LONG BREAK", seconds(LONG_BREAK_MIN), COLOR_LONG)
    elif reps % 2 == 0:
        return ("BREAK", seconds(SHORT_BREAK_MIN), COLOR_BREAK)
    else:
        return ("WORK", seconds(WORK_MIN), COLOR_WORK)

def start():
    """시작 또는 재시작"""
    global running, remaining, after_id
    if running:
        return
    # 남은 시간이 없으면 새 세션 시작
    if remaining <= 0:
        session, secs, color = next_session()
        status_var.set(session)
        status_lbl.configure(fg=color)
        remaining = secs
    running = True
    tick()

def pause():
    """일시정지"""
    global running, after_id
    if not running:
        return
    running = False
    if after_id:
        root.after_cancel(after_id)
        # after_id는 취소 후 None으로
    # 일시정지 상태 유지

def reset():
    """전부 초기화"""
    global reps, running, remaining, after_id
    running = False
    remaining = 0
    reps = 0
    if after_id:
        root.after_cancel(after_id)
    time_var.set("00:00")
    status_var.set("READY")
    status_lbl.configure(fg=COLOR_TEXT)
    tomatoes_var.set("")
    # 버튼 상태
    start_btn.configure(state="normal")
    pause_btn.configure(state="disabled")

def skip():
    """현재 세션 즉시 종료하고 다음으로 넘어감"""
    global running, remaining, after_id
    if after_id:
        root.after_cancel(after_id)
    running = False
    remaining = 0
    # 완료 알림 없이 바로 다음 세션
    start()

def update_tomatoes():
    # 완료된 work 세션 개수: reps 중 홀수(1,3,5,7)가 work 시작이므로 floor(reps/2)
    done = reps // 2
    tomatoes_var.set(" ".join("🍅" for _ in range(done)))

def tick():
    """1초 카운트다운"""
    global remaining, running, after_id
    time_var.set(format_mmss(remaining))
    if not running:
        return
    if remaining > 0:
        remaining -= 1
        after_id = root.after(1000, tick)
    else:
        # 세션 완료
        root.bell()  # 알림
        update_tomatoes()
        running = False
        # 자동으로 다음 세션 시작
        start()

# ---------------- UI ----------------
root = tk.Tk()
root.title("Pomodoro Timer")
root.configure(bg=COLOR_BG)
root.geometry("360x260")

# 상단 상태
status_var = tk.StringVar(value="READY")
status_lbl = tk.Label(root, textvariable=status_var, font=("Arial", 16, "bold"),
                      bg=COLOR_BG, fg=COLOR_TEXT)
status_lbl.pack(pady=(16, 6))

# 타이머 표시
time_var = tk.StringVar(value="00:00")
time_lbl = tk.Label(root, textvariable=time_var, font=("Arial", 40, "bold"),
                    bg=COLOR_BG, fg=COLOR_TEXT)
time_lbl.pack(pady=(0, 10))

# 진행(🍅)
tomatoes_var = tk.StringVar(value="")
tomatoes_lbl = tk.Label(root, textvariable=tomatoes_var, font=("Arial", 16),
                        bg=COLOR_BG, fg="#ff7043")
tomatoes_lbl.pack(pady=(0, 10))

# 버튼들
btns = tk.Frame(root, bg=COLOR_BG)
btns.pack(pady=4)

start_btn = ttk.Button(btns, text="Start", command=start)
pause_btn = ttk.Button(btns, text="Pause", command=pause, state="disabled")
reset_btn = ttk.Button(btns, text="Reset", command=reset)
skip_btn  = ttk.Button(btns, text="Skip →", command=skip)

start_btn.grid(row=0, column=0, padx=6)
pause_btn.grid(row=0, column=1, padx=6)
reset_btn.grid(row=0, column=2, padx=6)
skip_btn.grid(row=0, column=3, padx=6)

# 버튼 상태 동기화: 시작하면 Pause 활성화
def on_running_changed(*_):
    if running:
        start_btn.configure(state="disabled")
        pause_btn.configure(state="normal")
    else:
        start_btn.configure(state="normal")
        pause_btn.configure(state="disabled")

# 간단한 폴링(상태 버튼 반영)
def poll_buttons():
    on_running_changed()
    root.after(200, poll_buttons)

poll_buttons()

# 시작
root.mainloop()
