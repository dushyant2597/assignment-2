#Q.no.1
lst=['jacob','will','sam',11,23,44]
lst.reverse()
print(lst)


#Q.no.2
str="This World Is Beautiful"
for i in str:
    if i==i.upper():
        print(i,end=" ")

print(str)


#Q.no.3
string=(input("enter elements separated by comma")).split(",")
s=list(string)
print(s)


#Q.no.4
a=input("enter number:")
if a[::-1]==a:
    print("num is palindrome")
else:
    print("num not palindrome")


#Q.no.5
x=['java','ruby','python','abc']
id(x)
print(id(x))
p=x
id(p)
print(id(p))
s=x.copy()
id(s)
print(id(s))
del x[-1]
print(x)
print(p)
print(s)
