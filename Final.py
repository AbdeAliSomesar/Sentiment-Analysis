def rate(string):
    dicti={'good':+1,'awesome':+2,'superb':+2,'super':+2,'excellent':+2,'amazing':+1,'bad':-1,'worse':-2,'worst':-2,'better':+2,'bum1':-1, 'poor':-1, 'unsatisfactory':-1,'disagreeable':-1, 'displeasing':-1, 'offensive':-1, 'uncongenial':-1, 'unpleasant':-1, 'unsympathetic':-1, 'icky':-1,'yucky':-1,'nice':+1,'bonny':+1,'braw':+1,'agreeable':+1,'congenial':+1,'favorable':+1,'meorable':+1, 'grateful':+1, 'gratifying':+1, 'nice':+1, 'pleasant':+1, 'pleasing':+1, 'pleasurable':+1,'best':+1, 'satisfying':+1, 'welcome':+1}
    extra={'not':-.5,'very':+2,'awfully':-2}
    exitwords = {'could', 'would', 'be', 'been', 'have', 'might', 'may'}
    #string= str(input("enter comment"))
    #print(string)
    reveiw= string.lower().split()
    total=0
    flag=0
   # print(reveiw)
    reveiw=clean(reveiw)
   # print(reveiw)
    for val in reveiw:

        thisindex = reveiw.index(val)

        # print(thisindex)
        if val in extra:

            for i in range(thisindex,len(reveiw)):
                if reveiw[i] in dicti:
                    total=total+(dicti.get(reveiw[i])*extra.get(val))
                    reveiw[i]='0'
                    #print("------------")
                    #print()
                    break

        elif val in dicti:
            total=total+dicti.get(val)
        elif val in exitwords:
            if reveiw[thisindex+1] in exitwords:
                for i in range(thisindex,len(reveiw)):
                    if reveiw[i] in dicti:
                        reveiw[i]='0'
                        break

        reveiw[thisindex]='0'
        #print(reveiw)
    #print(total)
    return total
#cleaning the review
def clean(word_list):
    cleanlist = []
    for word in word_list:
        symbols = "!@~#$%^&*()_+=-<>?:{}[];',./"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")  # replace those symbols with nothing

        if len(word) > 0:
            # print(word)
            cleanlist.append(word)
    return cleanlist

#database connection

