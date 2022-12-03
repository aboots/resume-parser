import pandas as pd
from cv_info_extractor import run

# cvs = ['CV1', 'CV2', 'CV3']
cvs = ['CV4']
res = []

for cv in cvs:
    res.append(run(cv + ".pdf"))

df = pd.DataFrame(res)
df.to_csv("output.csv", index=True)
