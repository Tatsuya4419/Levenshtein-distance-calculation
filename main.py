import Levenshtein
import itertools
import pandas as pd
import os

strings = ["今川焼き", "今川義元", "武田信玄", "信玄餅", "武田信玄と今川義元", "武田信玄と上杉謙信"]

def calc_dist(str):
    r = pd.DataFrame()
    for tpl in list(itertools.combinations(str, 2)):
       dist = Levenshtein.distance(tpl[0], tpl[1]) / max(len(tpl[0]), len(tpl[1]))
       r.at[tpl[0], tpl[1]] = dist
       r.at[tpl[1], tpl[0]] = dist
    r = r.sort_index(ascending=False).sort_index(ascending=False, axis=1)
    return(r)

result = calc_dist(strings)
print(result)

if os.path.isdir("./outputs") != True:
    os.makedirs("./outputs")

result.to_csv("./outputs/result.csv", encoding="utf-8")