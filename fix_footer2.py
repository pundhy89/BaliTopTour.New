import re

def fix_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    content = content.replace("replace('[NAMA PEMESAN]', pemesan)}\n`;", "replace('[NAMA PEMESAN]', pemesan)}\\n`;")
    
    with open(filepath, 'w') as f:
        f.write(content)

fix_file('src/views/PackageDetailView.tsx')
fix_file('src/views/ActivityDetailView.tsx')
