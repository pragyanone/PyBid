import tkinter as tk
from pathlib import Path
import os
import pickle
from .classes import *


settings_path = os.path.join(os.path.dirname(__file__), "PyTender-settings.pkl")


def generate_documents():
    D = {
        "FIRM": v_firm_name.get(),
        "FIRM_ADDR": v_firm_addr.get(),
        "PERSON": person.get(),
    }
    settings = open(settings_path, "wb")
    pickle.dump(D, settings)

    global path
    path = os.path.join(short_name.get(), "SOURCE")
    Path(path).mkdir(parents=True, exist_ok=True)
    args = (
        path,
        v_firm_name.get(),
        v_firm_addr.get(),
        v_jv_name.get(),
        v_jv_addr.get(),
        v_jv_repr.get(),
        jv.get(),
        short_name.get(),
        contract_name.get(1.0, "end-1c"),
        IoB.get(),
        Contract_ID.get(),
        to.get(1.0, "end-1c"),
        days.get(),
        line_of_cr.get(),
        person.get().rstrip(),
        date.get(),
        jv_list_entry.get(1.0, "end-1c"),
    )

    DbtB = declaration(*args)
    DbtB.create_doc(24)
    if jv.get() == 2:
        jvAgr = jv_agr(*args)
        jvAgr.create_doc()
        PoA = poa(*args)
        PoA.create_doc()

    if large_or_small.get() == 1:
        LoB = bid(*args)
        LoB.create_doc()
    elif large_or_small.get() == 2:
        LoTB = tech(*args)
        LoPB = price(*args)
        LoTB.create_doc()
        LoPB.create_doc()

    if "pvt" not in v_firm_name.get().lower():
        PoAself = poa_self(*args)
        PoAself.create_doc(12)

    EndofCode = tk.Label(contract_frame, text="SUCCESS", bg="lime green")
    EndofCode.grid(row=11, column=2, sticky="e")


def check_status(event=None):
    if large_or_small.get() == 2:
        loc_entry.configure(state="normal")
    else:
        loc_entry.configure(state="disabled")

    if large_or_small.get():
        if jv.get() == 1:
            generateBtn.configure(state="normal")

        elif jv.get() == 2:
            if jv_name_entry.get():
                generateBtn.configure(state="normal")
            else:
                generateBtn.configure(state="disabled")

    if jv.get() == 2:
        jvSubFrame.grid(row=2, column=1, sticky="ew")
        jvSubFrame.columnconfigure(1, weight=3)
        jvSubFrame.columnconfigure(3, weight=2)
        jv_name_label.grid(row=0, column=0, sticky="e")
        jv_name_entry.grid(row=0, column=1, columnspan=3, sticky="ew")
        jv_name_entry.bind("<FocusOut>", check_status)

        jv_addr_label.grid(row=1, column=0, sticky="e")
        jv_addr_entry.grid(row=1, column=1, sticky="ew")

        jv_repr_label.grid(row=1, column=2, sticky="e")

        jv_repr_entry.grid(row=1, column=3, sticky="ew")
        jv_list_label.grid(column=1, sticky="ew")
        jv_list_entry.grid(column=1, sticky="ew")
        jv_list_entry.bind("<FocusOut>", remove_newlines)
        root.geometry("1000x600")

    if jv.get() == 1:
        jv_name_label.grid_forget()
        jv_name_entry.grid_forget()
        jv_name_entry.delete(0, tk.END)

        jv_addr_label.grid_forget()
        jv_addr_entry.grid_forget()

        jv_list_label.grid_forget()
        jv_list_entry.grid_forget()
        root.geometry(gui_size)


def remove_newlines(event=None):
    spam = contract_name.get(1.0, "end-1c")
    contract_name.delete(1.0, tk.END)
    contract_name.insert(tk.END, spam.rstrip().replace("\n", " "))

    spam = jv_list_entry.get(1.0, "end-1c")
    jv_list_entry.delete(1.0, tk.END)
    jv_list_entry.insert(tk.END, spam.rstrip())

    spam = to.get(1.0, "end-1c")
    to.delete(1.0, tk.END)
    to.insert(tk.END, spam.rstrip())


## Gui
root = tk.Tk()
root.title("PyTender")
screen_width = root.winfo_screenwidth()
gui_size = "1000x500"
# root.geometry(gui_size + f"+{int(screen_width/8)}+0")
root.geometry(gui_size + "+0+0")
# root.resizable(False, False)
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

v_firm_name = tk.StringVar()
v_jv_name = tk.StringVar()
v_jv_addr = tk.StringVar()
jv = tk.IntVar()
large_or_small = tk.IntVar()
v_firm_addr = tk.StringVar()
short_name = tk.StringVar()
IoB = tk.StringVar()
Contract_ID = tk.StringVar()
days = tk.StringVar()
person = tk.StringVar()
date = tk.StringVar()
line_of_cr = tk.StringVar()
v_jv_repr = tk.StringVar()


try:
    settings = open(settings_path, "rb")
    data = pickle.load(settings)
except:
    pass

firm_frame = tk.Frame(root, bg="Snow3")
contract_frame = tk.Frame(root, bg="azure3")
button_frame = tk.Frame(root)

firm_frame.columnconfigure(1, weight=1)
firm_frame.grid(sticky="ew", ipady=2)

contract_frame.columnconfigure(1, weight=1)
contract_frame.grid(ipady=2, sticky="nsew")
contract_frame.rowconfigure(1, weight=1)
contract_frame.rowconfigure(4, weight=1)


tk.Label(firm_frame, text="Firm Name", bg="Snow3").grid(sticky="e")
firm_name = tk.Entry(firm_frame, textvariable=v_firm_name)
firm_name.grid(row=0, column=1, sticky="ew")
tk.Radiobutton(
    firm_frame, text="Single", variable=jv, value=1, command=check_status, bg="Snow3"
).grid(row=0, column=2, sticky="e")
tk.Radiobutton(
    firm_frame, text="JV", variable=jv, value=2, command=check_status, bg="Snow3"
).grid(row=0, column=3, sticky="e")
tk.Label(firm_frame, text="Firm Address", bg="Snow3").grid(row=1, sticky="e")
firm_addr = tk.Entry(firm_frame, textvariable=v_firm_addr)
firm_addr.grid(row=1, column=1, sticky="ew")

jvSubFrame = tk.Frame(firm_frame, bg="Snow3")
jv_name_label = tk.Label(jvSubFrame, text="JV Name", bg="Snow3")
jv_name_entry = tk.Entry(jvSubFrame, textvariable=v_jv_name)
jv_addr_label = tk.Label(jvSubFrame, text="JV Address", bg="Snow3")
jv_addr_entry = tk.Entry(jvSubFrame, textvariable=v_jv_addr)
jv_repr_label = tk.Label(jvSubFrame, text="JV Representative")
jv_repr_entry = tk.Entry(jvSubFrame, textvariable=v_jv_repr)

jv_list_label = tk.Label(
    firm_frame,
    text="JV Partners' Details\n( JVrank; Person; Post; Company; Address; Percentage )",
)
jv_list_entry = tk.Text(firm_frame, height=4, wrap="word")


tk.Label(contract_frame, text="Name of the Contract in short", bg="azure3").grid(
    sticky="e"
)
tk.Entry(contract_frame, textvariable=short_name).grid(row=0, column=1, sticky="ew")
tk.Label(contract_frame, text="Full Name of the Contract", bg="azure3").grid(
    sticky="ne"
)
contract_name = tk.Text(contract_frame, height=5, wrap="word")
contract_name.grid(row=1, column=1, sticky="nsew")
contract_name.bind("<FocusOut>", remove_newlines)
tk.Label(contract_frame, text="Invitation for Bid No.", bg="azure3").grid(sticky="e")
tk.Entry(contract_frame, textvariable=IoB).grid(row=2, column=1, sticky="ew")
tk.Label(contract_frame, text="Contract Identification No.", bg="azure3").grid(
    sticky="e"
)
tk.Entry(contract_frame, textvariable=Contract_ID).grid(row=3, column=1, sticky="ew")
tk.Label(contract_frame, text="To:", bg="azure3").grid(sticky="ne")
to = tk.Text(contract_frame, height=5)
to.insert(1.0, "The Chief of the Office,\n")
to.grid(row=4, column=1, sticky="nsew")
to.bind("<FocusOut>", remove_newlines)
tk.Label(contract_frame, text="Bid validity period", bg="azure3").grid(sticky="e")
tk.Entry(contract_frame, textvariable=days).grid(row=5, column=1, sticky="ew")
tk.Radiobutton(
    contract_frame,
    text="Letter of Bid",
    variable=large_or_small,
    value=1,
    command=check_status,
    bg="azure3",
).grid(row=6, column=1, sticky="w")
tk.Radiobutton(
    contract_frame,
    text="Letter of Technical Bid & Letter of Price Bid",
    variable=large_or_small,
    value=2,
    command=check_status,
    bg="azure3",
).grid(row=7, column=1, sticky="w")
tk.Label(contract_frame, text="Line of Credit", bg="azure3").grid(sticky="e")
loc_entry = tk.Entry(contract_frame, textvariable=line_of_cr)
loc_entry.configure(state="disabled")
loc_entry.grid(row=8, column=1, sticky="ew")
tk.Label(contract_frame, text="Authorized Person", bg="azure3").grid(
    row=11, column=0, sticky="e"
)
auth_person = tk.Entry(contract_frame, textvariable=person)
auth_person.grid(row=11, column=1, sticky="ew")
tk.Label(contract_frame, text="Date", bg="azure3").grid(row=12, column=0, sticky="e")
tk.Entry(contract_frame, textvariable=date).grid(row=12, column=1, sticky="ew")

generateBtn = tk.Button(
    contract_frame, text="Generate Documents", command=generate_documents
)
generateBtn.grid(row=12, column=2, columnspan=2, padx=15, pady=15)
generateBtn.configure(state="disabled")

try:
    firm_name.insert(0, data["FIRM"])
    firm_addr.insert(0, data["FIRM_ADDR"])
    auth_person.insert(0, data["PERSON"])
    designation = "Managing Director" if "pvt" in data["FIRM"].lower() else "Proprietor"
    jv_list_entry.insert(
        tk.END,
        f"2; {data['PERSON']}; {designation}; {data['FIRM']}; {data['FIRM_ADDR']}; 50",
    )
    jv_addr_entry.insert(0, data["FIRM_ADDR"])
    jv_repr_entry.insert(0, data["PERSON"])

except:
    pass

root.mainloop()
