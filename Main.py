import Return
import ListSplit
import dt
import Borrow

def start():
    while(True):
        print("        Welcome to the library management system     ")
        print("------------------------------------------------------")
        print("Enter 1. To Display")
        print("Enter 2. To Borrow a book")
        print("Enter 3. To return a book")
        print("Enter 4. To exit")
        try:
            a=int(input("Select a choice from 1-4: "))
            print()
            if(a==1):
                with open("Stock.txt","r") as f:
                    lines=f.read()
                    print(lines)
                    print ()
   
            elif(a==2):
                ListSplit.listSplit()
                Borrow.borrowBook()
            elif(a==3):
                ListSplit.listSplit()
                Return.returnBook()
            elif(a==4):
                print("Thank you for using library management system")
                break
            else:
                print("Please enter a valid choice from 1-4")
        except ValueError:
            print("Please input as suggested.")
start()
