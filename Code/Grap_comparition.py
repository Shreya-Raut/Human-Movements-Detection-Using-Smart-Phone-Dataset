list_feq1 = [0]
for i in range(0,6):
    for n in range(1,int(cmatrix_svmk2[i][i]+1)):
        list_feq1.append(i)

## similarly list_feq2 can be calculated using different dataset and graphycal comparision is made ######

plt.xlabel('walking     upstairs      downstairs       sitting     standing        laying')
plt.ylabel('no. of times')   
plt.hist([list_feq,list_feq1] , bins=[1,2,3,4,5,6], rwidth=0.95 , color=['green','orange'] , label=['previous activities','resent activities'])
plt.legend()
plt.show()