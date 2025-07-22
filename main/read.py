class read_cl:
    # Function to read data from the text file and create a 2D list
    def reads():
        data = []
        file = open("lands.txt", "r") 
        for line in file.readlines():
            row = line.replace("\n","").split(",")  # Define 'row' here
            data.append(row)
        file.close()
        return data

    # print_data function to print the data 
    def print_data(data):
        print("K.Nu" + " " + "Location" + " " * (15 - len("Location")) + "Facing" + " " * (7 - len("Facing")) + "Area (Anna)" + " " * (7 - len("Area (Anna)")) + "Rate" + " " * (7 - len("Rate")) + "Status"+"\n")
    
        for row in data:
            print(row[0] + row[1] + " " * (15 - len(row[1])) + row[2]+ " " * (7 - len(row[2])) + row[3] + " " * (3 - len(row[3]))+ row[4]+ " " * (7 - len(row[4])) + row[5])
        print("\n")