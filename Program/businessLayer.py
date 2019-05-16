from dataLayer import *
import datetime
now = datetime.datetime.now()

class Business:
    D = GetData


if __name__ == "__main__":
    D = GetData()
    B = Business()
    D.get_members()
    member_list = D.get_contacts_ordered()
   
    for memb in member_list:
        print(memb._member_id, " | ", memb._name, " | ", memb._phone, " | ", memb._job, " | ", (now.year - int(memb._age)))