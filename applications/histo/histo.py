# method on a dictionary might be useful
# it's possible for .sort() to sort on multiple keys at once
# negatives might help where reverse won't
# you can print a variable field width in an f-string with nested braces, like so {x:{y}}

import pandas 
from collections import Counter

letter_counts = Counter(robin.txt)
df = pandas.DataFrame.from_dict(letter_counts, orient='index')
df.plot(kind='bar')