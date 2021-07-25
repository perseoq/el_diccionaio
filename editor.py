from sqlite3.dbapi2 import Cursor
from tkinter import *
from tkinter import ttk
from database import conexion




def editor():

	def select(event):
		db = conexion()
		cursor = lista.curselection()
		print("es el cursor: " + str(cursor))
		try:
			index = cursor[0]
			data = event.widget.get(index)
			print("el elemento es: " + data)
			query = f"DELETE FROM terminos WHERE rubro='{data}'"
			db.consulta(query)
			show()

		except:
			print("selecciona algo")
		
		
	def insertar():
		db = conexion()
		if(len(rubro.get())>0 and len(concepto.get("1.0","end-1c"))>0):
			query = "INSERT INTO terminos(rubro, concepto) VALUES(?, ?)"
			params = (rubro.get(), concepto.get("1.0","end-1c"))
			db.parametros(query,params)
			show()
			rubro.delete(0,END)
			concepto.delete('1.0', END)
	def show():
		db = conexion()
		query = "SELECT rubro FROM terminos ORDER BY rubro DESC"
		rows = db.consulta(query)
		lista.delete(0,END)
		for row in rows:		
			lista.insert(0,row[0])

	app = Toplevel()
	app.title("Editor del Diccionario")
	#app.geometry("900x600")
	app.resizable(0,0)

	left = LabelFrame(app, text="Nueva Entrada")
	left.pack(fill=BOTH, expand=True, side=LEFT, pady=10, padx=5)
	right = Frame(app)
	right.pack(fill=Y, expand=True, side=LEFT, pady=10, padx=5)
	
	Label(left, text="Ingresa un término o rubro").grid(row=0, column=0, sticky="w", padx=5)
	
	rubrovar = StringVar()
	rubro = Entry(left, textvariable=rubrovar)
	rubro.grid(row=1, column=0, sticky="we", columnspan=2, padx=5)
	
	Label(left, text="Redacta referencia o concépto").grid(row=2, column=0, sticky="w", padx=5)
	
	concepto = Text(left)
	concepto.grid(row=3, column=0, sticky="nw", columnspan=2, padx=5)
	
	Button(left, text="Guardar", command=insertar).grid(row=4, column=0, columnspan=2, sticky="we")
	# Button(left, text="Actualizar", command=show).grid(row=4, column=1, sticky="we")

	Label(right, text="Doble click para \n borrar elementos").pack()
	lista = Listbox(right, height=28)

	lista.bind('<Double-1>', select)
	lista.pack(side=TOP, fill=Y)
	show()

	scroll_lista = Frame(app)
	scroll_lista.pack(side=RIGHT, fill=Y, expand=True)
	s_lista = Scrollbar(scroll_lista, command=lista.yview)
	s_lista.pack(side=RIGHT, fill=Y)
	lista.config(yscrollcommand=s_lista.set)


	



	app.mainloop()




#if __name__=="__main__":
#	editor()


