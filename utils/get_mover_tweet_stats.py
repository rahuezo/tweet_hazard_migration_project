# Need to get one user per fips per day and number of tweets from that day

from database import Database
import tkFileDialog as fd
import cPickle as pk
import csv





mover_db_files = fd.askopenfilenames(title="Choose mover databases")

if not mover_db_files: 
    print "\nNo mover dbs selected. Goodbye!\n"
    sys.exit()



with open('mover_daily_statistics.csv', 'wb') as f: 
    writer = csv.writer(f, delimiter=',')

    # Write the file header    
    writer.writerow(["User ID", "Fips", "Date", "Total Tweets"])

    print "\nGrabbing mover tweet stats..."

    for i, mover_db_file in enumerate(mover_db_files): 
        print "\t{} out of {}".format(i + 1, len(mover_db_files))

        current_db = Database(mover_db_file)

        results = current_db.select(    
            """
            SELECT
                user_id "User ID",
                fips "Fips", 
                tweet_date "Date", 
                COUNT(tweet_text) "Total Tweets"
            FROM
            tweets
            GROUP BY
            user_id, fips, substr(tweet_date, 0, 11)
            """
        )

        print "\t\tWriting results to output csv..."
        writer.writerows(results)
        print "\t\tFinished writing results to output csv!"

    print "\nFinished grabbing mover tweet stats..."