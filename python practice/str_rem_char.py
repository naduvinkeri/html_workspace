Str1 = input('Enter a String: ')

Str2 =''

for i in Str1:

    if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):

        Str2+=i

print('String with alpbhabets only: ' +Str2)