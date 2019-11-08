import random

def MSort(listneedtosort): 
	if len(listneedtosort) >1: 
		middle_number = len(listneedtosort)//2 #Finding the middle_number of the listneedtosortay 
		L = listneedtosort[ # Dividing the listneedtosortay elements 
		R = listneedtosort[middle_number:] # into 2 halves 

		MSort(L) # Sorting the first half 
		MSort(R) # Sorting the second half 

		i = j = k = 0

		while i < len(L) and j < len(R): 
			if L[i] < R[j]: 
				listneedtosort[k] = L[i] 
				i+=1
			else: 
				listneedtosort[k] = R[j] 
				j+=1
			k+=1
		
		# Checking if any element was left 
		while i < len(L): 
			listneedtosort[k] = L[i] 
			i+=1
			k+=1
		
		while j < len(R): 
			listneedtosort[k] = R[j] 
			j+=1
			k+=1

# 
def printList(listneedtosort): 
	for i in range(len(listneedtosort)):		 
		print(listneedtosort[i],end=" ") 
	print() 
'''
# test
testlist = list()

for g in range(10000):
    testlist.append(random.randint(1,10000000))

print ("原始數列", end="\n") 
printList(testlist) 
MSort(testlist) 
print("排序數列", end="\n") 
printList(testlist) 

'''

listneedtosort = [12, 11, 13, 5, 6, 7] 
print ("原始數列", end="\n") 
	for i in range(len(listneedtosort)):		 
		print(listneedtosort[i]) 
	print() 
MSort(listneedtosort) 
print("排序數列", end="\n") 
printList(listneedtosort) print ("原始數列", end="\n") 
	for i in range(len(listneedtosort)):		 
	    print(listneedtosort[i]) 
	print()

# This code is contributed by Mayank Khanna 
