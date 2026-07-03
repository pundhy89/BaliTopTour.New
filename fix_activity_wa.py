with open('src/views/ActivityDetailView.tsx', 'r') as f:
    content = f.read()

import re

target = re.search(r'let textMsg = \'\';.*?window\.open\(', content, re.DOTALL)
if target:
    replacement = """
    const pemesan = userName || 'Guest';
    let textMsg = '';
    
    let customMsg = '';
    if (settings.wa_template_activity) {
      customMsg = settings.wa_template_activity
        .replace('[NAMA_PEMESAN]', pemesan)
        .replace('[NAMA_AKTIVITAS]', actName)
        .replace('[PAKET]', selectedPkgName)
        .replace('[OPSI]', selectedPrice ? selectedPrice.label : '')
        .replace('[HARGA]', priceStr);
    } else {
      customMsg = `${baseMsg} ${actName}${pkgStr}${labelStr}. ${translate('wa_price', language)}: ${priceStr}`;
    }

    textMsg = customMsg;

    if (settings.receipt_company_name) {
      let receipt = `\\n\\n==========================\\n`;
      receipt += `  *${settings.receipt_company_name.toUpperCase()}*\\n`;
      receipt += `==========================\\n`;
      receipt += `*INVOICE / PESANAN*\\n`;
      receipt += `Pemesan: ${pemesan}\\n`;
      receipt += `Aktivitas: ${actName}${pkgStr}${labelStr}\\n`;
      receipt += `Total: ${priceStr}\\n`;
      if (settings.receipt_footer) {
        receipt += `--------------------------\\n`;
        receipt += `${settings.receipt_footer}\\n`;
      }
      receipt += `==========================`;
      textMsg += receipt;
    }

    // Log tracking
    trackAction('book_now', `Booked activity: ${actName} - ${selectedPkgName} (${selectedPrice?.label || ''})`);

    window.open("""
    content = content.replace(target.group(0), replacement)
    
    with open('src/views/ActivityDetailView.tsx', 'w') as f:
        f.write(content)
else:
    print("Could not find target")
