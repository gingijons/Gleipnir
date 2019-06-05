def main(what_to_change, id_num, value):
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

if __name__ == "__main__":
    pass