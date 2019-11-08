import random   #設定亂數

def mergesort(listneedtosort):  #定義mergesort這個函數
	index1 = index2 = index3 = 0  

	if len(listneedtosort) > 1:   #假設list超過一個依上的字元
		middlenumber = len(listneedtosort)//2   #就要分成兩邊
		leftsort = listneedtosort[:middlenumber]    
		rightsort = listneedtosort[middlenumber:]

		mergesort(leftsort)  #排序左邊
		mergesort(rightsort)   #排序右邊

		while index1 < len(leftsort) and  index2 < len(rightsort):   #開始假設數值比較過程
			if(leftsort[index1] < rightsort[index2]): 
				listneedtosort[index3] = leftsort[index1] 
				index1 = index1 + 1
			elif(leftsort[index1] >= rightsort[index2]): 
				listneedtosort[index3] = rightsort[index2] 
				index2 = index2 + 1
			index3 = index3 + 1
		
		while index1 < len(leftsort): 
			listneedtosort[index3] = leftsort[index1] 
			index1 = index1 + 1
			index3 = index3 + 1
		
		while index2 < len(rightsort): 
			listneedtosort[index3] = rightsort[index2] 
			index2 = index2 + 1
			index3 = index3 + 1

# test
testlist = list() 

for g in range(20):
    testlist.append(random.randint(1,500))
print('')
print ("原始數列", end="\n") 
for i in range(len(testlist)):		 
	print(testlist[i],end=" ")  
mergesort(testlist) 
print('\n')
print("排序數列", end="\n") 
for i in range(len(testlist)):		 
	print(testlist[i],end=" ") 
print('')

