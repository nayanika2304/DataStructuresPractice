import heapq

H = [21,1,45,78,3,5]
# Create the heap

heapq.heapify(H)
print(H)

# Remove element from the heap
# always removes the element at the first position
heapq.heappop(H)

print(H)