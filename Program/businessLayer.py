from dataLayer import *
import datetime
now = datetime.datetime.now()

class Business:
    D = GetData


if __name__ == "__main__":
    D = GetData()
    B = Business()
    D.get_members()
    D.get_utilities()
    
    member_list = D.get_member_list()
   
    for member in member_list:
        print(member._member_id, " | ", member._name, " | ", member._phone, " | ", member._job, " | ", (now.year - int(member._age)))

    utilities_list = D.get_utilities_list()

    for utility in utilities_list:
        print(utility._utility_id, " | ", utility._name, " | ", utility._year, " | ", utility._manufacturer, " | ", utility._modified )