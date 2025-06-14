# set1={1,2,4,5,6,7,1,2,2,2}
# print(set1)
# print(len(set1))

# set1.add(8)
# print(set1)
# set1.remove(2)
# print(set1)
# set1.discard(3)
# print(set1) 
# print(set1.pop())
# print(set1.pop())
# print(set1.pop())
# print(set1)

A={1,2,3,4,5}
B={4,5,6,7,8}
# Union of two sets
C = A.union(B)
print("Union of A and B:", C)
# Intersection of two sets
D = A.intersection(B)
print("Intersection of A and B:", D)
# Difference of two sets
E = A.difference(B)         
print("Difference of A and B:", E)  
# Symmetric difference of two sets
F = A.symmetric_difference(B)
print("Symmetric difference of A and B:", F)
