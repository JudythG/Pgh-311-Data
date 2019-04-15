# Future improvements:
# * crashes on invalid key type, shouldn't

import csv
import operator
import io
import prompter_311

# I want to be able to count data for two colums
# ie. show neighborhoods by request type

# data structure
# { 'field1': <field 1 data>, 'field2', <field 2 data>, 'count': <count>}

def countCalls (f_in, dictReader, colHeader1, colHeader2):
    # reset file pointer to start and skip header
    # if calls dictReader.next () after f_in.seek(0), 
    #    the first call to this function will skip the first row of data
    # if don't call dictReader.next (), 
    #    all other calls to this function will include the header
    #    as a data row so check for colHeader as data field below
    f_in.seek(0)

    callsDict = {}
    for row in dictReader:
        fieldType1 = row[colHeader1]
        fieldType2 = row[colHeader2]

	# if field empty, skip to next row
        if fieldType1  == '' or fieldType2 == '': 
            continue 

	# side effect of seeking to start of file
        if fieldType1 == colHeader1:
            continue

        if fieldType1 in callsDict.keys():
            if fieldType2 in callsDict[fieldType1].keys():
                callsDict[fieldType1][fieldType2] += 1
            else:
                tempDict = {}
                tempDict [fieldType2] = 0
                callsDict[fieldType1][fieldType2] = 1
        else:
            tempDict = {}
            tempDict [fieldType2] = 1
            callsDict[fieldType1] = tempDict
    return callsDict

def printCalls (callsDict):
    sorted1 = sorted (callsDict.items())
    for k1, v1 in sorted1:
        print (k1)
	
        # reverse sort the data so highest number of calls at top
        sorted2 = sorted(v1.items(), key=operator.itemgetter(1), reverse=True)
        for k2, v2 in sorted2:
            print ("\t" + k2 + ": count is " + str (v2))
    print ()

# main

fname = prompter_311.getFileName()
f_in = open(fname) 
with f_in:
    reader = csv.DictReader(f_in)

    # store column headers into headers to print as list for user to 
    # select from
    header = next(reader)
    headers = 'list of field: '
    for k in header.keys():
        headers += k + ' '

    while True:
        print (headers)
        response1 = input ("Enter first field name or q to quit: ")
        if response1 == 'q':
            break
        response2 = input ("Enter second field name or q to quit: ")
        if response2 == 'q':
            break

        if response1.upper() in headers and response2.upper() in headers:
            callsDict = countCalls (f_in, reader, response1.upper(), response2.upper())
            printCalls (callsDict)

