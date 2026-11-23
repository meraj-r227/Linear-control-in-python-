import numpy  as  np 
from  colorama  import Fore,init
init()
import  time  
matrix_diagonal =np.array([[5,0,0],[0,3,0],[0,0,12]])
matrix_identity =np.array([[1,0,0],[0,1,0],[0,0,1]]) 
print(Fore.RED+"[+]"+Fore.GREEN+"Matrix D:")
time.sleep(0.5)
print(Fore.CYAN+str(matrix_diagonal))

print(Fore.RED+"[+]"+Fore.GREEN+"Matrix i:")
time.sleep(0.5)
print(Fore.MAGENTA+str(matrix_identity))


#determinant
det_matrix_diagonal = np.linalg.det(matrix_diagonal)
print(Fore.RED+"[+]"+Fore.GREEN+"Determinant D:")
time.sleep(0.5)
if det_matrix_diagonal ==  0  :
    print("singular matrix ") 
else:
    print(Fore.BLUE+str(int(det_matrix_diagonal))) 
    
print(Fore.RED+"[+]"+Fore.GREEN+"Determinant i:")
time.sleep(0.5)
det_matrix_identity = np.linalg.det(matrix_identity)
print(Fore.BLUE+str(int(det_matrix_identity)))


#inverse 

inv_matrix_identity = np.linalg.inv(matrix_identity)
print(Fore.RED+"[+]"+Fore.GREEN+"Inverse i:")
time.sleep(0.5)
print(Fore.LIGHTBLUE_EX+str(inv_matrix_identity))


# Multiplaction  
mult =  np.dot(matrix_diagonal,matrix_identity)
print(Fore.RED+"[+]"+Fore.GREEN+"Mult D & i:")
time.sleep(0.5)
print(Fore.MAGENTA+str(mult))
# (meghdar  vezhe)Eigenvalues & (Bordar vezhe)Eigenvector
#Eginvalues are  USed to  check the  stability  of  the  system  
#while  Eigenvector  are  Used  to  determine the directions and  paths  of  stability  (which represent  the  modes  of  motion)
Eig_value , Eig_vector =  np.linalg.eig(matrix_identity)
print(Fore.RED+"[+]"+Fore.GREEN+"Eginvalues matrix_identity:")
time.sleep(0.5)
print(Fore.CYAN+str(Eig_value))
print(Fore.RED+"[+]"+Fore.GREEN+"Eigenvector matrix_identity:")
time.sleep(0.5)
print(Fore.CYAN+str(Eig_vector))


# Ax=b
A = np.array([[1,0,0],[0,1,0],[0,0,1]])
print(Fore.RED+"[+]"+Fore.GREEN+"A:")
time.sleep(0.5)
print(Fore.LIGHTBLUE_EX+str(A))
b = np.array([[12,2,1],[11,34,3],[54,53,2]])
print(Fore.RED+"[+]"+Fore.GREEN+"b:")
time.sleep(0.5)
print(Fore.LIGHTBLUE_EX+str(b))
x =  np.linalg.solve(A,b)
print(Fore.RED+"[+]"+Fore.GREEN+"Ax=b:")
time.sleep(0.5)
print(Fore.CYAN+str(x))
    