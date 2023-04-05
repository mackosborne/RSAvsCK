
from prettytable import PrettyTable


def veryPrettyPrint(rowlist, times, start, end,limit, version, isTraining, algorithim):
    table= PrettyTable()
    x = 0
#Training Mode
    if(isTraining == 1):
        largest = 0
        for entry in rowlist:
            row = []
            if entry[2] == 1:
                row.append("True") 
            else:
                row.append("False") 
            cryptWords = str(entry[1]).split('\\')
            del cryptWords[0]
            i =0
            for word in cryptWords:
                row.append(word)
                if len(word)-1 > largest:
                    largest = len(word)-1
            table.add_row(i, row)
            i = i + 1
        x = 0
        header = ["ID", "isReal"]
        while x < largest:
            header.append(str(x))
            x = x + 1
        table.field_names = header
        print(table)
        print("Total Time: ", end - start)
        print("Average Time: ", sum(times)/len(times))
        print("Total Entries: ", limit)
        print("Version: ", version)
        print("Algorithim: ", algorithim)
#Testing Mode    
    else:
        for entry in rowlist:
            row = []
            cryptWords = str(entry[1]).split('\\')
            del cryptWords[0]
            for word in cryptWords:
                row.append(word)
            table.add_row(row)
        header = ["ID"]
        while x < largest:
            header.append(str(x))
            x = x + 1
        table.field_names = header
        print(table)
        print("Total Time: ", end - start)
        print("Average Time: ", sum(times)/len(times))
        print("Total Entries: ", limit)
        print("Version: ", version)
        print("Algorithim: ", algorithim)