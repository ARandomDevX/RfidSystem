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
def fpbar(fname,lname,klasse,id,erw1,erw2,add,n1,n2):
    enum = 0
    from Schritt3_support import probar
    try:
        from sql import nsa
        nsa.nsa(fname=fname,lname=lname,klasse=klasse,erw1=erw1,erw2=erw2,add=add,n1=n1,n2=n2)
        probar.set(50.0)
        from time import sleep
        sleep(0.5)
        probar.set(60.0)
        sleep(0.5)
        probar.set(100.0)
    except:
        from tkinter import messagebox
        probar.set(0.0)
        messagebox.showerror("ein fehler ist aufgetreten","Ein fehler ist aufgetreten der rechner guckt was es war und versucht es herauszufinden")
        if fname == "" or lname == "" or klasse == "" or id == "" or id.isdigit == False or erw1 == "" or erw2=="" or n1.isdigit == False or n1 == "" or n2.isdigit == False or n2 == "" or add == "":
            from time import sleep
            sleep(1)
            enum +=1
            messagebox.showinfo("Gefunden...",
                                "Der rechner hat gerade das problem herausgefunden,Sie haben die daten falsh eingegeben")
            messagebox.showinfo("Geben","Bitte geben sie die daten nochmall richtigein.")
        from time import sleep
        time.sleep(1)
    finally:
        if enum == 1:
            messagebox.showinfo("fertig","Die person wurde nicht eingetragen")
            from sql import cur
            cur.execute("SELECT id FROM student WHERE id = {}".format(id))
            if cur.rowcount > 0 :
                cur.execute('DELETE * FROM student WHERE id = {}'.format(id))
            else:
                pass
        else:
            messagebox.showinfo("fertig","Die Person ist eingetragen")
