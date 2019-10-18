# 201809000123
计算机1801徐金鸿
for i in range (2,100):
	c=0
	for j in range (1,i):
		if i%j==0 :
			c=c+1
			pass
		pass
	if c==1 :
		print(i)
		pass
