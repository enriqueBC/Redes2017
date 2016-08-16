import sys
sys.path.insert(0,'../Constants')
from Constants.Constants import *
"""
Clase auxiliar que recibie usuario y contrasena (no cifrada)
Para realizar el login
"""
class Login:
  """
  Constructor
  """
  def __init__(self, user, password):
    self.usuario = user
    self.password_original = password
    self.verificacion = False
    self.password_encriptado = ""
  """
  Revisa en el archivo Input.txt que el usuario pasado por la interfaz exista
  En caso de existir, cifrara la contrsaena y verificara con la almacenada en el archivo
  En otro caso, cambiara su estado a falso, lo que le indicara a la interfaz grafica que
  la contrasena introducida no es valida
  """
  def autentificar(self):
    lineas = [line.rstrip('\n') for line in open(INPUT_PATH)]
    for linea in lineas:
      linea = linea.replace(" ", "")
      linea = linea.split(",", 1)
      usuario_linea = linea[0]
      if usuario_linea == self.usuario: # El usuario existe
	contrasena_cifrada = self.cifrar_contrasena()
	contrasena_linea = linea[1]
	if contrasena_linea == self.password_encriptado:
	  self.verificacion = True
  """
  Toma el password original del objeto y lo cifra de acuerdo a lo indicado
  (sumarle 5 al codigo ascii de cada letra de la contrasena)
  """
  def cifrar_contrasena(self):
    password_cifrado = ""
    for letra in self.password_original:
      codigo_ascii = ord(letra)
      codigo_ascii += LLAVE_CIFRADO
      nueva_letra = chr(codigo_ascii)
      password_cifrado += nueva_letra
    self.password_encriptado = password_cifrado
  """
  Agrega un nuevo usuario a la base de datos (Input.txt)
  """
  def agregar_usuario(self, usuario, contrasena):
    self.password_original = contrasena
    self.cifrar_contrasena()
    contrasena_cifrada = self.password_encriptado
    linea = "\n"+usuario+", "+contrasena_cifrada
    with open(INPUT_PATH, "a") as archivo:
      archivo.write(linea)   