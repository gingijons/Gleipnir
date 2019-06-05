import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from UI import uiLayer_admin, uiLayer_user




class User:
    def __init__(self, login):
        self.login = login
    
    def ui(self, login):
        if login == "u":
            uiLayer_user.main()

        elif login == "a":
            print("ssd")
            uiLayer_admin.main()
            

class Login:
    def run(self):
        selection = 0
        while selection != "Q" or selection != "q":
            print("(U) User access (A) Admin access")
            print("input: ", end="")
            selection = input()
            while selection != "Q" or selection != "q":
                if selection == "U" or selection == "u":
                    U = User("u")
                    U.ui("u")
                elif selection == "A" or selection == "a":
                    print("Password: ", end="")
                    selection = input()
                    if selection == "no":
                        A = User("a")
                        A.ui("a")
                    else:
                        print("please try again")
                else:
                    if selection == "Q" or selection == "q":
                        break
                    print("invalid")
                    break
            if selection == "Q" or selection == "q":
                        break



#==================================================================================
#===================================FIREWALL=======================================
#==================================================================================

if __name__ == "__main__":
    L = Login()
    L.run()