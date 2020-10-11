# creating an empty list 
lst = []

# number of elements as input
n = int(input("Enter number of elements : ")) 

# iterating till the n number of times 
for i in range(0, n): 
	ele = int(input("element: ")) # taking user input 

	lst.append(ele) # adding the element in list
# printing the original list
print("Original numbers in the list: ",lst)

# filtering the list
new_lst = list(filter(lambda x: x >0, lst))

# printing the new filtered list
print("Positive numbers in the list: ",new_lst)
