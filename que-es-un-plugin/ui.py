# -*- encoding:utf-8 -*-

from Tkinter import Tk, END, LEFT, RIGHT, BOTH, INSERT, Frame, Button, Entry, \
                    Label, Text

class Barra(Frame):
  """
  ui.Barra
  --------

  Control Barra de botones.
  """
  def __init__(self, padre):
    Frame.__init__(self, padre)
    self.__botones = dict()
    self.__salir = Button(self, text="Salir", command=exit)
    self.__salir.pack(side=RIGHT)
    self.__limpiar = Button(self, text="Limpiar", command=self.master.limpiar)
    self.__limpiar.pack(side=RIGHT)

  def agrega(self, nombre, comando):
    """
    ui.Barra.agrega()
    -----------------

    Crea un control tipo Button bajo el nombre <nombre> y le asocia la acción
    <comando>. Una vez creado el control, lo agrega a la barra de botones.

    ARGUMENTOS
      * nombre: Nombre asociado al comando.
      * comando: Función que implementa la acción que ejecuta el comando.

    DEVUELVE
      * Nada
    """
    boton = Button(self, text=nombre, command=comando)
    boton.pack(side=LEFT, padx=2)

    self.__botones[nombre] = boton

  def quita(self, nombre):
    """
    ui.Barra.quita()
    ----------------

    Quita el comando asociado al nombre dado, también retira el botón
    correspondiente de la barra de botones y lo destruye.

    ARGUMENTOS
      * nombre: Nombre asociado al comando.

    DEVUELVE
      * Nada
    """
    boton = self.__botones[nombre]
    del self.__botones[nombre]
    boton.destroy()
    del boton


class Entrada(Frame):
  """
  ui.Entrada
  ----------

  Control para obtener la entrada del usuario.
  """
  def __init__(self, padre):
    Frame.__init__(self, padre)
    self.__prompt  = Label(self, text=">>> ")
    self.__entrada = Entry(self)

    self.__prompt.pack(side=LEFT)
    self.__entrada.pack(fill=BOTH)

  def leer(self):
    """
    ui.Entrada.leer()
    -----------------

    Lee la entrada ingresada por el usuario en el campo de texto.

    DEVUELVE
      * Una cadena de caracteres con la entrada leida del usuario.
    """
    return self.__entrada.get()

  def limpiar(self):
    """
    ui.Entrada.limpiar()
    --------------------

    Elimina el texto actualmente contenido en el campo de texto

    DEVUELVE
      * Nada
    """
    self.__entrada.delete(0, END)

class Salida(Frame):
  """
  ui.Salida
  ---------

  Control para desplegar resultados
  """
  def __init__(self, padre):
    Frame.__init__(self, padre)
    self.__texto = Text(self)
    self.__texto.pack(fill=BOTH, expand=True)

  def escribir(self, mensaje):
    """
    ui.Salida.escribir()
    --------------------

    Escribe el texto contenido en <mensaje> en el área de texto

    ARGUMENTOS
      * mensaje: Texto que se despliega en la interfaz.
    DEVUELVE
      * Nada
    """
    self.__texto.insert(INSERT, str(mensaje) + "\n")

  def limpiar(self):
    """
    ui.Salida.limpiar()
    -------------------

    Elimina el texto actualmente contenido en el área de texto

    DEVUELVE
      * Nada
    """
    self.__texto.delete(1.0, END)

class Interfaz(Frame):
  """
  ui.Interfaz
  -----------

  Ventana principal del programa
  """
  def __init__(self):
    """
    ui.Interfaz.__init__
    --------------------
    """
    ventana = Tk()
    Frame.__init__(self, ventana)
    ventana.title("¿Qué es un plug-in? - codingornot.com")
    ventana.geometry("700x600+200+200")

    self.__barra   = Barra(self)
    self.__salida  = Salida(self)
    self.__entrada = Entrada(self)

    self.__barra.pack  (fill=BOTH, padx=4, pady=4)
    self.__salida.pack (fill=BOTH, padx=4, expand=True)
    self.__entrada.pack(fill=BOTH, padx=4, pady=4)
    self.pack(fill=BOTH, expand=True)

  def agrega(self, nombre, funcion):
    """
    ui.Interfaz.agrega()
    --------------------

    Agrega una función a la interfaz bajo el nombre dado.

    ARGUMENTOS
      * nombre: Nombre bajo el que se registra la nueva función.
      * funcion: Función que se va a agregar.

    DEVUELVE
      * Nada
    """
    self.__barra.agrega(nombre, funcion)

  def quita(self, nombre):
    """
    ui.Interfaz.quita()
    -------------------

    Quita de la interfaz la función identificada por el nombre dado.

    ARGUMENTOS
      * nombre: Nombre bajo el que está registrada la función.

    DEVUELVE
      * Nada
    """
    self.__barra.quita(nombre)

  def leer_entrada(self):
    """
    ui.Interfaz.leer_entrada()
    --------------------------

    Recupera los datos ingresados por el usuario

    DEVUELVE
      * Una cadena de caracteres con la entradaleida del usuario.
    """
    texto = self.__entrada.leer()
    self.__entrada.limpiar()
    return texto

  def escribir_salida(self, texto):
    """
    ui.Interfaz.escribir_salida()
    -----------------------------

    Escribe <texto> en la interfaz gráfica

    ARGUMENTOS
      * texto: Texto que se despliega en la interfaz.

    DEVUELVE
      * Nada
    """
    self.__salida.escribir(texto)

  def limpiar_entrada(self):
    """
    ui.Interfaz.limpiar_entrada()
    -----------------------------

    Limpia la entrada ingresada por el usuario.

    DEVUELVE
      * Nada
    """
    self.__entrada.limpiar()

  def limpiar_salida(self):
    """
    ui.Interfaz.limpiar_salida()
    ----------------------------

    Elimina el texto presentado al usuario.

    DEVUELVE
      * Nada
    """
    self.__salida.limpiar()

  def limpiar(self):
    """
    ui.Interfaz.limpiar()
    ----------------------------

    Elimina todo el texto de la interfaz gráfica

    DEVUELVE
      * Nada
    """
    self.limpiar_entrada()
    self.limpiar_salida()

