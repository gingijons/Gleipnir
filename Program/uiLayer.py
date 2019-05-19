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
                        pass

                    elif selection == "A" or selection == "a":
                        pass
                    
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
                            pass

                        elif selection == "A" or selection == "a":
                            pass
                        
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
                        print("(V) View parties (A) Add to party (R) Remove from party")
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
                        print("(A) View active events (P) View past events")
                        selection = input()
                        if selection == "A" or selection == "a":
                            pass
                        
                        elif selection == "R" or selection == "r":
                            pass
                        else:
                            if selection == "Q" or selection == "q":
                                break
                            print("invalid input")
                else:
                    if selection == "Q" or selection == "q":
                        break
                    print("invalid input")
        elif selection == "E" or selection == "e":
            while selection != "Q" or selection != "q":
                if selection == "w":
                    pass
                else:
                    if selection == "Q" or selection == "q":
                        break
                    print("invalid input")

        else:
            if selection == "Q" or selection == "q":
                break
            print("invalid input")