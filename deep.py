def deep(a):
	if (type(a) != list):
		return 0
	if (type(a[0])!=list):
		return (1+deep(a[1:]))
	else:
		return(deep(a[0]) + deep(a[1:]))

a = [[['j'], 'f'],[['h'],'d']]
print deep(a)

