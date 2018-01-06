# Lossy-Counter
Assignment 3 - Advanced Algorithms - MEI - UA

This is my third assignment for the Advanced Algorithms course of University of Aveiro,
for my Masters Degree in Computer Engineering.

NOTE: The code needs to be executed twice if you change the datastream size or run it for the first time. This is because the first time it searches for a text file with the datastream length desired. If it can't find it, it will create a new one and exit. You'll need to run it again in order to run the algorithm over that same datastream.

This code executes a lossy counter over a datastream of chars, ranging from 'a' to 'z' (low case alphabet) and returns the result.
On a first part, the code reads the values for the size of the datastream the user wants and tries to find a datastream with matching size. If successful, the code reads the datastream to a list and uses it as the algorithm's input. Otherwise, it will create a text file with the wanted size and fill it with random data and then proceed to read it This data is comprised of random chars taken from a small list, filled with the lower case alphabet, using different probability values for each char. These values are taken from a gamma probabilistic distribution, so that the datastream randomness doesn't vary too much with it's size.

After this, the algorithm outputs a dictionary with the char as the key, and a tuple with a counter and its delta. This dictionary is then used in the statistics part of the code, where it's compared against a normal counter function's results.

The workings of the algorithm are based on the following works:
- G. Cormode & M. Hadjieleftheriou, Finding the frequent items in  streams of data,  Commun . ACM, Vol. 52, N. 10, 2009
- G. Manku and R. Motwani. Approximate frequency counts over data streams. In International Conference on Very Large Data Bases, pages 346–357, 2002.
- G. S. Manku. Frequency counts over data streams.http://www.cse.ust.hk/vldb2002/VLDB2002-proceedings/slides/S10P03slides.pdf, 2002.
