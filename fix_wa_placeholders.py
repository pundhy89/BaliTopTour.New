with open('src/views/AdminView.tsx', 'r') as f:
    content = f.read()

content = content.replace(
    'Gunakan placeholder berikut: <br/>',
    'Gunakan placeholder berikut: <br/>\\n                    <code className="text-fuchsia-600 font-bold bg-fuchsia-50 px-1 py-0.5 rounded">[NAMA_PEMESAN]</code> untuk nama pemesan (dari profil)<br/>'
)

content = content.replace(
    '`Halo, saya ingin memesan:\\nPaket: [NAMA_PAKET]\\nOpsi: [OPSI]\\nHarga: [HARGA]`',
    '`Halo, saya [NAMA_PEMESAN] ingin memesan:\\nPaket: [NAMA_PAKET]\\nOpsi: [OPSI]\\nHarga: [HARGA]`'
)

content = content.replace(
    '`Halo, saya tertarik dengan aktivitas:\\nAktivitas: [NAMA_AKTIVITAS]\\nPaket: [PAKET]\\nOpsi: [OPSI]\\nHarga: [HARGA]`',
    '`Halo, saya [NAMA_PEMESAN] tertarik dengan aktivitas:\\nAktivitas: [NAMA_AKTIVITAS]\\nPaket: [PAKET]\\nOpsi: [OPSI]\\nHarga: [HARGA]`'
)

content = content.replace(
    '.replace(\'[NAMA_PAKET]\',',
    '.replace(\'[NAMA_PEMESAN]\', \'Budi\').replace(\'[NAMA_PAKET]\','
)

content = content.replace(
    '.replace(\'[NAMA_AKTIVITAS]\',',
    '.replace(\'[NAMA_PEMESAN]\', \'Budi\').replace(\'[NAMA_AKTIVITAS]\','
)

with open('src/views/AdminView.tsx', 'w') as f:
    f.write(content)
