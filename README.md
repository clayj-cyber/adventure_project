# COMS W3132 Individual Project
## Author
Clayton Boyce cjb2270@columbia.edu
## Project Title
Dungeon Maester, A Turn-based Combat Game
## Project Description

My project aims to implement the Python knowledge I have garnered through this course and E1006. I plan to create an inventory system and a combat system with different pathways depending on the player's chosen role. There will be three paths that a player can choose, and each path will have a different string of scenarios that the player can navigate through. Certain decisions will invoke different probability rolls which will affect the player's trajectory in a positive or negative fashion. The main aspect of this game will be the pseudo-random event system which will be triggered by a simple "Ready to Adventure? Y/N". Once that happens, a story will begin and a list of events that will carry out. Depending on how far the player gets in the interative list of events, they will either lose the game or win in whatever role they choose to embody. There is a dungeon system that adventurers will be able to enter, gather loot, and fight monsters to get stronger. That is going to be the core of this project.

My motivation for this project is a mix of Pokémon and my love for the Song of Ice and Fire book series. The problem I want my project to solve is combining my artistic capacities with my more technical way of thinking. I want to be able to code a program that marries my creativity and ability to apply that creativity in a quantitative way. I believe my project might be interesting to others because it will hopefully allow to think strategically about which decisions they make and how they make them. I want the game to feel like an interactive puzzle, one that is a little luck but mostly intuition.

## Timeline
*To track progress on the project, we will use the following intermediate milestones for your overall project. Each milestone will be marked with a tag in the git repository, and we will check progress and provide feedback at key milestones.*

| Date            | Milestone Description                                                                 | Deliverables                              | Git Tag     |
|-----------------|---------------------------------------------------------------------------------------|-------------------------------------------|-------------|
| **July 15**     | Submit project description                                                            | README.md                                 | proposal    |
| **July 17**     | Update project scope/direction based on instructor/TA feedback                        | README.md                                 | approved    |
| **July 22**     | Basic project structure with empty functions/classes (incomplete implementation), architecture diagram | Source code, comments, docs               | milestone1  |
| **August 2**    | More or less complete implementation. The goal is to have something you can share with others. | Source code, unit tests                    | milestone2  |
| **August 9**    | Complete implementation. Final touches (conclusion, documentation, testing, etc.)     | Source code, Conclusion (README.md)       | conclusion  |

*The column Deliverables lists deliverable suggestions, but you can choose your own, depending on the type of your project.*

## Requirements, Features and User Stories
The problem I'm solving is creating a project that fully implements all of the things that I love about turn-based games. Magic, special swords, boss fights, and unique monsters that have their own pseudo-artificial intelligence (is that a double-negative? haha). Currency, loot, etc. 

1. Player Character Management
Feature: The player can create and manage a character with various attributes such as strength, defense, magic power, stamina, and more.
User Story: As a player, I want to create a character with customizable attributes so that I can tailor the gameplay experience to my preferred style, whether it be combat-focused or magic-focused.

2. Turn-Based Combat System
Feature: The game features a turn-based combat system where the player and monsters take turns to attack, use abilities, and defend.
User Story: As a player, I want to engage in strategic combat where I can choose to attack, defend, or use special abilities, so that I can outsmart the monsters and progress through the game.

3. Monster Encounters
Feature: The game generates random monster encounters as the player progresses through different levels of the dungeon.
User Story: As a player, I want to encounter a variety of monsters with different abilities and strengths, so that each battle feels unique and challenging.

4. Inventory and Equipment System
Feature: The game includes an inventory system where the player can manage items, such as potions, weapons, and rings. Players can also equip or change their equipment during the game.
User Story: As a player, I want to collect, use, and manage items and equipment, so that I can improve my character's abilities and survive longer in the dungeon.

5. Leveling and Experience System
Feature: Players earn experience points (XP) from battles, and when enough XP is accumulated, the player levels up, improving their stats and abilities.
User Story: As a player, I want to earn experience from battles and level up my character, so that I can face tougher challenges as I progress deeper into the dungeon.

6. Special Abilities and Magic System
Feature: Players can use a variety of special abilities and spells during combat, which can have various effects such as dealing damage, healing, or applying status effects.
User Story: As a player, I want to use special abilities and magic spells during combat, so that I can employ different strategies to defeat monsters.

7. Dungeon Exploration
Feature: The game features a multi-level dungeon that the player must explore, with each level presenting new challenges, monsters, and potential rewards.
User Story: As a player, I want to explore different levels of the dungeon, each with its own unique challenges, so that I can experience a sense of progression and discovery.

8. Random Loot and Rewards System
Feature: Upon defeating monsters or clearing dungeon levels, players can receive random loot such as weapons, rings, potions, and other items.
User Story: As a player, I want to find and collect random loot from defeated enemies and dungeon exploration, so that I can improve my character and prepare for tougher battles.

9. Puzzle and Boss Challenges
Feature: The game includes special puzzle rooms and boss battles that provide significant challenges and rewards.
User Story: As a player, I want to encounter and solve puzzles or defeat powerful bosses, so that I can earn rare rewards and experience a sense of achievement.

10. Save and Load Game Progress (tentative)
Feature: The game allows players to save their progress and load it later, ensuring that they can continue their adventure from where they left off.
User Story: As a player, I want to be able to save my game and continue later, so that I don't have to restart my progress if I need to stop playing. (This may be the hardest thing I'll have to try to implement!)

11. Required Software
Python 3.x (required to run the game)

## Technical Specification
*Detail the main algorithms, libraries, and technologies you plan to use. Explain
your choice of technology and how it supports your project goals.*

Using time and random as the main libraries which are built-in Python libraries. I used built-in libraries because they are easy to implement. This also ensures the game is lightweight and can run without outside dependencies.

Combat System:

The combat system is a turn-based algorithm that alternates between the player’s and the monster’s actions. This is designed to provide a strategic gameplay experience where the player must consider their moves carefully.
The system handles different types of attacks (physical, magical), special abilities, and status effects (e.g., burning, freezing).

Leveling System:

The leveling system uses a mathematical formula (exponential growth) to determine the experience points needed for the player to advance to the next level. This ensures a progressively challenging experience as the player advances through the game.
Inventory Management:

The game uses a dictionary-based system to manage the player's inventory, including potions, weapons, and other items. The algorithm supports item addition, usage, and limits on the number of items the player can carry.

## System or Software Architecture Diagram
*Include a block-based diagram illustrating the architecture of your software or
system. This should include major components, such as user interface elements,
back-end services, and data storage, and show how they interact. Tools like
Lucidchart, Draw.io, or even hand-drawn diagrams photographed and uploaded are
acceptable. The purpose of the diagram is to help us understand the architecture of
your solution. Diagram asthetics do not matter and will not be graded.*

User Interface (UI)

Component: Command Line Interface (CLI)
Description: The UI is a text-based command line interface where the player interacts with the game. Players input commands and receive feedback through the CLI.
Game Logic

Component: Main Game Loop (main.py)
Description: This component controls the flow of the game, handling player input, progressing through the game’s story, and managing state transitions (e.g., from exploration to combat).
Player Management

Component: Player Class (playerplayer.py)
Description: Manages the player’s character, including attributes like health, magic, inventory, and level progression. Handles player-specific actions, such as attacking, using items, or equipping gear.
Monster Management

Component: Monster Class (monstermonster.py)
Description: Manages monster behaviors, attributes, and interactions with the player during combat. Handles spawning of monsters, their actions in combat, and their defeat.
Combat System

Component: Combat Logic (dungeondungeon.py)
Description: Manages turn-based combat between the player and monsters. Handles the execution of attacks, spells, and abilities, as well as the application of damage and status effects.
Inventory and Equipment

Component: Inventory System (playerplayer.py)
Description: Manages the player’s inventory, including adding, removing, and using items. Handles the logic for equipping weapons and rings, as well as using consumables like potions.
Dungeon Exploration

Component: Dungeon Class (dungeondungeon.py)
Description: Manages the player’s exploration of the dungeon. Controls the generation of dungeon levels, encounters with monsters, and special events like puzzles or boss fights.
Special Abilities and Magic

Component: Abilities and Magic System (player/abilities.py)
Description: Manages the special abilities and magic spells that players and monsters can use. Includes logic for spell effects, cooldowns, and the impact on gameplay.
Data Storage (Optional)

Component: Save/Load System
Description: If I am to have this implemented, this component would handle saving and loading the game’s state to and from a file. This includes the player's progress, inventory, and current position in the dungeon.

![output](https://github.com/user-attachments/assets/ef4a2e9a-27d9-4528-bfc7-96fc0f40e2fd)

## Development Methodology
*Describe the methodology you'll use to organize and progress your work.*
*First, describe your plan for developing your project.*

I have a timeline on my notepad that I've been using, but that may not be very professional. I'm still learning github so I have been somewhat conservative in how I've used it. I may try to use the calendar function for adding my project plans, but otherwise I am content with my notepad app until I get more comfortable with the github framework. 

I have been using repl.it to test my code's behavior in the console, but I am not planning to use any specific libraries or frameworks. This project will be fully text-based since I am still relatively new to coding. (I decided to start consistently coding earlier this year!)

## Potential Challenges and Roadblocks
*Identify any potential challenges or roadblocks you anticipate facing during the
development of your project. For each challenge, propose strategies or solutions
you might use to overcome them, which may include getting help from the
TAs/instructor. This could include technical hurdles or learning new technologies.*

A few potential challenges and roadblocks I thought about initially were creating a functional inventory that allows the player to store items in it that stack. The other challenge I knew I'd have was surrounding a 'moveset' implementation. After researching on YouTube and other github repositories, I was able to find a way to implement it. I used AI to doublecheck any mistakes I made on the way. AI was a great way for me to overcome roadblocks when I was unable to implement code properly. Having a code skeleton for a function I was struggling to create and giving AI a prompt that built off the code I did make made my project progress grow exponentially. 

## Additional Resources
https://www.youtube.com/watch?v=pSYeMdIrKQw
https://stackoverflow.com/
https://www.reddit.com/r/learnprogramming/
openAI resources via chatGPT for finding mistakes and adding comments for correctly explaining some aspects of the code

## Conclusion and Future Work
*Wrap up your project description with any final thoughts, expectations, or goals
not covered in the sections above. Also briefly discuss potential future work,
i.e., what could be done next to improve the project.*

From the Conclusion release:

I expect for the program to run OK. I have fun playing the game, and I think that's what's most important. I did not receive feedback for the project, but I'm hopeful that it will be well-received. I did not run into any performance issues last time I ran dungeongame.py this afternoon, but I implemented a lot of different functions and methods so I'm sure there are some bugs I didn't find. I tried to create a multiple file directory but ran into a few issues with the code working together. I opted for a longer program but I think it's organized enough for someone to read and understand it if they know how to code. 

I am happy with how I designed the game, even if it's not fully-realized in terms of how I wanted to approach it. I would love to create 8-bit characters that can be encountered in an early Pokémon-style of play. I think if I had another three months to develop this I could get to that. I have never done that before, so I know I would probably need a lot of time to do so. Even then, it may not be done. I think the visual aspect would improve this project tremendously. The code, although imperfect, is from my own mind and I executed it as intended. I have no major qualms about it. I am happy with the progress I made, but any feedback will be helpful for my advancement. I did try to implement a tree data structure for the save/load function in the Dungeon Class, but I ran into too many issues to confidently implement it. If I were start this project over, I would definitely try to add the save / load game functionality earlier so it would be easier to streamline it into my code. I would also find ways to use a multiple file directory more efficiently. Separating my code after writing it all proved fruitless toward that effort.

