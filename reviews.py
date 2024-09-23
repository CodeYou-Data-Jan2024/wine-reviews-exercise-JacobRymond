import pandas as pd

Reviews = pd.read_csv('data/winemag-data-130k-v2.csv.zip')

NewData = Reviews.groupby('country').agg({'country': 'count', 'points': 'mean'})

NewDataReNamed = NewData.rename(columns={'country': 'count'})

NewDataReNamed['points'] = NewDataReNamed['points'].round(1)

NewDataReNamed.to_csv('data/reviews-per-country.csv')

print(NewDataReNamed)