from read import read_cl
from operations import operations_cl
def main():
    print("\t |--------------------------------------|")
    print("\t |      Ram lakhan  land rentals        |")
    print("\t |--------------------------------------|")
    keepRunning = True
    while keepRunning == True:
        print("Type 1 to rent land.")
        print("Type 2 to return land.")
        print("Type 3 to exit system.")
        data = read_cl.reads()
        #checks weather the input is valid or not 
        try:
            userOption=int(input("Enter a value:"))
            print("\n")
            if userOption == 1:

                #display land information, ask kitta no, validate kitta no,
                #ask month, month validate, update available status

                read_cl.print_data(data)
                operations_cl.kita()

            elif userOption == 2:
                read_cl.print_data(data)
                operations_cl.return_data()
            elif userOption == 3:
                print("You are exiting the system")
                keepRunning = False
            else:
                print("Enter valid input only 1 or 2 or 3")
        except ValueError:
            print("Input is not a valid integer.")
            
main()           
     