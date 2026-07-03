import re

def fix_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Replace [NAMA PEMESAN] with [NAMA_PEMESAN] during variable replacement just in case they typed it with a space
    content = content.replace(".replace('[NAMA_PEMESAN]', pemesan)", ".replace('[NAMA_PEMESAN]', pemesan).replace('[NAMA PEMESAN]', pemesan)")
    
    with open(filepath, 'w') as f:
        f.write(content)

fix_file('src/views/PackageDetailView.tsx')
fix_file('src/views/ActivityDetailView.tsx')
