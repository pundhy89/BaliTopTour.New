import re

def fix_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Replace receipt_footer logic to include [NAMA_PEMESAN] replacements
    target = r"receipt \+= \`\$\{settings\.receipt_footer\}\\n\`;"
    replacement = "receipt += `${settings.receipt_footer.replace('[NAMA_PEMESAN]', pemesan).replace('[NAMA PEMESAN]', pemesan)}\\n`;"
    
    content = re.sub(target, replacement, content)
    
    with open(filepath, 'w') as f:
        f.write(content)

fix_file('src/views/PackageDetailView.tsx')
fix_file('src/views/ActivityDetailView.tsx')
