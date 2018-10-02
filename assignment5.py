#Q.No1.
a=int(input("enter any year"))
if (a%4==0):
    print("leap year")
else:
    print("not a leap year")

#Q.No2.
l=int(input("enter the length"))
b=int(input("enter the breadth"))
def dimensions(l,b):
    if l==b:
        return("dimensions of square")
    else:
        return ("dimensions of rectangle")
print(dimensions(l,b))

#Q.No3.

a=int(input("enter the age of first person"))
b=int(input("enter the age of second person"))
c=int(input("enter the age of third person"))
oldest_person=max(a,b,c)
youngest_person=min(a,b,c)
print("oldest is ",oldest_person)
print("youngest is",youngest_person)


#Q.No.4
emp_age=int(input("enter the age"))
emp_sex = str(input("enter the sex(M or F)"))
emp_status = str(input("enter the marital status(Y or N)"))
if(emp_sex==('F')):
    print("she will work in urban areas")
elif(emp_sex==('M'))and (20<=emp_age<40):
    print("he may work in anywhere")
elif(emp_sex==('M'))and (40<=emp_age<60):
    print("he will work in urban areas")
else:
    print("ERROR!!!!")


#Q.NO.5
quant=int(input("enter the quantity "))
cost=(quant*100)
if cost>1000:
    discount=(cost)*.10
    cost-=discount

    print("the cost  is",cost)
else:
    print("the cost is",cost)


#Q.NO.6
x=[]
for i in range(10):
    x.append(input("enter a number:"))
    print(x,sep='\n')

    
#Q.NO.7
while True:
    print("infinite loop")

#Q.No.8
a=[11,12,23,44]
b=[]
for i in a:
    b.append(i**2)
    
    print(b)


#Q.No.9
lst=[12,2.3,"abc"]
l1=[]
l2=[]
l3=[]
for i in lst:
    if type(i)==int:
        l1.append(i)
        print(l1)
    elif type(i)==float:
        l2.append(i)
        print(l2)
    else:
        l3.append(i)
        print(l3)


#Q.N0.10
l=[]
for i in range(1,101):
     if i>1:
         for j in range(2,i):
             if i%j==0:
                 break
     else:
         l.append(i)
print(l)

#Q.No.11
for i in range(0, 4):
    for j in range(0,i+1):
        print("* ", end=" ")
    print()



#Q.NO.12
n=int(input("enter total number of elements:"))
l=[]
for i in range(n):
    n1=int(input("enter number:"))
    l.append(n1)
print(l)
n2=int(input("enter element to be searched:"))
for j in 1:
    if j==n2:
        k=l.index(j)
        l.pop()
print(l)
