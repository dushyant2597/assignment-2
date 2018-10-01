#Q.no.1
x=list()
print(x)


#Q.no.2
x=['google','apple','facebook','microsoft','tesla']
print(x)


#Q.no.3
print(x.count("google"))
print(x.count("apple"))
print(x.count("microsoft"))
print(x.count("facebook"))
print(x.count("tesla"))


#Q.no.4
y=[33,12,55,76,21,3,43]
y.sort()
print(y)


#Q.no.5
a=[76,21,3,43]
b=[33,12,55,21]
c=a+b
c.sort()
print(c)


#Q.no.6
numbers=[1,2,4,5,3,7,8]
count_odd=0
count_even=0
for x in numbers:
    if x%2==0:
        count_even+=1
print("no of odd number",count_odd)
print("no of even numbers",count_even)


#Q.no.7
t=("sam","will","kasaab","feroz")
print(list(reversed(t)))


#Q.no.8
a=(77,99,11,100,55,33,121)
print(max(a))
print(min(a))



#Q.no.9
value="infinity"
x=value.upper()
print(x)


#Q.no.10
a="1234"
print(a.isdigit())

#Q.no.11
a="Hello World"
print(a.replace("World","Balwant"))
