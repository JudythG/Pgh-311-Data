Coding challenge:

    Visit the WPRDC 311 data home page at the WPRDC. Study the data dictionary. Learn about the 311 program if you don't about their system.
    Extract a research question about the data that can be answered by processing the 300,000+ entries in their central data. Examples include:
        * Budgets cuts are coming! Which public works district seems to have the lightest load of 311 requests? The Heaviest? How would you redirect resources between districts?
        * Which submission mechanism is used most for which types of complaints?
        * Which neighborhood receives the most requests? Can we make any inferences between number of requests and the quality of life in that neighborhood?
    Write a program in python to answer these questions by ingesting the entire set of 311 data posted to the WPRDC. HINT: Start with a small subset of the data, like this random extraction of a few dozen rows.
    Come prepared to share your results!

The above is my assignment for a Python 2 class at CCAC.
I noticed that each of his examples has us picking a column from the 311 Pgh data file
and counting how many times each different data field occurs in that column. So I wrote
a program that allows the user to pick a field at run-time, via user input. 

In addition, I was interested in data from two columns. For example, instead of looking
at just response types, how do response types vary across neighborhoods. Again, this
is implemented with user input.




