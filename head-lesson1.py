man=[]
said=[]
try:
	data=open('zy.txt','w')
	for line in data:
		try:
			(r,said1)=data.split(':')
			print 'Man say:',
			print '\t'
			print 'fine',said1
		except ValueError :
			print 'value is wrong'
except IOError:
	print 'no file'
