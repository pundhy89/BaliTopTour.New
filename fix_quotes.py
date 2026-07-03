with open('src/views/AdminView.tsx', 'r') as f:
    content = f.read()

content = content.replace("'Halo, saya ingin memesan:\\nPaket: [NAMA_PAKET]\\nOpsi: [OPSI]\\nHarga: [HARGA]'", "`Halo, saya ingin memesan:\\nPaket: [NAMA_PAKET]\\nOpsi: [OPSI]\\nHarga: [HARGA]`")
content = content.replace("'Halo, saya tertarik dengan aktivitas:\\nAktivitas: [NAMA_AKTIVITAS]\\nPaket: [PAKET]\\nOpsi: [OPSI]\\nHarga: [HARGA]'", "`Halo, saya tertarik dengan aktivitas:\\nAktivitas: [NAMA_AKTIVITAS]\\nPaket: [PAKET]\\nOpsi: [OPSI]\\nHarga: [HARGA]`")

# and fix the physical newlines inside '' if any
import re
content = re.sub(r"'Halo, saya ingin memesan:\nPaket: \[NAMA_PAKET\]\nOpsi: \[OPSI\]\nHarga: \[HARGA\]'", "`Halo, saya ingin memesan:\\nPaket: [NAMA_PAKET]\\nOpsi: [OPSI]\\nHarga: [HARGA]`", content)
content = re.sub(r"'Halo, saya tertarik dengan aktivitas:\nAktivitas: \[NAMA_AKTIVITAS\]\nPaket: \[PAKET\]\nOpsi: \[OPSI\]\nHarga: \[HARGA\]'", "`Halo, saya tertarik dengan aktivitas:\\nAktivitas: [NAMA_AKTIVITAS]\\nPaket: [PAKET]\\nOpsi: [OPSI]\\nHarga: [HARGA]`", content)


with open('src/views/AdminView.tsx', 'w') as f:
    f.write(content)
