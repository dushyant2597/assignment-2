#Q.No.1
#Create a function to calculate the area of a sphere by taking radius from user.

def AreaOfSphere(radius):
    return(4*3.14*radius**2)
a=int(input("enter the radius."))
print(AreaOfSphere(a))


#Q.NO.2
#Write a function “perfect()” that determines if parameter number is a perfect number.
#Use this function in a program that determines and prints all the perfect numbers between 1 and 1000. 

def perf_num(n):
    l=[]
    for i in range(1,n):
        if n%i==0:
            l.append(i)
    if sum(l)==n:
        return True
for i in range(1,78):
    if perf_num(i):
        print(i,"is perfect number")    

#Q.NO.3

#Print multiplication table of n using loops,
#where n is an integer and is taken as input from the user.

def multi_table(n):
    for i in range(1,11):
        print(n,'*',i,"=",n*i)
n=int(input("enter the number:"))
multi_table(n)

#Q.NO.4
#Write a function to calculate power of a number raised to other ( a^b ) using recursion.

def power(base,exp):
    if(exp==1):
        return base
    if(exp!=1):
        return (base*power(base,exp-1))
base=int(input('enter the base:'))
exp=int(input('enter the exponent:'))
print(power(base,exp))










