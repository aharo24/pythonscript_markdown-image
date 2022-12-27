# import os
# import urllib.parse

# # Get a list of all the files in the 'z' directory
# image_paths = [f for f in os.listdir('z') if os.path.isfile(os.path.join('z', f))]

# # Open the Markdown file in append mode
# with open('Main.md', 'a') as f:
#   # Iterate over the list of file paths and write an image tag for each path to the file
#   for path in image_paths:
#     # Encode the file path using the quote() function
#     encoded_path = urllib.parse.quote(path)
#     f.write('![](z/%s)' % encoded_path)
#     f.write('\n')  # Add a newline character
#   # The file is automatically closed when the block ends





import os
import re
import urllib.parse

# Read the contents of the Markdown file into a string
with open('Main.md', 'r') as f:
  contents = f.read()

# Find all the image tags in the string using a regular expression
image_tags = re.findall(r'!\[\]\((.+?)\)', contents)

# Iterate over the list of image tags and modify the file paths to include the 'z' directory
for i, tag in enumerate(image_tags):
  file_path = tag.split('/')[-1]  # Get the file path from the tag
  encoded_path = urllib.parse.quote(file_path)  # Encode the file path
  new_tag = '![](z/%s)' % encoded_path  # Create the new image tag
  contents = contents.replace(tag, new_tag)  # Replace the old image tag with the new one

# Write the modified string back to the Markdown file
with open('Main.md', 'w') as f:
  f.write(contents)
