from math import ceil


weight = input("Enter weight of letter in oz:")

if weight>3.5:
    cost = .88 + ceil(weight-1.00) *.17
else:
    cost = .44
        
    if weight>1.00:
        cost = cost + ceil(weight-1.00)*.17
        
print "Cost" , cost

    
    
    
