import heapq

H = [21,1,45,78,3,5]
# Create the heap

heapq.heapify(H)
print(H)

# Replace an element
# always removes the smallest element and inserts at no fixed position
heapq.heapreplace(H,6)
print(H)