doornumber = list()

def doors(n):
    global doornumber
    doors = [False] * n
    
    for i in range(n):
        for j in range(i, n, i+1):
            doors[j] = not doors[j]
    
    for k, doors in enumerate(doors):
        if doors == True:
            doornumber.append(k+1)

doors(100)
print("The following door are opened: ", doornumber)