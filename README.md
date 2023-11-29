A Python program that goes to a random Wikipedia article and selects the first link that redirects to another Wikipedia article. To run, just execute the .py file. Dependent on requests and bs4. pip install requests, pip install bs4 if you don't have these.

In theory, this should almost always lead to the Philosophy article being selected within a reasonable number of steps, typically under 20.

The program also identifies when loops occur between articles. In other words, when one article links back to a previous article which links to it, creating an infinite loop. When this occurs, the program halts, the "Philsoohpy" article is unreachable and the loop will go on forever.
It may be interesting to investigate loops more, perhaps by removing the target article and just letting the program run until loops are found. How long on average does it take for a loop to occur? What is the longest loop we can find, or the longest we can go without looping, etc.

The crux of the program is finding ways to avoid links that lead to weird places. eg. links leading to images or references rather than other articles.
The program also avoid links of to articles such as "Latin Language" or "Arabic Language" because these articles are often linked at the beginning of articles in reference to the etymology of the article title.
They are avoided because such links always lead down very similar paths, leading to "Language" and then eventually "Philosophy" in the same way every time. They also typically have very little to do with the meaning of the article, other than with regard to etymology, so they are not particularly intersting.

The program may be edited to allow these language articles to be clicked, simply by removing line 53 in the function to filter links.
The program may also be edited to have a different target article. It may be interesting to see how quickly different articles can be reached. Do some articles have a lower average number of steps to reach them than "Philosophy"?
Perhaps the "Science" article. It is often reached before the "Philosophy" article.

In the future, I would like to create some kind of graphical interpretation of this program. A vertex for "Philosophy" in the middle, with different vertices representing different articles, and edges representing directional paths between them.
