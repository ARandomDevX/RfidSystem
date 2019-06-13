class raise_frame:
    def raise_frame(frame):
        frame.tkarise()
def delete():
    import tkinter.messagebox

    question1 = tkinter.messagebox.askquestion("LETZTE WARNUNG!!!", "Sind sie sich sicher das sie diesen schüler löschen möchten?", icon='warning')
    if (question1):
        import mysql.connector.connection
