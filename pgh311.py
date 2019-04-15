import csv
import operator
import io
import prompter_311

# I wanted to see if I could reset the DictReader pointer to the start
# so I created a function to count the number of calls by column header
# name.
#
# Since the assignments were all variants of count the number of calls
# for this column header, I chose user input so I could count the number
# of calls for a a column header chosen at run-time.

def countCalls (f_in, dictReader, colHeader):
    # reset file pointer to start and skip header
    # if calls dictReader.next () after f_in.seek(0), 
    #    the first call to this function will skip the first row of data
    # if don't call dictReader.next (), 
    #    all other calls to this function will include the header
    #    as a data row so check for colHeader as data field below
    f_in.seek(0)

    callsDict = {}
    for row in dictReader:
        fieldType = row [colHeader]

	# if field empty, skip to next row
        if fieldType  == '': 
            continue 

	# side effect of seeking to start of file
        if fieldType == colHeader:
            continue

        if fieldType in callsDict.keys():
            callsDict[fieldType] += 1
        else:
            callsDict[fieldType] = 1
    return callsDict

def printCalls (callsDict, fieldLabel):
    # reverse sort the data so highest number of calls at top
    sorted_calls = sorted(callsDict.items(), key=operator.itemgetter(1), reverse=True)

    # print 
    for k, v in sorted_calls:
        print (fieldLabel + " " + k + "  has " + str(v) + " calls")
    print ()



# main

fname = prompter_311.getFileName()
f_in = open(fname) 
with f_in:
    reader = csv.DictReader(f_in)

    # store column headers into headers to print as list for user to 
    # select from
    header = next(reader)
    #header = reader.next ()
    headers = 'list of field: '
    for k in header.keys():
        headers += k + ' '

    while True:
        print (headers)
        response = input ("Enter field name or q to quit: ")
        if response == 'q':
            break
        if response.upper() in headers: 
            callsDict = countCalls (f_in, reader, response.upper())
            printCalls (callsDict, response)

