pca2 = PCA(n_components = 2)
pca2.fit(X_train)
X_train_2 = pca2.transform(X_train)
X_test_2 = pca2.transform(X_test)

x11 = []
x12 = []
x21 = []
x22 = []
x31 = []
x32 = []
x41 = []
x42 = []
x51 = []
x52 = []
x61 = []
x62 = []

for i in range(len(y_test)):
    if (y_test[i] == 1):
        x11.append(X_test_2[i][0])
        x12.append(X_test_2[i][1])
    elif (y_test[i] == 2):
        x21.append(X_test_2[i][0])
        x22.append(X_test_2[i][1])
    elif (y_test[i] == 3):
        x31.append(X_test_2[i][0])
        x32.append(X_test_2[i][1])
    elif (y_test[i] == 4):
        x41.append(X_test_2[i][0])
        x42.append(X_test_2[i][1])
    elif (y_test[i] == 5):
        x51.append(X_test_2[i][0])
        x52.append(X_test_2[i][1])
    else:
        x61.append(X_test_2[i][0])
        x62.append(X_test_2[i][1])

plt.figure() 
plt.plot(x41, x42, 'xr', label = 'Sitting')
plt.plot(x51, x52, 'xm', label = 'Standing')     
plt.plot(x11, x12, 'xc', label = 'Walking')
plt.plot(x21, x22, 'xb', label = 'Upstairs')
plt.plot(x31, x32, 'xy', label = 'Downstairs')
plt.plot(x61, x62, 'xg', label = 'Laying')
plt.legend(loc='lower left')
plt.show()
