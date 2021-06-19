def wallis(n):
	x=1
	n=int(n)
	i=1
	while(i<=n):
		x*=((2*i)**2)/(((2*i)**2)-1)
		i+=1
	return x*2
n=input("enter the n:")
print(wallis(n)) 

  
