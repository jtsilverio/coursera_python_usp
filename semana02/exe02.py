n = []
for i in range(4):
    n.append(float(input("Digite a nota %d: " % (i+1))))

print("A média aritmética é %f" % (sum(n)/len(n)))