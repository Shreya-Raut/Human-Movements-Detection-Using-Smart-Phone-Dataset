a = [accuracy_lda , accuracy_logr , accuracy_knc , accuracy_svmk , accuracy_svmk2 , accuracy_svmk3 ]
gre = max(a)

if(gre == accuracy_lda):
    print("\n \n The accuracy of LDA alorithm is high : \n \n")
    walking = cmatrix_lda[0][0]/50
    print("walking :",walking,"sec" )
    upstairs = cmatrix_lda[1][1]/50
    print("upstairs :",upstairs,"sec" )
    downstairs = cmatrix_lda[2][2]/50
    print("downstairs :",downstairs,"sec" )
    sitting = cmatrix_lda[3][3]/50
    print("sitting :",sitting,"sec" )
    standing = cmatrix_lda[4][4]/50
    print("standing :",standing,"sec" )
    laying = cmatrix_lda[5][5]/50
    print("laying :",laying,"sec" )
    

if(gre == accuracy_logr):
    print("\n \n The accuracy of Logistic Regression is high : \n \n")
    walking = cmatrix_logr[0][0]/50
    print("walking :",walking,"sec" )
    upstairs = cmatrix_logr[1][1]/50
    print("upstairs :",upstairs,"sec" )
    downstairs = cmatrix_logr[2][2]/50
    print("downstairs :",downstairs,"sec" )
    sitting = cmatrix_logr[3][3]/50
    print("sitting :",sitting,"sec" )
    standing = cmatrix_logr[4][4]/50
    print("standing :",standing,"sec" )
    laying = cmatrix_logr[5][5]/50
    print("laying :",laying,"sec" )

if(gre == accuracy_knc):
    print("\n \n The accuracy of knn alorithm is high : \n \n")
    walking = cmatrix_knc[0][0]/50
    print("walking :",walking,"secs" )
    upstairs = cmatrix_knc[1][1]/50
    print("upstairs :",upstairs,"secs" )
    downstairs = cmatrix_knc[2][2]/50
    print("downstairs :",downstairs,"secs" )
    sitting = cmatrix_knc[3][3]/50
    print("sitting :",sitting,"secs" )
    standing = cmatrix_knc[4][4]/50
    print("standing :",standing,"secs" )
    laying = cmatrix_knc[5][5]/50
    print("laying :",laying,"secs" )
    
if(gre == accuracy_svmk):
    print("\n \n The accuracy of SVM with rbf is high : \n \n")
    walking = cmatrix_svmk[0][0]/50
    print("walking :",walking,"secs" )
    upstairs = cmatrix_svmk[1][1]/50
    print("upstairs :",upstairs,"secs" )
    downstairs = cmatrix_svmk[2][2]/50
    print("downstairs :",downstairs,"secs" )
    sitting = cmatrix_svmk[3][3]/50
    print("sitting :",sitting,"secs" )
    standing = cmatrix_svmk[4][4]/50
    print("standing :",standing,"secs" )
    laying = cmatrix_svmk[5][5]/50
    print("laying :",laying,"secs" )
    
if(gre == accuracy_svmk2):
    print("\n \n The accuracy of SVM with kernel linear is high : \n \n")
    walking = cmatrix_svmk2[0][0]/50
    print("walking :",walking,"secs" )
    upstairs = cmatrix_svmk2[1][1]/50
    print("upstairs :",upstairs,"secs" )
    downstairs = cmatrix_svmk2[2][2]/50
    print("downstairs :",downstairs,"secs" )
    sitting = cmatrix_svmk2[3][3]/50
    print("sitting :",sitting,"secs" )
    standing = cmatrix_svmk2[4][4]/50
    print("standing :",standing,"secs" )
    laying = cmatrix_svmk2[5][5]/50
    print("laying :",laying,"secs" )
        
if(gre == accuracy_svmk3):
    print("\n \n The accuracy of SVM with kernel poly is high : \n \n")
    walking = cmatrix_svmk3[0][0]/50
    print("walking :",walking,"secs" )
    upstairs = cmatrix_svmk3[1][1]/50
    print("upstairs :",upstairs,"secs" )
    downstairs = cmatrix_svmk3[2][2]/50
    print("downstairs :",downstairs,"secs" )
    sitting = cmatrix_svmk3[3][3]/50
    print("sitting :",sitting,"secs" )
    standing = cmatrix_svmk3[4][4]/50
    print("standing :",standing,"secs" )
    laying = cmatrix_svmk3[5][5]/50
    print("laying :",laying,"secs" )
