import re
with open('src/views/ActivityDetailView.tsx', 'r') as f:
    content = f.read()

# Replace state
content = content.replace(
    'const [selectedPriceIdx, setSelectedPriceIdx] = useState(0);',
    'const [quantities, setQuantities] = useState<Record<string, number>>({});'
)

# Replace handleBooking
handle_booking_old = """  const handleBooking = () => {
    const selectedPkgName = activePkg?.name || '';
    const selectedPrice = activePrices[selectedPriceIdx];
    const num = settings.whatsapp_number || '6282143415254';
    
    const baseMsg = translate('wa_message', language);
    const actName = getEntityName(activity);
    const pkgStr = selectedPkgName ? ` - ${selectedPkgName}` : '';
    const labelStr = selectedPrice ? ` (${selectedPrice.label})` : '';
    const priceStr = selectedPrice ? `Rp ${selectedPrice.price_idr.toLocaleString('id-ID')}` : `Rp ${activity.price_per_person_idr?.toLocaleString('id-ID')}`;"""

handle_booking_new = """  const handleBooking = () => {
    const selectedPkgName = activePkg?.name || '';
    
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
    const priceStr = `Rp ${totalHarga.toLocaleString('id-ID')}`;"""

content = content.replace(handle_booking_old, handle_booking_new)

# Replace the textMsg generation
text_msg_old = """      customMsg = settings.wa_template_activity
        .replace('[NAMA_PEMESAN]', pemesan)
        .replace('[NAMA_AKTIVITAS]', actName)
        .replace('[PAKET]', selectedPkgName)
        .replace('[OPSI]', selectedPrice ? selectedPrice.label : '')
        .replace('[HARGA]', priceStr);"""
text_msg_new = """      customMsg = settings.wa_template_activity
        .replace('[NAMA_PEMESAN]', pemesan)
        .replace('[NAMA_AKTIVITAS]', actName)
        .replace('[PAKET]', selectedPkgName)
        .replace('[OPSI]', selectedItemsStr)
        .replace('[HARGA]', priceStr);"""
content = content.replace(text_msg_old, text_msg_new)

# Replace logging
log_old = "trackAction('book_now', `Booked activity: ${actName} - ${selectedPkgName} (${selectedPrice?.label || ''})`);"
log_new = "trackAction('book_now', `Booked activity: ${actName} - ${selectedPkgName} (${selectedItemsStr})`);"
content = content.replace(log_old, log_new)

with open('src/views/ActivityDetailView.tsx', 'w') as f:
    f.write(content)
