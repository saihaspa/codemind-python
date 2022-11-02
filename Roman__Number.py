def Roman(n):
	num = [1,4,5,9,10,40,50,90,
		100,400,500,900,1000]
	sym=["I","IV","V", "IX", "X", "XL",
		"L", "XC", "C", "CD", "D", "CM","M"]
	i=12
	d=0
	while(n):
	    d=n//num[i]
	    n=n%num[i]
	    while(d):
	        print(sym[i],end="")
	        d-=1
	    i-=1
n=int(input())
Roman(n)
