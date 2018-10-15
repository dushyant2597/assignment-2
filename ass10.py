#Q.NO.1
import re
str1='valid email id is balwantrawat333@gmail.com'
addresses=re.findall(r'[\w\.-]+@[\w\.-]+',str1)
print(addresses)

#Q.NO.2
import re
pattern=r"[6-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$"
str1=(' my phone no is 9876543210')
valid_no=re.findall(pattern,str1)
print(valid_no)
