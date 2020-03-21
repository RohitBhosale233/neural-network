print('-------------------------------------------------------------------------')
print("\nPerceptron Network for AND function having both bipolar input and outputs")
print("\nNotations used:\nx1 and x2 are two inputs ,t is target output, lr is learning rate,yin is net input ,y is calculated output,y=t is checking condition 1 if y=t else 0,first w1,w2,b are delta w1,delta w2 and delta bias respectively and last w1,w2,b are updated weigths and bias.")
print("\nInitial weights: w1=0  w2=0  b=0 theta=0\n ")
print('------------------------------------------------------------------------')
table=[[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,-1],[1,1,1,1],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0],[0,0,0]]
theta=0

def customprint(value):
    if(value>=0):
        print(" ",value,end=" ")
    else:
        print("",value,end=" ")

def epoch(step):
    
    if(step<5):
        print("\nEpoch ",step,": \n")
        print(" x1  x2   t  lr  yin  y  y=t  w1  w2  b  w1   w2  b ")
        print('------------------------------------------------------------------------')
        correct=0
        for i in range(len(table[0])):
            
            yin=table[8][0]*table[0][i]+table[8][1]*table[1][i]+table[8][2]
            table[4][i]=yin
            if(yin>theta):
                y=1
            elif(yin<theta):
                y=-1  
            else:
                y=0

            table[5][i]=y
            if(table[5][i]==table[2][i]):
                table[6][i]=1            
                correct=correct+1
                
            else:
                table[7][0]=table[2][i]*table[0][i]*table[3][i]
                table[7][1]=table[2][i]*table[1][i]*table[3][i]
                table[7][2]=table[2][i]*table[3][i]

                table[8][0]=table[8][0]+table[7][0]
                table[8][1]=table[8][1]+table[7][1]
                table[8][2]=table[8][2]+table[7][2]
                    
            #print(table[0][i]," ",table[1][i]," ",table[2][i]," ",table[3][i],"  ",table[4][i]," ",table[5][i]," ",table[6][i]," ",end="")
            #customprint(table[0][i])
            for j in range(7):
                customprint(table[j][i])
            for i in range(len(table[7])):
                customprint(table[7][i])
                #print(table[7][i],"    |","",end="")
            for i in range(len(table[7])):
                customprint(table[8][i])
                #print(table[8][i],"|","",end="")
            
            print('\n------------------------------------------------------------------------')        
        
        if(correct==4):
            print("\n Condition Satisfied\n")
            print(" Updated Weights are:\n w1: ",table[8][0]," w2: ",table[8][1],"\n Updated  bias: ",table[8][2])

        else:
            epoch(step+1)
    else:
        return False
                
epoch(1)