import tkinter as tk
from adbs import ad2bs, bs2ad


def bs2adM(date):
    tk.Label(root, text=date + " BS = " + bs2ad(date) + " AD").grid(columnspan=2)


def ad2bsM(date):
    tk.Label(root, text=date + " AD = " + ad2bs(date) + " BS").grid(columnspan=2)


def clear():
    for widget in root.winfo_children():
        if type(widget) == tk.Label:
            widget.grid_forget()


root = tk.Tk()
root.title("ADBS")
root.resizable(0, 0)
clearButton = tk.Button(root, text="Clear", command=clear).grid(
    columnspan=2, sticky="e", padx=3, pady=3
)
bsDate = tk.StringVar()
adDate = tk.StringVar()
bsFrame = tk.Frame(root)
adFrame = tk.Frame(root)
bsFrame.grid()
adFrame.grid(row=1, column=1)
tk.Label(bsFrame, text="BS date").grid()
tk.Label(adFrame, text="AD date").grid()
tk.Entry(bsFrame, textvariable=bsDate).grid(padx=2)
tk.Entry(adFrame, textvariable=adDate).grid(padx=2)
tk.Button(bsFrame, text="Convert to AD", command=lambda: bs2adM(bsDate.get())).grid(
    padx=5, pady=5
)
tk.Button(adFrame, text="Convert to BS", command=lambda: ad2bsM(adDate.get())).grid(
    padx=5, pady=5
)
root.mainloop()
