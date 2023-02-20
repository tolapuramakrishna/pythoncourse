import sys,os

name = "RK"
def clear():
    os.system('cls')
    print(f"Welcome Mr.{name}")
    first,second = [10,20] # array destructring
    print(f"{first} - {second}")

if __name__ == '__main__':
    clear()
    sys.exit()