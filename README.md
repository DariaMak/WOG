Create a New Python Program: wog:
Begin by creating a new Python program named wog. This program will serve as the foundation for
your World of Games project.
• Develop Functions in app.py
In your app.py file, you will define two functions: welcome() and start_play().
o welcome()
This function takes a person's name as input and displays a personalized welcome message in
the following format:
This function has a person name as an input and print a string in the following layout:
“Hi [username] and welcome to the World of Games: The Epic Journey”
o start_play()
This function presents a list of available games to the user:
Please choose a game to play:
1. Memory Game - a sequence of numbers will appear for 1 second and you have to
guess it back.
2. Guess Game - guess a number and see if you chose like the computer.
3. Currency Roulette - try and guess the value of a random amount of USD in ILS
The user will select a game by entering the corresponding number. After choosing a game,
the function will prompt the user to select a difficulty level between 1 and 5:
• Implement the Main Execution in main.py
Create a new Python file named main.py to orchestrate the execution of your program. Your
main.py file should include the following lines:
This code imports the necessary functions from app.py, welcomes the user by name, and
prompts the user to select a game and difficulty level.
• Submission Details
Prepare a compressed zip file containing the following files:
o main.py
o app.py
Ensure the files are organized and structured appropriately within the zip archive.
Congratulations! You've completed the first level of World of Games. Take pride in your progress and get
ready to delve deeper into the exciting world of coding and game development.
Remember to reach out if you encounter any challenges or need further assistance. Best of luck on your
World of Games journey!


Guess Game – guess_game.py:
The Guess Game module is designed to initiate a new game by generating a random number
within a specified range of 0 to a variable named difficulty. The game involves receiving a number
input from the player based on the provided properties.
o The game function(play) will get the following properties:
§ Difficulty: Determines the range within which the secret number will be generated.
o Functions:
§ generate_number: Generates a random number between 0 and the specified difficulty,
saving it as the secret_number.
§ get_guess_from_user: Prompts the user to input a number within the range of 0 to the
difficulty and returns the entered number.
§ compare_results: Compares the generated secret number with the user's input and
determines if they match.
§ play: Initiates the game by calling the functions above and returns True if the user wins, and
False if the user loses.

• Currency Roulette Game – currency_roulette_game.py:
The Currency Roulette Game module utilizes a free currency API(package) to retrieve the current
exchange rate from USD to ILS (Israeli Shekel). Players are tasked with guessing the value of a newly
generated random number (between 1 to 100) in USD converted to ILS. The accuracy of their guess
depends on the game's difficulty level.
The allowed difference is found by subtracting the given difficulty level from 10 NIS. For instance, if
the difficulty level is 3, the acceptable difference is 10 - 3, which equals 7 NIS. Therefore, the
acceptable range is 7 NIS.
o The game function(play) will get the following properties:
§ Difficulty: Determines the range within which the secret number will be generated.
o Functions:
§ get_money_interval: Retrieves the current USD to ILS exchange rate and calculates an
interval for the correct answer based on the game's difficulty level.
get_guess_from_user: Prompts the user to input a guess for the converted value of a
specified amount in USD.
§ compare_results: Executes the game by employing the functions above, and returns True if
the user wins, and False if the user loses.
§ play: Executes the game by invoking the functions above and returns True if the user wins,
and False if the user loses.
• Memory Game - memory_game.py:
The Memory Game module aims to challenge players' memory by displaying a sequence of
random numbers (for example if the difficulty is 3 the random numbers can be: 100, 15, 80) for a
brief duration (0.7 seconds) and then prompting them to recall and input the displayed numbers.
The objective is to determine whether the player's input matches the original sequence.
o The game function(play) will get the following properties:
§ Difficulty: Determines the range within which the secret number will be generated.
o Functions:
§ generate_sequence: Generates a list of random numbers between 1 and 101, with a length
equal to the difficulty.
§ get_list_from_user: Prompts the user to input a list of numbers matching the length of the
generated sequence.
§ is_list_equal: Compares two lists to verify if they are identical, returning True if they match
and False otherwise.
§ play: Executes the game by invoking the functions above and returns True if the user wins,
and False if the user loses.

• Function Update
o Revise the function `start_play()` as follows: Upon receiving the user's selection of the
desired game and preferred difficulty level, the function will initiate the corresponding
game function with the specified difficulty. As an illustration, if the user opts for the
'memory_game' and selects a difficulty of 3, the `play()` function from the 'memory_game'
module will be invoked with a difficulty level of 3.
• Submission Details
Prepare a compressed zip file containing the following files:
o main.py
o app.py
o All games file.




Utils file – utils.py:
A general purpose python file. This file will contain general information and operations we need for
our games.
o Variables:
§ SCORES_FILE_NAME - A string representing a file name. By default “Scores.txt”
§ BAD_RETURN_CODE - A number representing a bad return code for a function.
o Functions:
§ Screen_cleaner - A function to clear the screen (useful when playing memory game or
before a new game starts).
• Score utils file – score.py:
A package that is in charge of managing the scores file. The scores file at this point will consist of
only a number. That number is the accumulation of the winnings of the user. Amount of points for
winning a game is as follows: POINTS_OF_WINNING = (DIFFICULTY X 3) + 5 Each time the user is
winning a game, the points he one will be added to his current amount of point saved in a file.
o Functions:
§ add_score: - The function’s input is a variable called difficulty. The function will try to read
the current score in the scores file, if it fails it will create a new one and will use it to save the
current score.

• Main scores file – main_score.py:
This file’s sole purpose is to serve the user’s score currently in the scores.txt file over HTTP with HTML.
This will be done by using python’s flask library.
o Functions:
§ score_server: This function will serve the score. It will read the score from the scores file and
will return an HTML that will be as follows
If the function will have a problem showing the result of reading the error it will return the
following:
• Function Update
o Change the function start_play() as follows: In case the user won the game, the function will
call the function called add_score to add the new score the user won to the score saved in
the Scores.txt function..
• Submission Details
Upload the project (as public) to GitHub and send me the link.
These game modules have been meticulously designed to provide an engaging and challenging
experience. Feel free to explore and enjoy the diverse gameplay offered by the World of Games!

e2e.py
This file will have two functions.
Functions
1. test_scores_service - it’s purpose is to test our web service. It will get the application
URL as an input, open a browser to that URL, select the score element in our web page,
check that it is a number between 1 to 1000 and return a boolean value if it’s true or not.
2. main_function to call our tests function. The main function will return -1 as an OS exit
code if the tests failed and 0 if they passed.
Dockerfile
The Dockerfile will package our flask project and run it as a command (set it in the CMD block).
The Dockerfile will also package inside it the Scores.txt file at: /Scores.txt .
Docker-compose.yml
This file will be used to manage our application. It will be used to build the application, run it and
push to docker hub.
Jenkinsfile
This will consist the jenkins pipeline that we do the following stages:
1. Checkout - checkout the repository.
2. Build - Build our docker image.
3. Run - will run our dockerized application. The application will expose the port 8777 on
localhost, and a dummy Scores.txt will be mounted to it in order to server the results for
the tests.
4. Test - With our e2e.py file it will selenium test our scores web service and fail the
pipeline if the tests failed.
5. Finalize - Will terminate our tested container and push to DockerHub the new image we
created.

