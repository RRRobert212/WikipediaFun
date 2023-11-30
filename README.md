A Python program that opens a random Wikipedia article and selects the first link that redirects to another Wikipedia article. The process repeats until a loop is found or the Philosophy article is reached.

To run, just execute the .py file. Dependent on requests and bs4. pip install requests, pip install bs4 if you don't have these.

In theory, the Philosophy article should be opened within a reasonable number of steps, typically under 20.

The program also identifies when loops occur between articles. I.e. when one article links back to a previous article which links to it, creating an infinite loop. This halts the program as otherwise an infinite loop occurs and the "Philsoohpy" article is unreachable.
It may be interesting to investigate loops more, perhaps by removing the target article and just letting the program run until loops are found. How long on average does it take for a loop to occur? What is the longest loop we can find, or the longest we can go without looping, etc.

The crux of the program is finding ways to avoid links that lead to weird places. eg. links leading to images or references rather than other articles.
The program also avoid links to articles such as "Latin Language" or "Arabic Language" because these articles are often linked at the beginning of articles in reference to the etymology of the article title.
They are avoided because such links often lead down very similar paths (through "Language" for example). They also typically have little to do with the meaning of the article, other than with regard to etymology, so they are not particularly intersting.

The program may be edited to allow these language articles to be selected by changing the list of articles which are hardcoded exclusions (the list: excluded_hrefs). Other articles can also be excluded in this way.
The program may also be edited to have a different target article. It may be interesting to see how quickly different articles can be reached. Do some articles have a lower average number of steps to reach than "Philosophy"?
Perhaps the "Science" article. It is often reached before the "Philosophy" article.

In the future, I would like to create some kind of graphical interpretation of this program. A vertex for "Philosophy" in the middle, with different vertices representing different articles, and edges representing directional paths between them.
