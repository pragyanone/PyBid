import tkinter as tk
from pathlib import Path
import os
import pickle
from .classes import *


settings_path = os.path.join(os.path.dirname(__file__), 'PyTender-settings.pkl')

def generate_documents():
    D = {'FIRM':v_firm_name.get(), 'FIRM_ADDR':v_firm_addr.get(), 'PERSON':person.get()}
    settings = open(settings_path, 'wb')
    pickle.dump(D, settings)
     
    global path
    path = os.path.join(short_name.get(), 'SOURCE')
    Path(path).mkdir(parents=True, exist_ok=True)
    args = (path,
            v_firm_name.get(),
            v_firm_addr.get(),
            v_jv_name.get(),
            v_jv_addr.get(), 
            jv.get(),
            short_name.get(), 
            contract_name.get(1.0, 'end-1c'),
            IoB.get(),
            Contract_ID.get(), 
            to.get(1.0, 'end-1c'),
            days.get(), 
            line_of_cr.get(), 
            person.get().rstrip(), 
            date.get())
    
    DbtB = declaration(*args)
    DbtB.create_doc(24)

    if large_or_small.get() == 1:
        LoB = bid(*args)
        LoB.create_doc()
    elif large_or_small.get() == 2:
        LoTB = tech(*args)
        LoPB = price(*args)
        LoTB.create_doc()
        LoPB.create_doc()
    

    if 'pvt' not in v_firm_name.get().lower():
        PoA = poa_self(*args)
        PoA.create_doc(12)


def check_status(event=None):
    if large_or_small.get() == 2:
        loc_entry.configure(state='normal')
    else:
        loc_entry.configure(state='disabled')

    if jv.get() and large_or_small.get():
            generateBtn.configure(state='normal')

    if jv.get() == 2: 
        jv_name_label.grid(sticky='e')        
        jv_name_entry.grid(row=2, column=1, sticky='ew')
        jv_addr_label.grid(sticky='e')
        jv_addr_entry.grid(row=3, column=1, sticky='ew')

    if jv.get() == 1:
        jv_name_label.grid_forget()
        jv_name_entry.grid_forget()
        jv_addr_label.grid_forget()
        jv_addr_entry.grid_forget()


def remove_newlines(event=None):
    spam = contract_name.get(1.0, 'end-1c')
    contract_name.delete(1.0, tk.END)
    contract_name.insert(tk.END, spam.rstrip().replace('\n', ' '))


## Gui
root = tk.Tk()
root.title('PyTender')
root.columnconfigure(1, weight=5)
root.resizable(False, False)


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


try:
    settings = open(settings_path, 'rb')
    data = pickle.load(settings)
except: pass

firm_frame = tk.Frame(root, bg='Snow3')
contract_frame = tk.Frame(root, bg='azure3')
button_frame = tk.Frame(root)

firm_frame.columnconfigure(1, weight=1)
firm_frame.grid(sticky='ew', ipady=2)

contract_frame.columnconfigure(1, weight=1)
contract_frame.grid(ipady=2)


tk.Label(firm_frame, text='Firm Name', bg='Snow3').grid(sticky='e')
firm_name = tk.Entry(firm_frame, textvariable=v_firm_name)
firm_name.grid(row=0, column=1, sticky='ew')
tk.Radiobutton(firm_frame, text='Single',variable=jv, value=1, command=check_status, bg='Snow3').grid(row=0, column=2, sticky='e')
tk.Radiobutton(firm_frame, text='JV', variable=jv, value=2, command=check_status, bg='Snow3').grid(row=0, column=3, sticky='e')
tk.Label(firm_frame, text='Firm Address', bg='Snow3').grid(row=1, sticky='e')
firm_addr = tk.Entry(firm_frame, textvariable=v_firm_addr)
firm_addr.grid(row=1, column=1, sticky='ew')
jv_name_label = tk.Label(firm_frame, text='JV Name', bg='Snow3')
jv_name_entry = tk.Entry(firm_frame, textvariable=v_jv_name)
jv_addr_label = tk.Label(firm_frame, text='JV Address', bg='Snow3')
jv_addr_entry = tk.Entry(firm_frame, textvariable=v_jv_addr)

tk.Label(contract_frame, text='Name of the Contract in short', bg='azure3').grid(sticky='e')
tk.Entry(contract_frame, textvariable=short_name).grid(row=0, column=1, sticky='ew')
tk.Label(contract_frame, text='Full Name of the Contract', bg='azure3').grid(sticky='ne')
contract_name = tk.Text(contract_frame, height=5, wrap='word')
contract_name.grid(row=1, column=1, sticky='ew')
contract_name.bind('<FocusOut>', remove_newlines)
tk.Label(contract_frame, text='Invitation for Bid No.', bg='azure3').grid(sticky='e')
tk.Entry(contract_frame, textvariable=IoB).grid(row=2, column=1, sticky='ew')
tk.Label(contract_frame, text='Contract Identification No.', bg='azure3').grid(sticky='e')
tk.Entry(contract_frame, textvariable=Contract_ID).grid(row=3, column=1, sticky='ew')
tk.Label(contract_frame, text='To:', bg='azure3').grid(sticky='ne')
to = tk.Text(contract_frame, height=5)
to.insert(1.0, 'The Chief of the Office,\n')
to.grid(row=4, column=1, sticky='ew')
tk.Label(contract_frame, text='Bid validity period', bg='azure3').grid(sticky='e')
tk.Entry(contract_frame, textvariable=days).grid(row=5, column=1, sticky='ew')
tk.Radiobutton(contract_frame, text='Letter of Bid', variable=large_or_small, value=1, command=check_status, bg='azure3').grid(row=6, column=1, sticky='w')
tk.Radiobutton(contract_frame, text='Letter of Technical Bid & Letter of Price Bid', variable=large_or_small, value=2, command=check_status, bg='azure3').grid(row=7, column=1, sticky='w')
tk.Label(contract_frame, text='Line of Credit', bg='azure3').grid(sticky='e')
loc_entry = tk.Entry(contract_frame, textvariable=line_of_cr)
loc_entry.configure(state='disabled')
loc_entry.grid(row=8, column=1, sticky='ew')
tk.Label(contract_frame, text='Authorized Person', bg='azure3').grid(row=11, column=0, sticky='e')
auth_person = tk.Entry(contract_frame, textvariable=person)
auth_person.grid(row=11, column=1, sticky='ew')
tk.Label(contract_frame, text='Date', bg='azure3').grid(row=12, column=0, sticky='e')
tk.Entry(contract_frame, textvariable=date).grid(row=12, column=1, sticky='ew')

generateBtn = tk.Button(contract_frame, text='Generate Documents', command=generate_documents)
generateBtn.grid(column=2, sticky='sw', columnspan=2, padx=15, pady=15)
generateBtn.configure(state='disabled')

try:
    firm_name.insert(0, data['FIRM'])
    firm_addr.insert(0, data['FIRM_ADDR'])
    jv_addr_entry.insert(0, data['FIRM_ADDR'])
    auth_person.insert(0, data['PERSON'])
except: pass

root.mainloop()