#result->stops the functions and sends the value.
def numbers():
    return(1,2,3,4,5)
result = numbers()
print(result)


#yield-> allows the execution pause and run, turns function into generator
def numbers():
    for i in range(6):
        yield i

result = numbers() #will print the generator as output
print(result)

for num in result:
    print(num)  #will print the values in the range of for loop
 
