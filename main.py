import os

ida = int(input("Qual a idade do nadador: "))

os.system('clear')

if(ida >=5 and ida <= 7):
  print("infantil A")
if(ida >=8 and ida <= 10):
  print("infantil B")
if(ida >=11 and ida <= 13):
  print("juvenil A")
if(ida >=14 and ida <= 17):
  print("juvenil B")
if(ida >=18):
  print("adulto")
