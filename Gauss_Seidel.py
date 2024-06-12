# <abc Crea 2020> - <Oscar Eduardo Ochoa Velasco>

#Creating the menu
menu = """
1.- Three Variable Matrix
2.- Four Variable Matrix
3.- Five Variable Matrix
4.- Example
"""

#Iteration variable - If you want more iterations per equation modify this variable
ITA = 20

#Example Function
def Example():
    VAR = 3 
    A = [ [9, 2, -1], [7, 8, 5], [3, 4, -10] ]
    B = [-2, 3, 6]
    x = [0, 0, 0]
    print("Equation System: ")
    print("")
    print(A[0], "= ", B[0])
    print(A[1], "= ", B[1]) 
    print(A[2], "= ", B[2])
    for i in range(ITA):
        x[0] = (B[0] - (A[0][1]*x[1]) - (A[0][2]*x[2])) / A[0][0]
        x[1] = (B[1] - (A[1][0]*x[0]) - (A[1][2]*x[2])) / A[1][1]
        x[2] = (B[2] - (A[2][0]*x[0]) - (A[2][1]*x[1])) / A[2][2]
        print("")
        print("Iteration: ", i + 1)
        for e in range(VAR):
            print("X", e+1, ":", x[e])

#Function that resolve equations with three variables
def Matrix3():
    VAR = 3 
    A = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]
    B = [0, 0, 0]
    x = [0, 0, 0]
    print("Enter the values of the Equation System")
    for u in range(3):
        print("Ecuacion ", u + 1, ":")
        for v in range(3):
            A[u][v] = float(input())
            print(A)
    print("Ingresa las igualaciones del sistema de ecuaciones")
    for w in range(3):
        print("Igualación de la Ecuacion ", w + 1, ":")
        B[w] = float(input())
        print(B)
    print("Equation System: ")
    print("")
    print(A[0], "= ", B[0])
    print(A[1], "= ", B[1]) 
    print(A[2], "= ", B[2])
    for i in range(ITA):
        x[0] = (B[0] - (A[0][1]*x[1]) - (A[0][2]*x[2])) / A[0][0]
        x[1] = (B[1] - (A[1][0]*x[0]) - (A[1][2]*x[2])) / A[1][1]
        x[2] = (B[2] - (A[2][0]*x[0]) - (A[2][1]*x[1])) / A[2][2]
        print("")
        print("Iteration: ", i + 1)
        for e in range(VAR):
            print("X", e+1, ":", x[e])

#Function that resolve equations with four variables
def Matrix4():
    VAR = 4 
    A = [ [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0] ]
    B = [0, 0, 0, 0]
    x = [0, 0, 0, 0]
    print("Enter the values of the Equation System")
    for u in range(4):
        print("Equation ", u + 1, ":")
        for v in range(4):
            A[u][v] = float(input())
            print(A)
    print("Enter the Right-Hand Sides of the Equation System")
    for w in range(4):
        print("Right-Hand Side ", w + 1, ":")
        B[w] = float(input())
        print(B)
    print("Equation System: ")
    print("")
    print(A[0], "= ", B[0])
    print(A[1], "= ", B[1]) 
    print(A[2], "= ", B[2])
    print(A[3], "= ", B[3])
    for i in range(ITA):
        x[0] = (B[0] - (A[0][1]*x[1]) - (A[0][2]*x[2]) - (A[0][3]*x[3])) / A[0][0]
        x[1] = (B[1] - (A[1][0]*x[0]) - (A[1][2]*x[2]) - (A[1][3]*x[3])) / A[1][1]
        x[2] = (B[2] - (A[2][0]*x[0]) - (A[2][1]*x[1]) - (A[2][3]*x[3])) / A[2][2]
        x[3] = (B[3] - (A[3][0]*x[0]) - (A[3][1]*x[1]) - (A[3][2]*x[2])) / A[3][3]
        print("")
        print("Iteration: ", i + 1)
        for e in range(VAR):
            print("X", e+1, ":", x[e])

#Function that resolve equations with five variables
def Matrix5():
    VAR = 5
    A = [ [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0] ]
    B = [0, 0, 0, 0, 0]
    x = [0, 0, 0, 0, 0]
    print("Enter the values of the Equation System")
    for u in range(5):
        print("Equation ", u + 1, ":")
        for v in range(5):
            A[u][v] = float(input())
            print(A)
    print("Enter the Right-Hand Sides of the Equation System")
    for w in range(5):
        print("Right-Hand Side ", w + 1, ":")
        B[w] = float(input())
        print(B)
    print("Equation System: ")
    print("")
    print(A[0], "= ", B[0])
    print(A[1], "= ", B[1]) 
    print(A[2], "= ", B[2])
    print(A[3], "= ", B[3])
    print(A[4], "= ", B[4])
    for i in range(ITA):
        x[0] = (B[0] - (A[0][1]*x[1]) - (A[0][2]*x[2]) - (A[0][3]*x[3]) - (A[0][4]*x[4])) / A[0][0]
        x[1] = (B[1] - (A[1][0]*x[0]) - (A[1][2]*x[2]) - (A[1][3]*x[3]) - (A[1][4]*x[4])) / A[1][1]
        x[2] = (B[2] - (A[2][0]*x[0]) - (A[2][1]*x[1]) - (A[2][3]*x[3]) - (A[2][4]*x[4])) / A[2][2]
        x[3] = (B[3] - (A[3][0]*x[0]) - (A[3][1]*x[1]) - (A[3][2]*x[2]) - (A[3][4]*x[4])) / A[3][3]
        x[4] = (B[4] - (A[4][0]*x[0]) - (A[4][1]*x[1]) - (A[4][2]*x[2]) - (A[4][3]*x[3])) / A[4][4]
        print("")
        print("Iteration: ", i + 1)
        for e in range(VAR):
            print("X", e+1, ":", x[e])

#Main Menu
print("Welcome to the program: Equation Resolution with Gauss Seidel method")
print("Select one option to do")
while True:
    print(menu)
    opc = int(input())
    try:
        if opc is 1:
            Matrix3()
        if opc is 2:
            Matrix4()
        if opc is 3:
            Matrix5()
        elif opc is 4:
            Example()
        else:
            print("Please select an Appropiate Option")
    except ValueError:
        print("ERROR!! Enter only numbers")