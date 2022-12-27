import os
import urllib.parse

# Get a list of all the files in the 'z' directory
image_paths = [f for f in os.listdir('z') if os.path.isfile(os.path.join('z', f))]

# Open the Markdown file in append mode
with open('Main.md', 'a') as f:
  # Iterate over the list of file paths and write an image tag for each path to the file
  for path in image_paths:
    # Encode the file path using the quote() function
    encoded_path = urllib.parse.quote(path)
    f.write('![](z/%s)' % encoded_path)
    f.write('\n')  # Add a newline character
  # The file is automatically closed when the block ends
