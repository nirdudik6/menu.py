


def menu2():
    while (True):
        choice = input("enter your choice: \n1.show availabe rooms \n2.search date \n3.order a room \n4.cancel an order \n5.search order and print the order ")
        if (choice == "1"):
            show_rooms2()
        elif (choice == "2"):
            search_date2()
        elif (choice == "3"):
            order_room2()
        elif (choice == "4"):
            cancel_order()
        elif (choice == "5"):
            search_print()
        else:
            print("enter 1-5 only!!")
            continue
        if (input("Do you want to exit? y/n") == "y"):
            break
    print("thanks and bye bye...")
def show_rooms2():
    hotel = input("enter the hotel: ")
    if (hotel == "setai"):
        room1_setai = "C:/Users/User/Desktop/hotels2/setai/room1_setai.txt"
        room2_setai = "C:/Users/User/Desktop/hotels2/setai/room2_setai.txt"
        room3_setai = "C:/Users/User/Desktop/hotels2/setai/room3_setai.txt"
        room4_setai = "C:/Users/User/Desktop/hotels2/setai/room4_setai.txt"
        file1 = open(room1_setai, "r")
        file2 = open(room2_setai, "r")
        file3 = open(room3_setai, "r")
        file4 = open(room4_setai, "r")
        print("---------- \nroom1:")
        print(file1.read())
        print("---------- \nroom2:")
        print(file2.read())
        print("---------- \nroom3:")
        print(file3.read())
        print("---------- \nroom4:")
        print(file4.read())
    elif (hotel == "herodes"):
        room1_herodes = "C:/Users/User/Desktop/hotels2/herodes/room1_herodes.txt"
        room2_herodes = "C:/Users/User/Desktop/hotels2/herodes/room2_herodes.txt"
        room3_herodes = "C:/Users/User/Desktop/hotels2/herodes/room3_herodes.txt"
        room4_herodes = "C:/Users/User/Desktop/hotels2/herodes/room4_herodes.txt"
        file1 = open(room1_herodes, "r")
        file2 = open(room2_herodes, "r")
        file3 = open(room3_herodes, "r")
        file4 = open(room4_herodes, "r")
        print("---------- \nroom1:")
        print(file1.read())
        print("---------- \nroom2:")
        print(file2.read())
        print("---------- \nroom3:")
        print(file3.read())
        print("---------- \nroom4: ")
        print(file4.read())


def search_date2():
    setai1 = "C:/Users/User/Desktop/hotels2/setai/room1_setai.txt"
    setai2 = "C:/Users/User/Desktop/hotels2/setai/room2_setai.txt"
    setai3 = "C:/Users/User/Desktop/hotels2/setai/room3_setai.txt"
    setai4 = "C:/Users/User/Desktop/hotels2/setai/room4_setai.txt"
    herodes1 = "C:/Users/User/Desktop/hotels2/herodes/room1_herodes.txt"
    herodes2 = "C:/Users/User/Desktop/hotels2/herodes/room2_herodes.txt"
    herodes3 = "C:/Users/User/Desktop/hotels2/herodes/room3_herodes.txt"
    herodes4 = "C:/Users/User/Desktop/hotels2/herodes/room4_herodes.txt"
    day = input("enter a date you want to check: (sunday-thoursday)  ")
    file1 = open(setai1, "r")
    file2 = open(setai2, "r")
    file3 = open(setai3, "r")
    file4 = open(setai4, "r")
    room1_list = file1.read().splitlines()
    room2_list = file2.read().splitlines()
    room3_list = file3.read().splitlines()
    room4_list = file4.read().splitlines()
    print("setai:")
    print("room1:")
    if day in room1_list:
        print("available")
    else:
        print("X")
    print("room2:")
    if day in room2_list:
        print("available")
    else:
        print("X")
    print("room3:")
    if day in room3_list:
        print("available")
    else:
        print("X")
    print("room4:")
    if day in room4_list:
        print("available")
    else:
        print("X")
    print("--------------------------------------------------")
    file5 = open(herodes1, "r")
    file6 = open(herodes2, "r")
    file7 = open(herodes3, "r")
    file8 = open(herodes4, "r")
    room5_list = file5.read().splitlines()
    room6_list = file6.read().splitlines()
    room7_list = file7.read().splitlines()
    room8_list = file8.read().splitlines()
    print("herodes:")
    print("room1:")
    if day in room5_list:
        print("available")
    else:
        print("X")
    print("room2:")
    if day in room6_list:
        print("available")
    else:
        print("X")
    print("room3:")
    if day in room7_list:
        print("available")
    else:
        print("X")
    print("room4:")
    if day in room8_list:
        print("available")
    else:
        print("X")


def order_room2():
    room1_setai = "C:/Users/User/Desktop/hotels2/setai/room1_setai.txt"
    room2_setai = "C:/Users/User/Desktop/hotels2/setai/room2_setai.txt"
    room3_setai = "C:/Users/User/Desktop/hotels2/setai/room3_setai.txt"
    room4_setai = "C:/Users/User/Desktop/hotels2/setai/room4_setai.txt"
    room1_herodes = "C:/Users/User/Desktop/hotels2/herodes/room1_herodes.txt"
    room2_herodes = "C:/Users/User/Desktop/hotels2/herodes/room2_herodes.txt"
    room3_herodes = "C:/Users/User/Desktop/hotels2/herodes/room3_herodes.txt"
    room4_herodes = "C:/Users/User/Desktop/hotels2/herodes/room4_herodes.txt"
    hotel=input("enter the hotel that do you want to order: (setai/herodes)\n")
    if hotel==("setai"):
        print("welcome to setai!")
        date=input("Enter the check in day: (sunday-thoursday)\n ")
        adults=int(input("how many adults you are? (2/3)\n"))
        if adults == 2:
            kids = int(input("how many kids you are? (0-2)\n"))
            if (kids == 0):
                room1_setai = open(room1_setai, "r")
                room1_list = room1_setai.read().splitlines()
                if date in room1_list:
                    print("room 1 in setai is available! it'll cost you\n" + "350 NIS")
                    invite=input("Do you want to order this room?\n")
                    if invite=="yes":
                        filename = "C:/Users/User/Desktop/hotels2/setai/orderroom1.txt"
                        file = open(filename, "a")
                        file.write("\n" + input("enter your name: ") + "-" + input("enter your day: (sunday-thoursday) " + "\n"))
                        file.close()
                        with open("C:/Users/User/Desktop/hotels2/setai/room1_setai.txt", "r") as f:
                            lines = f.readlines()
                        with open("C:/Users/User/Desktop/hotels2/setai/room1_setai.txt", "w") as f:
                            for line in lines:
                                if line.strip("\n") != date:
                                    f.write(line)
                        print("order complete!!")
                    else:
                        print("so why did you choose 3...?")
                else:
                    print("sorry this room isn't available :( ")
            elif (kids == 1):
                room2_setai = open(room2_setai, "r")
                room2_list = room2_setai.read().splitlines()
                if date in room2_list:
                    print("room 2 in setai is available! it'll cost you\n" + "450 NIS")
                    invite = input("Do you want to order this room?\n")
                    if invite == "yes":
                        filename = "C:/Users/User/Desktop/hotels2/setai/orderroom2.txt"
                        file = open(filename, "a")
                        file.write("\n" + input("enter your name: ") + "-" + input("enter your day: (sunday-thoursday) " + "\n"))
                        file.close()
                        with open("C:/Users/User/Desktop/hotels2/setai/room2_setai.txt", "r") as f:
                            lines = f.readlines()
                        with open("C:/Users/User/Desktop/hotels2/setai/room2_setai.txt", "w") as f:
                            for line in lines:
                                if line.strip("\n") != date:
                                    f.write(line)
                        print("order complete!!")
                    else:
                        print("so why did you choose 3...?")
                else:
                    print("sorry this room isn't available :( ")

            elif (kids == 2):
                room3_setai = open(room3_setai, "r")
                room3_list = room3_setai.read().splitlines()
                if date in room3_list:
                    print("room 3 in setai is available! it'll cost you\n" + "600 NIS")
                    invite = input("Do you want to order this room?\n")
                    if invite == "yes":
                        filename = "C:/Users/User/Desktop/hotels2/setai/orderroom3.txt"
                        file = open(filename, "a")
                        file.write("\n" + input("enter your name: ") + "-" + input("enter your day: (sunday-thoursday) " + "\n"))
                        file.close()
                        with open("C:/Users/User/Desktop/hotels2/setai/room3_setai.txt", "r") as f:
                            lines = f.readlines()
                        with open("C:/Users/User/Desktop/hotels2/setai/room3_setai.txt", "w") as f:
                            for line in lines:
                                if line.strip("\n") != date:
                                    f.write(line)
                        print("order complete!!")
                    else:
                        print("so why did you choose 3...?")
                else:
                    print("sorry this room isn't available :( ")
        elif (adults == 3):
            room4_setai = open(room4_setai, "r")
            room4_list = room4_setai.read().splitlines()
            if date in room4_list:
                print("room 4 in setai is available! it'll cost you\n" + "550 NIS")
                invite = input("Do you want to order this room?\n")
                if invite == "yes":
                    filename = "C:/Users/User/Desktop/hotels2/setai/orderroom4.txt"
                    file = open(filename, "a")
                    file.write("\n" + input("enter your name: ") + "-" + input("enter your day: (sunday-thoursday) " + "\n"))
                    file.close()
                    with open("C:/Users/User/Desktop/hotels2/setai/room4_setai.txt", "r") as f:
                        lines = f.readlines()
                    with open("C:/Users/User/Desktop/hotels2/setai/room4_setai.txt", "w") as f:
                        for line in lines:
                            if line.strip("\n") != date:
                                f.write(line)
                    print("order complete!!")
                else:
                    print("so why did you choose 3...?")
            else:
                print("sorry this room isn't available :( ")
    elif hotel==("herodes"):
        print("welcome to herodes!")
        date=input("Enter the check in day: (sunday-thoursday)\n ")
        adults=int(input("how many adults you are? (2/3)\n"))
        if adults == 2:
            kids = int(input("how many kids you are? (0-2)\n"))
            if (kids == 0):
                room1_herodes = open(room1_herodes, "r")
                room1her_list = room1_herodes.read().splitlines()
                if date in room1her_list:
                    print("room 1 in herodes is available! it'll cost you\n" + "200 NIS")
                    invite=input("Do you want to order this room?\n")
                    if invite=="yes":
                        filename = "C:/Users/User/Desktop/hotels2/herodes/orderroom1.txt"
                        file = open(filename, "a")
                        file.write("\n" + input("enter your name: ") + "-" + input("enter your day: (sunday-thoursday) " + "\n"))
                        file.close()
                        with open("C:/Users/User/Desktop/hotels2/herodes/room1_herodes.txt", "r") as f:
                            lines = f.readlines()
                        with open("C:/Users/User/Desktop/hotels2/herodes/room1_herodes.txt", "w") as f:
                            for line in lines:
                                if line.strip("\n") != date:
                                    f.write(line)
                        print("order complete!!")
                    else:
                        print("so why did you choose 3...?")
                else:
                    print("sorry this room isn't available :( ")
            elif (kids == 1):
                room2_herodes = open(room2_herodes, "r")
                room2her_list = room2_herodes.read().splitlines()
                if date in room2her_list:
                    print("room 2 in herodes is available! it'll cost you\n" + "250 NIS")
                    invite = input("Do you want to order this room?\n")
                    if invite == "yes":
                        filename = "C:/Users/User/Desktop/hotels2/herodes/orderroom2.txt"
                        file = open(filename, "a")
                        file.write("\n" + input("enter your name: ") + "-" + input("enter your day: (sunday-thoursday) " + "\n"))
                        file.close()
                        with open("C:/Users/User/Desktop/hotels2/herodes/room2_herodes.txt", "r") as f:
                            lines = f.readlines()
                        with open("C:/Users/User/Desktop/hotels2/herodes/room2_herodes.txt", "w") as f:
                            for line in lines:
                                if line.strip("\n") != date:
                                    f.write(line)
                        print("order complete!!")
                    else:
                        print("so why did you choose 3...?")
                else:
                    print("sorry this room isn't available :( ")

            elif (kids == 2):
                room3_herodes = open(room3_herodes, "r")
                room3her_list = room3_herodes.read().splitlines()
                if date in room3her_list:
                    print("room 3 in herodes is available! it'll cost you\n" + "350 NIS")
                    invite = input("Do you want to order this room?\n")
                    if invite == "yes":
                        filename = "C:/Users/User/Desktop/hotels2/herodes/orderroom3.txt"
                        file = open(filename, "a")
                        file.write("\n" + input("enter your name: ") + "-" + input("enter your day: (sunday-thoursday) " + "\n"))
                        file.close()
                        with open("C:/Users/User/Desktop/hotels2/herodes/room3_herodes.txt", "r") as f:
                            lines = f.readlines()
                        with open("C:/Users/User/Desktop/hotels2/herodes/room3_herodes.txt", "w") as f:
                            for line in lines:
                                if line.strip("\n") != date:
                                    f.write(line)
                        print("order complete!!")
                    else:
                        print("so why did you choose 3...?")
                else:
                    print("sorry this room isn't available :( ")

        elif (adults == 3):
            room4_herodes = open(room4_herodes, "r")
            room4her_list = room4_herodes.read().splitlines()
            if date in room4her_list:
                print("room 4 in herodes is available! it'll cost you\n" + "350 NIS")
                invite = input("Do you want to order this room?\n")
                if invite == "yes":
                    filename = "C:/Users/User/Desktop/hotels2/herodes/orderroom4.txt"
                    file = open(filename, "a")
                    file.write("\n" + input("enter your name: ") + "-" + input("enter your day: (sunday-thoursday) " + "\n"))
                    file.close()
                    with open("C:/Users/User/Desktop/hotels2/herodes/room4_herodes.txt", "r") as f:
                        lines = f.readlines()
                    with open("C:/Users/User/Desktop/hotels2/herodes/room4_herodes.txt", "w") as f:
                        for line in lines:
                            if line.strip("\n") != date:
                                f.write(line)
                    print("order complete!!")
                else:
                    print("so why did you choose 3...?")
            else:
                print("sorry this room isn't available :( ")
    else:
        print("choose setai or herodes only!!!")
def cancel_order():
    room1_setai = "C:/Users/User/Desktop/hotels2/setai/room1_setai.txt"
    room2_setai = "C:/Users/User/Desktop/hotels2/setai/room2_setai.txt"
    room3_setai = "C:/Users/User/Desktop/hotels2/setai/room3_setai.txt"
    room4_setai = "C:/Users/User/Desktop/hotels2/setai/room4_setai.txt"
    room1_herodes = "C:/Users/User/Desktop/hotels2/herodes/room1_herodes.txt"
    room2_herodes = "C:/Users/User/Desktop/hotels2/herodes/room2_herodes.txt"
    room3_herodes = "C:/Users/User/Desktop/hotels2/herodes/room3_herodes.txt"
    room4_herodes = "C:/Users/User/Desktop/hotels2/herodes/room4_herodes.txt"
    hotel = input("enter the hotel that do you want to cancel: (setai/herodes)\n")
    if (hotel=="setai"):
        print("welcome to setai hotel! :)")
        day=input("enter a day that you want to cancel: (sunday-thoursday)\n")
        room=input("enter the room number that you want to cancel: (1-4)\n")
        if (room=="1"):
            room1_setai = open(room1_setai, "r")
            room1_list = room1_setai.read().splitlines()
            if day in room1_list:
                print("you didn't order this room!")
            else:
                print("you want to cancel room 1, you'll get back\n" + "350 NIS")
                invite = input("Do you want to cancel this room?\n")
                if invite == "yes":
                    filename = "C:/Users/User/Desktop/hotels2/setai/room1_setai.txt"
                    file = open(filename, "a")
                    file.write("\n" + input("enter the day you want to cancel: (sunday-thoursday)" + "\n"))
                    file.close()
                    details=input("enter the name of the order with '-' and the day: (like nir-sunday)\n")
                    with open("C:/Users/User/Desktop/hotels2/setai/orderroom1.txt", "r") as f:
                        lines = f.readlines()
                    with open("C:/Users/User/Desktop/hotels2/setai/orderroom1.txt", "w") as f:
                        for line in lines:
                            if line.strip("\n") != details:
                                f.write(line)
                    print("the order has canceled!!")
                else:
                    print("so why did you choose 4...?")
        elif (room=="2"):
            room2_setai = open(room2_setai, "r")
            room2_list = room2_setai.read().splitlines()
            if day in room2_list:
                print("you didn't order this room!")
            else:
                print("you want to cancel room 2, you'll get back\n" + "450 NIS")
                invite = input("Do you want to cancel this room?\n")
                if invite == "yes":
                    filename = "C:/Users/User/Desktop/hotels2/setai/room2_setai.txt"
                    file = open(filename, "a")
                    file.write("\n" + input("enter the day you want to cancel: (sunday-thoursday)" + "\n"))
                    file.close()
                    details=input("enter the name of the order with '-' and the day: (like nir-sunday)\n")
                    with open("C:/Users/User/Desktop/hotels2/setai/orderroom2.txt", "r") as f:
                        lines = f.readlines()
                    with open("C:/Users/User/Desktop/hotels2/setai/orderroom2.txt", "w") as f:
                        for line in lines:
                            if line.strip("\n") != details:
                                f.write(line)
                    print("the order has canceled!!")
                else:
                    print("so why did you choose 4...?")
        elif (room=="3"):
            room3_setai = open(room3_setai, "r")
            room3_list = room3_setai.read().splitlines()
            if day in room3_list:
                print("you didn't order this room!")
            else:
                print("you want to cancel room 3, you'll get back\n" + "600 NIS")
                invite = input("Do you want to cancel this room?\n")
                if invite == "yes":
                    filename = "C:/Users/User/Desktop/hotels2/setai/room3_setai.txt"
                    file = open(filename, "a")
                    file.write("\n" + input("enter the day you want to cancel: (sunday-thoursday)" + "\n"))
                    file.close()
                    details=input("enter the name of the order with '-' and the day: (like nir-sunday)\n")
                    with open("C:/Users/User/Desktop/hotels2/setai/orderroom3.txt", "r") as f:
                        lines = f.readlines()
                    with open("C:/Users/User/Desktop/hotels2/setai/orderroom3.txt", "w") as f:
                        for line in lines:
                            if line.strip("\n") != details:
                                f.write(line)
                    print("the order has canceled!!")
                else:
                    print("so why did you choose 4...?")
        elif (room=="4"):
            room4_setai = open(room4_setai, "r")
            room4_list = room4_setai.read().splitlines()
            if day in room4_list:
                print("you didn't order this room!")
            else:
                print("you want to cancel room 4, you'll get back\n" + "550 NIS")
                invite = input("Do you want to cancel this room?\n")
                if invite == "yes":
                    filename = "C:/Users/User/Desktop/hotels2/setai/room4_setai.txt"
                    file = open(filename, "a")
                    file.write("\n" + input("enter the day you want to cancel: (sunday-thoursday)" + "\n"))
                    file.close()
                    details=input("enter the name of the order with '-' and the day: (like nir-sunday)\n")
                    with open("C:/Users/User/Desktop/hotels2/setai/orderroom4.txt", "r") as f:
                        lines = f.readlines()
                    with open("C:/Users/User/Desktop/hotels2/setai/orderroom4.txt", "w") as f:
                        for line in lines:
                            if line.strip("\n") != details:
                                f.write(line)
                    print("the order has canceled!!")
                else:
                    print("so why did you choose 4...?")
        else:
            print("choose 1-4 only!!!")
    elif (hotel=="herodes"):
        print("welcome to herodes hotel! :)")
        day=input("enter a day that you want to cancel: (sunday-thoursday)\n")
        room=input("enter the room number that you want to cancel: (1-4)\n")
        if (room=="1"):
            room1_herodes = open(room1_herodes, "r")
            room1her_list = room1_herodes.read().splitlines()
            if day in room1her_list:
                print("you didn't order this room!")
            else:
                print("you want to cancel room 1, you'll get back\n" + "200 NIS")
                invite = input("Do you want to cancel this room?\n")
                if invite == "yes":
                    filename = "C:/Users/User/Desktop/hotels2/herodes/room1_herodes.txt"
                    file = open(filename, "a")
                    file.write("\n" + input("enter the day you want to cancel: (sunday-thoursday)" + "\n"))
                    file.close()
                    details=input("enter the name of the order with '-' and the day: (like nir-sunday)\n")
                    with open("C:/Users/User/Desktop/hotels2/herodes/orderroom1.txt", "r") as f:
                        lines = f.readlines()
                    with open("C:/Users/User/Desktop/hotels2/herodes/orderroom1.txt", "w") as f:
                        for line in lines:
                            if line.strip("\n") != details:
                                f.write(line)
                    print("the order has canceled!!")
                else:
                    print("so why did you choose 4...?")
        elif (room=="2"):
            room2_herodes = open(room2_herodes, "r")
            room2her_list = room2_herodes.read().splitlines()
            if day in room2her_list:
                print("you didn't order this room!")
            else:
                print("you want to cancel room 2, you'll get back\n" + "250 NIS")
                invite = input("Do you want to cancel this room?\n")
                if invite == "yes":
                    filename = "C:/Users/User/Desktop/hotels2/herodes/room2_herodes.txt"
                    file = open(filename, "a")
                    file.write("\n" + input("enter the day you want to cancel: (sunday-thoursday)" + "\n"))
                    file.close()
                    details=input("enter the name of the order with '-' and the day: (like nir-sunday)\n")
                    with open("C:/Users/User/Desktop/hotels2/herodes/orderroom2.txt", "r") as f:
                        lines = f.readlines()
                    with open("C:/Users/User/Desktop/hotels2/herodes/orderroom2.txt", "w") as f:
                        for line in lines:
                            if line.strip("\n") != details:
                                f.write(line)
                    print("the order has canceled!!")
                else:
                    print("so why did you choose 4...?")
        elif (room=="3"):
            room3_herodes = open(room3_herodes, "r")
            room3her_list = room3_herodes.read().splitlines()
            if day in room3her_list:
                print("you didn't order this room!")
            else:
                print("you want to cancel room 3, you'll get back\n" + "350 NIS")
                invite = input("Do you want to cancel this room?\n")
                if invite == "yes":
                    filename = "C:/Users/User/Desktop/hotels2/herodes/room3_herodes.txt"
                    file = open(filename, "a")
                    file.write("\n" + input("enter the day you want to cancel: (sunday-thoursday)" + "\n"))
                    file.close()
                    details=input("enter the name of the order with '-' and the day: (like nir-sunday)\n")
                    with open("C:/Users/User/Desktop/hotels2/herodes/orderroom3.txt", "r") as f:
                        lines = f.readlines()
                    with open("C:/Users/User/Desktop/hotels2/herodes/orderroom3.txt", "w") as f:
                        for line in lines:
                            if line.strip("\n") != details:
                                f.write(line)
                    print("the order has canceled!!")
                else:
                    print("so why did you choose 4...?")
        elif (room=="4"):
            room4_herodes = open(room4_herodes, "r")
            room4her_list = room4_herodes.read().splitlines()
            if day in room4her_list:
                print("you didn't order this room!")
            else:
                print("you want to cancel room 4, you'll get back\n" + "350 NIS")
                invite = input("Do you want to cancel this room?\n")
                if invite == "yes":
                    filename = "C:/Users/User/Desktop/hotels2/herodes/room4_herodes.txt"
                    file = open(filename, "a")
                    file.write("\n" + input("enter the day you want to cancel: (sunday-thoursday)" + "\n"))
                    file.close()
                    details=input("enter the name of the order with '-' and the day: (like nir-sunday)\n")
                    with open("C:/Users/User/Desktop/hotels2/herodes/orderroom4.txt", "r") as f:
                        lines = f.readlines()
                    with open("C:/Users/User/Desktop/hotels2/herodes/orderroom4.txt", "w") as f:
                        for line in lines:
                            if line.strip("\n") != details:
                                f.write(line)
                    print("the order has canceled!!")
                else:
                    print("so why did you choose 4...?")
        else:
            print("choose 1-4 only!!")
    else:
        print("choose only setai or herodes only!!")

def search_print():
    hotel=input("enter the hotel: (setai/herodes)\n")
    if (hotel=="setai"):
        room=input("enter the room number that you want to see the orders: (1-4)\n")
        if (room=="1"):
            f = open("C:/Users/User/Desktop/hotels2/setai/orderroom1.txt", 'r')
            print (f.read())
            f.close()
        elif (room=="2"):
            f = open("C:/Users/User/Desktop/hotels2/setai/orderroom2.txt", 'r')
            print (f.read())
            f.close()
        elif (room=="3"):
            f = open("C:/Users/User/Desktop/hotels2/setai/orderroom3.txt", 'r')
            print (f.read())
            f.close()
        elif (room=="4"):
            f = open("C:/Users/User/Desktop/hotels2/setai/orderroom4.txt", 'r')
            print (f.read())
            f.close()
        else:
            print("choose 1-4 only!!!")
    elif (hotel=="herodes"):
        room=input("enter the room number that you want to see the orders: (1-4)\n")
        if (room=="1"):
            f = open("C:/Users/User/Desktop/hotels2/herodes/orderroom1.txt", 'r')
            print (f.read())
            f.close()
        elif (room=="2"):
            f = open("C:/Users/User/Desktop/hotels2/herodes/orderroom2.txt", 'r')
            print (f.read())
            f.close()
        elif (room=="3"):
            f = open("C:/Users/User/Desktop/hotels2/herodes/orderroom3.txt", 'r')
            print (f.read())
            f.close()
        elif (room=="4"):
            f = open("C:/Users/User/Desktop/hotels2/herodes/orderroom4.txt", 'r')
            print (f.read())
            f.close()
        else:
            print("choose 1-4 only!!!")
    else:
        print("choose setai or herodes only!!!")




















