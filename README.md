# Guess the Word Game

Welcome to the Guess the Word game! This is an interactive CLI-based game where players try to guess a hidden word, one letter at a time. Each word is a type of fruit, and players must guess the word within a limited number of attempts. The difficulty level determines how many attempts players have to guess each word.

![image](https://github.com/user-attachments/assets/e05af144-4875-4b0f-ac7a-ef9ad4150ad2)

## Game Description
In Guess the Word, players are presented with a word hidden by underscores. They must guess the letters of the word correctly to reveal it. Players are given a certain number of attempts to guess the word, which depends on the difficulty level chosen.

## Gameplay

Players have a limited number of attempts based on the chosen difficulty level:
Easy: 8 attempts
Hard: 6 attempts
Extreme: 4 attempts

![image](https://github.com/user-attachments/assets/247e5351-f977-431d-9a0d-d0279c5dddd3)


Players guess one letter at a time. After each guess, the game informs players if their guess was correct or incorrect.
If the guess is correct, the corresponding letter is revealed in the word. If the guess is incorrect, an attempt is deducted.
Attempts:

![image](https://github.com/user-attachments/assets/28af2ba0-f647-44a8-8c30-65c948aa9437) ![image](https://github.com/user-attachments/assets/b7d90e2c-3098-4ccc-bdec-f0d8c57449d2) ![image](https://github.com/user-attachments/assets/b92a93aa-6d6c-470e-adf3-196f762e0d5d)

If players use up all their attempts without guessing the word correctly, the game reveals the word and moves on to the next word in the list. If the player guesses correctly it is revealed they guessed the word correctly and it movs onto the next word.The game continues with a new word until all words have been guessed.

![image](https://github.com/user-attachments/assets/74168d08-ec92-43d7-ac12-c7141f595313) ![image](https://github.com/user-attachments/assets/3a041baf-4045-4687-a434-63f6dc8a8e93)

## End of the Game
At the end of each game session, players are presented with a summary of their performance and given the option to continue or exit. Here’s how it works:

Score Presentation:

Once the game is over, players are shown their final score, which is the number of words they correctly guessed during the game.
The score is displayed by the total number of words that were available to guess and how many the users got right out.

![image](https://github.com/user-attachments/assets/87d9b825-91df-43a2-a48f-0da84351bb7e)


### Play Again Option:

After the score is presented, players are asked if they would like to play another round.
They can choose to start a new game or exit. If they choose to play again, the game resets with a new set of words and the chosen difficulty level.
Example prompt:

![image](https://github.com/user-attachments/assets/94f2c206-4b93-4c6d-9af0-a4473d919544)



### Game Exit:

If players decide not to play again, the game thanks them for playing and exits. A friendly farewell message is displayed.
Example:

![image](https://github.com/user-attachments/assets/a52468b0-26da-408b-b20d-08911a9ac29c)


# Design

## Color and Formatting

To make the game more visually appealing and engaging, the colorama library was utilized. This library allows for the addition of color to terminal text, which helps to:

### Highlight Important Information: 

Key elements such as instructions, success messages, and errors are displayed in different colors to draw the player's attention.

![image](https://github.com/user-attachments/assets/cfdb7ad7-329b-4338-8dc5-2a9270d59059)


### Differentiate Feedback: 
Correct and incorrect guesses are clearly distinguished using colors, enhancing readability and user interaction.

![image](https://github.com/user-attachments/assets/3e304739-0ed9-4702-9d9d-ecb911b05fd4) ![image](https://github.com/user-attachments/assets/d0a97a3c-4575-4b90-a388-b76f52f89100)



## Spacing and Layout: 
Strategic use of spacing between different sections of text and game prompts helps to improve readability. For example, extra lines are added between the game's description, user input prompts, and feedback messages to ensure a clear and pleasant visual separation.

## Instructional Prompts:
Clear and concise prompts guide the player through the game. Instructions are provided before each game round to ensure that users understand the rules and objectives.


## Progress Updates: 
During gameplay, the state of the word being guessed is updated to reflect correct and incorrect guesses and also the users attemptr remaining is always informed to the users as they progress. This real-time feedback helps players stay engaged and informed about their progress.

![image](https://github.com/user-attachments/assets/9324ae21-07da-49ec-bede-ea24f25f635f)


## End-of-Game Information: 
At the end of each game session, players receive a summary of their performance, including the number of correctly guessed words, and are given an option to play again. This feedback loop maintains player engagement and encourages replayability.

# Authentication and Input Validation

To ensure a smooth and error-free gameplay experience, the Guess the Word game incorporates several authentication and input validation mechanisms. These mechanisms are designed to handle user inputs appropriately and guide the user through a consistent and error-free experience:

### Difficulty Level Selection
When choosing the difficulty level, the game verifies that the user inputs a valid option:

Accepted Inputs: Users must enter '1', '2', or '3' to select the difficulty level. Each input corresponds to a predefined number of attempts:
1 for Easy (8 attempts)
2 for Hard (6 attempts)
3 for Extreme (4 attempts)
If the user enters an invalid choice, an error message is displayed, and the user is prompted to enter a valid option again. This ensures that only acceptable inputs are processed.

![image](https://github.com/user-attachments/assets/7b3b91e7-a998-4b0f-9dde-417142e65da5)

### Input Validation:
During gameplay, when users are guessing letters for the hidden word:
Users must enter a single letter, and only alphabetic characters are accepted. The game checks that the input meets these criteria:

![image](https://github.com/user-attachments/assets/92c1eb09-9d5f-4686-8bff-08e614562c7e) ![image](https://github.com/user-attachments/assets/917b88d5-9e55-4b69-8e92-b5c79dbf43e1)



### Repeated Guesses
To prevent repeated guessing of the same letter users are informed if they ahve aready guessed the letter even if the letter guessed is an incorrect letter:

![image](https://github.com/user-attachments/assets/f0840e56-0a6e-41f7-a934-c2b4153dbe40)


### Replay Option
When the game ends, players are given the option to play again:

Accepted Inputs: Users must enter 'y' or 'n' to decide whether to play another round:
'y' to play again
'n' to exit the game
If the user enters anything other than 'y' or 'n', the game will prompt them again until a valid input is received. This prevents unintended exits or invalid replay attempts.

![image](https://github.com/user-attachments/assets/d37c2653-5d5f-4e39-bef2-83bb34af18d9)

# Testing and Quality Assurance

## Manual Testing

The primary method of testing for Guess the Word was manual testing. This approach involved running the game multiple times and engaging with it under various scenarios to identify any potential issues. Here’s how the manual testing was conducted:

### User Testing: 
Friends and I played the game extensively to test different aspects, including:

#### Difficulty Selection: 
Ensuring the correct number of attempts was assigned based on the selected difficulty level.

#### Input Validation: 
Testing how the game handled different types of inputs, including valid and invalid guesses, repeated letters, and incorrect difficulty selections.
#### Game Flow: 
Checking the overall game flow, including the game ending conditions, score calculation, and replay functionality.

#### Error Handling: 
Observing how the game responded to edge cases and invalid inputs to ensure appropriate error messages and gameplay behavior.
This hands-on approach allowed us to identify and address any usability issues and ensure the game provided a smooth and enjoyable experience.

### Unit Testing
In addition to manual testing, initial efforts were made to implement automated unit tests. However, these were later removed due to the following reasons:

#### Test Execution: 
The unit tests were primarily designed to run the game and validate its functionality. They consistently passed 4/4 tests but you had to play the game even in the test.py file to get the result so I decided to remove the automated tests.

Despite the removal of automated unit tests, the core functionality and robustness of the game were ensured through thorough manual testing and continuous feedback from friends and colleagues

# Known Issues

While Guess the Word has been extensively tested and refined, there are a few known issues that will not be addressed. These bugs do not impact the core gameplay but may affect the overall user experience in specific scenarios. Here’s a brief overview:

### CLI Usability After Game Ends
Once users decide not to replay the game, the CLI (Command Line Interface) becomes unusable.

After the user chooses not to play again, the game ends, but the terminal may not reset properly. This can result in the CLI not accepting new inputs or appearing to hang.

#### Impact: 

This issue affects users who wish to continue interacting with the terminal after the game has concluded. While it does not affect the functionality of the game itself, it may inconvenience users who need to manually close and reopen the terminal.

#### Reason for Not Fixing: 
Due to the constraints of the current implementation and the nature of the CLI environment, fixing this issue would require significant changes to how the game interacts with the terminal. Given the low impact on gameplay and the technical challenges involved, this issue was not addressed.

### Difficulty Level Selection When Replay Option is Chosen
Users are unable to choose a difficulty level when they decide to play again after completing a game.

Description: When a user opts to replay the game, they are not prompted to select a difficulty level again. Instead, the game proceeds with the same difficulty level that was set during the previous game.

#### Impact: 

This issue limits the ability of users to change the difficulty level between games, which can be frustrating if they wish to try a different difficulty setting.

#### Reason for Not Fixing:
The current game flow design does not easily support difficulty selection upon replay. Addressing this would require redesigning the game’s state management and difficulty selection logic. Given the scope of changes needed and the relatively low impact on overall gameplay, this issue will not be resolved.

# How to Fork and Clone the Repository

If you’d like to contribute to this project or just experiment with it on your own, follow these steps to fork and clone the repository:

### Forking the Repository
Navigate to the Repository: Go to the GitHub page of the repository.
https://github.com/cmoynan/Guess-The-Word-2

Fork the Repository: Click on the "Fork" button in the upper right corner of the page. This will create a copy of the repository under your GitHub account.

Ths is how to fork but due to me not being a memeber of any organistions forking is not possible at present. 

### Cloning the Repository
Navigate to the forked repository on GitHub. Click on the "Code" button and copy the URL under "Clone with HTTPS" or "Clone with SSH", depending on your preference.

Open Your Terminal: Open a terminal or command prompt on your local machine.

Run the Clone Command: Use the git clone command followed by the copied URL:

#### git clone https://github.com/cmoynan/Guess-The-Word-2


# Deployment:

Created a new Heroku app by selecting new app and adding the name of my app and chose Europe forthe region

Set the Buildpacks to python and Nodejs in that order.

![image](https://github.com/user-attachments/assets/def3a91d-1aa0-4124-9e5a-d8328c60d609)


Added port 8000 to the config vars

![image](https://github.com/user-attachments/assets/0e83550f-eee4-4bb9-8c97-1e7248fdd99f)


Linked the Github repo to the Heroku app

![image](https://github.com/user-attachments/assets/14e850e9-5ae1-4aea-839f-fe5849032de1)


https://github.com/cmoynan/Guess-The-Word-2

Deployed the app by clicking deploy branch in Heroku deployment

The live app website is https://guesstheword89-bbd1e8207f7c.herokuapp.com/



