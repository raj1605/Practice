def knapsack(weights,values):

    target = 7

    mat = [[0 for i in range(7+1)] for j in range(len(weights))]

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if(i == 0):
                if(j<weights[i]):
                    continue
                else:
                    mat[i][j] = values[i]

            else:
                if(j<weights[i]):
                    mat[i][j] = mat[i-1][j]
                else:
                    mat[i][j] = max(mat[i-1][j], values[i]+mat[i-1][j-weights[i]])

    i,j = len(mat)-1,len(mat[0])-1
    fin = []
    while(mat[i][j] != 0):
        if(i == 0):
            fin.append(i)
            break
        else:
            if(mat[i-1][j] == mat[i][j]):
                i = i-1
            else:
                fin.append(i)
                j -= weights[i]
                i -= 1

    print(mat)
    print(fin)
                
            

w,v = [1,3,4,5],[1,4,5,7]
knapsack(w,v)

