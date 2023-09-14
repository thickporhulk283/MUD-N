import tkinter as tk

def button_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set("Lỗi")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

root = tk.Tk()
root.geometry("400x600")
root.title("calculator")

# Hiển thị màn hình tính toán
screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="lucida 40 bold")
entry.pack(fill=tk.X, ipadx=8, pady=10, padx=10)

# Tạo các nút số và phép tính
button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "", "", "", "",   # Thêm dòng trống ở đây
    "1", "2", "3", "*",
    "C", "0", "=", "/"
]

row, col = 1, 0
for button_text in buttons:
    if button_text:
        button = tk.Button(
            button_frame, text=button_text, font="lucida 25 bold", padx=20, pady=20
        )
        button.grid(row=row, column=col, padx=5, pady=5)
        button.bind("<Button-1>", button_click)
    else:
        label_frame = tk.Frame(button_frame)
        label_frame.grid(row=3, column=1, columnspan=2)  # Đặt columnspan=2 cho Frame

        tk.Label(label_frame, text="MÁY TÍNH CẦM TAY", font=("arial", 16)).pack(fill="both", expand=True)  # Đặt font
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
