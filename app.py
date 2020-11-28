import sqlite3, time
import sys, getpass
import hashlib

# variables sin valor inicial
conexion = None
cursor = None
usuario = None
contraseña = None

# crea conexion con la base de datos 'database.db' ubicada en mismo path
# ademas genera el cursor para poder modificar y etc
def conectar():
	global conexion
	global cursor
	conexion = sqlite3.connect("db/database.db")
	cursor = conexion.cursor()

# inicia sesion con una 
# query de sql, buscando usuario y pwd igual al introducido
def iniciar_sesion(usuario_inicio, contraseña_inicio):
	global usuario
	global contraseña
	contraseña = contraseña.encode("utf-8")
	contraseña_encriptada = hashlib.sha256(contraseña)
	contraseña_encriptada = contraseña_encriptada.hexdigest()
	try:
		query = cursor.execute("""SELECT * FROM usuarios
							WHERE usuario = '%s' AND
							contraseña = '%s'
						""" % (usuario, contraseña_encriptada))
		answer = cursor.fetchall()
		if answer == []:
			print("Verifique usuario o contraseña...")
			time.sleep(1)
			main()
		else:
			print(f"Hola {usuario}!")
			# AQUI IRIA LO QUE ES EL
			# POST O LOGIN SUCCESS
			# PARA CREAR UN MENU INICIO RELACIONADO CON LA PAGINA
	except:
		print("Error al iniciar sesion...")
# hace un execute de tipo insert
def registrarse(usuario_registro, conntraseña_registro):
	global usuario
	global contraseña
	contraseña = contraseña.encode("utf-8")
	contraseña_encriptada = hashlib.sha256(contraseña)
	contraseña_encriptada = contraseña_encriptada.hexdigest()
	cursor.execute("""INSERT INTO usuarios VALUES('%s','%s') """ % (usuario, contraseña_encriptada))
	conexion.commit()

# esta es la funcion principal que maneja el menu
# y las secciones
def main():
	conectar()
	global usuario
	global contraseña
	titulo = """

	CHAINSYS
	-------------------
	[1] Iniciar sesión
	[2] Registrarse
	[0] Salir
	-------------------

	"""
	print(titulo)
	eleccion = str(input("Menu >> "))
	while eleccion == " " or eleccion == "":
		eleccion = str(input("Menu >> "))
	if eleccion == "1":
		usuario = str(input("Usuario: "))
		contraseña = getpass.getpass(f"Contraseña para {usuario}: ")
		iniciar_sesion(usuario, contraseña)
	elif eleccion == "2":
		usuario = str(input("Usuario: "))
		contraseña = getpass.getpass(f"Contraseña para {usuario}: ")
		registrarse(usuario, contraseña)
	else:
		sys.exit(0)

if __name__ == '__main__':
	main()
