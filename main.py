from sqlite3.dbapi2 import Cursor
from tkinter import *
from tkinter import ttk
from tkhtmlview import *
from database import conexion
from editor import *


def diccionario():
    def select(event):
        db = conexion()
        c = lista.curselection()
        
        if c:
            index = c[0]
            dato = event.widget.get(index)
            #print(dato)
            query = f"SELECT * FROM terminos WHERE rubro = '{dato}'"
            rows = db.consulta(query)
            
            for row in rows:
                r.delete('1.0', END)
                r.insert(END, f"{row[1]}: \n\n{row[2]}")       
        else:
            print("Error")        

    def show():
        db = conexion()
        query = "SELECT rubro FROM terminos ORDER BY rubro DESC"
        rows = db.consulta(query)
        lista.delete(0,END)
        for row in rows:		
            lista.insert(0,row[0])
    
    def srch():
        termino = se.get()
        db = conexion()
        query = f"SELECT rubro FROM terminos WHERE concepto = %'{termino}'%"
        rows = db.consulta(query)
        lista.delete(0,END)
        for row in rows:		
            lista.insert(0,row[0])    

    app  = Tk()
    app.title("Diccionario Enciclopédico DIER")
    app.geometry("710x620")
    #app.geometry("400x80")
    app.resizable(0,0)
    sidef = Frame(app)
    sidef.pack(side=LEFT, fill=BOTH, expand=True)
    lista = Listbox(sidef)
    lista.config(width=28)
    lista.pack(side=LEFT, fill=BOTH, expand=True)
    show()    
    lista.bind('<<ListboxSelect>>', select)
    
    scroll_lista = Frame(sidef)
    scroll_lista.pack(side=RIGHT,fill=Y, expand=True)
    s_lista = Scrollbar(scroll_lista, command=lista.yview)
    s_lista.pack(side=RIGHT, fill=Y)
    lista.config(yscrollcommand=s_lista.set)
    
    
    f =Frame(app)
    f.pack(fill=BOTH, expand=True)
    scroll_r = Frame(f)
    scroll_r.pack(side=RIGHT,fill=Y, expand=True)
    #htmlf = HTMLScrolledText(f, html=select)
    #htmlf.pack(expand=True, fill=BOTH)
    r = Text(f)
    r.tag_configure(tagName="texto", lmargin1=150, rmargin=150)
    r.pack(expand=True, fill=BOTH)
     
    s_r = Scrollbar(scroll_r, command=r.yview)
    s_r.pack(side=RIGHT, fill=Y)
    r.config(yscrollcommand=s_r.set)

    b = Frame(app)
    b.pack(fill=X)
    Button(b, text="Listar", command=show).pack(side=LEFT)
    Label(b, text="Buscar término").pack(side=LEFT, ipadx=5)
    
    se = StringVar()
    search  =  Entry(b, textvariable=se)
    search.pack(side=LEFT, expand=True, fill=X)
    
    Button(b, text="Buscar", command=srch).pack(side=LEFT)
    Button(b, text="Editar", command=editor).pack(side=LEFT)
    mainloop()

if __name__=="__main__":
    diccionario()