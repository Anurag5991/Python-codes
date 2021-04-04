#print("Hello world")
#name = input("Name:")
#print("Hello: " + name)
#print(f"Hello: {name}")
#num1= input ("Enter a number:")
#num2=input("Enter another number:")
#result = int(num1)+int(num2)
#print(result)
#a = {1 : "s", 2 : 'g'}
#print(a[2])

print(f"file2 __name__ is set to : {__name__}")

def function3():
   print("Function three is executed")

def function4():
   print("Function Four is executed")

if __name__ == "__main__":
    print("File two executed when ran directly")
else:
    print("file two executed when imported")