import sqlite3

database = "diccionario.db"
class conexion:
	def consulta(self, query):
		try:
			connection =  sqlite3.connect(database)
			cursor = connection.cursor()
			catch = cursor.execute(query)
			connection.commit()
			return catch
		except:
			print("Error de conexion para consulta")
	
	def parametros(self, query, params):
		try:
			connection =  sqlite3.connect(database)
			cursor = connection.cursor()
			catch = cursor.execute(query, params)
			connection.commit()
			return catch
		except:
			print("Error de conexion para parametros")
	
