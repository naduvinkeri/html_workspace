# #reverse function using list function

# #for string reverse() function is will through error
# list1 = [1, 2, 3, 4, 1, 2, 6] 
# list1.reverse() 
# print(list1) 


# #converting string into list
# list_String = list ("nnamam")
# list_String.reverse()
# print(list_String)


# #count the number occurance using count() fun
# Rand = [1,3,2,4,1,3,2,4,5,2,3]
# #lets count occurence of 2
# print(Rand.count(2))




# #count() takes one funstion
# list1 = [1, 1, 1, 2, 3, 2, 1] 
# # Error when two parameters is passed. 
# print(list1.count(1, 2))




# Python3 program to count the number of times
# an object appears in a list using count() method 
# lst = ['Cat', 'Bat', 'Sat', 'Cat', 'Mat', 'Cat', 'Sat']
# print ([ [l, lst.count(l)] for l in set(lst)])
# print (dict( (l, lst.count(l) ) for l in set(lst)))

# [['Bat', 1], ['Cat', 3], ['Sat', 2], ['Mat', 1]]
# {'Bat': 1, 'Cat': 3, 'Sat': 2, 'Mat': 1}


def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

my_array = [1, 45, 54, 71, 76, 12]
reverse_array(my_array)
print("Reversed Array:", my_array)
