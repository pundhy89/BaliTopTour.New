with open('src/views/AdminView.tsx', 'r') as f:
    content = f.read()

content = content.replace('{/* Printer, MessageCircle & Struk */}', '{/* Printer & Struk */}')
content = content.replace('<Printer, MessageCircle size={18} className="stroke-[2.2px]" />', '<Printer size={18} className="stroke-[2.2px]" />')
content = content.replace('Printer, MessageCircle & Struk', 'Printer & Struk')
content = content.replace('<Printer, MessageCircle size={15} className="text-teal-600" />', '<Printer size={15} className="text-teal-600" />')
content = content.replace('Pengaturan Struk & Printer, MessageCircle Thermal', 'Pengaturan Struk & Printer Thermal')

with open('src/views/AdminView.tsx', 'w') as f:
    f.write(content)
