import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from App import businessLayer

def main():

        
    B = businessLayer.Business()
    selection = ""
    while selection != "Q" or selection != "q":
        print("(you can press Q to go back and to quit)")
        print("what would you like to do?")
        print("(I) Get or manage info (Q) Quit")
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
                    print("(V) View member (E) Edit member")
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

                    else:
                        if selection == "Q" or selection == "q":
                            break
                        print("invalid input")

                elif selection == "U" or selection == "u":
                    while selection != "Q" or selection != "q":
                        print("what would you like to do?", end="\n")
                        print("(V) View utility (E) Edit utility")
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

                        else:
                            if selection == "Q" or selection == "q":
                                break
                            print("invalid input")
                
                elif selection == "P" or selection == "p":
                    while selection != "Q" or selection != "q":
                        print("what would you like to do?", end="\n")
                        print("(V) View parties")
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
                        print("Active events: ", B.number_active_events())
                        print("what would you like to do?", end="\n")
                        print("(A) View active events (P) View past events")
                        selection = input()
                        if selection == "A" or selection == "a":
                            print(B.get_list_overview("eActive"))
                        
                        elif selection == "P" or selection == "p":
                            print(B.get_list_overview("ePast"))

                        else:
                            if selection == "Q" or selection == "q":
                                break
                            print("invalid input")
                else:
                    if selection == "Q" or selection == "q":
                        break
                    print("invalid input")
        elif selection == "Q" or selection == "q":
            break
        else:
            print("as")
            if selection == "Q" or selection == "q":
                break
            print("invalid input")

if __name__ == "__main__":
    pass