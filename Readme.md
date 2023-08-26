# Graded Project on Building CI-CD Pipeline Tool

## Mahendra | Israrul | Sai
1. Create a Repository and Python code
    * Create two branches in the repository namely PROD and MAIN
    * Checkout to main branch
    * Create .env files add repository name, owner and username
    * Create a python program that will use github api's to check if last commit stored in the static file 'latest-commit.txt' is matching with the latest commit id present in the github.
    * If not matching then write the latest commit to the text file.
2. Go to your linux terminal 
    * Install nginx by using the command
        - `sudo apt-get install nginx`
    * Clone your repo to a folder
        - `git clone <repository-name>`
    * Goto your user's folder and create a bash script
        - `nano git-pull-script.sh`
        - Add code that will execute the python file in the repository
        - CODE: https://github.com/Mahi2k/cicdpipeline/blob/prod/git-pull-script.sh
        - This will create a different file old-commit.txt. When latest-commit and old-commit do not match.
    * When bash script will run it will pull the latest code based on the condition the we provided in the bash script
    * After pulling the latest code bash script will copy the folder to NGINX server folder
    * Path to copy is specified in bash script itself
        - `(cp /home/mahi2k/repos/cicdpipeline/index.html /var/www/html/)`
    
3. Reload the NGINX server by using the command in script
    - `systemctl reload NGINX`

-----------------------------------------------------------------------------------------------------------------------------