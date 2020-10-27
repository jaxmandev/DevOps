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

## Time and Taks Management

- Pareto Principle (80 / 20)
- Eisenhower Principle (Important / Urgent)
- Task Management Tools: Teams + Outlook Calendar / Trello
- Two minutes rule
- How to prioritise tasks
- Best practices of prioritising and managing tasks
- Communication

## Biases

Biases are one of the key ways we can communicate with others

### Anchoring bias
Relies too heavily on the first piece of information received e.g. someone told you something about someone else and you anchor to that and assume that for a fact

### Choice-Supportive bias
The tendency to retroactively ascribe positive attributes to an option one has selected and/or to demote the forgone options. It is part of cognitive science, and is a distinct cognitive bias that occurs once a decision is made.

### Confirmation bias
The tendency to search for, interpret, favor, and recall information in a way that confirms or supports one's prior beliefs or values.

### Bandwagon bias
The tendency people have to adopt a certain behavior, style, or attitude simply because everyone else is doing it.
There were other biases covered

## Exploiting bias in the workplace

- Reactance - by telling people they are able to say no will make them more likely to say yes.
- Reciprocity - be the first to give the feeling of obligation to give when you receive. Personalised and unexpected makes it even better.
- Door in the face - Forcing people to refuse a large request increases the likelihood of agreeing to a second smaller request.
- Likeability - give compliments and build cooperation. Freely give honest flattery.
- Social proof - people look to others to determine their own actions

## Colour Hats

* White Hat = Facts Only / Need for information
* Yellow Hat = Optimism / Benefits / Explore Positives
* Black Hat = Judgement / Spot diffiulties and dangers
* Red Hat = Intuition / Likes and Dislikes / Feelings
* Green Hat = Creativity / Possibilites / Alternatives / New Ideas
* Blue Hat = Thinking Process / Ensures Six Thinking Hats guideliness are observed

## Dealing with conflict

* Take time to understand the situation
* Know your audience
* Ask others for their perspective
* Compromise
* LISTENING IS KEY
* Different Personalities

* Understand each personality and how they work/think
* Establish how to approach them
* Adapt accordingly
* Respect differences
* Each has their own work ethic and style
* Be on the same team
* Its your responsibility to make diffucult relationships work

## Personality Traits

1. Extroverts
2. Introverts
3. Supporter
4. Director
5. Analytical
