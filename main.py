# Definición de la clase Estudiante
class Estudiante:
  # Constructor
  def __init__(self, codigo, nombre, apellido,genero,programa,semestre):
    # Atributos
    self.codigo = codigo
    self.nombre = nombre
    self.apellido = apellido
    self.programa = programa
    self.genero = genero
    self.semestre= semestre
    self.materias = [] # una lista vacia
  # Métodos
  def __str__(self): 
    # devuelve una cadena que representa el objeto 
    # equivale al método ToString() de otros lenguajes
    resp = "{} {} ({}) {}\n".format(self.nombre, self.apellido, self.codigo,self.programa)
    for m in self.materias:
      resp += "{}\n".format(m)
    resp += "promedio = {:.2f}".format(self.promedio())
    return resp
    
  def adicionarMateria(self, materia):
    # adiciona la materia (objeto) a materias (lista)
    self.materias.append(materia)
  def promedio(self):
    # calcula el promedio de todas las materias
    suma = 0
    for materia in self.materias:
      suma += materia.calcularPromedio()
    return suma / len(self.materias)

# Definición de la clase Materia
class Materia:
  # Constructor
  def __init__(self, nombre, pp, sp, tp):
    self.nombre = nombre
    self.pp = pp
    self.sp = sp
    self.tp = tp
  # Métodos
  def __str__(self):
    # método ToString()
    return "{}: {}, {}, {} = {:.2f}".format(self.nombre, self.pp, self.sp, self.tp, self.calcularPromedio())
  
  def calcularPromedio(self):
    # calcula el promedio de esta materia
    return 0.3*self.pp + 0.3*self.sp + 0.4*self.tp

# Programa Principal

import csv
estudiante=dict()
estudiantes = []
with open("notas.csv") as archivo:
  fuente = csv.reader(archivo, delimiter='|')
  for linea in fuente:
    
    codigo=linea[0]
    d1=list()
    if codigo in estudiante=='':
      print("")
    else:
      materias=dict()
      codigo=linea[0]
      nombre=linea[1]
      apellido=linea[2]
      sexo=linea[3]
      programa=linea[4]
      semestre=linea[5]
    materia=linea[6]
    notas=[float(linea[7]),float(linea[8]),float(linea[9])]
    d1.append(nombre)
    d1.append(apellido)
    d1.append(sexo)
    d1.append(programa)
    d1.append(semestre)
    materias[materia]= notas
    d1.extend(materias)
    print(d1,codigo,notas)