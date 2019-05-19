from businessLayer import Business

if __name__ == "__main__":
    B = Business()
    selection = ""
    while selection != "Q" or selection != "q":
        if selection == "Q" or selection == "q":
            break
        print("what would you like to do?", end="\n")
        print("(I) Get or manage info (E) Begin Event")
        print("input: ")
        selection = input()
        if selection == "I" or selection == "i":
            while selection != "Q" or selection != "q":
                print("What information would you like to access?", end="\n")
                print("(M) Members (U) Utilities (P) Search parties (E) Events", end="\n")
                print("input: ")
                selection = input()
                if selection == "M" or selection == "m":
                    print("what would you like to do?", end="\n")
                    print("(V) View member (E) Edit member (A) Add member (R) Remove member")
                    selection = input()
                    if selection == "V" or selection == "v":
                        print(B.get_list_overview("m"))
                        print("input ID to see details")
                        print("input: ")
                        while B.valid_member(selection) == False:
                            selection = input()
                            if B.valid_member(selection):
                                print(B.get_details("m", selection))
                            elif selection == "Q" or selection == "q":
                                break
                            else:
                                print("Invalid. try again")

                    elif selection == "E" or selection == "e":
                        print(B.get_list_overview("m"))
                        print("input ID to see details")
                        print("input: ")
                        while B.valid_member(selection) == False:
                            selection = input()
                            if B.valid_member(selection):
                                print(B.get_details("m", selection))
                                print("What would you like to change?")
                                print("(N) Name (A) Age (P) Phone (J) Job")
                                print("input: ")
                                id_num = selection
                                while selection != "Q" or selection != "q":
                                    selection = input()
                                    if selection == "N" or selection == "n":
                                        print("New name: ")
                                        selection = input()
                                        B.update_member_details("name", id_num, selection)
                                        break
                                    elif selection == "A" or selection == "a":
                                        print("New age (birthyear): ")
                                        selection = input()
                                        B.update_member_details("age", id_num, selection)
                                        break
                                    elif selection == "P" or selection == "p":
                                        print("New phone: ")
                                        selection = input()
                                        B.update_member_details("phone", id_num, selection)
                                        break
                                    elif selection == "J" or selection == "j":
                                        print("New job (1 = Fjallgönguliði 2 = Vélsleðaliði 3 = Jeppaliði): ")
                                        selection = input()
                                        B.update_member_details("job", id_num, selection)
                                        break
                                    elif selection == "Q" or selection == "q":
                                        break
                                    else:
                                        print("Invalid. try again")
                                    print("Member updated")
                            elif selection == "Q" or selection == "q":
                                break
                            else:
                                print("Invalid. try again")
                            break

                    elif selection == "A" or selection == "a":
                        print("Name: ")
                        name = input()
                        print("Birthyear: ")
                        age = input()
                        print("Phone: ")
                        phone = input()
                        print("Job (1 = Fjallgönguliði 2 = Vélsleðaliði 3 = Jeppaliði): ")
                        job = input()
                        print(B.add_member_to_file(str(name), str(age), str(phone), str(job)))
                    
                    elif selection == "R" or selection == "r":
                        print(B.get_list_overview("m"))
                        print("ID to remove")
                        print("input: ")
                        while B.valid_member(selection) == False:
                            selection = input()
                            if B.valid_member(selection):
                                print(B.delete_line("m", selection))
                                break
                            elif selection == "Q" or selection == "q":
                                break
                            else:
                                print("Invalid. try again")


                    else:
                        if selection == "Q" or selection == "q":
                            break
                        print("invalid input")

                elif selection == "U" or selection == "u":
                    while selection != "Q" or selection != "q":
                        print("what would you like to do?", end="\n")
                        print("(V) View utility (E) Edit utility (A) Add utility (R) Remove utility")
                        selection = input()
                        if selection == "V" or selection == "v":
                            print(B.get_list_overview("u"))
                            print("input ID to see details")
                            print("input: ")
                            while B.valid_utility(selection) == False:
                                selection = input()
                                if B.valid_utility(selection):
                                    print(B.get_details("u", selection))
                                    break
                                elif selection == "Q" or selection == "q":
                                    break
                                else:
                                    print("Invalid. try again")

                        elif selection == "E" or selection == "e":
                            print(B.get_list_overview("u"))
                            print("input ID to see details")
                            print("input: ")
                            while B.valid_utility(selection) == False:
                                selection = input()
                                if B.valid_utility(selection):
                                    print(B.get_details("u", selection))
                                    print("What would you like to change?")
                                    print("(N) Name (Y) Year (M) Manufacturer (I) IsModified")
                                    print("input: ")
                                    id_num = selection
                                    while selection != "Q" or selection != "q":
                                        selection = input()
                                        if selection == "N" or selection == "n":
                                            print("New name: ")
                                            selection = input()
                                            B.update_utility_details("name", id_num, selection)
                                            break
                                        elif selection == "Y" or selection == "y":
                                            print("New year: ")
                                            selection = input()
                                            B.update_utility_details("year", id_num, selection)
                                            break
                                        elif selection == "M" or selection == "m":
                                            print("New manufacturer: ")
                                            selection = input()
                                            B.update_utility_details("manufacturer", id_num, selection)
                                            break
                                        elif selection == "I" or selection == "i":
                                            print("Is modified (0 = No 1 = Yes): ")
                                            selection = input()
                                            B.update_utility_details("modified", id_num, selection)
                                            break
                                        elif selection == "Q" or selection == "q":
                                            break
                                        else:
                                            print("Invalid. try again")
                                        print("Unit updated")
                                elif selection == "Q" or selection == "q":
                                    break
                                else:
                                    print("Invalid. try again")
                                break

                        elif selection == "A" or selection == "a":
                            print("Name: ")
                            name = input()
                            print("Modelyear: ")
                            year = input()
                            print("Manufacturer: ")
                            manufacturer = input()
                            print("Is modified (0 = No 1 = Yes): ")
                            modified = input()
                            print(B.add_utility_to_file(str(name), str(year), str(manufacturer), str(modified)))
                        
                        elif selection == "R" or selection == "r":
                            print(B.get_list_overview("u"))
                            print("ID to remove")
                            print("input: ")
                            while B.valid_utility(selection) == False:
                                selection = input()
                                if B.valid_utility(selection):
                                    print(B.delete_line("u", selection))
                                    break
                                elif selection == "Q" or selection == "q":
                                    break
                                else:
                                    print("Invalid. try again")
                                

                        else:
                            if selection == "Q" or selection == "q":
                                break
                            print("invalid input")
                
                elif selection == "P" or selection == "p":
                    while selection != "Q" or selection != "q":
                        print("what would you like to do?", end="\n")
                        print("(V) View parties (A) Add to party (R) Remove from parties")
                        selection = input()
                        if selection == "V" or selection == "v":
                            print(B.get_list_overview("p"))
                            print("input ID to see details")
                            print("input: ")
                            while B.valid_party(selection) == False:
                                selection = input()
                                if B.valid_party(selection):
                                    print(B.get_details("p", selection))
                                    break
                                elif selection == "Q" or selection == "q":
                                    break
                                else:
                                    print("Invalid. try again")

                        elif selection == "E" or selection == "e":
                            pass

                        elif selection == "A" or selection == "a":
                            pass
                        
                        elif selection == "R" or selection == "r":
                            print(B.get_list_overview("p"))
                            print("ID to remove")
                            print("input: ")
                            while B.valid_party(selection) == False:
                                selection = input()
                                if B.valid_party(selection):
                                    party = selection
                                    print(B.get_list_overview("pDetails", party))
                                    print("ID to remove")
                                    print("input: ")
                                    while B.valid_party(selection, party) == False:
                                        selection = input()
                                        if B.valid_party(selection, party):
                                            print(B.delete_specific_from_party(party, selection))
                                            break
                                        elif selection == "Q" or selection == "q":
                                            break
                                        else:
                                            print("Invalid. try again")
                                elif selection == "Q" or selection == "q":
                                    break
                                else:
                                    print("Invalid. try again")

                        else:
                            if selection == "Q" or selection == "q":
                                break
                            print("invalid input")

                elif selection == "E" or selection == "e":
                    while selection != "Q" or selection != "q":
                        print("Active events: ", B.number_active_events())
                        print("what would you like to do?", end="\n")
                        print("(A) View active events (P) View past events (E) End active events")
                        selection = input()
                        if selection == "A" or selection == "a":
                            print(B.get_list_overview("eActive"))
                        
                        elif selection == "P" or selection == "p":
                            print(B.get_list_overview("ePast"))
                        
                        elif selection == "E" or selection == "e":
                            print(B.get_list_overview("eActive"))
                            while B.valid_active_event(selection) == False:
                                selection = input()
                                if B.valid_active_event(selection):
                                    B.update_event_status(selection)
                                    break
                                else:
                                    if selection == "Q" or selection == "q":
                                        break
                                    print("invalid input")


                        else:
                            if selection == "Q" or selection == "q":
                                break
                            print("invalid input")
                else:
                    if selection == "Q" or selection == "q":
                        break
                    print("invalid input")
        elif selection == "E" or selection == "e":
            print("Enter information")
            print("Name: ")
            name = input()
            print("Location: ")
            location = input()
            print(B.get_list_overview("p"))
            print("Select party")
            party = 0
            while B.valid_party(party) == False:
                party = input()
                if B.valid_party(party):
                    print(B.add_event_to_file(str(name), str(location), str(party)))
                    break
                elif selection == "Q" or selection == "q":
                    break
                else:
                    print("Invalid. try again")

        else:
            if selection == "Q" or selection == "q":
                break
            print("invalid input")