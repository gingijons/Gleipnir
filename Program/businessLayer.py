from dataLayer import *
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

    def get_list_overview(self, input):  
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
        print(int(unit_id))
        if int(unit_id) >= 10000:
            print(True)
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
    print(B.get_details("p", 200003))