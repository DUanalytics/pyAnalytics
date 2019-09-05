#Topic ---- MB - apyori
#%%%
from apyori import apriori

transactions = [    ['beer', 'nuts'],   ['beer', 'cheese'], ]
results = list(apriori(transactions))
results

#%%%
First, prepare input data as tab-separated transactions.

Each item is separated with a tab.
Each transactions is separated with a line feed code.
Second, run the application. Input data is given as a standard input or file paths.

Run with python apyori.py command.
If installed, you can also run with apyori-run command.


#%%%

