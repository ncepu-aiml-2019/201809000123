Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range (2,100):
	c=0
	for j in range (1,i):
		if i%j==0 :
			c=c+1
			pass
		pass
	if c==1 :
		print(i)
		pass

	
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
>>> 
