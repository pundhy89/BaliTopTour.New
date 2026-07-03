with open('src/views/PackageDetailView.tsx', 'r') as f:
    content = f.read()

import re

target = re.search(r'let textMsg = \'\';.*?window\.open\(', content, re.DOTALL)
if target:
    replacement = """
    const pemesan = userName || 'Guest';
    let textMsg = '';
    
    let customMsg = '';
    if (settings.wa_template_package) {
      customMsg = settings.wa_template_package
        .replace('[NAMA_PEMESAN]', pemesan)
        .replace('[NAMA_PAKET]', tourName)
        .replace('[OPSI]', selectedOptionName)
        .replace('[HARGA]', priceStr);
    } else {
      customMsg = `${baseMsg} ${tourName}${optionStr}. ${translate('wa_price', language)}: ${priceStr}`;
    }

    textMsg = customMsg;

    if (settings.receipt_company_name) {
      let receipt = `\\n\\n==========================\\n`;
      receipt += `  *${settings.receipt_company_name.toUpperCase()}*\\n`;
      receipt += `==========================\\n`;
      receipt += `*INVOICE / PESANAN*\\n`;
      receipt += `Pemesan: ${pemesan}\\n`;
      receipt += `Paket: ${tourName}${optionStr}\\n`;
      receipt += `Total: ${priceStr}\\n`;
      if (settings.receipt_footer) {
        receipt += `--------------------------\\n`;
        receipt += `${settings.receipt_footer}\\n`;
      }
      receipt += `==========================`;
      textMsg += receipt;
    }

    // Save to Visitor booking logs
    trackAction('book_now', `Clicked book now for package: ${tourName} (${selectedOptionName})`);
    window.open("""
    content = content.replace(target.group(0), replacement)
    
    with open('src/views/PackageDetailView.tsx', 'w') as f:
        f.write(content)
else:
    print("Could not find target")
