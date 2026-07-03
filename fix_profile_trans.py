with open('src/views/ProfileView.tsx', 'r') as f:
    content = f.read()

content = content.replace(
    'Metode Pembayaran\n          </h4>',
    '{translate(\'payment_method\', language)}\n          </h4>'
)

content = content.replace(
    'Pilih metode pembayaran untuk melihat informasi rekening\n          </p>',
    '{translate(\'payment_method_desc\', language)}\n          </p>'
)

with open('src/views/ProfileView.tsx', 'w') as f:
    f.write(content)
