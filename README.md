This project was developped By Pobux And Deasel011
The goal of this project is to find safe investements on a daily basis on market shares defined by the user.

To achieve this goal, we are using a genetic machine learning algorithm. The needs for safe (near zero risk) investments will content themselves with a well trained genetic algorithm. It is true that a Neural Network could make much better investments with increased risk factor, but the goal of this project is merely to find safe patterns within the market itself.

Individuals are comprised of a start date, an end date, a profit and a select Title share.

To evaluate the fitness of an individual, we can simply look at the profit it made between the buy and the sell.

The mutations will happen on the different buy and sell times of an investment.

The populations are bound to many strict hour brackets inside which the individuals will have buys and sells.

The evolution of a population happens at the closure of a defined market, where fitness is calculated and children are bread.

This is a long term project and all data will be archived in a database.




Yahoo finance
pip install yahoo-finance
