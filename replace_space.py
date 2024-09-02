#replace the string space with character 

string="m d m"
cha="a"
result=""
for i in string:
    if i ==" ":
        i=cha
    result+=i
print(result)