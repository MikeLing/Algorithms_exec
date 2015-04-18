def heap_sort(a):
	build_max_heap(a)
	d = {}
	heap_size = len(a) + 1
	list_to_dic(a,d)
	for i in reversed(range(2,heap_size)):
		exchange(d,1,i)
		a[i-1] = d.pop(i)
		max_heapifu(d,1)		
	a[0] = d[1]	

def build_max_heap(a):
	heap_size = len(a)
	d = {}
	list_to_dic(a,d)
	for i in reversed(range(1,int(heap_size/2))):
		max_heapifu(d,i)
	dic_to_list(d,a)	


def max_heapifu(a,i):
	l = left(i)
	r = right(i)
	heap_size = len(a)
	largest_index = i
	if l <= heap_size and a[l] > a[i]:
		largest_index = l
	if r <= heap_size and a[r] > a[largest_index]:
		largest_index = r
	if largest_index != i:
		exchange(a,i,largest_index)
		max_heapifu(a,largest_index)


def list_to_dic(a,c):
	for i in reversed(range(1,len(a)+1)):
		c[i] = a[i-1]

def dic_to_list(c,a):
	for i in c.keys():
		a[i-1] = c[i]
def left(i):
	return 2*i

def right(i):
	return 2*i + 1
def exchange(a,i,l):
	temp = a[i]
	a[i] = a[l]
	a[l]= temp
