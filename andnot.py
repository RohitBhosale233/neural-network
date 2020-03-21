def epoch(w1,w2,step,data):
    print('----------------------------------------------------')
    print("Iteration :",step," w1: ",w1,' w2: ',w2)

    print('----------------------------------------------------')
    data[3]=[0,0,0,0]

 
    
    for j in range(4):
        y=(data[0][j]*w1)+(data[1][j]*w2)
            
        data[3][j]=y
        
    print('---------------')
    print("x1  x2  t  yin")
    print('---------------')

    for i in range(len(data)):
        print(data[0][i]," ",data[1][i]," ",data[2][i]," ",data[3][i])
    theta=max(data[3])  
    print('----------------')
    print("theta is",theta)

    for i in range(4):
        if(data[3][i]>=theta):
            data[3][i]=1
        else:
            data[3][i]=0

    

    correct=0
    for i in range(4):
        if(data[2][i]==data[3][i]):
            correct=correct+1
            #print("correct",correct)
       

    print('---------------')
    print("x1  x2  t  yin")
    print('---------------')
    for i in range(len(data)):
        print(data[0][i]," ",data[1][i]," ",data[2][i]," ",data[3][i])
    theta=max(data[3])  
    
    if(correct==4):
        print('----------------')
        print("condition satisfied")
        print('-----------------------------Stop here-------------------')
        print("Final weights w1:",w1, "w2:",w2," theta:",theta)
        print('---------------------------------------------------')
    else:
        
        if(step==1):
            print('----------------')
            print("condition not satisfied")
            epoch(1,-1,2,data)
        if(step==2):
            print('----------------')
            print("condition not satisfied")
            epoch(-1,1,3,data)
        if(step==3):
            print('----------------')
            print("condition not satisfied")
            epoch(-1,-1,4,data)

        

data=[[1,1,0,0],[1,0,1,0],[0,1,0,0]] 
data.append([0,0,0,0]) 

epoch(1,1,1,data)