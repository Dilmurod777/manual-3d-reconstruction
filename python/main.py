import pandas as pd

df = pd.read_csv('./data/ShapeNetCore.v2/all.csv')
training_data = df[df['split'] == 'train']
testing_data = df[df['split'] == 'test']
print(len(training_data), len(testing_data))
