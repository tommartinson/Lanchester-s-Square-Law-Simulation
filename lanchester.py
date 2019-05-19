import numpy as np
import matplotlib.pyplot as plt
#Thomas Martinson

#*This program simulates Lanchester's Square Law for aimed fire. It assumes two opposing forces are firing
#continuously at each other. The attrition of each side is proportional to the opposing side troop
#level and it's lethality of firing according to: x(over time)=-By; x>0 && y(over time)=-Ax; y>0. A = alpha,  
#B = beta. x and y are the troop levels of opposing sides, A and B are their respecrtive lethality coefficients.

#initialize 
t_initial = 0.0
t_final = 5.0
dt = 0.01 #time step, delta t 

red_team_size = input('Enter Red Team Size: ')
blue_team_size = input('Enter Blue Team Size: ')
red_team_coeff = input('Enter Red Team Lethality Coefficient: ')
blue_team_coeff = input('Enter Blue Team Lethality Coefficient: ')


num_steps = int((t_final-t_initial)/dt)

t = np.zeros(num_steps) #time
A = np.zeros(num_steps) #red team size
B = np.zeros(num_steps) #blue team size

A[0] = int(red_team_size) #initial red team size
B[0] = int(blue_team_size) #initial blue team size
t[0] = t_initial #initial time

alpha = float(red_team_coeff) #red team hit chance
beta = float(blue_team_coeff) #blue team hit chance

def dA_dt(red, blue):  #calculates change in blue team, doesn't go below 0
  return -beta*blue if red > 0 and blue > 0 else 0

def dB_dt(red, blue):   #calculates change in red team, doesn't go below 0
  return -alpha*red if red > 0 and blue > 0 else 0

for i in range(num_steps-1):
  A[i+1] = A[i] + dt*dA_dt(A[i], B[i])
  B[i+1] = B[i] + dt*dB_dt(A[i], B[i])
  t[i+1] = t[i] + dt

#-----Table Section---------------------------------------------
print ("Time   Red Team   Blue Team")
i=0
while(i < num_steps and A[i]>0 and B[i]>0): #prints while troop levels are above 0
    print ("%2.2f   %2.2f      %2.2f"%(t[i], A[i], B[i]))
    i=i+1

if(t[i-1]<t_final-(2*dt)):
    if(A[i]<B[i]): #prints final value, sets losing team to 0 to prevent a negative
        print("%2.2f   %2.2f      %2.2f"%(t[i], 0, B[i]))
        print("Blue Team Won!")
    else: #prints final value, sets losing team to 0 to prevent a negative
        print("%2.2f   %2.2f      %2.2f"%(t[i], A[i], 0))
        print("Red Team Won!")
else:
    print("Not enough time alloted to finish.")
    if(A[i-1]>B[i-1]):
        print("Red Team is currently winning.")
    else:
        print("Blue Team is currently winning.")

#-----Plot Section----------------------------------------------
plt.figure()
plt.step(t,A,'-r',where = 'post',label='Red Team (A)') #'-r' for red line, time on X, size of red on Y
plt.step(t,B,'-b',where = 'post',label='Blue Team (B)') #'-b' for blue line, time on X, size of blue on Y
plt.ylabel('Team Size') #y-axis label
plt.xlabel('Time (t)')  #x-axis label
plt.legend(loc='best') #adds a legend in the best fit location

