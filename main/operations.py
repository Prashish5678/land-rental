from read import read_cl
from write import generate_invoice,modifydata,modifydatareturn,generate_invoice_with_returns

invoice=[]
data=read_cl.reads()
class operations_cl:
    def get_user_details():
        while True:
            user_name = input("Please enter your name: ")
            if user_name:
                break
            print("Name cannot be blank. Please try again.")
        
        while True:
            try:
                number = input("Please enter your number: ")
                # Attempt to convert the number to an integer to check validity
                user_number = int(number)
                break
            except ValueError:
                print("Invalid number. Please enter a numeric value.")
        return user_name, user_number
    #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

            
    def kita():
         #display land information, ask kitta no, validate kitta no,
        #ask month, month validate, update available status
        keepRunning=True
        user_name, user_number = operations_cl.get_user_details()
        while keepRunning == True: 
            
            try:
                file = open(f"{user_name}.txt", "r")
                print("A file with this username already exists. Please enter a different username.")
                file.close()  # Close the file explicitly if it exists
                continue  # Skip to the next iteration of the loop to get a new username
            except FileNotFoundError:
                # File does not exist, so proceed to create a new record
                pass  # Do nothing and continue the logic

        
                if user_name!="":
                    try:
                        data=read_cl.reads()
                        uKita=int(input("enter the kita number: "))
                        if uKita == "":
                            print ("the Kita number can't be blank ")
                        elif uKita > 110 or uKita < 101:
                            print ("Enter a valid kita number between 101- 110")
                        else:
                            x = uKita - 101

                        if data[x][5].strip() == "Unavailable":
                            print ("the land is currently Unavailable please select a valid kita ")           
                        else:
                            month=int(input(f"Enter how many months do you want rent {data[x][1]} land for "))
                            if month<=0:
                                print ("the value of month must be greater than 0 ")
                            else:
                                print ("the land was selected sucessfully")
                                rate=int(data[x][4].strip())
                                name=data[x][1]
                                ana=data[x][3]
                                facing=data[x][2]
                                invoice.append([name, ana, facing, rate, month])
                                while keepRunning==True:
                                    user_input = input("Would you like to rent another land? (Y/N): ").upper()
                                    if user_input == "Y":
                                        modifydata (x, status=" Unavailable")
                                        break
                                    elif user_input == "N":
                                        generate_invoice(invoice, user_name,user_number)
                                        keepRunning = False
                                        modifydata (x, status=" Unavailable")
                                    else:
                                        print("Please enter 'Y' for yes or 'N' for no.")
                    except ValueError:
                        print ("enter any number ")

    def return_data():
        keepRunning=True
        keepRunning1=True
        while keepRunning1==True:
            user_name, user_number = operations_cl.get_user_details()
            try:
                file = open(user_name+".txt", "r") 
                if user_name!="":
                    while keepRunning == True:
                        try:
                            data=read_cl.reads()
                            uKita=int(input("enter the kita number: "))
                            if uKita == "":
                                print ("the Kita number can't be blank ")
                            elif uKita > 110 or uKita < 101:
                                print ("Enter a valid kita number between 101- 110")
                            else:
                                x = uKita - 101

                            if data[x][5].strip() == "Available":
                                print ("the land hasn't been rented yet, pleasse select a valid kita number ")           
                            else:
                                month=int(input(f"Enter how many months did you want rent {data[x][1]} land for "))
                                rtn_mth=int(input(f"Enter after how many months are yor returing the land "))
                                if month<=0 and rtn_mth<=0:
                                    print ("the value of month and return month must be greater than 0 ")
                                else:
                                    rate=int(data[x][4].strip())
                                    name=data[x][1]
                                    ana=data[x][3]
                                    facing=data[x][2]
                                    invoice.append([name, ana, facing, rate, month, rtn_mth])
                                    while keepRunning==True:
                                        user_input = input("would you like to return another land (Y/N): ").upper()
                                        if user_input == "Y":
                                            modifydatareturn (x, status=" Available")
                                            break
                                        elif user_input == "N":
                                            generate_invoice_with_returns(invoice, user_name, user_number)
                                            keepRunning = False
                                            modifydatareturn (x, status=" Available")
                                            keepRunning1=False
                                        else:
                                            print("Please enter 'Y' for yes or 'N' for no.")
                        except:
                            print ("enter any number ")
            except FileNotFoundError:
                print ("please enter the username that has already rented a land ")



        