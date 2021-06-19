import random
def monte_carlo(n):
	n=int(n)
	x=1
	i=0
	y=0
	while(i<=n):
		
		p=random.random()
		q=random.random()
		d=(p**2+q**2)**(1/2)
		if (d<=1):
			y+=1
		i+=1
			
	x=(4*y)/n
	return x
n=input("enter the n:")
print(monte_carlo(n))
