# Election Analysis

## Overview of Election Audit
The purpose of this election analysis was to further analyze the data to provide metrics concerning voter turnout by county.  Organizing the data by county provides another layer of information that makes the work of the election commission easier.  The more information that is supplied to the election commision the easier the auditing process is in general.  The python script written extracts key data points and makes them easily readable which will benefit the election commission greatly.

## Election Audit Results

* The total number of votes cast in this election was 369,711 votes.

* The breakdown for voting in the relevant counties is as follows.
    ###### County Votes:
    ###### Jefferson: 10.5% (38,855)
    ###### Denver: 82.8% (306,055)
    ###### Arapahoe: 6.7% (24,801)
    
* The county with the largest number of votes was by far Denver.  Denver made up over 80% of the total vote count for the three counties with a total number of 306,055 votes.

* The breakdown of voting for each particular candidate is as follows.
    ###### Charles Casper Stockham: 23.0% (85,213)

    ###### Diana DeGette: 73.8% (272,892)

    ###### Raymon Anthony Doane: 3.1% (11,606)

* The winner of the election was...
   ###### Winner: Diana DeGette
   ###### Winning Vote Count: 272,892
   ###### Winning Percentage: 73.8%

## Election Audit Summary
This script is extremely valuable to the Election Commission because it can be used for a statewide election.  In its current form, this script could loop through all of the counties in Colorado and return the same results as it does now.  This script could be further optimized to include realtime population counts of each county to compare to the voter turnout to identify counties in which further auditing could be needed.  It could also be used to finder the winner of each county in order to identify regional political trends.  The core methodology of the current script is quite broad and can be applied to identify many different metrics and is a valuable addition to the technical analysis of the Election Commission.

