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

tk.Label(root, text='Firm Name').grid(row=0, column=0, sticky='e')
firm_name = tk.Entry(root, textvariable=v_firm_name)
firm_name.grid(row=0, column=1, sticky='ew', ipady=10)
try:
    firm_name.insert(0, data['FIRM'])
except: pass

tk.Radiobutton(root, text='Single',variable=jv, value=1, command=check_status).grid(row=0, column=2)
tk.Radiobutton(root, text='JV', variable=jv, value=2, command=check_status).grid(row=0, column=3)
tk.Label(root, text='Firm Address').grid(row=1, column=0, sticky='e')
firm_addr = tk.Entry(root, textvariable=v_firm_addr)
firm_addr.grid(row=1, column=1, sticky='ew')
try:
    firm_addr.insert(0, data['FIRM_ADDR'])
except: pass

tk.Label(root, text='Name of the Contract in short').grid(row=2, column=0, sticky='e')
tk.Entry(root, textvariable=short_name).grid(row=2, column=1, sticky='ew')
tk.Label(root, text='Full Name of the Contract').grid(row=3, column=0, sticky='ne')
contract_name = tk.Text(root, height=5, wrap='word')
contract_name.grid(row=3, column=1, sticky='ew')
contract_name.bind('<FocusOut>', remove_newlines)
tk.Label(root, text='Invitation for Bid No.').grid(row=4, column=0, sticky='e')
tk.Entry(root, textvariable=IoB).grid(row=4, column=1, sticky='ew')
tk.Label(root, text='Contract Identification No.').grid(row=5, column=0, sticky='e')
tk.Entry(root, textvariable=Contract_ID).grid(row=5, column=1, sticky='ew')
tk.Label(root, text='To:').grid(row=6, column=0, sticky='ne')
to = tk.Text(root, height=5)
to.insert(1.0, 'The Chief of the Office,\n')
to.grid(row=6, column=1, sticky='ew')
tk.Label(root, text='Bid validity period').grid(row=7, column=0, sticky='e')
tk.Entry(root, textvariable=days).grid(row=7, column=1, sticky='ew')
tk.Radiobutton(root, text='Letter of Bid', variable=large_or_small, value=1, command=check_status).grid(row=8, column=1, sticky='w')
tk.Radiobutton(root, text='Letter of Technical Bid & Letter of Price Bid', variable=large_or_small, value=2, command=check_status).grid(row=9, column=1, sticky='w')

tk.Label(root, text='Line of Credit').grid(row=10, column=0, sticky='e')
loc_entry = tk.Entry(root, textvariable=line_of_cr)
loc_entry.configure(state='disabled')
loc_entry.grid(row=10, column=1, sticky='ew')

tk.Label(root, text='Authorized Person').grid(row=11, column=0, sticky='e')
auth_person = tk.Entry(root, textvariable=person)
auth_person.grid(row=11, column=1, sticky='ew')
try:
    auth_person.insert(0, data['PERSON'])
except: pass

tk.Label(root, text='Date').grid(row=12, column=0, sticky='e')
tk.Entry(root, textvariable=date).grid(row=12, column=1, sticky='ew')
generateBtn = tk.Button(root, text='Generate Documents', command=generate_documents)
generateBtn.configure(state='disabled')
generateBtn.grid(column=2, sticky='e', columnspan=2, padx=15, pady=15)

root.mainloop()