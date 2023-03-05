import os
import pymysql
import subprocess

'''con = pymysql.connect(host='127.0.0.1',user='root',password='',database='pami')
cursor = con.cursor()

path = os.getcwd()
for file in os.listdir(path+"/qr"):
	bene = file.split('-')[0]
	nombre = file.split('-')[1]
	dni = file.split('-')[2].replace('.pdf','')

	print(f"'{nombre}',{dni},{bene}")

	sql = f"insert into pacientes (nombre,dni,beneficio,filename) values ('{nombre}',{dni},{bene},'{file}')"
	cursor.execute(sql)
	con.commit()
con.close()'''

con = pymysql.connect(host='127.0.0.1',user='root',password='',database='pami')
cursor = con.cursor()

print('''
	*** PamiBolsillo ***
	1. Buscar por nombre
	2. Buscar por Bene
	3. Buscar por DNI
	4. Salir
	''')

op = int(input("Choose your destiny: "))
path = os.getcwd()
if op == 1:
	nombre = input("who?: ")
	sql = f"select * from pacientes where nombre like '%{nombre}%'"
	cursor.execute(sql)
	paciente = cursor.fetchall()
	print(paciente)
if op == 2:
	bene = input("who?: ")
	sql = f"select * from pacientes where beneficio like '%{bene}%'"
	cursor.execute(sql)
	paciente = cursor.fetchall()
	print(paciente)
if op == 3:
	dni = input("who?: ")
	sql = f"select * from pacientes where dni like '%{dni}%'"
	cursor.execute(sql)
	paciente = cursor.fetchall()
	print(path+"/qr/"+paciente[-1][-1])
subprocess.Popen(path+"/qr/"+paciente[-1][-1],shell=True)