import sys
from Code.Calculator import Calculator
sys.path.insert(0,'../Constants')
from Constants.Constants import *

class ScientificCalculator(Calculator):
	"""
	Constructor de la calculadora cientifica
	"""
	def __init__(self):
		Calculator.__init__(self)

	"""
	Procesa la linea como la Calculadora sencilla
	Pero con la posibilidad de identificar modulo, multiplicacion, division y potencia
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
			if ord(letra) == ASCII_MODULO:
				operandos = self.linea.split(letra, 1)
				self.codigo_operacion = ASCII_MODULO
			if ord(letra) == ASCII_MULTIPLICACION:
				operandos = self.linea.split(letra, 1)
				self.codigo_operacion = ASCII_MULTIPLICACION
			if ord(letra) == ASCII_DIVISION:
				operandos = self.linea.split(letra, 1)
				self.codigo_operacion = ASCII_DIVISION
			if ord(letra) == ASCII_POTENCIA:
				operandos = self.linea.split(letra, 1)
				self.codigo_operacion = ASCII_POTENCIA

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
	Tomando en cuenta particularidades de la calculadora cientifica
	"""
	def ejecutar_operacion(self):
		if self.codigo_operacion == ASCII_SUMA:
			self.resultado = str(self.operando1+self.operando2)

		if self.codigo_operacion == ASCII_RESTA:
			self.resultado = str(self.operando1-self.operando2)

		if self.codigo_operacion == ASCII_MODULO:
			if self.operando2 == 0:
				self.resultado = "X_X ERROR Operacion no definida"
				self.verificacion = False
			else:
				self.resultado = str(self.operando1%self.operando2)

		if self.codigo_operacion == ASCII_MULTIPLICACION:
			self.resultado = str(self.operando1*self.operando2)

		if self.codigo_operacion == ASCII_DIVISION:
			if self.operando2 != 0:
				self.resultado = str(self.operando1/self.operando2)
			else:
				self.resultado = "X_X ERROR No puedo dividir entre 0 (aun)"
				self.verificacion = False

		if self.codigo_operacion == ASCII_POTENCIA:
			if self.operando1 == 0 and self.operando2 == 0:
				self.resultado = "X_X ERROR Operacion no definida"
				self.verificacion = False
			else:
				self.resultado = str(self.operando1**self.operando2)