def raise_frame(frame):
    frame.tkarise()
def onActiveRaiseFrame(fname,lname):

    from Notfall import Toplevel1 as t1
    raise_frame(t1())
def delete():
    import tkinter.messagebox

    question1 = tkinter.messagebox.askquestion("LETZTE WARNUNG!!!", "Sind sie sich sicher das sie diesen schüler löschen möchten?", icon='warning')
    if (question1):
        from sql import delete
        delete.delete()
