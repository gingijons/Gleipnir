def main(what_to_change, id_num, value):
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

if __name__ == "__main__":
    pass