import math
import tkinter as tk
from tkinter import ttk


def calculate(*_):
    try:
        tx = float(target_x.get())
        ty = float(target_y.get())
        mx = float(my_x.get())
        my = float(my_y.get())
    except ValueError:
        result.set("Enter numbers in all four fields")
        return

    dx = tx - mx
    dy = ty - my
    c = math.hypot(dx, dy)          # pythagoras: sqrt(dx² + dy²)
    metres = c * 100                # 4.12 in-game -> 412 m

    result.set(f"C = {c:.2f}   ->   {metres:.0f} m")


root = tk.Tk()
root.title("Wardogs range calculator")
root.resizable(False, False)

frame = ttk.Frame(root, padding=12)
frame.grid()

target_x, target_y = tk.StringVar(), tk.StringVar()
my_x, my_y = tk.StringVar(), tk.StringVar()
result = tk.StringVar(value="C = -")

ttk.Label(frame, text="").grid(row=0, column=0)
ttk.Label(frame, text="X").grid(row=0, column=1)
ttk.Label(frame, text="Y").grid(row=0, column=2)

ttk.Label(frame, text="Target").grid(row=1, column=0, sticky="w", padx=(0, 8))
ttk.Entry(frame, textvariable=target_x, width=8).grid(row=1, column=1, padx=2, pady=2)
ttk.Entry(frame, textvariable=target_y, width=8).grid(row=1, column=2, padx=2, pady=2)

ttk.Label(frame, text="You").grid(row=2, column=0, sticky="w", padx=(0, 8))
ttk.Entry(frame, textvariable=my_x, width=8).grid(row=2, column=1, padx=2, pady=2)
ttk.Entry(frame, textvariable=my_y, width=8).grid(row=2, column=2, padx=2, pady=2)

ttk.Button(frame, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=3, pady=(8, 4), sticky="ew")
ttk.Label(frame, textvariable=result, font=("TkDefaultFont", 11, "bold")).grid(row=4, column=0, columnspan=3)

# recalculate live as you type
for var in (target_x, target_y, my_x, my_y):
    var.trace_add("write", calculate)

root.bind("<Return>", calculate)
root.mainloop()
