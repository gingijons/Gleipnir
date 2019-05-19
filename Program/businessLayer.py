from dataLayer import GetData
import datetime
now = datetime.datetime.now()

class Business:
    D = GetData()
    def __init__(self):
        D = GetData()
        D.get_members()
        D.get_utilities()
        D.get_events()
        D.get_parties()
        self.member_list = D.get_member_list()
        self.utilities_list = D.get_utilities_list()
        self.events_list = D.get_events_list()
        self.parties_list = D.get_parties_list()

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
        elif input == "u":
            for utility in self.utilities_list:
                lis += (utility._utility_id + " | " + utility._name + "\n")
        elif input == "e":
            for event in B.events_list:
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
                    if utility._modified == "0":
                        string += "Yes" 
                    else:
                        string += "No"
                    string += "\n"
        elif from_list == "e":
            for event in B.events_list:
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
                    if utility._modified == "0":
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

    #If changed make variable update file and data within program

    def add_member_to_file(self, name, age, phone, job):
        D.add_member(name, age, phone, job, None, True)
        return "member added"
    
    def add_utility_to_file(self, name, year, manufacturer, modified):
        D.add_utility(name, year, manufacturer, modified, None, True)
        return "utility added"


    def update_member_details(self, what_to_change, value):
        if what_to_change == "name":
            pass
        elif what_to_change == "age":
            pass
        elif what_to_change == "phone":
            pass
        elif what_to_change == "job":
            pass
    
    def update_utility_details(self, what_to_change, value):
        if what_to_change == "name":
            pass
        elif what_to_change == "year":
            pass
        elif what_to_change == "manufacturer":
            pass
        elif what_to_change == "modified":
            pass
    
    # if deleted, update file and data within program

    def delete_line(self, delete_from, id_num):
        D = GetData()
        if delete_from == "m":
            D.delete_member(id_num)
            i = 0
            for member in self.member_list:
                if member._member_id == id_num:
                    self.member_list.pop(i)
                i+=1
            return "Member removed"

        elif delete_from == "u":
            D.delete_utility(id_num)
            self.utilities_list = D.get_utilities_list()
            i = 0
            for utility in self.utilities_list:
                if utility._utility_id == id_num:
                    self.utilities_list.pop(i)
                i+=1
        D.delete_from_party(id_num)
    
    def delete_specific_from_party(self, party_num, unit_num):
        D = GetData()
        print(str(party_num), str(unit_num))
        D.delete_specific_from_party(party_num, unit_num)
        i = 0
        for party in self.parties_list:
            if party._party_id == str(party_num) and party._unit_id == str(unit_num):
                self.parties_list.pop(i)
            i+=1
        return "Unit removed"
        
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



if __name__ == "__main__":
    D = GetData()
    B = Business()
    D.get_members()
    D.get_utilities()
    D.get_events()
    D.get_parties()
    
    """
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
    print(B.delete_line("m", "0"))