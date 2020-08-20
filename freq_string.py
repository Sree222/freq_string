from collections import Counter

b=input("enter string:")
a=Counter(b).most_common()
print(a)
#[('a', 5), ('r', 2), ('b', 2), ('c', 1), ('d', 1)]
