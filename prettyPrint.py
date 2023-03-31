import os

def prettyPrint(rowlist, times, start, end,limit, version, isTraining, algorithim):
    prevCount = 0
    for file in os.listdir():
        if file.endswith('.txt'):
            prevCount = prevCount + 1
    filename = 'prettyResults' + str(prevCount) + '.txt'
    f = open(filename, 'w+')
    largest_word = 0  
    words = 0      
    for entry in rowlist:
        #Grab each word in ciphertext breaking on \\
        cryptWords = str(entry[1]).split('\\')
        del cryptWords[0]
        if len(cryptWords) > words:
            words = len(cryptWords)
        for word in cryptWords:
            if len(word) > largest_word:
                largest_word = len(word)
    #------ Build Inputs------
    lines = []
    lines1 = "*" * largest_word * words
    lines2 = "* ECRYPTION ALGORITHIM:" + algorithim + " " * (largest_word * words - (len(algorithim) + 22)) + "*" 
    #Calculate White Space
    whiteSpace = largest_word * words - len(lines2)
    lines2 = "*"  + lines2 + " " * int(whiteSpace) + "*"
    lines3 = "* Number of Entries: " + str(limit) + " " * (largest_word * words - 27) + "*"
    lines4 = "* Total Time: " + str(end - start) + " " * (largest_word * words - 20) + "*"
    lines5 = "* Average Time: " + str(sum(times)/len(times)) + " " * (largest_word * words - 20) + "*"
    if isTraining == 1:
        flagged = "True"
    else:
        flagged = "False"
    lines6 = "* Training Mode: " + str(flagged) + " " * (largest_word * words - 19) + "*"
    if version == 1:
        stringVersion = "Static"
    else:
        stringVersion = "Generated"
    lines7 = "* Version: " + str(stringVersion) + " " * (largest_word * words - (11+len(stringVersion))) + "*"
    lines8 = "*" * largest_word * words
    #LABLES
    IDCush = (len(str(limit)) - 2)
    CTCush = (largest_word - 10)/2
    isRealCush = (largest_word - 6)/2

    lines10 = "=" * largest_word * words
    lines11 = "||" + "isReal"  + "|" + " " * int(IDCush) + "ID" + " " * int(IDCush) + "|"
    
    for y in range(words):
        lenNum = len(str(y))
        iBuffer = int(largest_word - lenNum)
        lines11 = lines11 + str(y) + " " * iBuffer + "|"
    #Append Lines
    #* Break
    lines.append(lines1)
    #Encryption Algorithim
    lines.append(lines2)
    #Number of Entries
    lines.append(lines3)
    #Total Time
    lines.append(lines4)
    #Average Time
    lines.append(lines5)
    #Training Mode
    lines.append(lines6)
    #Version
    lines.append(lines7)
    lines.append(lines8)
    #lines.append(lines9)
    lines.append(lines10)
    lines.append(lines11)
    #Append Entries
    if IDCush < 1:
        IDCush = 1
    for entry in rowlist:
        if entry[2] == 1:
            view = "|| True |"+str(entry[0])+ " " * IDCush + "|" 
        else:
            view = "||False |"+str(entry[0])+ " " * IDCush + "|" 
        #Grab each word in ciphertext breaking on \\
        cryptWords = str(entry[1]).split('\\')
        del cryptWords[0]
        for word in cryptWords:
            view = view + str(word) + (" " * (largest_word - len(str(word)))) + "|"
        if isTraining == 1:
            view = view + str(entry[2]) + (" " * (largest_word - len(str(entry[2])))) + "||"
        else:
            view = view + "||"
        lines.append(view)
    lines.append(lines10)
    #Write to file
    for line in lines:
        f.write(line)
        f.write('\n')
    f.close()