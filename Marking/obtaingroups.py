#!/usr/bin/env python

import csv
import argparse

"""
Script to create a csv file for every group with students in alphabetical order
"""

parser = argparse.ArgumentParser(description='Identify all groups of students and create seperate csv files')
parser.add_argument('rawdata', help='A data file with 4 columns, number, first name, last name and group')
args = parser.parse_args()
rawdata = args.rawdata

print 'Reading students from %s' % rawdata

f = open(rawdata, 'r')
rawdata = csv.reader(f)
rawdata = [row for row in rawdata]
f.close()

groups = {}
for row in rawdata:
    grp = row[-1]
    if grp != '':
        if grp not in groups:
            groups[grp] = [row[1] + ' ' + row[2]]
        else:
            groups[grp].append(row[1] + ' ' + row[2])


print '%s groups identified' % len(groups)

tickables = ['W02-A1',
             'W02-A2',
             'W02-01',
             'W02-03',
             'W02-05',
             'W02-06',
             'W02-09',
             'W02-11',
             'W02-13',
             'W02-18',
             'W02-19',
             'W02-21',
             'W02-24',
             'W03-A1',
             'W03-A2',
             'W03-01',
             'W03-03',
             'W03-05',
             'W03-07',
             'W03-10',
             'W03-12',
             'W03-14',
             'W03-15',
             'W04-A1',
             'W04-A2',
             'W04-01',
             'W04-02',
             'W04-05',
             'W04-07',
             'W05-A1',
             'W05-A2',
             'W05-01',
             'W05-04',
             'W05-05',
             'W05-07',
             'W05-10',
             'W06-A1',
             'W06-A2',
             'W06-01',
             'W06-02',
             'W06-04',
             'W06-07',
             'W06-09',
             'W07-A1',
             'W07-A2',
             'W07-03',
             'W07-05',
             'W07-09',
             'W07-12',
             'W07-14',
             'W08-A1',
             'W08-A2',
             'W08-02',
             'W08-03',
             'W08-05',
             'W08-06',
             'W08-07',
             'W08-08',
             'W09-A1',
             'W09-A2',
             'W09-01',
             'W09-04',
             'W09-07',
             'W09-08',
             'W10-A1',
             'W10-A2',
             'W10-01',
             'W10-02',
             'W10-03',
             'W10-04',
             'W10-05',
             'W10-06',
             'W10-07',
             'W10-08',
             'W10-09',
             'W10-10',
             'W10-11',
             'W10-12',
             'W10-13',
             'W10-14',
             'W10-15',
             'W10-16',
             'W10-17',
             'W10-18',
             'W10-19',
             'W10-20',
             'W10-21'
]

for grp in groups:
    outfile = open('%s.csv' % grp, 'w')
    writeobj = csv.writer(outfile)
    writeobj.writerow([' '] + groups[grp])
    for e in tickables:
        writeobj.writerow([e])
    outfile.close()