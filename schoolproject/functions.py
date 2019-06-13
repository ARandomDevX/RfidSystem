class raise_frame:
    def raise_frame(frame):
        frame.tkarise()
def delete():
    import tkinter.messagebox

    question1 = tkinter.messagebox.askquestion("LETZTE WARNUNG!!!", "Sind sie sich sicher das sie diesen schüler löschen möchten?", icon='warning')
    if (question1):
        from sql import delete
        delete.delete()
    tkinter.mainloop()
def onActiveRaiseFrame():
    from Schritt2 import Toplevel1 as t1
    from sql import nsa