import re
with open('src/views/ActivityDetailView.tsx', 'r') as f:
    content = f.read()

handle_booking_regex = re.compile(r'  const handleBooking = \(\) => \{.*?\n  \};\n\n  const handleReviewSubmit', re.DOTALL)

new_handle_booking = """  const handleBooking = () => {
    const activePkg = packages.find(p => p.id === activePackId);
    const selectedPkgName = activePkg ? getEntityName(activePkg) : '';
    
    const num = settings.whatsapp_number || '6282143415254';
    const baseMsg = translate('wa_message', language);
    const actName = getEntityName(activity);
    const pkgStr = selectedPkgName ? ` - ${selectedPkgName}` : '';
    
    let selectedItemsStr = '';
    let totalHarga = 0;
    
    if (activePrices.length > 0) {
      const parts: string[] = [];
      activePrices.forEach(pr => {
        const q = quantities[pr.id] || 0;
        if (q > 0) {
          parts.push(`${q}x ${pr.label}`);
          totalHarga += q * pr.price_idr;
        }
      });
      selectedItemsStr = parts.join(', ');
    } else {
      const q = quantities['default'] || 1;
      selectedItemsStr = `${q}x pax`;
      totalHarga = q * (activity.price_per_person_idr || 0);
    }
    
    if (totalHarga === 0) {
      alert("Silakan pilih jumlah tiket terlebih dahulu");
      return;
    }
    
    const labelStr = selectedItemsStr ? ` (${selectedItemsStr})` : '';
    const priceStr = `Rp ${totalHarga.toLocaleString('id-ID')}`;
    
    const pemesan = userName || 'Guest';
    let textMsg = '';
    
    let customMsg = '';
    if (settings.wa_template_activity) {
      customMsg = settings.wa_template_activity
        .replace('[NAMA_PEMESAN]', pemesan).replace('[NAMA PEMESAN]', pemesan)
        .replace('[NAMA_AKTIVITAS]', actName)
        .replace('[PAKET]', selectedPkgName)
        .replace('[OPSI]', selectedItemsStr)
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
        receipt += `${settings.receipt_footer.replace('[NAMA_PEMESAN]', pemesan).replace('[NAMA PEMESAN]', pemesan)}\\n`;
      }
      receipt += `==========================`;
      textMsg += receipt;
    }

    // Log tracking
    trackAction('book_now', `Booked activity: ${actName} - ${selectedPkgName} (${selectedItemsStr})`);

    window.open(`https://wa.me/${num}?text=${encodeURIComponent(textMsg)}`, '_blank');
  };

  const handleReviewSubmit"""

content = handle_booking_regex.sub(new_handle_booking, content)

with open('src/views/ActivityDetailView.tsx', 'w') as f:
    f.write(content)
