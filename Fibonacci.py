f=0
s=1
count=0
n=int(input("Enter the number of terms\n"))
if n<=0:
    print("Enter a positive integer")
elif n==1:
    print("Fibonacci series for the term is:")
    print(n)
else:
    print("Fibonacci series for the term is:")
    while count<n:
        print(f)
        nth=f+s
        f=s
        s=nth
        count+=1
        
        
    
