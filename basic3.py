# # # # class BinarysearchTree():
# # # # 	def __init__(self,data):
# # # # 		self.data =  data
# # # # 		self.right = None
# # # # 		self.left = None
	
# # # # 	def insert(self,data):
# # # # 		if self.data == data:
# # # # 			return 
# # # # 		else:
# # # # 			if self.data > data:
# # # # 				if self.left:
# # # # 					self.left.insert(data)
# # # # 				else:
# # # # 					self.left = BinarysearchTree(data)
# # # # 			else:
# # # # 				if self.right:
# # # # 					self.right.insert(data)
# # # # 				else:
# # # # 					self.right = BinarysearchTree(data)
	
# # # # 	def inorder(self):
# # # # 		elements = []
# # # # 		if self.left :
# # # # 			elements+= self.left.inorder()
		
# # # # 		elements.append(self.data)

# # # # 		if self.right:
# # # # 			elements += self.right.inorder()
		
# # # # 		return elements

	
# # # # 	def search(self,val):
# # # # 		if self.data == val:
# # # # 			return True
		
# # # # 		if val < self.data:
# # # # 			if self.left :
# # # # 				return self.left.search(val)
# # # # 			else:
# # # # 				return False
# # # # 		if val > self.data:
# # # # 			if self.right:
# # # # 				return self.right.search(val)
# # # # 			else:
# # # # 				return False

# # # # 	def findMax(self):
# # # # 		if self.right is None:
# # # # 			return self.data
# # # # 		return self.right.findMax()
	
# # # # 	def findMin(self):
# # # # 		if self.left is None:
# # # # 			return self.data
# # # # 		return self.left.findMin()
	
# # # # 	def delnode(self,val):
# # # # 		if val < self.data:
# # # # 			if self.left:
# # # # 				self.left = self.left.delnode(val)
# # # # 		elif val> self.data:
# # # # 			if self.right:
# # # # 				self.right =self.right.delnode(val)
# # # # 		else:
# # # # 			if self.left is None and self.right is None:
# # # # 				return None
# # # # 			if self.left is None:
# # # # 				return self.right
# # # # 			if self.right is None:
# # # # 				return self.left
			
# # # # 			minVal = self.right.findMin()
# # # # 			self.data = minVal
# # # # 			self.right = self.right.delnode(minVal)
# # # # 		return self



# # # # root = BinarysearchTree(50)
# # # # root.insert(30)
# # # # root.insert(40)
# # # # root.insert(70)
# # # # val = root.inorder()
# # # # print('before deleting ', val)
# # # # root.delnode(30)
# # # # val = root.inorder()
# # # # print('after deleting', val)



# # # class BinaryTree():
# # # 	def __init__(self,key):
# # # 		self.data = key
# # # 		self.left = None
# # # 		self.right = None
	
# # # 	def insert(self, key):
# # # 		if self.data == key:
# # # 			return 
		
# # # 		if self.data < key:
# # # 			if self.right:
# # # 				self.right.insert(key)
# # # 			else:
# # # 				self.right = BinaryTree(key)
# # # 		else:
# # # 			if self.left:
# # # 				self.left.insert(key)
# # # 			else:
# # # 				self.left = BinaryTree(key)
		
# # # 	def inorder(self):
# # # 		elements =[]

# # # 		if self.left:
# # # 			elements+= self.left.inorder()
		
# # # 		elements.append(self.data)

# # # 		if self.right:
# # # 			elements+= self.right.inorder()
		
# # # 		return elements

	
# # # 	def search(search,key):
# # # 		if self.data == key:
# # # 			return True
		
# # # 		if self.data > key:
# # # 			if self.left:
# # # 				return self.left.search(key)
# # # 			else:
# # # 				return None
# # # 		else:
# # # 			if self.right:
# # # 				return self.right.search(key)
# # # 			else:
# # # 				return None
	
# # # 	def minVal(self):
# # # 		if self.left  is None:
# # # 			return self.data
# # # 		return self.left.minVal()
		
	
# # # 	def delete(self,key):
# # # 		if self.data > key:
# # # 			print("left running",self.data)
# # # 			if self.left:
# # # 				self.left = self.left.delete(key)
# # # 		elif self.data < key:
# # # 			print("right running")
# # # 			if self.right:
# # # 				self.right = self.right.delete(key)
# # # 		else:
# # # 			if self.left is None and self.right is None:
# # # 				print("both none running",self.data)
# # # 				return None
# # # 			if self.left is None:
# # # 				print("left none running")
# # # 				return self.right
# # # 			if self.right is None:
# # # 				print("right none running")
# # # 				return self.left
			
# # # 			minValue = self.right.minVal()
# # # 			self.data = minValue
# # # 			print("mininmum values is",minValue)
# # # 			self.right = self.right.delete(minValue)
			
# # # 		return self
		
# # # def buildTree(lst):
# # # 	root = BinaryTree(lst[0])
# # # 	for i in range(1,len(lst)):
# # # 		root.insert(lst[i])
	
# # # 	print(root.inorder())
# # # 	root.delete(40)
# # # 	print(root.inorder())
# # # 	return root

	

# # # if __name__ == "__main__":
# # # 	values = [50,60,20,40,10,21,45]
# # # 	buildTree(values)




# # # def factorial(n):
# # # 	if n ==1:
# # # 		return n
	
# # # 	else:
# # # 		value = factorial(n-1)*n
# # # 	return value

# # # if __name__ == "__main__":
# # # 	val = factorial(5)
# # # 	print(val)		


# # # def sequential(lst,val):
# # # 	pos =0
# # # 	found = False
# # # 	while pos < len(lst) and not found:
# # # 		if lst[pos] == val:
# # # 			found = True
# # # 		else:
# # # 			pos = pos+1
# # # 	return found

# # # lst = [50,2,4,7,90]
# # # val = sequential(lst,100)
# # # print(val)


# # # def biarySearch(lst,val):
# # # 	first = 0
# # # 	last = len(lst)
# # # 	found = False

# # # 	while first<= last and not found:
# # # 		mid = (first+last)//2
# # # 		if lst[mid] == val:
# # # 			found = True
# # # 		else:
# # # 			if val < lst[mid]:
# # # 				last = mid-1
# # # 			else:
# # # 				first = mid+1
# # # 	return found


# # # lst = [50,2,4,7,90]
# # # lst.sort()
# # # print(lst)
# # # val = biarySearch(lst,90)
# # # print(val)



# # # def binarysearch(arr,ele):
# # # 	if len(arr) ==0:
# # # 		return False
# # # 	else:
# # # 		mid = len(arr)//2
# # # 		if ele == arr[mid]:
# # # 			return True
# # # 		else:
# # # 			if ele < arr[mid]:
# # # 				return binarysearch(arr[:mid],ele)
# # # 			else:
# # # 				return binarysearch(arr[mid+1:],ele)
# # # 	return found


# # # val = [10,20,30,40]
# # # code = binarysearch(val,40)
# # # print(code)



# # # def bubblesort(lst):
# # # 	for n in range(0,len(lst)-1,1):
# # # 		for k in range(n):
# # # 			if lst[k+1] < lst[k]:
# # # 				temp = lst[k+1]
# # # 				lst[k+1] = lst[k]
# # # 				lst[k] = temp
# # # 	return lst





# # # def selectionsort(arr):
# # # 	for fillslot in range(0,len(arr)-1,1):
# # # 		postionMax = 0
# # # 		for location in range(1,fillslot+1):
# # # 			if arr[location] > arr[postionMax]:
# # # 				postionMax = location
# # # 		temp = arr[fillslot]
# # # 		arr[fillslot] = arr[postionMax]
# # # 		arr[postionMax] = temp
# # # 	return arr


# # def insertsort(arr,start,gap):
# # 	for i in range(start+gap,len(arr)-1,gap):
# # 		curVal = arr[i]
# # 		position = i
# # 		while position>=gap and arr[position-gap] > curVal:
# # 			arr[position] = arr[position-gap]
# # 			position = position-gap
# # 		arr[position] = curVal


# # def shellsort(arr):
# # 	sublistcount = len(arr)//2

# # 	while sublistcount>0:
# # 		for start in range(sublistcount):
# # 			insertsort(arr,start,sublistcount)
# # 		sublistcount = sublistcount//2
# # 	return arr


# # val = shellsort([10,1,3,20,50])
# # print(val)

# # [10,1,3,20,50]








# def selectionsort(arr):
# 	for fillslot in range(0,len(arr)-1 , 1):
# 		pmax = 0
# 		for location in range(1,fillslot+1):
# 			if arr[location]> arr[pmax]:
# 				pmax = location
		
# 		temp = arr[fillslot]
# 		arr[fillslot]= arr[pmax]
# 		arr[pmax] = temp


# def insertion(arr,first , gap):
# 	for i in range(start,len(arr)-gap):
# 		currval = arr[i]
# 		pos = i
# 		while pos>0 and arr[pos-gap] > currval:
# 			arr[pos] = currval
# 			pos = pos-gap
# 		arr[pos-gap] = currval 


# def shellsort(arr):
# 	sublistcount = len(arr)//2
# 	while sublistcount>0:
# 		for start in range(sublistcount):
# 			insertion(arr , start , sublistcount)

# 		sublistcount = sublistcount//2




# def quicksort(arr):
# 	quicksorthelper(arr,0 , len(arr)-1)

# def quicksorthelper(arr,first , last):
# 	if first<last:
# 		split = partition(arr , first ,last)

# 		partition(arr, first , split-1)
# 		partition(arr , split+1 , last)
	

# def partition(arr , first , last):
# 	pivot = arr[first]
# 	left = first
# 	right = last
	
# 	done = False

# 	while not done:

# 		while left<=right and arr[left] <= pivot:
# 			left = left+1
		
# 		while arr[right]>= pivot and right>=left:
# 			right = right-1
		
# 		if right<left:
# 			done = True
# 		else:
# 			temp = arr[left]
# 			arr[left] = arr[right]
# 			arr[right] = temp
	
# 	temp = arr[first]
# 	arr[first] = arr[right]
# 	arr[right] = temp



# def merge(arr):
# 	if len(arr)>1:
# 		mid = len(arr)//2
# 		left = arr[:mid]
# 		right = arr[mid:]
		
# 		merge(left)
# 		merge(right)
# 		i= 0
# 		j=0
# 		k=0
# 		while i<len(left) and i< len(right):
# 			if left[i] < right[j]:
# 				arr[k] = left[i]
# 				i = i+1
# 			else:
# 				arr[k] = right[j]
# 				j = j-1
# 		k = k+1
		
# 		while i<len(left):
# 			arr[k]= left[i]
# 			i = i+1
# 			k = k+1

# 		while j<len(right):
# 			arr[k] = right[j]
# 			j = j+1
# 			k = k+1
# 	return arr


adjacent_list = {
	"A":["B","C"],
	"B":["A","D"],
	"C":["A","D","E"],
	"D":["B","C","E"],
	"E":["C","D"]
}

# class Graph:
# 	def __init__(self,nodes, is_directed=False):
# 		self.nodes =nodes
# 		self.adj_list = {}
# 		self.is_directed = is_directed

# 		for node in self.nodes:
# 			self.adj_list[node] = []
	
# 	def add_edge(self,u,v):
# 		self.adj_list[u].append(v)
# 		if not self.is_directed:
# 			self.adj_list[v].append(u)
	
# 	def degree(self,node):
# 		return len(self.adj_list[node])
	
# 	def printlist(self):
# 		for node in self.nodes:
# 			print(node ," --> ", self.adj_list[node] )




# nodes = ["A","B","C","D","E"]
# graph = Graph(nodes , is_directed=True)
# graph.add_edge("A","B")
# print(graph.degree("A"))
# graph.printlist()


from queue import Queue

adj_list = {
	"A":["B","C"],
	"B":["A","D"],
	"C":["A","D","E"],
	"D":["B","C","E"],
	"E":["C","D"]
}
	
visited = {}
parent = {}
level = {}
queue = Queue()
bfs_output = []

for node in adj_list.keys():
	visited[node] = False
	parent[node] = None
	level[node] = -1


s = "A"
visited[s] = True
level[s] = 0

queue.put(s)

while not queue.empty():
	u = queue.get()
	bfs_output.append(u)

	for v in adj_list[u]:
		if not visited[v]:
			visited[v] =True
			parent[v] = u
			level[v] = level[u]+1
			queue.put(v)
print("output",bfs_output)
	


print(parent)
print(visited)
print(level)


v = "D"
path = []
while v is not None:
	path.append(v)
	v = parent[v]
path.reverse()
print(path)