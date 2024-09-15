# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 15:03:32 2024

@author: timho
"""

from pathlib import Path
import matplotlib.pyplot as plt

def count_files_by_extension(directory_path, extensions):
  """Counts files with specified extensions in a directory and its subdirectories.

  Args:
    directory_path: Path to the directory.
    extensions: List of desired file extensions.

  Returns:
    Dictionary containing extension and count pairs.
  """

  # Ensure the directory exists
  if not directory_path.exists():
    print(f"Directory {directory_path} does not exist.")
    return {}

  # Count files for each extension in the current directory and subdirectories
  counts = {}
  for extension in extensions:
    for file_path in directory_path.rglob(f"*{extension}"):
      if extension not in counts:
        counts[extension] = 0
      counts[extension] += 1

  return counts

# Example usage:
main_drive = "C:/"  #NOTE: must use a forward slash
folder_name = "python_stuff"
subfolder_name = "rrWork"
#I used these options for testing
#directory_path = Path(main_drive, folder_name, subfolder_name)
#directory_path = Path(main_drive, folder_name)
directory_path = Path(main_drive)

extensions = [".py",  ".jpg", ".pdf", ".ipynb" ,'.m', '.pas','.for','.f90', '.f', '.f03', '.cpp','.jmp','.jsl', 
             '.xls', '.xlsx', '.for', '.f90','.bas'    ]  # Adjust extensions as desired

print ('Beginning to process this target', directory_path)
file_counts = count_files_by_extension(directory_path, extensions)

print(file_counts)

#Plotting Section - Get a nice look at the distribution
# Separate the dictionary into two lists: keys and values
file_types = list(file_counts.keys())
values = list(file_counts.values())
# Create the horizontal bar chart
plt.figure(figsize=(4, 4))  #size can vary as wanted
plt.barh(file_types, values, color='skyblue')
plt.xlabel('Number of Files')
plt.ylabel('File Types')
#plt.title('File Types and Their Counts')
plt.title('File Types and Their Counts - No Python')
plt.grid(axis='x', linestyle='--', alpha=0.7)
# Show the plot
plt.show()    




