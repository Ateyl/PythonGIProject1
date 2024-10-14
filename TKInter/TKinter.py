from tkinter import *
from tkinter import messagebox

from openpyxl.styles.alignment import horizontal_alignments

root = Tk()

root.title('TKinter sample app')
root.geometry('800x600')

# user_text = StringVar()
#
# user_entry = Entry(root, textvariable=user_text)
# user_entry.place(x=80, y=50)
#
# myLabel = Label(root, textvariable=user_text)
# myLabel.pack()

# myLabel1 = Label(root, text='HI!')
# myLabel2 = Label(root, text='HI!')
# myLabel3 = Label(root, text='HI!')
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=2, column=2)
# myLabel3.grid(row=1, column=1)
#
# def myClick(number):
#     # Label(root, text=f'hello {user_entry.get()} world!',).pack()
#     user_entry.delete(0, END)
#     user_entry.insert(0, int(number) ** 2)


# user_entry = Entry(root, width=300, bd=1)
# user_entry.pack()
# user_entry.insert(0, 'Please enter your name: ')
#
# myButton = Button(root, text='Click',fg='white', bg='black',padx=50, pady=15, command=lambda: myClick(user_entry.get()))
# myButton.pack()

# root.iconbitmap('my1.ico')

# image1 = PhotoImage(file='liq_spike_5000x2813.png')
# myLabel = Label(root, image=image1)
# myLabel.pack()

# color = tkinter.colorchooser.askcolor()
# print(color)
#
# quit_button = Button(root, text='EXIT', command=root.quit)
# quit_button.pack()
#
# frame = LabelFrame(root, text='I am frame', width=300, height=300)
# frame.pack()
#
# btn = Button(frame, text='click me')
# btn.place(x=0, y=0)
#
# radio_choice = IntVar()
# radio_choice.set(3)
#
#
# text_var = StringVar()
# def make_choice():
#     global text_var
#     text_var.set= (f'Your choice is {radio_choice.get()}')
#
# text_var= StringVar()
# def make_choice2():
#     global text_var
#     text_var.set(f'Your choice is {check_choice.get()}')
#
# Radiobutton(root, text='Choice 1', variable=radio_choice, value=1,command=make_choice).pack()
# Radiobutton(root, text='Choice 2', variable=radio_choice, value=2,command=make_choice).pack()
# Radiobutton(root, text='Choice 3', variable=radio_choice, value=3,command=make_choice).pack()
#
# myLabel= Label(root, textvariable=text_var)
# myLabel.pack()
#
# check_choice = StringVar()
# chk_box = Checkbutton(root, text='check me', variable=check_choice, command=make_choice2,onvalue='Selected', offvalue='Not selected')
# chk_box.deselect()
# chk_box.pack()
#
# r_message = StringVar()
# Label(root, textvariable=r_message).pack()
# def clicked():
#    response = messagebox.askyesno('I am title.', 'I am content of this window')
#
#    if not response:
#         r_message.set('you clickes NO')
#    else:
#        r_message.set('you clickes YES')

# Button(root, text='MessageBox', command=clicked).pack()

v_var = IntVar()
h_var = IntVar()

vertical = Scale(root, from_=0, to=5, variable=v_var)
vertical.pack()

horizontal = Scale(root, from_=0, to=5, orient=HORIZONTAL, variable=h_var)
horizontal.pack()

Label(root, textvariable=v_var).pack()
Label(root, textvariable=h_var).pack()

Button(root, text='click', command=lambda: print(horizontal.get(), vertical.get())).pack()
root.mainloop()