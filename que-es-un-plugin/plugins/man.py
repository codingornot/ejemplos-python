# -*- encoding:utf-8 -*-
"""
man
---

Plugin para consultar el manual en línea.
"""

import subprocess

__nucleo = None
__activo = True

def hacer():
  global __nucleo
  comando = __nucleo.leer_entrada()
  comando_man = ["man", "-P", "cat", comando ]

  manual = subprocess.check_output(comando_man)
  __nucleo.limpiar()
  __nucleo.escribir_salida(manual)

def iniciar(nucleo):
  global __nucleo
  __nucleo = nucleo

def activo():
  global __activo
  return __activo == True
