import re
with open('src/views/AdminView.tsx', 'r') as f:
    content = f.read()

content = content.replace("Halo, saya ingin memesan:\\\\nPaket", "Halo, saya ingin memesan:\\nPaket")
content = content.replace("Halo, saya tertarik dengan aktivitas:\\\\nAktivitas", "Halo, saya tertarik dengan aktivitas:\\nAktivitas")

with open('src/views/AdminView.tsx', 'w') as f:
    f.write(content)
