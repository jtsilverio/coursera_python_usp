""" Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder, respectivamente, às coordenadas x e y de um ponto em um plano cartesiano. 
Os dois últimos devem corresponder, respectivamente, às coordenadas x e y de um outro ponto no mesmo plano.

Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima

longe

na saída. Caso o contrário, quando a distância for menor que 10, imprima

perto """
numbers = []

for i in range(4):
    numbers.append(int(input("Digite um número: ")))

dist = ((numbers[0] - numbers[2]) ** 2 + (numbers[1] - numbers[3]) ** 2) ** (1 / 2)

if dist >= 10:
    print("longe")
else:
    print("perto")
