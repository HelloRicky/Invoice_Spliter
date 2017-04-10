from Tkinter import *
from tkFileDialog import askopenfilename
import tkMessageBox
import splitPDF

# initial
app = Tk() # create a Tk app window
app_title = "Eutility Invoice Spliter"
w = 550 # width for the Tk app
h = 150 # height for the Tk app

# get screen width and height
ws = app.winfo_screenwidth() # width of the screen
hs = app.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk app window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

app.title(app_title)

# set dimensions of the screen
app.geometry('%dx%d+%d+%d' % (w, h, x, y))

"""
action function:

"""

def load_file():
    fname = askopenfilename(filetypes=(("PDF files", "*.pdf"), ("All files", "*.*")))
    if fname:
        try:
            labelText.set(fname)
        except:
            showerror("Open Source File", "Failed to read file\n'%s'" % fname)
        return

def msgbox(msg, type='Alert'):
    return tkMessageBox.showinfo(type, msg)

def split_file():
    pages_list = []
    path = labelText.get()
    pages_val = splitPage.get().strip()

    # input file can't be empty
    if not path:
        return msgbox('Please select a PDF')

    # split page can't be empty
    if not pages_val:
        return msgbox('Please entry the split page')

    # check if pages are integer
    pages_split = pages_val.split(',')
    for p in pages_split:
        p = p.strip()   # remove all space
        if p:
            try:
                num = int(p)
                pages_list.append(num)
            except:
                return msgbox('All page must be integer number')
    action_result = splitPDF.splitPdf(path, pages_list)
    if action_result == True:
        return msgbox("File generated", "Successful")
    return msgbox(action_result)

"""
app content

"""
# 1. select a file

btn_browse = Button(app, text='1. Select a PDF', width = 10, command=load_file)
btn_browse.grid(row = 0, sticky=W)

# labels after selection
labelText = StringVar()
#labelText.set()
label1 = Label(app, textvariable=labelText)
label1.grid(row = 0, column = 1, pady=15, sticky=W)

# 2. enter split page
label2 = Label(app, text='2. Entry split page numer. e.g. 2, 4, 6')
label2.grid(row=1, columnspan=2, sticky=W)

# page field
custName = StringVar(None)
splitPage = Entry(app, width = 50, textvariable=custName)
splitPage.grid(row = 3, columnspan=2, sticky=W+E)

# 3. split button
btn_split = Button(app, text='3. Split Files', width=10, command=split_file)
btn_split.grid(row = 4, sticky=W, pady=15)

# main loop
app.mainloop()
