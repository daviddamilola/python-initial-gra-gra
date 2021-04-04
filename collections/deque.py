# deques are list-like objects that support thread-safe, memory-efficient appends.
# its mutable and suppports some operation of list like indexing
# deques can not be directly sliced like dq[1:2]
from collections import deque
import itertools
dq = deque('abc')
dq.append('d')

#dq ---> deque(['a', 'b', 'c', 'd'])
dq.appendleft('z')

#dq --->deque(['z', 'a', 'b', 'c', 'd'])
dq.extend('efg')

#dq --->deque(['z', 'a', 'b', 'c', 'd', 'e', 'f', 'g'])
dq.extendleft('yxw')

#dq --->deque(['w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g'])


#pop and pop left
dq.pop()
#returns 'g'
#dq ---> deque(['w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f'])

dq.popleft()
#returns 'w'
#dq --->deque(['x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f'])

#rotate

"""
rotate(n) method to move and rotate all items of n steps to the right
for positive values of the integer n, or left for negative values of n the left, using positive
integers as the argument, for example:
"""

# to slice a deque
list(itertools.islice(dq, 3, 9))
