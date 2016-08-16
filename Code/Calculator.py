import sys
sys.path.insert(0,'../Constants')
from Constants.Constants import *
"""
Clase que representa a una calculadora con la que se realizan operaciones basicas
Se usara para auxiliar a la interfaz grafica en las operaciones
y anadir robustez a las operaciones (errores de tipo posibles con los botones, como por ejemplo "5 + /")
(Algunos aspectos poco comunes de la calculadora se hicieron tomando en cuenta su interaccion con la Interfaz Grafica)
"""
class Calculator:

	"""
	Constructor
	"""
	def __init__(self):
		self.resultado = ""
		self.operando1 = 0
		self.operando2 = 0
		self.codigo_operacion = 0
		self.linea = ""
		self.verificacion =  False
	"""
	Recibe una entrada (por medio de un boton)
	Esta entrada es almacenada en un string que acumula todas las entradas
	Hasta que se debe realizar la operacion ("=" es oprimido)
	"""
	def recibe_entrada(self, entrada):
		self.linea += entrada
	"""
	Procesa la entrada almacenada en la linea de la calculadora
	Esto es, quitar los espacios innecesarios en la linea de entrada,
	identificar la operacion a realizar en la calculadora,
	identificar ambos operandos, revisar errores del numero de operandos y
	verificar el tipo de los operandos
	"""
	def procesar_linea(self):
		self.linea = self.linea.replace(" ", "")
		operandos = []
		for letra in self.linea:
			if ord(letra) == ASCII_SUMA:
				operandos = self.linea.split(letra, 1)
				self.codigo_operacion = ASCII_SUMA
			if ord(letra) == ASCII_RESTA:
				operandos = self.linea.split(letra, 1)
				self.codigo_operacion = ASCII_RESTA

		if len(operandos) != 2: # Revisando cardinalidad de operandos
			self.resultado = "x_x ERROR en el numero de operandos"
		else: # Revisando el tipo de cada operando (que sean numeros)
			try:
				self.operando1 = float(operandos[0])
				self.operando2 = float(operandos[1])
				self.verificacion = True
			except ValueError:
				self.resultado = "x_x ERROR en el tipo de los operandos"
	"""
	Ejecuta la operacion solicitada con los operandos procesados
	"""
	def ejecutar_operacion(self):
		if self.codigo_operacion == ASCII_SUMA:
			self.resultado = str(self.operando1+self.operando2)
		if self.codigo_operacion == ASCII_RESTA:
			self.resultado = str(self.operando1-self.operando2)
	"""
	Rutina que procesa el resultado de la linea de la calculadora
	Procesa la linea, realiza una verificacion de tipo y cardinalindad sobre los operandos
	Ejecuta la operacion, y reinicia sus atributos para anticipar la siguiente operacion de la calculadora
	"""
	def procesar_resultado(self):
		self.procesar_linea()
		# Al ser todo correcto, ejecutamos la operacion para definir el resultado
		if(self.verificacion):
			self.ejecutar_operacion()
		self.operando1 = 0
		self.operando2 = 0
		self.linea = ""
		self.verificacion = False