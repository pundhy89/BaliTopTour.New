import re
with open('src/views/AdminView.tsx', 'r') as f:
    content = f.read()

content = content.replace("replace('\\[NAMA_PAKET\\]',", "replace('[NAMA_PAKET]',")
content = content.replace("replace('\\[OPSI\\]',", "replace('[OPSI]',")
content = content.replace("replace('\\[HARGA\\]',", "replace('[HARGA]',")
content = content.replace("replace('\\[NAMA_AKTIVITAS\\]',", "replace('[NAMA_AKTIVITAS]',")
content = content.replace("replace('\\[PAKET\\]',", "replace('[PAKET]',")

with open('src/views/AdminView.tsx', 'w') as f:
    f.write(content)
