import pandas as pd
from cv_info_extractor import run

#print(run("CV1.pdf"))

# run("cv_test_2.pdf")

cvs = ['CV2']
res = []

for cv in cvs:
    res.append(run(cv + ".pdf"))

df = pd.DataFrame(res)
df.to_csv("output.csv", index=True)