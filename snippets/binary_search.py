# Standard-library search and insertion examples.
import bisect

# examples
a=[1,3,5,7,9,11,13,15,17,19]
x=4

insert_index = bisect.bisect_left(a,x)
# insert_index=2

a.insert(insert_index,x)
# a = [1,3,4,5,7,9,11,13,15,17,19]

bisect.insort_left(a, x)
# a = [1,3,4,5,7,9,11,13,15,17,19] Insert before equal values

bisect.insort_right(a,x)
# a = [1,3,4,5,7,9,11,13,15,17,19] Insert after equal values