A Python program that goes to a random Wikipedia article and selects the first link that redirects to another Wikipedia article. To run, just execute the .py file. Dependent on requests and bs4. pip install requests, pip install bs4 if you don't have these.

In theory, this should almost always lead to the Philosophy article being selected within a reasonable number of steps, probably less than 30?

The crux of the program is finding ways to avoid links that lead to weird places. eg. links leading to images or references rather than other articles.
Currently it does this somewhat well but it regularly selects the "Ancient Greek" or "Latin" articles because they often come up early in Wikipedia articles,
in reference to the article title's etymology or pronunciation. To avoid this, the program should include a way to avoid selecting links within parentheses,
(as these links always are).
