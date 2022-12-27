# Open the Markdown file in write mode
with open('markdown_file.md', 'w') as f:
  # Write the image tag with the file path to the file
  f.write('![](z/Screenshot%202022-12-26%20at%202.11.18%20PM.png)')
  f.write('\n')  # Add a newline character
  f.write('![](z/Screenshot%202022-12-26%20at%202.39.39%20PM.png)')
  # The file is automatically closed when the block ends
