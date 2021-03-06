from database import Database

import tkFileDialog as fd
import cPickle as pk
import os, csv, sys


relevant_counties = [
    '6021', '6097', '6041', '6017', '6023', '6093', '6115', '6033', '6049', 
    '6063', '6103', '6057', '6113', '6089', '6067', '6105', '6045', '6011', 
    '6015', '6095', '6035', '6061', '6007', '6005', '6091', '6101', '6055'
]

wd = fd.askdirectory(title="Choose folder with 2015 mover databases")

if not wd: 
    print "\nNo folder selected. Goodbye!\n"
    sys.exit()

databases_2015 = [os.path.join(wd, f) for f in os.listdir(wd) if '2015' in f]

if not databases_2015: 
    print "\nNo databases found. Goodbye!\n"
    sys.exit()

relevant_users = set()

# Loop through 2015 databases

print "\nGrabbing 2015 movers..."

for i, db_file in enumerate(databases_2015): 
    print "\t{} out of {}".format(i + 1, len(databases_2015))

    current_db = Database(db_file)

    for fips in relevant_counties: 
        results = current_db.select(
            """
                SELECT user_id
                FROM tweets 
                WHERE fips={} AND substr(tweet_date, 0, 11) BETWEEN '2015-01-01' AND '2015-06-30'            
            """.format(fips))

        for result in results: 
            if result: 
                relevant_users.add(result[0])

print "\n\tPickling 2015 movers..."

with open('resources/movers_2015.pkl', 'w') as f: 
    pk.dump(relevant_users, f)

print "\n\tFinished pickling 2015 movers!"
print "\nFinished grabbing 2015 movers!\n"