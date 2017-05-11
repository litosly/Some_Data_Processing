import tensorflow as tf
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import string
import pickle
import json
%matplotlib inline 

##get the list of trajectories start with result[1] indicates the first car
data = pd.read_csv('test.csv', header=None)
res = data[8]
del res[0]

#change to list
trajectory1 = res[1].split(',')
trajectory1_new=[]
for i in range(len(trajectory1)):
    temp1 = trajectory1[i].replace(']','')
    temp2 = temp1.replace('[','')
    trajectory1_new.append(float(temp2))  

i = 1
trajectory =[]
trajectory_new = []
while(i<len(res)+1):
    trajectory.append(res[i].split(','))
    i+=1


#initialize
trajectory = []
temp = []
final_res = []

test_res = []

for i in range(len(res)):
    #get the str version of each trajectory
    trajectory.append(res[i+1].split(','))  
    
    ##get the float version of each trajectory
    for j in range(len(trajectory[i])):
        
        #remove unnecessary element 
        temp1 = trajectory[i][j].replace(']','')
        temp2 = temp1.replace('[','')
        
        #save the i-th element of the fianl result into temp
        temp.append(float(temp2))
        
        test_res.append(float(temp2))
        
    #copy the i-th trajectory into the i-th element of final result
    final_res.append(temp) 
    #reset temp
    temp = [] 


longitude = [1]*(len(final_res))
latitude = [1]*(len(final_res))

#to get data for tableau
test_x = test_res[::2]
test_y = test_res[1::2]

#longitude and latitude for graph
for i in range(len(final_res)):
    longitude[i] = final_res[i][::2]
    latitude[i] = final_res[i][1::2]



for i in range(len(final_res)-1):
    xlable = longitude[i]
    ylable = latitude[i]
    plt.plot(xlable,ylable)
plt.show()


## to get start and end points 
#initialize
start_x = []
start_y = []
end_x = []
end_y = []
#find start and end point
for i in range(len(final_res)-1):
    start_x.append(final_res[i][0])
    start_y.append(final_res[i][1])
    end_x.append(final_res[i][-2])
    end_y.append(final_res[i][-1])


## get during_trip data for trajectories
modified_data = {'x':test_x,'y':test_y}
df = pd.DataFrame(modified_data, columns = ['x', 'y'])
df.to_csv('i_just_want_to_use_a_very_long_name', sep='\t')

## get start point data for trajectories
start_points = {'start_x':start_x,'start_y':start_y}
df = pd.DataFrame(start_points, columns = ['start_x', 'start_y'])
df.to_csv('start points collections', sep='\t')

## get end point data for trajectories
end_points = {'end_x':end_x,'end_y':end_y}
df = pd.DataFrame(end_points, columns = ['end_x', 'end_y'])
df.to_csv('end points collections', sep='\t')
