import datetime
from read import read_cl

def generate_invoice(invoice, user_name,user_number):
    today_date = datetime.datetime.now().strftime("%Y-%m-%d")  # Get today's date in YYYY-MM-DD format
    output = []
    output.append("\nFinal Invoice:\n")
    output.append(f"Name: {user_name}                              Date: {today_date}\n")
    output.append("------------------------------------------------------------\n")
    output.append("Name" + " " * 11 + "Facing" + " " * 6 + "Area (Ana)" + " " * 3 + "Rate" + " " * 2 + "Months\n")
    output.append("------------------------------------------------------------\n")
    total_cost = 0
    for item in invoice:
        name, ana, facing, rate, month = item
        cost = rate * month
        total_cost += cost
        # Prepare formatted row
        formatted_row = name + " " * (15 - len(name)) \
                            + facing + " " * (15 - len(facing)) \
                            + str(ana) + " " * (10 - len(str(ana))) \
                            + str(rate) + " " * (7 - len(str(rate))) \
                            + str(month) + " " * (7 - len(str(month)))
        output.append(formatted_row + "\n")
    output.append("------------------------------------------------------------\n")
    output.append(f"Total Due: {total_cost}\n")
    output.append("------------------------------------------------------------\n")

    # Write to file
    with open(user_name + ".txt", "w") as file:
        for line in output:
            file.write(line)
    
    
    # Display the invoice on console
    for line in output:
        print(line, end="")


def modifydata (x, status=" Unavailable"):
    lands = read_cl.reads() 

    lands[x][5] = status  
    
    # Write the updated data back to the file
    with open('lands.txt', 'w') as file:
        for land in lands:
            file.write(','.join(map(str, land)) + '\n')


def modifydatareturn (x, status=" Available"):
    lands = read_cl.reads() 

    lands[x][5] = status  
    
    # Write the updated data back to the file
    with open('lands.txt', 'w') as file:
        for land in lands:
            file.write(','.join(map(str, land)) + '\n')



def generate_invoice_with_returns(invoice, user_name, user_number):
    try:
        today_date = datetime.datetime.now().strftime("%Y-%m-%d")  # Current date
        output = ["\nFinal Invoice:\n"]
        output.append(f"Customer Name: {user_name}                              Date: {today_date}\n")
        output.append(f"Customer Number: {user_number}\n")
        output.append("-------------------------------------------------------------------------\n")
        output.append("Name           Facing     Area       Rate    Month    Returned    Penalty\n")
        output.append("-------------------------------------------------------------------------\n")
        total_cost = 0
        total_penalty = 0

        for item in invoice:
            if len(item) == 6:
                name, ana, facing, rate, month, rtn_mth = item
                penalty_rate = 0.1

                cost = rate * month
                penalty = 0
                if rtn_mth > month:  # Calculate penalty if applicable
                    extra_months = rtn_mth - month
                    penalty = (rate * penalty_rate) * extra_months
                total_cost += cost  # Update total cost
                total_penalty += penalty  # Update total penalty

                formatted_row = f"{name:<15}{facing:<10}{ana:<10}{rate:<8}{month:<8}{rtn_mth:<10}{penalty:<10.2f}\n"
                output.append(formatted_row)
            else:
                print(f"Skipping invalid item with incorrect data length: {item}")

        output.append("-------------------------------------------------------------------------\n")
        output.append(f"Total Rent Cost: {total_cost:.2f}\n")
        output.append(f"Total Penalties: {total_penalty:.2f}\n")
        output.append(f"Grand Total Due: {total_cost + total_penalty:.2f}\n")
        output.append("-------------------------------------------------------------------------\n")

        # Write to file
        filename = f"{user_name}_return_invoice.txt"
        with open(filename, "w") as file:
            file.writelines(output)

        # Display the invoice on the console
        for line in output:
            print(line, end="")

    except Exception as e:
        print(f"Debug: An error occurred: {e}")

