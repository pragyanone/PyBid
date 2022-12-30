import tkinter as tk
from pathlib import Path
import os
import pickle
from .classes import *

settings_path = os.path.join("PyBid-settings.pkl")


def generate_documents():
    details = {
        "FIRM": firm_name.get(),
        "FIRM_ADDR": firm_addr.get(),
        "PERSON": auth_person.get(),
        "DESIGNATION": auth_person_designation.get(),
    }
    previous_data = {
        "SHORT_NAME": short_name.get(),
        "FULL_NAME": full_name_text.get(1.0, "end-1c"),
        "IOB": IoB.get(),
        "CONTRACT_ID": contract_ID.get(),
        "TO": to_text.get(1.0, "end-1c"),
        "BID_VALIDITY_PERIOD": bid_validity_period.get(),
        "LOC": loc.get(),
        "DATE": date.get(),
        "JV_NAME": jv_name.get(),
        "JV_ADDR": jv_addr.get(),
        "JV_REPR": jv_repr.get(),
        "JV_LIST": jv_list_text.get(1.0, "end-1c"),
    }
    settings = open(settings_path, "wb")
    pickle.dump((details, previous_data), settings)

    global path
    path = os.path.join(short_name.get(), "SOURCE")
    Path(path).mkdir(parents=True, exist_ok=True)
    args = (
        path,
        firm_name.get(),
        firm_addr.get(),
        jv_name.get(),
        jv_addr.get(),
        jv_repr.get(),
        single_or_jv.get(),
        short_name.get(),
        full_name_text.get(1.0, "end-1c"),
        IoB.get(),
        contract_ID.get(),
        to_text.get(1.0, "end-1c"),
        bid_validity_period.get(),
        loc.get(),
        auth_person.get().rstrip(),
        auth_person_designation.get(),
        date.get(),
        jv_list_text.get(1.0, "end-1c"),
    )

    result, resultColor = "SUCCESS", "lime green"
    try:
        if small_or_large.get() == 1:
            LoB = bid(*args)
            LoB.create_doc()
        elif small_or_large.get() == 2:
            LoTB = tech(*args)
            LoPB = price(*args)
            LoTB.create_doc()
            LoPB.create_doc()
        elif small_or_large.get() == 3:
            LoB = sealedQ(*args)
            LoB.create_doc()
        DbtB = declaration(*args)
        DbtB.create_doc()
        if single_or_jv.get() == 2:
            jvAgr = jv_agr(*args)
            jvAgr.create_doc()
            JVPoA = jv_poa(*args)
            JVPoA.create_doc()
        # if "pvt" not in firm_name.get().lower():
        #    PoAself = poa_self(*args)
        #    PoAself.create_doc()
    except Exception as e:
        import traceback

        result = "FAILED!\nCheck console\nfor error message"
        print(traceback.format_exc())
        resultColor = "Pink"

    EndofCode_label = tk.Label(contract_frame, text=result, bg=resultColor)
    EndofCode_label.grid(padx=20, row=7, column=2, rowspan=4, sticky="nsew")


def check_status(event=None):
    if small_or_large.get() == 2:
        loc_entry.configure(state="normal")
    else:
        loc_entry.configure(state="disabled")

    if small_or_large.get():
        if single_or_jv.get() == 1:
            generate_button.configure(state="normal")

        elif single_or_jv.get() == 2:
            if jv_name_entry.get():
                generate_button.configure(state="normal")
            else:
                generate_button.configure(state="disabled")

    if single_or_jv.get() == 2:
        jvSubFrame.grid(row=2, column=1, sticky="ew")
        jvSubFrame.columnconfigure(1, weight=3)
        jvSubFrame.columnconfigure(3, weight=2)

        jv_name_label.grid(row=0, column=0, sticky="e")
        jv_name_entry.grid(row=0, column=1, columnspan=3, sticky="ew")

        jv_addr_label.grid(row=1, column=0, sticky="e")
        jv_addr_entry.grid(row=1, column=1, sticky="ew")

        jv_repr_label.grid(row=1, column=2, sticky="e")
        jv_repr_entry.grid(row=1, column=3, sticky="ew")

        jv_list_label.grid(column=0, columnspan=4, sticky="ew")
        jv_list_text.grid(column=0, columnspan=4, sticky="ew")

        root.geometry("1000x600")

    if single_or_jv.get() == 1:
        jv_name_entry.delete(0, tk.END)
        jvSubFrame.grid_forget()
        root.geometry(gui_size)


def prettify(widget, event=None):
    if type(widget) == tk.Entry:
        spam = widget.get()
        widget.delete(0, tk.END)
    elif type(widget) == tk.Text:
        spam = widget.get(1.0, "end-1c")
        widget.delete(1.0, tk.END)
    if widget == full_name_text:
        spam = spam.replace("\n", " ")
    widget.insert(tk.END, spam.strip())


def load_previous():
    previous_data = settings[1]
    widgets = (
        short_name_entry,
        full_name_text,
        IoB_entry,
        contract_ID_entry,
        to_text,
        bid_validity_period_entry,
        loc_entry,
        date_entry,
        jv_name_entry,
        jv_addr_entry,
        jv_repr_entry,
        jv_list_text,
    )
    for widget, key in zip(widgets, previous_data):
        if type(widget) == tk.Entry:
            widget.delete(0, tk.END)
        elif type(widget) == tk.Text:
            widget.delete(1.0, tk.END)
        widget.insert(tk.END, previous_data[key])


## Gui
root = tk.Tk()
root.title("PyBid (ShresthaPragyan.com.np)")
gui_size = "1000x500"
root.geometry(gui_size + "+0+0")
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

firm_name = tk.StringVar()
firm_addr = tk.StringVar()
single_or_jv = tk.IntVar()
single_or_jv.set(1)
short_name = tk.StringVar()
IoB = tk.StringVar()
contract_ID = tk.StringVar()
bid_validity_period = tk.StringVar()
small_or_large = tk.IntVar()
loc = tk.StringVar()
auth_person = tk.StringVar()
auth_person_designation = tk.StringVar()
date = tk.StringVar()
jv_name = tk.StringVar()
jv_addr = tk.StringVar()
jv_repr = tk.StringVar()

try:
    settings = pickle.load(open(settings_path, "rb"))
    details = settings[0]
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


firm_name_label = tk.Label(firm_frame, text="Firm Name", bg="Snow3")
firm_name_label.grid(sticky="e")

firm_name_entry = tk.Entry(firm_frame, textvariable=firm_name)
firm_name_entry.grid(row=0, column=1, sticky="ew")

single_radio = tk.Radiobutton(
    firm_frame,
    text="Single",
    variable=single_or_jv,
    value=1,
    command=check_status,
    bg="Snow3",
)
single_radio.grid(row=0, column=2, sticky="e")

jv_radio = tk.Radiobutton(
    firm_frame,
    text="JV",
    variable=single_or_jv,
    value=2,
    command=check_status,
    bg="Snow3",
)
jv_radio.grid(row=0, column=3, sticky="e")

firm_addr_label = tk.Label(firm_frame, text="Firm Address", bg="Snow3")
firm_addr_label.grid(row=1, sticky="e")

firm_addr_entry = tk.Entry(firm_frame, textvariable=firm_addr)
firm_addr_entry.grid(row=1, column=1, sticky="ew")


jvSubFrame = tk.Frame(firm_frame, bg="Snow3")

jv_name_label = tk.Label(jvSubFrame, text="JV Name", bg="Snow3")
jv_name_entry = tk.Entry(jvSubFrame, textvariable=jv_name)
jv_addr_label = tk.Label(jvSubFrame, text="JV Address", bg="Snow3")
jv_addr_entry = tk.Entry(jvSubFrame, textvariable=jv_addr)
jv_repr_label = tk.Label(jvSubFrame, text="JV Representative", bg="Snow3")
jv_repr_entry = tk.Entry(jvSubFrame, textvariable=jv_repr)
jv_list_label = tk.Label(
    jvSubFrame,
    text="JV Partners' Details\n( JVrank;    Authorized Person;    Post;    Company;    Address;    Percentage )",
)
jv_list_text = tk.Text(jvSubFrame, height=4, wrap="word")


short_name_label = tk.Label(
    contract_frame, text="Name of the Contract in short", bg="azure3"
)
short_name_label.grid(sticky="e")

short_name_entry = tk.Entry(contract_frame, textvariable=short_name)
short_name_entry.grid(row=0, column=1, sticky="ew")

full_name_label = tk.Label(
    contract_frame, text="Full Name of the Contract", bg="azure3"
)
full_name_label.grid(sticky="ne")

full_name_text = tk.Text(contract_frame, height=5, wrap="word")
full_name_text.grid(row=1, column=1, sticky="nsew")

IoB_label = tk.Label(contract_frame, text="Invitation for Bid No.", bg="azure3")
IoB_label.grid(sticky="e")

IoB_entry = tk.Entry(contract_frame, textvariable=IoB)
IoB_entry.grid(row=2, column=1, sticky="ew")

contract_ID_label = tk.Label(
    contract_frame, text="Contract Identification No.", bg="azure3"
)
contract_ID_label.grid(sticky="e")

contract_ID_entry = tk.Entry(contract_frame, textvariable=contract_ID)
contract_ID_entry.grid(row=3, column=1, sticky="ew")

to_label = tk.Label(contract_frame, text="To:", bg="azure3")
to_label.grid(sticky="ne")

to_text = tk.Text(contract_frame, height=5)
to_text.insert(1.0, "The Chief of the Office,\n")
to_text.grid(row=4, column=1, sticky="nsew")

bid_validity_period_label = tk.Label(
    contract_frame, text="Bid validity period", bg="azure3"
)
bid_validity_period_label.grid(sticky="e")

bid_validity_period_entry = tk.Entry(contract_frame, textvariable=bid_validity_period)
bid_validity_period_entry.grid(row=5, column=1, sticky="ew")

small_radio = tk.Radiobutton(
    contract_frame,
    text="Single Envelope",
    variable=small_or_large,
    value=1,
    command=check_status,
    bg="azure3",
)
small_radio.grid(row=6, column=1, sticky="w")

large_radio = tk.Radiobutton(
    contract_frame,
    text="Double Envelope",
    variable=small_or_large,
    value=2,
    command=check_status,
    bg="azure3",
)
large_radio.grid(row=7, column=1, sticky="w")

sealedQ_radio = tk.Radiobutton(
    contract_frame,
    text="Sealed Quotation",
    variable=small_or_large,
    value=3,
    command=check_status,
    bg="azure3",
)
sealedQ_radio.grid(row=8, column=1, sticky="w")

loc_label = tk.Label(contract_frame, text="Line of Credit", bg="azure3")
# loc_label.grid(sticky="e")

loc_entry = tk.Entry(contract_frame, textvariable=loc)
loc_entry.configure(state="disabled")
# loc_entry.grid(row=8, column=1, sticky="ew")

auth_person_label = tk.Label(contract_frame, text="Authorized Person", bg="azure3")
auth_person_label.grid(row=11, column=0, sticky="e")

auth_person_frame = tk.Frame(contract_frame)
auth_person_frame.grid(row=11, column=1, sticky="ew")
auth_person_frame.columnconfigure(0, weight=1)
auth_person_frame.columnconfigure(2, weight=1)

auth_person_entry = tk.Entry(auth_person_frame, textvariable=auth_person)
auth_person_entry.grid(sticky="ew")

auth_person_designation_label = tk.Label(
    auth_person_frame, text="Designation", bg="azure3"
)
auth_person_designation_label.grid(row=0, column=1)

auth_person_designation_entry = tk.Entry(
    auth_person_frame, textvariable=auth_person_designation
)
auth_person_designation_entry.grid(row=0, column=2, sticky="ew")

date_label = tk.Label(contract_frame, text="Date", bg="azure3")
date_label.grid(row=12, column=0, sticky="e")

date_entry = tk.Entry(contract_frame, textvariable=date)
date_entry.grid(row=12, column=1, sticky="ew")

load_previous_button = tk.Button(
    contract_frame, text="Load Previous Data", command=load_previous
)
load_previous_button.grid(padx=15, pady=15, row=1, column=2, columnspan=2)

generate_button = tk.Button(
    contract_frame, text="Generate Documents", command=generate_documents
)
generate_button.grid(padx=15, pady=15, row=12, column=2, columnspan=2)
generate_button.configure(state="disabled")

firm_name_entry.bind("<FocusOut>", lambda _: prettify(firm_name_entry))
firm_addr_entry.bind("<FocusOut>", lambda _: prettify(firm_addr_entry))
jv_name_entry.bind("<FocusOut>", lambda _: [check_status(), prettify(jv_name_entry)])
jv_addr_entry.bind("<FocusOut>", lambda _: prettify(jv_addr_entry))
jv_repr_entry.bind("<FocusOut>", lambda _: prettify(jv_repr_entry))
jv_list_text.bind("<FocusOut>", lambda _: prettify(jv_list_text))
full_name_text.bind("<FocusOut>", lambda _: prettify(full_name_text))
loc_entry.bind("<FocusOut>", lambda _: prettify(loc_entry))
to_text.bind("<FocusOut>", lambda _: prettify(to_text))

try:
    # designation = (
    #    "Managing Director" if "pvt" in details["FIRM"].lower() else "Proprietor"
    # )

    firm_name_entry.insert(tk.END, details["FIRM"])
    firm_addr_entry.insert(tk.END, details["FIRM_ADDR"])
    auth_person_entry.insert(tk.END, details["PERSON"])
    auth_person_designation_entry.insert(tk.END, details["DESIGNATION"])
    jv_list_text.insert(
        tk.END,
        f"2; {details['PERSON']}; {details['DESIGNATION']}; {details['FIRM']}; {details['FIRM_ADDR']}; 50",
    )
    jv_addr_entry.insert(tk.END, details["FIRM_ADDR"])
    jv_repr_entry.insert(tk.END, details["PERSON"])
except:
    pass

root.mainloop()
