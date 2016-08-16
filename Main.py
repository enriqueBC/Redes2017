from Code.Calculator import Calculator
"""
Main
"""
def main():
	calculadora = Calculator()
	calculadora.recibe_entrada("5")
	calculadora.recibe_entrada(" ")
	calculadora.recibe_entrada("-")
	calculadora.recibe_entrada("4")
	calculadora.procesar_resultado()
	print calculadora.resultado
	calculadora.recibe_entrada("5")
	calculadora.recibe_entrada("+")
	calculadora.recibe_entrada(" ")
	calculadora.recibe_entrada("4")
	calculadora.procesar_resultado()
	print calculadora.resultado

if __name__ == '__main__':
	main()