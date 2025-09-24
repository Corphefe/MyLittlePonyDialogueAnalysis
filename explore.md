This file contains answers to questions posed in Task 3

How big is the dataset?
    - The dataset has 36859 lines of dialogue. Each line details 4 column attributes.
    > wc -l clean_dialog.csv

What’s the structure of the data? (i.e., what are the field and what are values in them)
    - The 4 columns are: 'title' for episode name, 'writer' for episode writer, 'pony' for dialogue speaker, 'dialog' for the dialogue spoken (plus astage instructions). The lines are also organized in the order in which they are spoken.
    > head -1 clean_dialog.csv

How many episodes does it cover?
    - The script covers 197 episodes of the show. 
    > cut -d',' -f1 clean_dialog.csv | sort -u | wc -l

During the exploration phase, find at least one aspect of the dataset that is unexpected – meaning that it seems like it could create issues for later analysis.
    - I ran a script to count the number of times the protagonist "Twilight Sparkle" speaks and found that she speaks 4831 times. However, I also found that "Twlight" speaks 4835 times. There is a discrepency between the two so, for a bout 4 lines "Twilight" speaks. I am only on episode 2 of the show, so I do not know if there is another character names just Twilight, but I assume this is just short of "Twlight Sparkle" which could pose questions for out analysis. Also looking at the list of unique speakers, I see things like "Twilight and Fluttershy" which would nto have been counted in the firsr counting.
    > csvcut -c pony clean_dialog.csv | grep -c "Twilight Sparkle"
    > csvcut -c pony clean_dialog.csv | grep -c "Twilight"


For Task 4, the above command is what I used for each MAIN pony.
