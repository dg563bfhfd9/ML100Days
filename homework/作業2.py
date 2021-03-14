import numpy as np
array1 = np.array(range(30))
a=array1.reshape((5, 6))
c=a.ravel(order='F')
print(a)
# 找出被6除於1的數值，就是7
# 但是要怎麼做?
for i in c:
    if i%6 == 1:
        print(i)
        
    
        
    




    



