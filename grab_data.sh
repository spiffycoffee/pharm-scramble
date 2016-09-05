#!/bin/bash

#--------------------------------------------------------------------
#  PhorCAS Login information  
#  DON'T add spaces BEFORE or AFTER the = sign 
#--------------------------------------------------------------------
  USER=username
  PASS=password
#--------------------------------------------------------------------


# login with the user name and pass to acquire cookie
wget --post-data "lockdown_username=$USER&lockdown_password=$PASS" \
     --save-cookies cookies.txt --keep-session-cookies \
     --delete-after --quiet \
     https://portal.phorcas.org/applicants15/index.cgi

# use cookie to grab the page with data
wget --load-cookies cookies.txt -O- --quiet \
  https://portal.phorcas.org/applicants15/index.cgi?rm=designations_search |

# extract line of json that was embedded in the html
grep 'ds.designations ' | 

# remove js cruft around the json
sed 's/.\{24\}//;s/.$//' | 

# remove trailing newline, then save the json 
tr -d '\n' > input.json 

# run python script to parse json and display/email updates
python ./parse.py
