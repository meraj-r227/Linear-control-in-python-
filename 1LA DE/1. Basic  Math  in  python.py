#basic  math  in  python  
# WHEN we  use  as  ,  we  can  change name    your  libriry  
#numpy == np 
from  colorama import Fore,init
init()
# for  graph   we  use  matplotlib
import numpy  as  np
import math
import matplotlib.pyplot as plt 

num1=np.sin(0)
print(Fore.CYAN+str(int(num1)))

# HOW   we to  convert  radian  to  degree  or vice versa====>>>

Radian =  math.pi/3
degree = math.degrees(Radian)
print(f"Radian:{Radian}")
print(f"degree:{degree}")

#factorial  
T=10  
Fact=math.factorial(T)
print(Fore.MAGENTA+str(Fact))
ss=4
s=math.sqrt(ss)
print(int(s))
logg= math.log10(T)
print(int(logg))
expp =  math.exp(0)
print(Fore.GREEN+str(int(expp)))

## imagine you have a ruler that starts at 0  and  ends at 10  
# Now what the linspace function does  is  ask  you:  
# "Tell  me  how  many  points you want me to place on this ruler?"
# for  ex if  Start of the  line : 0  & End  of  the line  :10  
# if  you  tell  python np.linspace(0,10,5),you  are saying :  
# Divide  the  space  from  0  to  10  into  5  equal  parts  and  mark them  for  me  
# Then  python  will  space 5 points with  equal  spacing  :  
# 0 -- 2.5 -- 5 -- 7.5 -- 10  
#** in  linspace the smaller  the  number  of  point  we  specify (the third argument),the  more  discrete the  function  will be
#** conversely , the lager the  number  we  specify, the  more continous  the  function  will  appear
# if  write  (x,x,100)===>>> is  countinous  
# if  wirte  (x,x,10)====>>>> is  discrete 
x = np.linspace(0,2*np.pi,100)
y1 = np.sin(x)
y2 = np.cos(x)
plt.figure(figsize=(10,6))
plt.plot(x,y1,label='sin(x)')
plt.plot(x,y2,label='cos(x)')
plt.xlabel('variable x')
plt.ylabel('variable y')
plt.title('sine & cosine functions')
#it  is  the  gragh's guide (legend) and  show what each  line  is  related to  .(plt.legend())
plt.legend()
# for  print  we  use  plt.show()
plt.show()




