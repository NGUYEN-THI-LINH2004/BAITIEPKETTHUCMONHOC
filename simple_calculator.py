import tkinter as tk
from tkinter import ttk, messagebox


def calculate():
    """Read inputs, perform the selected operation and display the result."""
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        op = operation.get()

        if op == '+':
            res = num1 + num2
        elif op == '-':
            res = num1 - num2
        elif op == '×':
            res = num1 * num2
        elif op == '÷':
            if num2 == 0:
                raise ZeroDivisionError("Division by zero")
            res = num1 / num2
        else:
            raise ValueError("Invalid operator selected")

        result_var.set(f"Kết quả: {res}")
    except ValueError:
        messagebox.showerror("Lỗi đầu vào", "Vui lòng nhập số hợp lệ.")
        result_var.set("")
    except ZeroDivisionError:
        messagebox.showerror("Lỗi toán học", "Không thể chia cho 0.")
        result_var.set("")


def reset():
    """Clear both Entry widgets and the result label."""
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    result_var.set("")
    operation.set('+')
    entry_num1.focus()


# --- GUI setup ---
root = tk.Tk()
root.title("Máy tính đơn giản")
root.resizable(False, False)

mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

# Input entries
entry_num1 = ttk.Entry(mainframe, width=15, justify="right")
entry_num2 = ttk.Entry(mainframe, width=15, justify="right")
entry_num1.grid(column=1, row=0, sticky=(tk.W, tk.E))
entry_num2.grid(column=1, row=1, sticky=(tk.W, tk.E))

ttk.Label(mainframe, text="Số 1:").grid(column=0, row=0, sticky=tk.W)
    
            

# Operation radio buttons
operation = tk.StringVar(value='+')
ops = [('+', 'Cộng (+)'), ('-', 'Trừ (−)'), ('×', 'Nhân (×)'), ('÷', 'Chia (÷)')]
for idx, (op_val, op_text) in enumerate(ops):
    ttk.Radiobutton(
        mainframe,
        text=op_text,
        variable=operation,
        value=op_val
    ).grid(column=2, row=idx, sticky=tk.W, padx=(10, 0))

ttk.Label(mainframe, text="Số 2:").grid(column=0, row=1, sticky=tk.W)

# Buttons
btn_calculate = ttk.Button(mainframe, text="Tính", command=calculate)
btn_reset = ttk.Button(mainframe, text="Reset", command=reset)
btn_calculate.grid(column=0, row=3, sticky=(tk.W, tk.E))
btn_reset.grid(column=1, row=3, sticky=(tk.W, tk.E))

# Result label
result_var = tk.StringVar(value="Kết quả: ")
result_label = ttk.Label(mainframe, textvariable=result_var, font=("Segoe UI", 12, "bold"))
result_label.grid(column=0, row=4, columnspan=3, pady=(10, 0))

# Padding for all widgets
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

entry_num1.focus()
root.bind('<Return>', lambda event: calculate())
root.mainloop()
