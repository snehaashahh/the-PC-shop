#Developed by: Sneha Shah
#Date: March 8, 2023
#Desc: Assignment 2

def pickItems():
    # Define the available PC components and their prices
    SSD = [['1', '250 GB', 69.99], ['2', '500 GB', 93.99], ['3', '4 TB', 219.99]]
    HDD = [['1', '500 GB', 106.33], ['2', '1 TB', 134.33]]
    CPU = [['1', 'Intel Core i7-11700K', 499.99], ['2', 'AMD Ryzen 7 5800X', 312.99]]
    MOTHERBOARD = [['1', 'MSI B550-A PRO', 197.46], ['2', 'MSI Z490-A PRO', 262.30]]
    RAM = [['1', '16 GB', 82.99], ['2', '32 GB', 174.99]]
    GRAPHICS_CARD = [['1', 'MSI GeForce RTX 3060 12GB', 539.99]]
    PSU = [['1', 'Corsair RM750', 164.99]]
    CASE = [['1', 'Full Tower (black)', 149.99], ['2', 'Full Tower (red)', 149.99]]
    PREBUILTS = [['1', 'Legion Tower Gen 7 with RTX 3080 Ti', 3699.99], ['2', 'SkyTech Prism II Gaming PC', 2839.99], ['3', 'ASUS ROG Strix G10CE Gaming PC', 1099.99]]
    prebuilts_price = 0
    total_price = 0
    
    #Introduction
    print("Welcome to my PC shop!")
    options = ["1", "2", "3"]
    checkout_complete = False
    
    choice = input("Would you like to build a custom PC (1), purchase a pre-built PC (2), or checkout (3)? ")
    
    while choice not in options:
        print("Invalid option. Please select one of the available options.")
        choice = input("Would you like to build a custom PC (1), purchase a pre-built PC (2), or checkout (3)? ")
    
    while not checkout_complete:
        
            
    # Selecting choice
        if choice == "1":
            print("Great! Let's start building your PC!")
            
            # Prompt user to select a CPU
            print("First, let's pick a CPU.")
            for cpu in CPU:
                print(f"{cpu[0]} : {cpu[1]}, ${cpu[2]}")
            cpu_price = 0
            valid_options = [cpu[0] for cpu in CPU]
            cpu_choice = input("Choose the number that corresponds with the part you want: ")
            while cpu_choice not in valid_options:
                print("Invalid option. Please choose a number from the list.")
                cpu_choice = input("Choose the number that corresponds with the part you want: ")
            if cpu_choice == "1":
                cpu_price += 499.99
            elif cpu_choice == "2":
                cpu_price += 312.99
            else:
                cpu_choice == None

            # Check if CPU is compatible with motherboard
            if cpu_choice == '1':  # Intel Core i7-11700K
                compatible_motherboard = '2'  # MSI Z490-A PRO
            elif cpu_choice == '2':  # AMD Ryzen 7 5800X
                compatible_motherboard = '1'  # MSI B550-A PRO
            else:
                print("Invalid choice.")
                return

            # Prompt user to select a compatible motherboard
            print("Next, let's pick a compatible motherboard.")
            compatible_motherboards = [mb[0] for mb in MOTHERBOARD if mb[0] == compatible_motherboard]
            

            while not compatible_motherboards:
                print("No compatible motherboard found.")
                return
            for motherboard in MOTHERBOARD:
                if motherboard[0] in compatible_motherboards:
                    print(f"{motherboard[0]} : {motherboard[1]}, ${motherboard[2]}")
                    motherboard_price = 0
            motherboard_choice = input("Choose the number that corresponds with the part you want: ")
            while motherboard_choice not in compatible_motherboards:
                print("Invalid choice. Please select a compatible motherboard.")
                motherboard_choice = input("Choose the number that corresponds with the part you want: ")
            if motherboard_choice == "1":
                motherboard_price += 197.46
            elif motherboard_choice == "2":
                motherboard_price += 262.30
            else:
                motherboard_choice == None

            # Prompt user to select a RAM
            print("Next, let's pick your RAM.")
            for ram in RAM:
                print(f"{ram[0]} : {ram[1]}, ${ram[2]}")
                ram_price = 0
            valid_options = [ram[0] for ram in RAM]
            ram_choice = input("Choose the number that corresponds with the part you want: ")
            while ram_choice not in valid_options:
                print("Invalid option. Please choose a number from the list.")
                ram_choice = input("Choose the number that corresponds with the part you want: ")
            if ram_choice == "1":
                    ram_price += 82.99
            elif ram_choice == "2":
                ram_price += 174.99
            else:
                ram_choice == None

            # Prompt user to select a PSU
            print("Next, let's pick your PSU.")
            for psu in PSU:
                print(f"{psu[0]} : {psu[1]}, ${psu[2]}")
                psu_price = 0
            valid_options = [psu[0] for psu in PSU]
            psu_choice = input("Choose the number that corresponds with the part you want: ")
            while psu_choice not in valid_options:
                print("Invalid option. Please choose a number from the list.")
                psu_choice = input("Choose the number that corresponds with the part you want: ")
            if psu_choice == "1":
                    psu_price += 164.99
            else:
                psu_choice == None

            # Prompt user to select a case
            print("Next, let's pick your case.")
            for case in CASE:
                print(f"{case[0]} : {case[1]}, ${case[2]}")
                case_price = 0
            valid_options = [case[0] for case in CASE]
            case_choice = input("Choose the number that corresponds with the part you want: ")
            while case_choice not in valid_options:
                print("Invalid option. Please choose a number from the list.")
                case_choice = input("Choose the number that corresponds with the part you want: ")
            if case_choice == "1":
                    case_price += 149.99
            elif case_choice == "2":
                case_price += 149.99
            else:
                case_choice == None

            ssd_choice = None
            hdd_choice = None

            # Prompt user to select an SSD 
            print("Next, let's pick an SSD (optional, but you must have at least one SSD or HDD).")
            for ssd in SSD:
                print(f"{ssd[0]} : {ssd[1]}, ${ssd[2]}")
            ssd_price = 0
            valid_options = [ssd[0] for ssd in SSD] + ['X', 'x']
            ssd_choice = input("Choose the number that corresponds with the part you want: ")
            while ssd_choice not in valid_options:
                print("Invalid option. Please choose a number from the list.")
                ssd_choice = input("Choose the number that corresponds with the part you want: ")
                if ssd_choice == "1":
                    ssd_price += 69.99
                elif ssd_choice == "2":
                    ssd_price += 93.99
                elif ssd_choice == "3" :
                    ssd_price += 219.99
                else:
                    ssd_choice == None
                    
            # Prompt user to select an HDD  
            print("Next, let's pick an HDD (optional, but you must have at least one SSD or HDD).")
            for hdd in HDD:
                print(f"{hdd[0]} : {hdd[1]}, ${hdd[2]}")
            hdd_price = 0
            valid_options = [hdd[0] for hdd in HDD] + ['x', 'X']
            hdd_choice = input("Choose the number that corresponds with the part you want: ")
            
            while hdd_choice not in valid_options or ssd_choice and hdd_choice == 'x' or ssd_choice.upper and hdd_choice.upper == "x":
                if hdd_choice != "x":
                    break
                if ssd_choice != 'x' and hdd_choice == 'x':
                    break
                if ssd_choice.upper and hdd_choice.upper == "x":
                    break
                print("Invalid option. Please choose a number from the list.")
                hdd_choice = input("Choose the number that corresponds with the part you want: ")
            if hdd_choice == "1":
                hdd_price += 106.33
            elif hdd_choice == "2":
                hdd_price += 134.33
            else:
                hdd_choice == None
                    
            # Prompt user to select a graphics card
            print("Finally, let's pick your graphics card (or X to not get a graphics card).")
            for graphics_card in GRAPHICS_CARD:
                print(f"{graphics_card[0]} : {graphics_card[1]}, ${graphics_card[2]}")
                graphics_card_price = 0
            valid_options = [graphics_card[0] for graphics_card in GRAPHICS_CARD]  + ["X" and "x"]
            graphics_card_choice = input("Choose the number that corresponds with the part you want: ")
            while graphics_card_choice not in valid_options:
                print("Invalid option. Please choose a number from the list.")
                graphics_card_choice = input("Choose the number that corresponds with the part you want: ")
            if graphics_card_choice == "1":
                    graphics_card_price += 539.99
            else:
                graphics_card_choice == None

            #Print total price
            total_price = ssd_price+hdd_price+cpu_price+motherboard_price+ram_price+graphics_card_price+psu_price+case_price
            print(f"You have selected all of the required parts! Your total price for this PC is ${total_price:.2f}")


        if choice == "2":
            print("Great! Let's pick a pre-built PC!")

            # Prompt user to select a prebuilt PC
            print("Which prebuilt would you like to order?")
            for prebuilts in PREBUILTS:
                print(f"{prebuilts[0]} : {prebuilts[1]}, ${prebuilts[2]}")
            valid_options = [prebuilts[0] for prebuilts in PREBUILTS]
            prebuilts_choice = input("Choose the number that corresponds with the part you want: ")
            while prebuilts_choice not in valid_options:
                print("Invalid option. Please choose a number from the list.")
                prebuilts_choice = input("Choose the number that corresponds with the part you want: ")
            if prebuilts_choice == "1":
                prebuilts_price += 3699.99
            elif prebuilts_choice == "2":
                prebuilts_price += 2839.99
            elif prebuilts_choice == "3":
                prebuilts_price += 1099.99
            else:
                prebuilts_choice == None
            print(f"Your total price for this prebuilt is ${prebuilts_price:.2f}")    

        if choice == "3":
            if total_price != 0:
                print (f"[{total_price:.2f}, {prebuilts_price:.2f}]")
            else:
                print(f"[, {prebuilts_price:.2f}]")
            # print(f"[{total_price:.2f}, {prebuilts_price:.2f}]")
            checkout_complete = True
            break    
    
        choice = input("Would you like to build a custom PC (1), purchase a pre-built PC (2), or checkout (3)? ")
        
pickItems()