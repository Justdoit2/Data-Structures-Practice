#/usr/bin/env python
# encoding: utf-8
from __future__ import print_function

#Objective: Output pascal triangles


n=int(input("Enter row."))
a=lambda x,y:x +y
def Pascal_rows(row):
  my,copy=[],[]
  start =0
  if row==0:
    return
  while start<row:
    my.append(1)
    print (my)
    start+=1
    if start==2:
      break
  while row>2:
    copy=my[:1]
    for s in range(1,len(my)):
      result=a(my[s-1],my[s])
      copy.append(result)
    copy.append(1)
    print(copy)
    my=copy
    row-=1
  return 
    
print(Pascal_rows(n))
  
  
  
  
  
  
