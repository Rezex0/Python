a = {10,20,30,40}
a.add(50)
a.update({1,2})
print(a)

a.remove(20)


a.discard(100) # This will not raise an error even if 100 is not present in the set.
a.pop()


#set mathametical operations
a={10,20,30 ,40 }
b = {10, 30, 40, 60}

print(a.union(b)) # Union of two sets
print(a|b)

#intersection of two sets
print(a.intersection(b))
print(a&b)

print(a.difference(b)) # elements present in a but not in b 
print(a-b)
print(b.difference(a))
print(b-a)


c = {30,40}
d = {30, 40 , 60 , 50}
print(d.issubset(c)) # check if c is subset of d
print(c.issubset(d)) # check if d is subset of c
print(c.issuperset(d)) # check if c is superset of d


#isdisjoint
e = {10,20,30}
f= {40,50,60}

print(e.isdisjoint(f)) # check if e and f have no elemnts in commmon 
