from strings import function3

print(f"File one __name__ is set to :  {__name__} ")

def function1():
    print("Function one executed")

def function2():
    print("Funtion two executed")

if __name__ == "__main__":
    print("File one executed when ran directly")
    function2()
    function3()
else:
    print("file one executed when imported")