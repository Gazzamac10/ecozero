import pandas as pd

# Create a sample Pandas DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': ['Apple', 'Banana', 'Cherry', 'Date', 'Fig'],
    'C': [0.1, 0.2, 0.3, 0.4, 0.5],
    'D': [True, False, True, False, True],
    'E': [10, 20, 30, 40, 50],
}

df = pd.DataFrame(data)


print (df)

# Specify the output JSON file path
json_file_path = 'output.json'

# Save the DataFrame as a JSON file
#df.to_json(json_file_path, orient='records', lines=True)

print(f"Data has been saved to {json_file_path}")
