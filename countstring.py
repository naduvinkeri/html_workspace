def find_String_length(input_string):
    len=0
    while input_string:
        input_string=input_string[1:]
        len+=1
    return len

input_string=input("enter the string ")
len = find_String_length(input_string)
print(len)