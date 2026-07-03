with open('src/views/ProfileView.tsx', 'r') as f:
    content = f.read()

target = "const [selectedBank, setSelectedBank] = useState<string | null>(null);"
insert = """  const hasBca = !!(settings.bank_bca_number || settings.bank_bca_logo);
  const hasSeabank = !!(settings.bank_seabank_number || settings.bank_seabank_logo);
  const hasPaypal = !!(settings.bank_paypal_number || settings.bank_paypal_logo);
  const hasAnyBank = hasBca || hasSeabank || hasPaypal;
"""

new_content = content.replace(target, target + "\n" + insert)

with open('src/views/ProfileView.tsx', 'w') as f:
    f.write(new_content)
print("Updated vars")
