# -*- encoding:utf-8 -*-
"""
calcula
-------

Plugin para evaluar expresiones aritméticas
"""
__nucleo = None
__activo = True

def hacer():
  global __nucleo
  entrada = __nucleo.leer_entrada()
  salida = eval(entrada)
  __nucleo.escribir_salida(salida)

def iniciar(nucleo):
  global __nucleo
  __nucleo = nucleo

def activo():
  global __activo
  return __activo == True
