import pandas as pd

print("\n The Given Training Data Set \n")
a = pd.read_csv('ws.csv', header=None)
a = a.values.tolist()
num_attributes = len(a[0])-1


print("\n The initial value of hypothesis: ")
S = ['0'] * num_attributes
G = ['?'] * num_attributes

print ("\n The most specific hypothesis S0 :[0,0,0,0,0,0]\n")
print (" \n The most general hypothesis G0 : [?,?,?,?,?,?]\n")

# Assigning S with First Training Example without target variable
S = a[0][:-1]

# Comparing with Remaining Training Examples of Given Data Set
print("\n Candidate Elimination algorithm Hypotheses Version Space Computation\n")
temp = []
for i in range(0,len(a)):
    print("------------------------------------------------------------------------------")
    if a[i][num_attributes]=='Yes':
        for j in range(0,num_attributes):
            if a[i][j]!=S[j]:
                S[j]='?'
        
        for j in range(0,num_attributes):
            for k in range(1,len(temp)):
                if temp[k][j]!= '?' and temp[k][j] !=S[j]:
                    del temp[k]



