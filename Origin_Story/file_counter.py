# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:51:34 2024

@author: timho
"""
import os
from pathlib import Path
import matplotlib.pyplot as plt

# Define the base path as a Path object
my_path = Path('C:\\Python_Stuff\\')
#my_path =  Path('C:\\')

def count_files(rootDir, extensions):
  """
  Counts the number of files with specific extensions in a directory and its subdirectories.
  Args:
      rootDir: The root directory to start searching from.
      extensions: A list of extensions (including the dot) to count (e.g., [".txt", ".jpg"]).
  Returns:
      A dictionary mapping extensions to their counts.
  """
  file_counts = {ext: 0 for ext in extensions}
  for root, dirs, files in os.walk(rootDir):
    for file in files:
      if os.path.splitext(file)[1].lower() in extensions:
        file_counts[os.path.splitext(file)[1].lower()] += 1
        #print(file)  
  return file_counts

#Let's try it:
target_dir = my_path
extensions = [".py",  ".jpg", ".pdf", ".ipynb" ,'.m', '.for','.f90', '.f', 'f03', 'cpp','h','.jmp','.jsl' 
              ,'.xls', '.xlxs', '.for', '.f90','.bas'    ]  # Adjust extensions as needed
file_counts = count_files(target_dir, extensions)
print(f"Here is file count by extension for {my_path}:")
for ext, count in file_counts.items():
    print(f"{ext}: {count}")
    
#Plotting Section - Get a nice look at the distribution
# Separate the dictionary into two lists: keys and values
file_types = list(file_counts.keys())
values = list(file_counts.values())
# Create the horizontal bar chart
plt.figure(figsize=(4, 4))  #size can vary as wanted
plt.barh(file_types, values, color='skyblue')
plt.xlabel('Number of Files')
plt.ylabel('File Types')
plt.title('File Types and Their Counts')
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Show the plot
plt.show()    
