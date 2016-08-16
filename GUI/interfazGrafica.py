import sys
sys.path.insert(0,'../Constants')
from Constants.Constants import *
from Code.Login import Login
from Code.ScientificCalculator import ScientificCalculator
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QWidget, QLabel
"""
Clase que representa a la ventana para iniciar sesion,
donde se requiere el usuario y la contrasena, almacenados en la base de datos
En caso de no existir en la base, o de introducir una contrasena incorrecta,
el aceso no es permitido
"""
class LoginWindow(QtGui.QWidget):
    """
    Constructor
    """
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.initUI()
    """
    Inicializa y muestra los componentes de la interfaz grafica
    En este caso, lo necesario para acceder a la calculadora por medio de usuarios
    almacenados en la base de datos
    """
    def initUI(self):
        # Definimos las etiquetas y los campos de entrada
        user_label = QtGui.QLabel('Nombre de usuario?:', self)
        user_widget = QtGui.QLineEdit()
        password_label = QtGui.QLabel('Contrasena?:', self)
        password_widget = QtGui.QLineEdit()
        # Definimos el boton a llamar y su funcion
        login_button = QtGui.QPushButton('Acceder')
        login_button.clicked.connect(lambda: self.accesso(user_widget, password_widget))
        # Definimos la cuadricula
        grid = QtGui.QGridLayout()
        grid.addWidget(user_label, 0, 0)
        grid.addWidget(user_widget, 1, 0)
        grid.addWidget(password_label, 2, 0)
        grid.addWidget(password_widget, 3, 0)
        grid.addWidget(login_button, 4, 1)
        self.setLayout(grid)
        self.setGeometry(DEFAULT_POSTION_X, DEFAULT_POSTION_Y, LOGIN_WIDTH, LOGIN_HEIGTH)
        self.setWindowTitle('Acceso a calculadora')
        self.show()
    """
    Realiza el acceso a la calculadora con los datos obtenidos en los campos de texto
    """
    def accesso(self, user_widget, pass_widget):
        contact_user = str(user_widget.text())
        contact_pass = str(pass_widget.text())
        print "%s intenta usar la calculadora." % contact_user
        login = Login(contact_user, contact_pass)
        login.autentificar()
        if login.verificacion: # Acceso correcto a la calculadora
            print "Acceso correcto!"
            mainWindow = CalcWindow()
        else: # Acceso incorrecto
            print "Acceso incorrecto!"
            mainWindow = MsgWindow('NO Tienes acceso al sistema :(', PANTALLA_LOGIN)
        self.close()
"""
Clase auxiliar para presentar en pantalla un mensaje
y redireccionar a otra pantalla
"""
class MsgWindow(QtGui.QWidget):
    """
    Constructor
    """
    def __init__(self, mensaje, redireccionamiento):
        super(MsgWindow, self).__init__()
        self.message = mensaje
        self.redirect = redireccionamiento
        self.initUI()
    """
    Inicializa y muestra los componentes de la interfaz grafica
    En este caso, un mensaje, y un redireccionamiento hacia otra ventana
    """
    def initUI(self):
        # Definimos la etiqueta con el mensaje a mostrar al usuario
        message_label = QtGui.QLabel(self.message, self)
        # Definimos el boton a llamar y su funcion
        continue_button = QtGui.QPushButton('Continuar')
        continue_button.clicked.connect(lambda: self.redireccionar())
        # Definimos la cuadricula
        grid = QtGui.QGridLayout()
        grid.addWidget(message_label, 0, 0)
        grid.addWidget(continue_button, 1, 0)
        self.setLayout(grid)
        self.setGeometry(DEFAULT_POSTION_X, DEFAULT_POSTION_Y, LOGIN_WIDTH, LOGIN_HEIGTH)
        self.setWindowTitle('Mensaje')
        self.show()
    """
    Se realiza el redireccionamiento hacia otra pantalla despues de mostrar un mensaje
    """
    def redireccionar(self):
        if self.redirect == PANTALLA_LOGIN:
            mainWindow = LoginWindow()
        if self.redirect == PANTALLA_CALCULADORA:
            mainWindow = CalcWindow()
        self.close()
"""
Clase para representar la calculadora
"""
class CalcWindow(QtGui.QWidget):
    """
    Constructor
    """
    def __init__(self):
        super(CalcWindow, self).__init__()
        self.calculadora = ScientificCalculator()
        self.line_label = None
        self.result_label = None
        self.initUI()
    """
    Inicializa y muestra los componentes de la interfaz grafica
    En este caso, lo necesario para acceder a la calculadora por medio de usuarios
    almacenados en la base de datos
    """
    def initUI(self):
        # Definimos el boton para agregar usuarios
        user_button = QtGui.QPushButton('+Usuario')
        user_button.clicked.connect(lambda: self.agregar_usuario())
        # Definimos la etiqueta donde se vera el resultado de la calculadora
        self.line_label = QtGui.QLabel(self.calculadora.linea, self)
        self.result_label = QtGui.QLabel(self.calculadora.resultado, self)
        # Definimos los botones de la calculadora
        seven_button = QtGui.QPushButton('7')
        seven_button.clicked.connect(lambda: self.apretar_boton('7'))
        eight_button = QtGui.QPushButton('8')
        eight_button.clicked.connect(lambda: self.apretar_boton('8'))
        nine_button = QtGui.QPushButton('9')
        nine_button.clicked.connect(lambda: self.apretar_boton('9'))
        plus_button = QtGui.QPushButton('+')
        plus_button.clicked.connect(lambda: self.apretar_boton('+'))
        less_button = QtGui.QPushButton('-')
        less_button.clicked.connect(lambda: self.apretar_boton('-'))

        four_button = QtGui.QPushButton('4')
        four_button.clicked.connect(lambda: self.apretar_boton('4'))
        five_button = QtGui.QPushButton('5')
        five_button.clicked.connect(lambda: self.apretar_boton('5'))
        six_button = QtGui.QPushButton('6')
        six_button.clicked.connect(lambda: self.apretar_boton('6'))
        times_button = QtGui.QPushButton('*')
        times_button.clicked.connect(lambda: self.apretar_boton('*'))
        power_button = QtGui.QPushButton('^')
        power_button.clicked.connect(lambda: self.apretar_boton('^'))

        one_button = QtGui.QPushButton('1')
        one_button.clicked.connect(lambda: self.apretar_boton('1'))
        two_button = QtGui.QPushButton('2')
        two_button.clicked.connect(lambda: self.apretar_boton('2'))
        three_button = QtGui.QPushButton('3')
        three_button.clicked.connect(lambda: self.apretar_boton('3'))
        div_button = QtGui.QPushButton('/')
        div_button.clicked.connect(lambda: self.apretar_boton('/'))
        mod_button = QtGui.QPushButton('%')
        mod_button.clicked.connect(lambda: self.apretar_boton('%'))

        zero_button = QtGui.QPushButton('0')
        zero_button.clicked.connect(lambda: self.apretar_boton('0'))
        result_button = QtGui.QPushButton('=')
        result_button.clicked.connect(lambda: self.apretar_boton('=')) # ESTE EJECUTA LA OPERACION
        point_button = QtGui.QPushButton('.')
        point_button.clicked.connect(lambda: self.apretar_boton('.'))
        # Definimos la cuadricula
        grid = QtGui.QGridLayout()
        grid.addWidget(user_button, 0, 0)

        grid.addWidget(self.line_label, 1, 0)
        grid.addWidget(self.result_label, 1, 1)

        grid.addWidget(seven_button, 2, 0)
        grid.addWidget(eight_button, 2, 1)
        grid.addWidget(nine_button, 2, 2)
        grid.addWidget(plus_button, 2, 3)
        grid.addWidget(less_button, 2, 4)

        grid.addWidget(four_button, 3, 0)
        grid.addWidget(five_button, 3, 1)
        grid.addWidget(six_button, 3, 2)
        grid.addWidget(times_button, 3, 3)
        grid.addWidget(power_button, 3, 4)

        grid.addWidget(one_button, 4, 0)
        grid.addWidget(two_button, 4, 1)
        grid.addWidget(three_button, 4, 2)
        grid.addWidget(div_button, 4, 3)
        grid.addWidget(mod_button, 4, 4)

        grid.addWidget(zero_button, 5, 1)
        grid.addWidget(result_button, 5, 2)
        grid.addWidget(point_button, 5, 3)

        self.setLayout(grid)
        self.setGeometry(DEFAULT_POSTION_X, DEFAULT_POSTION_Y, CALC_WIDTH, CALC_HEIGTH)
        self.setWindowTitle('Calculadora')
        self.show()
    """
    Redirecciona hacia la pantalla para agregar un nuevo usuario a la base de datos
    """
    def agregar_usuario(self):
        # Redireccionamiento a pantalla de usuario
        mainWindow = UserWindow()
        self.close()
        
    """
    Recibe una entrada por medio de los botones de la interfaz
    """
    def apretar_boton(self, boton):
        if boton == '=':
            self.calculadora.procesar_resultado()
            if not self.calculadora.verificacion:
                mainWindow = MsgWindow(self.calculadora.resultado, PANTALLA_CALCULADORA)
                self.close()
        else:
            self.calculadora.recibe_entrada(boton)
        self.line_label.setText(self.calculadora.linea)
        self.result_label.setText(self.calculadora.resultado)

"""
Clase para agregar a un nuevo usuario a la base de datos
y redireccionar a otra pantalla
"""
class UserWindow(QtGui.QWidget):
    """
    Constructor
    """
    def __init__(self):
        super(UserWindow, self).__init__()
        self.initUI()
    """
    Inicializa y muestra los componentes de la interfaz grafica
    En este caso, lo necesario para acceder a la calculadora por medio de usuarios
    almacenados en la base de datos
    """
    def initUI(self):
        # Definimos las etiquetas y los campos de entrada
        user_label = QtGui.QLabel('Nombre de usuario:', self)
        user_widget = QtGui.QLineEdit()
        password_label = QtGui.QLabel('Contrasena:', self)
        password_widget = QtGui.QLineEdit()
        # Definimos el boton a llamar y su funcion
        login_button = QtGui.QPushButton('Registrar')
        login_button.clicked.connect(lambda: self.anadir_usuario(user_widget, password_widget))
        # Definimos la cuadricula
        grid = QtGui.QGridLayout()
        grid.addWidget(user_label, 0, 0)
        grid.addWidget(user_widget, 1, 0)
        grid.addWidget(password_label, 2, 0)
        grid.addWidget(password_widget, 3, 0)
        grid.addWidget(login_button, 4, 1)
        self.setLayout(grid)
        self.setGeometry(DEFAULT_POSTION_X, DEFAULT_POSTION_Y, CALC_WIDTH, CALC_HEIGTH)
        self.setWindowTitle('Registro de usuario')
        self.show()
    """
    Realiza el acceso a la calculadora con los datos obtenidos en los campos de texto
    """
    def anadir_usuario(self, user_widget, pass_widget):
        contact_user = str(user_widget.text())
        contact_pass = str(pass_widget.text())
        print "Registrando a: %s." % contact_user
        login = Login(contact_user, contact_pass)
        login.agregar_usuario(contact_user, contact_pass)
        mainWindow = LoginWindow()
        self.close()