# NatWest-Assignment
Assignment for Intern @NatWest Group

# Problem Statement

```
Remember a childhood game "Rock, Paper and Scissors". It is a two-player game in which each
person simultaneously chooses either rock, paper, or scissors.
Following are the rules of game
1. The Rock beats the Scissors
2. The Scissors beats the Paper
3. The Paper beats the Rock
You need write a microservices where player 1 is user and player 2 is computer itself. Your code
should be able to find out winner as per above rules.
Player 1 will pass its move through a rest endpoint as parameter and possible values of parameters
are "Rock, Paper and Scissors".
Computer as player 2 will generate random move out of "Rock, Paper and Scissors". Write a method
which will generate random move.
Winner should be reported appropriately in response, possible values of response "Player wins",
"Computer wins", or "It is a tie".
While writing code take care of following points.
1. Code should be committed in GitHub.
2. Appropriate logging should be there.
3. Unit test cases should be there.
4. Swagger documentation should there. 
```


# Tech Stack 🧑‍💻
- Django is used for backend.
- SQLite used for database.
- Postman for endpoint documentation


#PostMan Request Response method:

-Endpoint for playing the move:
<kbd>![image](https://user-images.githubusercontent.com/78960121/208525703-0e6faa57-95d4-4a22-984f-ea2ea77040b8.png)</kbd>

-Endpoint for showing the logs of games:
<kbd>![image](https://user-images.githubusercontent.com/78960121/208525909-e8d68c60-e60a-4b04-ae63-58888e4f622d.png)</kbd>


 #How to run
 
 -Clone the Repo:
 ```
 git clone https://github.com/swastik8750/NatWest-Assignment.git
 ```
 -Jump to the project:
 ```
 cd RPS_Game
 ```
 -Install the Requirements:
 ```
 pip install -r requirements.txt
 ```
 - Run the Server:
 ```
 python manage.py runserver
 ```
 -Run the TestCase:
  ```
 python manage.py test
 ```
 
 #Postman Documentation
[postman link](https://elements.getpostman.com/redirect?entityId=21892039-088c025a-c6f6-44bd-ad51-22ea61037009&entityType=collection)
