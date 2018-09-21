import os
import random

csv_files = 'CSV_Database_of_First_Names.csv'

# For simplicity not performance we read the whole file twice

with open(csv_files) as f:
    len_file = len(f.readlines()) - 1

sample = random.sample(range(1, len_file), 100)

with open(csv_files) as f:
    with open('schema_file.csv', 'w') as schema:
        schema.write('sourceAttributeName;destinationAttributeName;sourceAttributeValue;destinationAttributeValue\n')
        lines = f.readlines()
        for i, line_index in enumerate(sample):
            name = lines[line_index].replace(';\n','')
            schema.write(f'ID;Name;{i};{name}\n')