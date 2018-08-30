# Need to get one user per fips per day and number of tweets from that day

from database import Database
import tkFileDialog as fd
import cPickle as pk





mover_db_files = fd.askopenfilenames(title="Choose mover databases")

if not mover_db_files: 
    print "\nNo mover dbs selected. Goodbye!\n"
    sys.exit()


print "\nGrabbing mover tweet stats..."

for i, mover_db_file in enumerate(mover_db_files): 
    print "\t{} out of {}".format(i + 1, len(mover_db_files))

    current_db = Database(db_file)

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

    for result in results: 
        print result

print "\nFinished grabbing mover tweet stats..."