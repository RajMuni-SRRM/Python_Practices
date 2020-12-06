import pymysql
con=pymysql.connect(host='10.80.100.173',user='db1',password='Root@123')
cursor=con.cursor()
if con!=None:
	print('Connection estblished successfully')
else:
	print('connection not estblished')
try:
	cursor.execute('use test')
	cursor.execute('drop table employees')
	cursor.execute('create table employees(eno int(5) primary key,ename varchar(10),esal varchar(5),eaddr varchar(10))')
	print('Table created')
	records=[]
	count=int(input('Enter the number records you need to insert:'))
	for i in range(count):
		eno=int(input('Enter the {}th person number:'.format(i)))
		ename=input('Enter the {}th person name:'.format(i))
		esal=float(input('Enter the {}th person salary:'.format(i)))
		eaddr=input('Enter the {}th person address:'.format(i))
		records.append((eno,ename,esal,eaddr))
	print('Records:',records)
	query="insert into employees(eno,ename,esal,eaddr) values(%s,%s,%s,%s)"
	cursor.executemany(query,records)
	con.commit()
	cursor.execute('select * from employees')
	data=cursor.fetchall()
	for row in data:
		print('Employee Number:',row[0])
		print('Employee Name:',row[1])
		print('Employee Salary:',row[2])
		print('Employee Address:',row[3])
		print()
except pymysql.DatabaseError as e:
	if con:
		con.rollback()
		print('There is a problem:',e)
finally:
	if cursor:
		cursor.close()
	if con:
		con.close()