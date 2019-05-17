
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
    def __init__(self, eventid, name, location, description, party):
        self._time = name
        self._location = location
        self._description = description
        self._party = party
        self._event_id = eventid

class Party:
    def __init__(self, partyid, unitid):
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
        self._member_size = 0
        self._utility_size = 0
        self._event_size = 0
        self._party_size = 0

    def get_members(self):
        member_list=open("members.csv", "r", encoding="utf-8").read().split('\n')
        for line in member_list[:-1]:
            fields = line.split(";")
            memberid = fields[0]
            name = fields[1]
            age = fields[2]
            phone = fields[3]
            job = fields[4]
            self.add_member(name, age, phone, job, memberid)

    def add_member(self, name, age, phone, job, memberid = None):
        if memberid == None:
            memberid = self._mid
        self._members_map[memberid] = Member(memberid, name, age, phone, job)
        self._member_size += 1 
        self._mid +=1

    def get_member_list(self):
        members_list = []
        for id in self._members_map:
            members_list.append(self._members_map[id])    
        return members_list


    def get_utilities(self):
        utilities_list=open("utilities.csv", "r", encoding="utf-8").read().split('\n')
        for line in utilities_list[:-1]:
            fields = line.split(";")
            utilityid = fields[0]
            name = fields[1]
            year = fields[2]
            manufacturer = fields[3]
            modified = fields[4]
            self.add_utility(name, year, manufacturer, modified, utilityid)
    
    def add_utility(self, name, year, manufacturer, modified, uid = None):
        if uid == None:
            uid = self._uid
        self._utilities_map[uid] = Utilities(uid, name, year, manufacturer, modified)
        self._utility_size += 1 
        self._uid +=1

    def get_utilities_list(self):
        utility_list = []
        for id in self._utilities_map:
            utility_list.append(self._utilities_map[id])    
        return utility_list

    def get_events(self):
        events_list=open("events.csv", "r", encoding="utf-8").read().split('\n')
        for line in events_list[:-1]:
            fields = line.split(";")
            eid = fields[0]
            name = fields[1]
            location = fields[2]
            description = fields[3]
            party = fields[4]
            self.add_events(name, location, description, party, eid)
    
    def add_events(self, name, location, description, party, eid = None):
        if eid == None:
            eid = self._eid
        self._event_map[eid] = Event(eid, name, location, description, party)
        self._event_size += 1 
        self._eid +=1
    
    def get_events_list(self):
        events_list = []
        for id in self._event_map:
            events_list.append(self._event_map[id])    
        return events_list

    def get_parties(self):
        parties_list=open("parties.csv", "r", encoding="utf-8").read().split('\n')
        for line in parties_list[:-1]:
            fields = line.split(";")
            uid = fields[0]
            pid = fields[1]
            self.add_party(uid, pid)
    
    def add_party(self, uid, pid):
        self._party_map[pid] = Party(uid, pid)
        self._party_size += 1 
        self._pid +=1
    
    def get_parties_list(self):
        parties_list = []
        for id in self._party_map:
            parties_list.append(self._party_map[id])    
        return parties_list