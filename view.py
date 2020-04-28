from tkinter import Tk, Frame, Label, Entry, Button, StringVar, OptionMenu



def close_window(window, action):
    global status

    if action == 'send':
        status = 'submit'
    else:
        status = 'cancel'

    window.destroy()


def createframe(window, frame, num, func):
    num = num
    global rownum

    options = ['PDM Report', 'Brio to SSRS', 'CPE -NA', 'CPE- SAPL', 'Evergreen', 'QV Monitoring', 'QV-Power BI',
               'WebFocus', 'IICE', 'Sales Cube',
               'DMM', 'Learning', 'Cognos-PBI', 'IO Modelling', 'FIDO', 'DBA', 'Bedrock']

    clicked = StringVar()
    clicked.set(options[0])

    if func == 'add':
        projects = OptionMenu(frame, clicked, *options).grid(row=num, column=0, padx=30)
        workhours = Entry(frame, width=10, borderwidth=5)
        workhours.grid(row=num, column=2, padx=10, pady=10)
        projectslist.append(clicked)
        rownum += 1

    if func == 'delete':
        lists = frame.grid_slaves()
        if len(lists) > 0:
            lists[0].destroy()
            lists[1].destroy()

    if func == 'show':
        children_widgets = frame.winfo_children()
        for child_widget in children_widgets:
            if child_widget.winfo_class() == 'Entry':
                hours.append(child_widget.get())

        for i in projectslist:
            finallist.append(i.get())

        close_window(window, 'send')


def createwindowpane(window):
    window.title('Timesheet')

    frame = Frame(window)
    frame.pack(padx=1, pady=1)

    frame1 = Frame(window)
    frame1.pack(padx=10, pady=10)

    frame2 = Frame(window, padx=50, pady=10)
    frame2.pack(padx=10, pady=10)

    lbl_project = Label(frame, text='Projects').grid(padx=60, row=0, column=0)
    lbl_hoursworked = Label(frame, text='Hours Worked').grid(row=0, column=1)

    createframe(window, frame1, 1, 'add')

    addbtn = Button(frame2, text='Add Project', width=10,
                    command=lambda: createframe(window, frame1, rownum, 'add')).grid(row=2, column=0, padx=30)
    deletebtn = Button(frame2, text='Delete Project', width=10,
                       command=lambda: createframe(window, frame1, rownum, 'delete')).grid(row=2, column=1, padx=30)
    submit = Button(frame2, text='Submit', width=10, command=lambda: createframe(window, frame1, rownum, 'show')).grid(
        row=2, column=3, padx=30)

    window.mainloop()

rownum = 1
projectslist = []
finallist = []
hours = []
status = ''