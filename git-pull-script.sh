#!/bin/bash

# Change the directory and run pyhton file that will fetch latest commit
(cd /home/mahi2k/repos/cicdpipeline/; sudo pyhton latestcommit.py)

# Sleep for 3 seconds as to wait for new commti file to get generated
(sleep 3)

oldCommitId=`cat old-commit.txt`
newCommitId=`cat /home/mahi2k/repos/cicdpipeline/latest-commit.txt`

# Add if condition to match old and new commit id.
# If they dont match then do a latest pull
if [ "${oldCommitId}" != "${newCommitId}" ]; then
    echo "Pulling latest code"
    (cd /home/mahi2k/repos/cicdpipeline/; git pull)
    echo "Created latest commit file"
    `cat /home/mahi2k/repos/cicdpipeline/latest-commit.txt > old-commit.txt`
    echo "Done!!"

    # Copy latest index file to hosted folder that is html/
    (cp /home/mahi2k/repos/cicdpipeline/index.html /var/www/html/)
    
    # Reload the nginx server
    (systemctl reload nginx)

fi
