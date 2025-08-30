import tkinter as tk
from tkinter import ttk

#   tk declaration
root = tk.Tk()
root.geometry('500x500')
root.title('Store Information')
root.geometry('400x700')
root.resizable(False, False)

#   storing widget
frame = ttk.LabelFrame(root)
frame.pack(expand = False, fill='both', anchor='s', padx=5, pady=2)

#   text entry widget for name 
name_label = ttk.Label(frame, text='Name').grid(row=1,column=1)
name_entry = ttk.Entry(frame, width=15).grid(row=1,column=2)

#   text entry widget for rank
rank_label = ttk.Label(frame, text='Rank').grid(row=2, column=1)
rank_entry = ttk.Entry(frame, width=15).grid(row=2, column=2)

#   insert button
insert_button = ttk.Button(frame, text='insert').grid(row=3, column=2)

#   treeview layout
treeview = ttk.Treeview(root, columns=('Date', 'Name'), show='headings')
treeview.pack(expand=True, fill='both', padx=10, pady=10)
treeview.heading(column=0, text='Rank')
treeview.heading(column=1, text='Name')

root.mainloop()