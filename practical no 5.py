
#****************Assignment No-05************************
"""
Name:-
Roll No.:-
"""
#Program to implement Bubble and Selection Sort
def Selection_Sort(arr, n):
	
	for i in range(n - 1):
		min_index = i 
		
		for j in range(i + 1, n):
			if (arr[j] < arr[min_index]):
				min_index = j
				
		arr[i], arr[min_index] = arr[min_index], arr[i] 
		
# Driver Code
n = 5
arr = [ 14, 33, 27, 35, 10 ]
Selection_Sort(arr, n)

print("The Sorted Array by using " \
	"Selection Sort is : ", end = '')
for i in range(n):
	print(arr[i], end = " ")
	
# This code is contributed by DIPAK

# OUTPUT:-
comp@comp-HP-EliteDesk-800-G2-SFF:~$ python3 dipakfds44.py

 The Sorted Array by using Selection Sort is : 10 14 27 33 35 comp@comp-HP-EliteDesk-800-G2-SFF:~$ 

 

