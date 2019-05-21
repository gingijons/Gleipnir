from sortedcontainers import SortedDict
import csv

class Member:
    def __init__(self, memberid, name, age, phone, job):
        self._name = name
        self._age = age
        self._phone = phone
        self._job = job
        self._member_id = memberid

class Utilities:
    def __init__(self, utilityid, name, year, manufacturer, modified):
        self._name = name
        self._year = year
        self._manufacturer = manufacturer
        self._modified = modified
        self._utility_id = utilityid

class Event:
    def __init__(self, eventid, name, time, location, status, party):
        self._name = name
        self._time = time
        self._location = location
        self._status = status
        self._party = party
        self._event_id = eventid

class Party:
    def __init__(self, connectionid, unitid, partyid):
        self._connection_id = connectionid
        self._unit_id = unitid
        self._party_id = partyid

class GetData:
    def __init__(self):
        self._members_map = SortedDict({})
        self._utilities_map = SortedDict({})
        self._event_map = SortedDict({})
        self._party_map = SortedDict({})
        self._mid = 0
        self._uid = 10000
        self._eid = 100000
        self._pid = 200000
        self._cid = 500000
        self._member_size = 0
        self._utility_size = 0
        self._event_size = 0
        self._party_size = 0

    def get_member_id(self):
        return str(self._mid)
    
    def get_unit_id(self):
        return str(self._uid)
    
    def get_party_id(self):
        pid = int(self._pid)
        pid +=1
        return str(pid)

    def get_members(self):
        member_list=open("./Data/members.csv", "r", encoding="utf-8-sig").read().split('\n')
        for line in member_list[:-1]:
            fields = line.split(";")
            memberid = fields[0]
            name = fields[1]
            age = fields[2]
            phone = fields[3]
            job = fields[4]
            self.add_member(name, age, phone, job, memberid)

    def add_member(self, name, age, phone, job, memberid = None, is_new = False):
        if memberid == None:
            self._mid +=1
            memberid = str(self._mid)
        self._members_map[self._mid] = Member(memberid, name, age, phone, job)
        self._member_size += 1 
        self._mid = int(memberid)
        if is_new:
            self.save_member(name, age, phone, job, memberid)

    def get_member_list(self):
        members_list = []
        for id in self._members_map:
            members_list.append(self._members_map[id])    
        return members_list

    def get_utilities(self):
        utilities_list=open("./Data/utilities.csv", "r", encoding="utf-8-sig").read().split('\n')
        for line in utilities_list[:-1]:
            fields = line.split(";")
            utilityid = fields[0]
            name = fields[1]
            year = fields[2]
            manufacturer = fields[3]
            modified = fields[4]
            self.add_utility(name, year, manufacturer, modified, utilityid)
    
    def add_utility(self, name, year, manufacturer, modified, uid = None, is_new = False):
        if uid == None:
            self._uid +=1
            uid = str(self._uid)
        self._utilities_map[self._uid] = Utilities(uid, name, year, manufacturer, modified)
        self._utility_size += 1 
        self._uid = int(uid)
        if is_new:
            self.save_utility(name, year, manufacturer, modified, uid)

    def get_utilities_list(self):
        utility_list = []
        for id in self._utilities_map:
            utility_list.append(self._utilities_map[id])    
        return utility_list

    def get_events(self):
        events_list=open("./Data/events.csv", "r", encoding="utf-8-sig").read().split('\n')
        for line in events_list[:-1]:
            fields = line.split(";")
            eid = fields[0]
            name = fields[1]
            time = fields[2]
            location = fields[3]
            status = fields[4]
            party = fields[5]
            self.add_events(name, time, location, status, party, eid)
    
    def add_events(self, name, time, location, status, party, eid = None, is_new = False):
        if eid == None:
            self._eid +=1
            eid = str(self._eid)
        self._event_map[self._eid] = Event(eid, name, time, location, status, party)
        self._event_size += 1 
        self._eid = int(eid)
        if is_new:
            self.save_event(eid, name, time, location, status, party)
    
    def get_events_list(self):
        events_list = []
        for id in self._event_map:
            events_list.append(self._event_map[id])    
        return events_list

    def get_parties(self):
        parties_list=open("./Data/parties.csv", "r", encoding="utf-8-sig").read().split('\n')
        for line in parties_list[:-1]:
            fields = line.split(";")
            cid = fields[0]
            uid = fields[1]
            pid = fields[2]
            self.add_party(uid, pid, cid)
    
    def add_party(self, uid, pid, cid = None, is_new = False):
        if cid == None:
            self._cid += 1
            cid = str(self._cid)
        self._party_map[self._cid] = Party(cid, uid, pid)
        self._party_size += 1
        self._cid = int(cid)
        if int(self._pid) < int(pid):
            self._pid = int(pid)
        if is_new:
            self.save_party(cid, uid, pid)
    
    def get_parties_list(self):
        parties_list = []
        for id in self._party_map:
            parties_list.append(self._party_map[id])  
        return parties_list

    def save_member(self, name, age, phone, job, memberid):
        f = open("./Data/members.csv", "a", encoding="utf-8-sig")
        f.write(memberid + ";" + name + ";" + age + ";" + phone + ";" + job + "\n")
        f.close

    def save_utility(self, name, year, manufacturer, modified, uid):
        f = open("./Data/utilities.csv", "a", encoding="utf-8-sig")
        f.write(uid + ";" + name + ";" + year + ";" + manufacturer + ";" + modified + "\n")
        f.close
    
    def save_event(self, eid, name, time, location, status, party):
        f = open("./Data/events.csv", "a", encoding="utf-8-sig")
        f.write(eid + ";" + name + ";" + time + ";" + location + ";" + status + ";" + party + "\n")
        f.close
    
    def save_party(self, cid, uid, pid):
        f = open("./Data/parties.csv", "a", encoding="utf-8-sig")
        f.write(cid + ";" + uid + ";" + pid + "\n")
        f.close
    
#============================================================
# delete_member og delete_utility eyða líka úr leitarhópum
#============================================================

    def delete_member(self, member_id):
        i = 0
        member_id = int(member_id)
        b = open("./Data/members.csv", "r", encoding="utf-8-sig")
        lines = b.readlines()
        b.close()
        for line in lines:
            fields = line.split(";")
            memberid = fields[0]
            name = fields[1]
            age = fields[2]
            phone = fields[3]
            job = fields[4]
            if int(memberid) != member_id:
                if i == 0:
                    f = open("./Data/members.csv", "w", encoding="utf-8")
                    f.write(str(memberid) + ";" + str(name) + ";" + str(age) + ";" + str(phone) + ";" + str(job))
                    f.close
                else:
                    f = open("./Data/members.csv", "a", encoding="utf-8")
                    f.write(str(memberid) + ";" + str(name) + ";" + str(age) + ";" + str(phone) + ";" + str(job))
                    f.close
                i +=1
        
        
    def delete_utility(self, utility_id):
        i = 0
        b = open("./Data/utilities.csv", "r", encoding="utf-8-sig")
        lines = b.readlines()
        b.close()
        for line in lines:
            fields = line.split(";")
            utilityid = fields[0]
            name = fields[1]
            year = fields[2]
            manufacturer = fields[3]
            modified = fields[4]
            if utilityid != utility_id:
                if i == 0:
                    f = open("./Data/utilities.csv", "w", encoding="utf-8")
                    f.write(str(utilityid) + ";" + str(name) + ";" + str(year) + ";" + str(manufacturer) + ";" + str(modified))
                    f.close
                else:
                    f = open("./Data/utilities.csv", "a", encoding="utf-8")
                    f.write(str(utilityid) + ";" + str(name) + ";" + str(year) + ";" + str(manufacturer) + ";" + str(modified))
                    f.close
                i +=1
        

    def delete_from_party(self, id_num):
        i = 0
        b = open("./Data/parties.csv", "r", encoding="utf-8-sig")
        lines = b.readlines()
        b.close()
        for line in lines:
            fields = line.split(";")
            cid = fields[0]
            uid = fields[1]
            pid = fields[2]
            if uid != id_num:
                if i == 0:
                    f = open("./Data/parties.csv", "w", encoding="utf-8")
                    f.write(str(cid) + ";" + str(uid) + ";" + str(pid))
                    f.close
                else:
                    f = open("./Data/parties.csv", "a", encoding="utf-8")
                    f.write(str(cid) + ";" + str(uid) + ";" + str(pid))
                    f.close
                i +=1



    def delete_specific_from_party(self, party_num, unit_num):
        i = 0
        b = open("./Data/parties.csv", "r", encoding="utf-8-sig")
        lines = b.readlines()
        b.close()
        for line in lines:
            fields = line.split(";")
            cid = fields[0]
            uid = fields[1]
            pid = fields[2]
            if pid != party_num and uid != unit_num:
                if i == 0:
                    f = open("./Data/parties.csv", "w", encoding="utf-8")
                    f.write(str(cid) + ";" + str(uid) + ";" + str(pid))
                    f.close
                else:
                    f = open("./Data/parties.csv", "a", encoding="utf-8")
                    f.write(str(cid) + ";" + str(uid) + ";" + str(pid))
                    f.close
                i +=1
        
    def delete_entire_party(self, party_num):
        i = 0
        b = open("./Data/parties.csv", "r", encoding="utf-8")
        lines = b.readlines()
        b.close()
        for line in lines:
            fields = line.split(";")
            cid = fields[0]
            uid = fields[1]
            pid = fields[2]
            if int(pid) != int(party_num):
                if i == 0:
                    f = open("./Data/parties.csv", "w", encoding="utf-8")
                    f.write(str(cid) + ";" + str(uid) + ";" + str(pid))
                    f.close
                else:
                    f = open("./Data/parties.csv", "a", encoding="utf-8")
                    f.write(str(cid) + ";" + str(uid) + ";" + str(pid))
                    f.close
                i +=1
    
            
    def update_member_file(self, what_to_change, id_num, value):
        i = 0
        member_id = int(id_num)
        b = open("./Data/members.csv", "r", encoding="utf-8-sig")
        lines = b.readlines()
        b.close()
        for line in lines:
            fields = line.split(";")
            memberid = fields[0]
            name = fields[1]
            age = fields[2]
            phone = fields[3]
            job = fields[4]
            
            if int(memberid) != member_id:
                if i == 0:
                    f = open("./Data/members.csv", "w", encoding="utf-8")
                    f.write(str(memberid) + ";" + str(name) + ";" + str(age) + ";" + str(phone) + ";" + str(job))
                    f.close
                else:
                    f = open("./Data/members.csv", "a", encoding="utf-8")
                    f.write(str(memberid) + ";" + str(name) + ";" + str(age) + ";" + str(phone) + ";" + str(job))
                    f.close

            elif int(memberid) == member_id:
                if what_to_change == "name":
                    if i == 0:
                        f = open("./Data/members.csv", "w", encoding="utf-8")
                        f.write(str(memberid) + ";" + str(value) + ";" + str(age) + ";" + str(phone) + ";" + str(job))
                        f.close
                    else:
                        f = open("./Data/members.csv", "a", encoding="utf-8")
                        f.write(str(memberid) + ";" + str(value) + ";" + str(age) + ";" + str(phone) + ";" + str(job))
                        f.close
                
                elif what_to_change == "age":
                    if i == 0:
                        f = open("./Data/members.csv", "w", encoding="utf-8")
                        f.write(str(memberid) + ";" + str(name) + ";" + str(value) + ";" + str(phone) + ";" + str(job))
                        f.close
                    else:
                        f = open("./Data/members.csv", "a", encoding="utf-8")
                        f.write(str(memberid) + ";" + str(name) + ";" + str(value) + ";" + str(phone) + ";" + str(job))
                        f.close

                elif what_to_change == "phone":
                    if i == 0:
                        f = open("./Data/members.csv", "w", encoding="utf-8")
                        f.write(str(memberid) + ";" + str(name) + ";" + str(age) + ";" + str(value) + ";" + str(job))
                        f.close
                    else:
                        f = open("./Data/members.csv", "a", encoding="utf-8")
                        f.write(str(memberid) + ";" + str(name) + ";" + str(age) + ";" + str(value) + ";" + str(job))
                        f.close

                elif what_to_change == "job":
                    if i == 0:
                        f = open("./Data/members.csv", "w", encoding="utf-8")
                        f.write(str(memberid) + ";" + str(name) + ";" + str(age) + ";" + str(phone) + ";" + str(value) + "\n")
                        f.close
                    else:
                        f = open("./Data/members.csv", "a", encoding="utf-8")
                        f.write(str(memberid) + ";" + str(name) + ";" + str(age) + ";" + str(phone) + ";" + str(value) + "\n")
                        f.close
            i += 1

    def update_utility_file(self, what_to_change, id_num, value):
        i = 0
        utility_id = id_num
        b = open("./Data/utilities.csv", "r", encoding="utf-8-sig")
        lines = b.readlines()
        b.close()
        for line in lines:
            fields = line.split(";")
            utilityid = fields[0]
            name = fields[1]
            year = fields[2]
            manufacturer = fields[3]
            modified = fields[4]
            if utilityid != utility_id:
                if i == 0:
                    f = open("./Data/utilities.csv", "w", encoding="utf-8")
                    f.write(str(utilityid) + ";" + str(name) + ";" + str(year) + ";" + str(manufacturer) + ";" + str(modified))
                    f.close
                else:
                    f = open("./Data/utilities.csv", "a", encoding="utf-8")
                    f.write(str(utilityid) + ";" + str(name) + ";" + str(year) + ";" + str(manufacturer) + ";" + str(modified))
                    f.close
            if utilityid == utility_id:
                if what_to_change == "name":
                    if i == 0:
                        f = open("./Data/utilities.csv", "w", encoding="utf-8")
                        f.write(str(utilityid) + ";" + str(value) + ";" + str(year) + ";" + str(manufacturer) + ";" + str(modified))
                        f.close
                    else:
                        f = open("./Data/utilities.csv", "a", encoding="utf-8")
                        f.write(str(utilityid) + ";" + str(value) + ";" + str(year) + ";" + str(manufacturer) + ";" + str(modified))
                        f.close
                if what_to_change == "year":
                    if i == 0:
                        f = open("./Data/utilities.csv", "w", encoding="utf-8")
                        f.write(str(utilityid) + ";" + str(name) + ";" + str(value) + ";" + str(manufacturer) + ";" + str(modified))
                        f.close
                    else:
                        f = open("./Data/utilities.csv", "a", encoding="utf-8")
                        f.write(str(utilityid) + ";" + str(name) + ";" + str(value) + ";" + str(manufacturer) + ";" + str(modified))
                        f.close
                if what_to_change == "manufacturer":
                    if i == 0:
                        f = open("./Data/utilities.csv", "w", encoding="utf-8")
                        f.write(str(utilityid) + ";" + str(name) + ";" + str(year) + ";" + str(value) + ";" + str(modified))
                        f.close
                    else:
                        f = open("./Data/utilities.csv", "a", encoding="utf-8")
                        f.write(str(utilityid) + ";" + str(name) + ";" + str(year) + ";" + str(value) + ";" + str(modified))
                        f.close
                if what_to_change == "modified":
                    if i == 0:
                        f = open("./Data/utilities.csv", "w", encoding="utf-8")
                        f.write(str(utilityid) + ";" + str(name) + ";" + str(year) + ";" + str(manufacturer) + ";" + str(value) + "\n")
                        f.close
                    else:
                        f = open("./Data/utilities.csv", "a", encoding="utf-8")
                        f.write(str(utilityid) + ";" + str(name) + ";" + str(year) + ";" + str(manufacturer) + ";" + str(value) + "\n")
                        f.close
            i +=1

    def update_event_status(self, id_num):
        i = 0
        id_num = str(id_num)
        b = open("./Data/events.csv", "r", encoding="utf-8-sig")
        lines = b.readlines()
        b.close()
        for line in lines:
            fields = line.split(";")
            eid = fields[0]
            name = fields[1]
            time = fields[2]
            location = fields[3]
            status = fields[4]
            party = fields[5]
            if id_num != eid:
                if i == 0:
                    f = open("./Data/events.csv", "w", encoding="utf-8")
                    f.write(str(eid) + ";" + str(name) + ";" + str(time) + ";" + str(location) + ";" + str(status) + ";" + str(party))
                    f.close
                else:
                    f = open("./Data/events.csv", "a", encoding="utf-8")
                    f.write(str(eid) + ";" + str(name) + ";" + str(time) + ";" + str(location) + ";" + str(status) + ";" + str(party))
                    f.close
            if id_num == eid:
                if i == 0:
                    f = open("./Data/events.csv", "w", encoding="utf-8")
                    f.write(str(eid) + ";" + str(name) + ";" + str(time) + ";" + str(location) + ";" + "inactive" + ";" + str(party))
                    f.close
                else:
                    f = open("./Data/events.csv", "a", encoding="utf-8")
                    f.write(str(eid) + ";" + str(name) + ";" + str(time) + ";" + str(location) + ";" + "inactive" + ";" + str(party))
                    f.close
            i += 1



        
if __name__ == "__main__":
    D = GetData()
    D.get_members()
    members_list = D.get_member_list()
    for member in members_list:
        string = ("Name: " + member._name  + " | Phone: " + member._phone + " | Job: ")
        if member._job == "1":
            string += "Fjallgönguliði"
        elif member._job == "2":
            string += "Vélsleðaliði"
        elif member._job == "3":
            string += "Jeppaliði"
        string += (" | Age: " + member._age + "\n")
        print(string)
    #D.add_utility("Sleði 14", "2017", "Kawaiisakii", "0", None, True)
    #D.add_utility("Sleði 14", "2017", "Kawaiisakii", "0", None, True)
    #D.delete_utility("10008")
    #D.add_utility("Sleði 14", "2017", "Kawaiisakii", "0", None, True)


