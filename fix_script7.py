import sys

with open('src/views/AdminView.tsx', 'r') as f:
    lines = f.readlines()

with open('/tmp/ImageUpload.tsx', 'r') as f:
    replacement = f.readlines()

new_lines = lines[:12] + replacement + lines[208:]

with open('src/views/AdminView.tsx', 'w') as f:
    f.writelines(new_lines)
