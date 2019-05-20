import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from Resource import dataLayer
import datetime
now = datetime.datetime.now()

class Business:
    
    def __init__(self):
        self.D = dataLayer.GetData()
        self.D.get_members()
        self.D.get_utilities()
        self.D.get_events()
        self.D.get_parties()
        self.member_list = self.D.get_member_list()
        self.utilities_list = self.D.get_utilities_list()
        self.events_list = self.D.get_events_list()
        self.parties_list = self.D.get_parties_list()

    def number_active_events(self):
        num = 0
        for event in self.events_list:
            if event._status == "active":
                num += 1
        return num

    def get_list_overview(self, input, partynum = None):  
        lis = ""
        if input == "m":
            for member in self.member_list:
                lis += (member._member_id + " | " + member._name + "\n")
        elif input == "mAndJobs":
            for member in self.member_list:
                lis += (member._member_id + " | " + member._name + " | ")
                if member._job == "1":
                    lis += "Fjallgönguliði"
                elif member._job == "2":
                    lis += "Vélsleðaliði"
                elif member._job == "3":
                    lis += "Jeppaliði" 
                lis += "\n"
        elif input == "uAndMod":
            for utility in self.utilities_list:
                lis += (utility._utility_id + " | " + utility._name)
                if utility._modified == "1":
                    lis += (" (Modified)")
                lis += "\n"
        elif input == "u":
            for utility in self.utilities_list:
                lis += (utility._utility_id + " | " + utility._name + "\n")
        elif input == "ePast":
            for event in self.events_list:
                if event._status == "inactive":
                    lis += (event._event_id + " | " +  event._name + "\n")
        elif input == "eActive":
            for event in self.events_list:
                if event._status == "active":
                    lis += (event._event_id + " | " +  event._name + "\n")
        elif input == "p":
            for party in self.parties_list:
                if party._party_id not in lis:
                    lis += (party._party_id + "\n")
        elif input == "pDetails":
            for party in self.parties_list:
                if party._party_id == str(partynum):
                    if int(str(party._unit_id)) < 10000:
                        for member in self.member_list:
                            if str(member._member_id) == str(party._unit_id):
                                lis += (member._member_id + " | " + member._name + "\n")
                    else:
                        for utility in self.utilities_list:
                            if utility._utility_id == party._unit_id:
                                lis += (utility._utility_id + " | " + utility._name + "\n")
        return lis

    def get_details(self, from_list, with_id):
        string = ""
        with_id = str(with_id)
        if from_list == "m":
            for member in self.member_list:
                if member._member_id == with_id:
                    string = ("Name: " + member._name  + " | Phone: " + member._phone + " | Job: ")
                    if member._job == "1":
                        string += "Fjallgönguliði"
                    elif member._job == "2":
                        string += "Vélsleðaliði"
                    elif member._job == "3":
                        string += "Jeppaliði"
                    string += (" | Age: " + str(now.year - int(member._age)) + "\n")
        elif from_list == "u":
            for utility in self.utilities_list:
                if utility._utility_id == with_id:
                    string = ("Name: " + utility._name +  " | Modelyear: " + utility._year + " | Manufacturer: " + utility._manufacturer + " | Modified: ")
                    if utility._modified == "1":
                        string += "Yes" 
                    else:
                        string += "No"
                    string += "\n"
        elif from_list == "e":
            for event in self.events_list:
                if event._event_id == with_id:
                    string = (event._name + " | " + event._time + " | " + event._location + " | " + event._status, " | " + event._party + "\n")
        elif from_list == "p":
            for party in self.parties_list:
                if party._party_id == with_id:
                    string += self.get_unit_details(party._unit_id)

        return string

    def get_unit_details(self, unit_id):
        string = ""
        if int(unit_id) >= 10000:
            for utility in self.utilities_list:
                if utility._utility_id == unit_id:
                    string = ("Name: " + utility._name +  " | Modelyear: " + utility._year + " | Manufacturer: " + utility._manufacturer + " | Modified: ")
                    if utility._modified == "1":
                        string += "Yes" 
                    else:
                        string += "No"
                    string += "\n"
        elif int(unit_id) < 10000:
            for member in self.member_list:
                if member._member_id == unit_id:
                    string = ("Name: " + member._name  + " | Phone: " + member._phone + " | Job: ")
                    if member._job == "1":
                        string += "Fjallgönguliði"
                    elif member._job == "2":
                        string += "Vélsleðaliði"
                    elif member._job == "3":
                        string += "Jeppaliði"
                    string += (" | Age: " + str(now.year - int(member._age)) + "\n")
        else:
            string += "no info"
        return string

#=============================================================================
#If changed, update file and data within program
#
#=============================================================================


    def add_member_to_file(self, name, age, phone, job):
        self.D.add_member(name, age, phone, job, None, True)
        self.member_list = self.D.get_member_list()
        return "member added"
    
    def add_utility_to_file(self, name, year, manufacturer, modified):
        
        self.D.add_utility(name, year, manufacturer, modified, None, True)
        self.utilities_list = self.D.get_utilities_list()
        return "utility added"
    
    def add_event_to_file(self, name, location, party):
        time = (str(now.year) + " " + str(now.month) + " " + str(now.day))
        self.D.add_events(name, time, location, "active", party, None, True)
        self.events_list = self.D.get_events_list()
        return "event active"
    
    def add_party_to_file(self, members_list, utilities_list):
        pid = self.D.get_party_id()
        for i in range(len(members_list)):
            self.D.add_party(str(members_list[i]), pid, None, True)
        for i in range(len(utilities_list)):
            self.D.add_party(str(utilities_list[i]), pid, None, True)
        self.parties_list = self.D.get_parties_list()
        return "party added with ID: ", pid


    def update_member_details(self, what_to_change, id_num, value):
        
        self.D.update_member_file(what_to_change, id_num, value)
        if what_to_change == "name":
            for member in self.member_list:
                if member._member_id == id_num:
                    member._name = str(value)
        elif what_to_change == "age":
            for member in self.member_list:
                if member._member_id == id_num:
                    member._age = str(value)
        elif what_to_change == "phone":
            for member in self.member_list:
                if member._member_id == id_num:
                    member._phone = str(value)
        elif what_to_change == "job":
            for member in self.member_list:
                if member._member_id == id_num:
                    member._job = str(value)

    
    def update_utility_details(self, what_to_change, id_num, value):
        
        self.D.update_utility_file(what_to_change, id_num, value)
        if what_to_change == "name":
            for utility in self.utilities_list:
                if utility._utility_id == id_num:
                    utility._name = str(value)
        elif what_to_change == "year":
            for utility in self.utilities_list:
                if utility._utility_id == id_num:
                    utility._year = str(value)
        elif what_to_change == "manufacturer":
            for utility in self.utilities_list:
                if utility._utility_id == id_num:
                    utility._manufacturer = str(value)
        elif what_to_change == "modified":
            for utility in self.utilities_list:
                if utility._utility_id == id_num:
                    utility._modified = str(value)

    def update_event_status(self, id_num):
        self.D.update_event_status(id_num)
        for event in self.events_list:
            if event._event_id == id_num:
                event._status = "inactive"


#=============================================================================
# if deleted, update file and data within program
#=============================================================================

    def delete_line(self, delete_from, id_num):
        self.D.delete_from_party(id_num)
        if delete_from == "m":
            self.D.delete_member(id_num)
            i = 0
            for member in self.member_list:
                if member._member_id == id_num:
                    self.member_list.pop(i)
                i+=1
            return "Member removed"
        elif delete_from == "u":
            self.D.delete_utility(id_num)
            i = 0
            for utility in self.utilities_list:
                if utility._utility_id == id_num:
                    self.utilities_list.pop(i)
                i+=1
            return "utility removed"
        
    
    def delete_specific_from_party(self, party_num, unit_num):
        self.D.delete_specific_from_party(party_num, unit_num)
        i = 0
        for party in self.parties_list:
            if party._party_id == str(party_num) and party._unit_id == str(unit_num):
                self.parties_list.pop(i)
            i+=1
        return "Unit removed"

    def delete_entire_party(self, party_num):
        self.D.delete_entire_party(party_num)
        self.parties_list = self.D.get_parties_list()
        return "party removed"
        
    def valid_member(self, id_num):
        for member in self.member_list:
                if member._member_id == id_num:
                    return True
        return False

    def valid_utility(self, id_num):
        for utility in self.utilities_list:
                if utility._utility_id == id_num:
                    return True
        return False
    
    def valid_party(self, id_num, is_unit_list = 0):
        if is_unit_list == 0:
            for party in self.parties_list:
                    if party._party_id == id_num:
                        return True
        elif is_unit_list != 0:
            for party in self.parties_list:
                if party._party_id == is_unit_list:
                    if party._unit_id == id_num:
                        return True
        return False

    def valid_active_event(self, id_num):
        for event in self.events_list:
                if event._event_id == id_num and event._status == "active":
                    return True
        return False

    def valid_pick(self, lis, pick):
        for i in range(len(lis)):
            print(lis[i])
            if lis[i] == pick:
                return False 
        return True

    def valid_inactive_member(self, pick):
        for event in self.events_list:   
            if event._status == "active":       
                for party in self.parties_list:
                    if int(party._party_id) == int(event._party):
                        if party._unit_id == str(pick):
                            return False
        return True



if __name__ == "__main__":
    pass
"""

    D = dataLayer.GetData()
    B = Business()
    D.get_members()
    D.get_utilities()
    D.get_events()
    D.get_parties()

    lis = [1, 2, 3, 6, 9, 10]
    lis.append(11)


    if B.valid_inactive_member(15):
        print("yes")


    for utility in B.utilities_list:
        print(utility._utility_id, " | ", utility._name, " | ", utility._year, " | ", utility._manufacturer, " | ", utility._modified )
    B.add_utility_to_file("Sleði 14", "2017", "Kawaiisakii", "0")
    for utility in B.utilities_list:
        print(utility._utility_id, " | ", utility._name, " | ", utility._year, " | ", utility._manufacturer, " | ", utility._modified )
    
    for member in B.member_list:
        print(member._member_id, " | ", member._name, " | ", member._phone, " | ", member._job, " | ", (now.year - int(member._age)))

    
    print(now.year, now.month, now.day)

    for utility in B.utilities_list:
        print(utility._utility_id, " | ", utility._name, " | ", utility._year, " | ", utility._manufacturer, " | ", utility._modified )

    

    for event in B.events_list:
        print(event._event_id, " | ", event._name, " | ", event._time, " | ", event._location, " | ", event._status, " | ", event._party )

    for party in B.parties_list:
        if party._party_id == "200001":
            print(party._unit_id)
    """
    #print(B.delete_line("m", "0"))