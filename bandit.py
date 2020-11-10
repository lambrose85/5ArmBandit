import random
from matplotlib import pyplot as plt

"""
Program works by first running 100 time steps on  the greedy algorithm and then the 
greedy-epsilon algorithm. Once both algorithms have executed, the data returned from each
will be plotted on a graph. The Epsilon greedy always out performs the greedy in the end
due to the exploration functionality. Without the exploration it is very possible it could get stuck
on a less than desirable arm and constantly call on it while receiving minimal rewards. Because
it can explore, it is able to switch to an arm that starts giving it a better reward, while at the 
same time having the trade off of potentially getting less of a reward. That is all part of exploring though
and becoming aware of the environment.

To run the program simply call python bandit.py and it will execute. As listed in the assignment a default
epsilon of .4 is used

"""



plotting = []

#Probability of winning 
prob_bands = [.18, .38, .84, .55, .1]
#rewards for each arm
rewards =[3, 2, 1, 2, 9]
#attempts for each bandit arm
attempts = [0,0,0,0,0]
#wins for each bandit arm
wins = [0, 0, 0, 0, 0]
total_rewards = [0,0,0,0,0]
total_rewardsG = [0,0,0,0,0]
#100 time steps
steps = 100
#assigned value to epsilon 
eps = .4
Qt = [0,0,0,0,0]

greedyPlotting=[]
#takes the sum of rewards for action prior to timestep t 
#and divides by the number of times this action has been taken prior to t
#then stores the result in an array where the max value is the returned and used 
#for the greedy algorithm
def sumRewards():
    for i in range(0,4):
        if attempts[i]==0:
            Qt[i]=0
        else:
            val = total_rewards[i]/attempts[i]
            Qt[i]=val
    return Qt.index(max(Qt))

def exploit():
    return sumRewards()
    
def explore():
    return random.randint(0,4)
def lever(x):

    if (random.randint(0,100)/100) < prob_bands[x]:
        wins[x]+= 1
        attempts[x] += 1
        return rewards[x]
    else:
        attempts[x] += 1
        return 0

#greedy algorithm will go for maximum reward at all times
for step in range(1,100):
    val = exploit()
    reward =  lever(val)
    total_rewardsG[val] += reward
    greedyPlotting.append(sum(total_rewardsG))
    

for i in (0,4):
    attempts[i]=0
    Qt[i]=0
    wins[i]=0
#greedy-epsilon option
for step in range(1, 100):
    if random.random() > eps:
        val = exploit()
        reward =  lever(val)
        total_rewards[val] += reward
        plotting.append(sum(total_rewards))
        

    else: 
       temp = explore()
       reward1 = lever(temp)
       total_rewards[temp]+= reward1
       plotting.append(sum(total_rewards))
       
    
    

plt.plot(greedyPlotting, label = 'Greedy')
plt.plot(plotting, label='Greedy-Epsilon')
plt.legend()
plt.xlabel("Total rewards")
plt.ylabel("Time Step")
plt.show()