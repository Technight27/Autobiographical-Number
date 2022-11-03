# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def auto(n):
   l=[]
   count=0
   for i in range(0,len(n)):
       index=int(n[i])
       c=0
       for j in range(0,len(n)): 
           if i==int(n[j]):
               c=c+1
       if c==index:
           l.append(index)
       else:
           return 0
           break
   
 
# taking an counter
   count=0
   l1=[]  
    # traversing the array
   for item in l:
       if item not in l1:
           count += 1
           l1.append(item)
   return count        
 


                
            
    
z=auto(input("Enter no "))               
print(z)
                
                
            
