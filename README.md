Ballot Box
=======

What you'll see
-----------
This project creates a website that allows users to create their own ballots and view real-time voting. Once
users sign up or login into the service, they are able to add items to their personal ballots and manage those
ballots as needed. The dashboard is used to display user information as well as a snapshot of the ballots that
the user has used. The items are depicted in a separate webpage that provides an image, description and item
name.


How to Run
-----------

In order to properly run this project you must first install Poetry, a tool used for dependency management and
packaging in Python. A link to the installation documents can be found here:
>https://python-poetry.org/docs/

Following installation run the command "poetry install", this will install all the project's dependencies.

In order to run the application, you must execute the following command in the appropriate directory
(vote_proj/vote_proj):
>python run.py

 This will cause the program to run locally on port 5000. The webpage is located in the following url:
>http://127.0.0.1:5000/
![Screen Shot 2022-01-18 at 4 21 30 PM](https://user-images.githubusercontent.com/44513190/150029387-43b55562-4871-48dc-aeea-2b0bee8d2596.png)

Once user has logged in or signed up, they will be directed to the following url where it will show snapshots of ballots:
>http://127.0.0.1:5000/dashboard/
![Screen Shot 2022-01-18 at 4 31 29 PM](https://user-images.githubusercontent.com/44513190/150029405-a193452d-f774-49ff-aee6-31f89b770786.png)

This will display user information as well as ballots under the users account, the items in those ballots and
the amount of votes each item has.

The following url is used to add a new ballot to a users account:
>http://127.0.0.1:5000/ballot_name/

The following url is used to add an item to a ballot:
>http://127.0.0.1:5000/ballot_items/

Clicking on the name of a ballot on the users dashboard takes you to the voting screen!
>http://127.0.0.1:5000/dashboard/(Your-Ballot!)
![Screen Shot 2022-01-18 at 4 43 38 PM](https://user-images.githubusercontent.com/44513190/150029997-17b45d64-bf09-4f62-accd-ff8a9e800154.png)
