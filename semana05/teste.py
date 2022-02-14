def maior_primo (x):
    primo = False
    while not primo:
        if x >= 2:
            z = x
            if  z % 1 == 0 and z % z == 0:
                primo == True
            else:    
                z = z - 1
            if z <= x and z % 1 == 0 and z % z == 0:
                primo == True
            else:
                primo == False
        else:
            primo == False
    return (z)


maior_primo(20)