# Software Development methodologies

## Waterfall (main key difference is the testing 
```
Waterfall is the most traditional and sequential choice. Although it’s usually viewed as an ”old school” or outdated method, it’s helpful to understand the history and structure of Waterfall to better appreciate the flexibility of more modern methodologies. First created in 1970, Waterfall was one of the most prominent methodologies for several decades because of its plan-driven approach.
```
- Waterfall requires plenty of structure and documentation up front. 
- It is divided into self-contained stages or steps. 
```
The first stage is vital, requiring a full understanding by both developers and customers of the project’s demands and scope before anything begins. 
The stages are relatively rigid and often follow this sequence: 
- determine the project’s requirements and scope, 
- analyze those requirements, 
- design, 
- implement, 
- test, 
- deploy 
- and finally, maintain.
```
### Pros:
```
Easy to manage due to well-defined starting and endpoints for each step
High-degree of accuracy surrounding cost estimates
Clearly defined requirements and outcomes
Technical documentation is created during initial requirement gathering
Test scenarios are defined in functional specifications
```
### Cons:
```
Slow delivery speed compared to other methodologies
Inflexibility regarding changes to initial requirements
Difficulty in defining the functional specifications of client requirements
Not suitable for large projects
```

## V-Model
```
The V-Model builds on the foundation of the Waterfall model that includes a testing phase associated with each development stage. 
It is also known as the validation and verification model. 
The V-Model is one of the most inflexible yet thorough of the various SDLC testing methodologies. Each phase of the model must be successfully completed before the next one begins.
```

### Pros:
```
Identifies defects early in the development process
High success rate
Simple to understand and easy to implement
Saves time by incorporating planning for testing before coding begins
```
### Cons:
```
Extremely rigid and inflexible
Early prototype creation is impossible
Updating test and requirement documents to reflect changes can take time
```

## Agile (inc. Scrum)
```
The Agile methodology was developed as a response to growing frustrations with Waterfall and other highly structured, inflexible methodologies. 
This approach is designed to accommodate change and the need to produce software faster.
- Agile values individuals and their relationships and interactions over tools; 
- Features customer collaboration throughout the development process; 
- Responds to change instead of following a set-in-stone plan;
- Focuses on presenting working software, rather than documentation. 
```

Unlike Waterfall, Agile is well equipped to handle the complexity and variability involved in development projects.
```
- Using the Agile approach, teams develop in short sprints or iterations, each of which includes a defined duration and list of deliverables, but in no particular order. 
- During sprints, teams work towards the goal of delivering working software (or some other tangible, testable output).
- Agile is collaboration-heavy, focusing on team strengths and efficiency, along with internal feedback from various departments and clients. 
--> Client satisfaction is the highest priority with the Agile approach, which teams achieve by continuously delivering working, tested, prioritized features.
```
### Pros:
``` 
No budgetary constraints to introducing new requirements
Fully engages business stakeholders in the development process
Lessened documentation requirements save time and money
Small issues are identified before they become major problems
```
### Benefits of Agile
```
Improved product quality 
A higher degree of collaboration between stakeholders 
Consistent time-frames and predictable costs 
Allows more focus on business values
```
### Cons:
```
Hard to estimate the effort required to complete complex projects
Requires experienced resources
High failure risk when end-user requirements are vague
```

## Scrum 
### Framework: a supporting structure around which something can be built

```
Another way to implement the Agile approach, Scrum borrows from Agile’s foundational beliefs and philosophy that teams and developers should collaborate heavily and daily.
Not a methodology but it is a framework used to manage the project, daily/weekly/monthly tasks. Great tool to use in a agile environment. 
```
### Scrum is a framework used for developing, delivering, and sustaining products.
``
With Scrum, software is developed using an iterative approach in which the team is front and center—experienced and disciplined workers on smaller teams might find the most success with this method, as: it requires self-organization and self-management.
```
- Team members break down end goals into smaller goals at the beginning and work through them using fixed-length iterations—or sprints—to build software and showcase it often (which usually last two weeks).
- Meetings play an important role in the Scrum approach, and during each sprint, daily planning meetings and demos take place to follow progress and gather feedback. - This incremental method promotes quick changes and development and adds value to complex projects. 
- Scrum incorporates the structure and discipline of more traditional software development methodologies with the flexibility and iterative practices of modern Agile. 
```

### How does it fit in with DevOps
```
- Agile turns enormous projects into smaller deliverables 
- DevOps continuously create, test and deploy software
- Sprints – the very heart of Agile and SCRUM 
- Assign sprints based on development requirements
- Promotes efficiency and ensures discipline
- FRAMEWORK definition - a system of rules, ideas, or beliefs that is used to plan or decide something:
``` 
### Three pillars of scrum: Transparency & Inspection & Adaptation

#### Scrum Roles
```
Product Owner 
Scrum Master 
Development Team 
Scrum Ceremonies 
```
#### Scrum Ceremonies
```
Sprint Planning 
Daily Scrum 
Sprint Review 
Sprint Retrospective
```
#### Scrum Artefacts
- Key information the Scrum Team and stakeholders NEED TO KNOW for understanding
```
1. Product under development 
2. Activities done 
3. Activities being planned 
```
- Here are a the minimum required artefacts in a scrum project. 
```
1. Product Backlog lists all features, requirements and fixes together form the changes to be made now
2. Sprint Backlog a forecast about what functionality will be made available in the next Increment and the work needed to deliver that functionality
3. Burn-Down Chart Sprint tracks total work remaining for every Daily Scrum to project the likelihood of achieving the Sprint Goal. Progress tracking tool.
4. Increment The Increment is the sum of all the Product Backlog items completed during a Sprint combined with the increments of all previous Sprints. At the end of a Sprint, the new Increment must be a working product, which means it must be in a useable condition.
```
#### Conclusion
```
Agile helps continuous deployment of software 
Works hand in hand with DevOps 
SCRUM framework delivers Agile
```

### ITERATIVE METHOD
```
- In computational mathematics, an iterative method is a mathematical procedure that uses an initial guess to generate a sequence of improving approximate solutions for a class of problems, in which the n-th approximation is derived from the previous ones
```
## EXTREME PROGRAMMING
``` 
Another Agile framework, Extreme Programming (or XP) focuses on producing higher quality software using the best practices in software development. As with most Agile approaches, XP allows for frequent releases in short development sprints that encourage change when needed.
In general, XP follows a set of values, rather than steps, including simplicity (develop what is required, nothing more); communication (teams must collaborate and work together on every piece of the software); consistent feedback; and respect.
Extreme Programing requires developers to first plan and understand the customer’s user stories—their informal descriptions of certain features. Other practices include: scheduling and dividing work into iterations. Design with simplicity in mind, code and test often, which helps to create fault-free software. Listen to feedback to best understand the functionality, and then test more.
```
## LEAN
```
Lean is at once a workflow methodology and a mindset, incorporating principles and practices from the manufacturing space and applying them broadly to a variety of industries, including software development. While Agile is an excellent methodology for the practical application of development best practices, it does not include instructions for scaling these practices across the organization or applying them outside of development-type work.
This is why many organizations who practice Agile at the team level begin to incorporate Lean philosophies, practices, and tools to help to innovate at scale. Lean’s basic principles—optimize the whole, eliminate waste, build quality in, create knowledge, defer commitment, deliver fast, and respect people—can help to guide decision-making across the organization in a way that can help to unearth potential issues and maintain a healthy organizational culture.
Combining the best of Lean thinking and Agile software development practices can create a healthy, sustainable culture of innovation that benefits not only the development organization, but the system as a whole.
```
### Pros:
```
Delivers increased functionality in a reduced timeframe
Eliminating unnecessary activity saves time and money
Enables fast decision making and is easily scalable
```
### Cons:
```
Requires excellent documentation for cross-team communication
A dependence on the team makes it easy to lose focus
```
## FEATURE-DRIVEN DEVELOPMENT
```
An iterative and incremental approach to software development, Feature-Driven Development
(FDD) is derived from the Agile methodology and is considered one way to implement it. Similar to Waterfall, FDD is typically viewed as an older methodology, a sort of precursor to modern Lean/Agile implementations. FDD still focuses on the goal of delivering working software frequently and is an especially client-centric approach, making it a good fit for smaller development teams.
Features are a foundational piece of FDD. Features are client-valued pieces of work that, according to the FDD approach, should be delivered every two weeks.
To produce tangible software often and efficiently, FDD has five steps, the first of which is to develop an overall model. Next, build a feature list and then plan by each feature. The final two steps—design by feature and build by feature—will take up the majority of the effort. At each step, status reporting is encouraged and helps to track progress, results, and possible errors. Although efficient response to change is one of FDD’s better attributes, an understanding of the client’s requirements and the overall model at the beginning of the project can reduce any surprises during development.
Additionally, any feature that takes longer than two weeks to design and build must be further broken down into separate features until it meets the two-week rule. The rigid structure of FDD make it less desirable to teams who balance project-driven and break-fix types of work.
```
