def encode(string):
    numbers=[]
    encodednum=''
    for i in range(len(string)):
        numbers.append(int(string[i])+3)
    for j in range(len(numbers)):
        encodednum+=str(numbers[j])
        return encodednum

def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
          
def decode(encoded):
    numbers=[]
    newdecoded=''
    for i in range(len(encoded)):
        numbers.append(int(encoded[i])-3)
    for j in range(len(numbers)):
        newdecoded+=str(numbers[j])
    return newdecoded 



def main():
   z=0
   while z==0:
        menu()
        choice= input("Please enter an option: ")
        if choice == "1":
            code= input("Please enter your password to encode")
            x= encode(code)
            print("Your password has been encoded and stored!")
        elif choice =="2":
            print("the encoded password is",x,  "and the original password is" , code)
        elif choice == "3":
            z==1000
        else:
            print("Wrong input")
if __name__ == '__main__':
    main()
