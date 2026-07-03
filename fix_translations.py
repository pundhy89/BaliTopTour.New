with open('src/data/translations.ts', 'r') as f:
    content = f.read()

insert = """
  payment_method: {
    id: 'Metode Pembayaran',
    en: 'Payment Method',
    zh: '付款方式'
  },
  payment_method_desc: {
    id: 'Pilih metode pembayaran untuk melihat informasi rekening',
    en: 'Select a payment method to view account information',
    zh: '选择一种付款方式以查看帐户信息'
  },
  view_more_tour: {
    id: 'View More Tour Packages',
    en: 'View More Tour Packages',
    zh: '查看更多旅游套餐'
  },
"""

content = content.replace("export const translations: Record<string, { id: string; en: string; zh: string }> = {", "export const translations: Record<string, { id: string; en: string; zh: string }> = {" + insert)

with open('src/data/translations.ts', 'w') as f:
    f.write(content)
