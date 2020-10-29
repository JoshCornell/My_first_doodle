# This program will run over a log file and create an identical copy in a text file.
# The text file will be created automatically if it does not already exist. If the File already exists, data will be appended to the existing file.


datadumpvar = []
todaydate = input("Enter Today's date, (format YYYYMMDD): ")

try:
    e = open(todaydate + "_Forensic_backup.txt", "x")
    print("New forensic backup file created for provided date.")
except:
    print("File already exists")
    e = open((todaydate) + "_Forensic_backup.txt", "a")
    print("Opening existing file for provided date.\nData will be appended to this file.")
datadumpsrc = open((todaydate) + "_Forensic_backup.txt", "r")
for datadumpline in datadumpsrc:
    datadumpline = datadumpline.strip()
    #print(datadumpline)
    datadumpvar.append(datadumpline)
#print('initialized datadumpvar')

try:
    f = open(input('Enter log filepath or filename here:\n'), 'r')
    for line in f:
        line = line.strip()
        if line in datadumpvar:
            print("This log entry is already contained in " +todaydate + "'s backup file")
            continue
        else:
            print("Added log entry to " + todaydate + "'s Forensic backup file")
            e.write(line + "\n")
            datadumpvar.append(line)




except:
    print('Filename and/or path provided is incorrect or does not exist')