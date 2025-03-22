#Printing Pyramid using Stars
def pyramid():
    n = int(input("Enter the no of rows:"))
    for i in range(n): 
        for j in range(n-i-1):
            print( " " ,end ="")
        for j in range(i+1):
            print("*",end=" ")   
        print()
pyramid()       

#Printing Right Angled Triangle using stars
def right_angle_triangle():
    n = int(input("Enter the number of rows:"))
    for i in range(n):
        for j in range(i,n):
            print(" ",end=" ")
        for j in range(i+1):
            print("*",end=" ")
        print()
right_angle_triangle()
    
    #Printing stars in diamond shape
def diamond():
    n = int(input("Enter the value of n:"))
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ", end=" ")
        for j in range(2*i-1):
            print("*",end=" ")
        print()
    for i in range(n-1,0,-1):
        for j in range(n-i):
            print(" ",end=" ")
        for k in range(2*i-1):
            print("*",end=" ")
        print()

diamond()
