# f=open('tes.txt','r+')
# f.write('Rajmuni\n')
# f.write('Seemala\n')
# f.writelines(('rajmuni\n','seemala\n','rohini\n','seemala rohiniraj muni\n'))
# data=f.read()
# print(data)
# print(f.read(10))
# print(f.readline())
# data=f.readlines()
# for i in data:
	# print(i)
# f.writelines(('rajmuni\n','seemala\n','rohini\n','seemala rohiniraj muni\n'))
# f.close()


# data="All staudents are STUPIDS"
# f=open('tes.txt','w')
# f.write(data)
# with open('tes.txt','r+') as f:
	# text=f.read()
	# print(text)
	# print('The current cursor porsition:',f.tell())
	# # f.seek(15)
	# # print('The current cursor position:',f.tell())
	# f.write('GEMS!!!')
	# f.seek(0)
	# text=f.read()
	# print('Data After modification')
	# print(text)
# print(f.closed)


import os,sys
fname=input('Enter the file name:')
if os.path.isfile(fname):
	print('File exists:',fname)
	f=open(fname,'r')
else:
	print('File not exists:',fname)
	sys.exist(0)
print('the content of the file is:')
data=f.read()
print(data)
f.close()
print(f.closed)