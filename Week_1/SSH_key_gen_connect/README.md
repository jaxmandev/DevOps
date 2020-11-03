# Day 2

## Trello

Join --> Keep track --> Refer back to the board whenever you want to revise

## SSH key

- Generate an SSH key using:
```
ssh-keygen -t rsa -b 4096 -C "your_email@email.com"
```
- copy the ssh key from localhost with
```
cd ~/.ssh cat id_rsa.pub
```
- paste the public key on your github in settings GPH SSH key option in your profile menu and create key

## Repos

- go back to your terminal after creating key
- go to the folder in which you want to initialise your repository
- initialise repo using:
``` git init```
- to create a new file use:
``` touch filename```
- add your file(s)
```
git add filename
or
git add . // adds all files in the folder to the repo
```
- edit file
```
nano filename
// save and exit using CTRL+X, then y
```
- run the following github commands:
```
git commit -m "msg"
git branch -M main
git remote add origin git@github.com:USER_NAME/Repo_name.git
git push -u origin main
```
- for all subsequent edits to the same files, you need to:
```
git add . // add the files
git commit -m "msg" // commit the changes
git push -u origin main // push to origin
```
- go back to github repo to verify the changes and connections
- when in local folder connected to the git cloud enter ```` git -T
```
