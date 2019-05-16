
from sortedcontainers import SortedDict
import csv


class Member:
    def __init__(self, memberid, name, age, phone, job):
        self._name = name
        self._age = age
        self._phone = phone
        self._job = job
        self._member_id = memberid

class GetData:
    def __init__(self):
        self._members_map = SortedDict({})
        self._mid = 0
        self._size = 0

    def get_members(self):
        print(self._size)
        member_list=open("members.csv", "r", encoding="utf-8").read().split('\n')
        #print("jj")
        for line in member_list[:-1]:
            fields = line.split(";")
            memberid = fields[0]
            print(memberid)
            name = fields[1]
            age = fields[2]
            phone = fields[3]
            job = fields[4]
            self.add_member(name, age, phone, job, memberid)

    def add_member(self, name, age, phone, job, memberid = None):
        #print(userid)
        if memberid == None:
            memberid = self._mid
        #print(self._size)
        self._members_map[memberid] = Member(memberid, name, age, phone, job)
        self._size += 1 
        self._mid +=1

    def get_contacts_ordered(self):
        ordered_contact_list = []
        for id in self._members_map:
            ordered_contact_list.append(self._members_map[id])    
        return ordered_contact_list

    def pass_members(self):
        return self._members_map