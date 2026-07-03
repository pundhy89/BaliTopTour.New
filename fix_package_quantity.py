import re
with open('src/views/PackageDetailView.tsx', 'r') as f:
    content = f.read()

# Replace state
content = content.replace(
    'const [activeOptId, setActiveOptId] = useState(options.length > 0 ? options[0].id : \'\');',
    'const [activeOptId, setActiveOptId] = useState(options.length > 0 ? options[0].id : \'\');\n  const [quantity, setQuantity] = useState(pkg.min_pax || 1);'
)

# Replace handleBooking
handle_booking_old = """  const handleBooking = () => {
    const selectedOptionName = activeOpt?.name || '';
    const num = settings.whatsapp_number || '6282143415254';
    
    const baseMsg = translate('wa_message', language);
    const tourName = getEntityName(pkg);
    const optionStr = selectedOptionName ? ` - ${selectedOptionName}` : '';
    const priceStr = `Rp ${displayPrice.toLocaleString('id-ID')}`;
    
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
    }"""

handle_booking_new = """  const handleBooking = () => {
    const selectedOptionName = activeOpt?.name || '';
    const num = settings.whatsapp_number || '6282143415254';
    
    const baseMsg = translate('wa_message', language);
    const tourName = getEntityName(pkg);
    
    let optionStr = selectedOptionName ? ` - ${selectedOptionName}` : '';
    optionStr += ` (${quantity}x pax)`;
    const totalHarga = quantity * displayPrice;
    
    const priceStr = `Rp ${totalHarga.toLocaleString('id-ID')}`;
    
    const pemesan = userName || 'Guest';
    let textMsg = '';
    
    let customMsg = '';
    if (settings.wa_template_package) {
      customMsg = settings.wa_template_package
        .replace('[NAMA_PEMESAN]', pemesan)
        .replace('[NAMA_PAKET]', tourName)
        .replace('[OPSI]', selectedOptionName ? `${selectedOptionName} (${quantity} pax)` : `${quantity} pax`)
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
    }"""

content = content.replace(handle_booking_old, handle_booking_new)

# Modify bottom bar UI to have counter
bottom_bar_old = """      <div className="fixed bottom-0 left-0 right-0 bg-white border-t border-slate-200 p-4 pb-6 sm:pb-4 flex justify-between items-center z-50">
        <div>
          <span className="text-slate-900 font-bold text-base block leading-none mb-1">
            Rp {displayPrice.toLocaleString('id-ID')}
          </span>
          <span className="text-[9px] font-medium text-slate-400 block uppercase tracking-wider">
            {language === 'zh' ? '每人 / 选项' : language === 'en' ? 'Per Person / Option' : 'Per Orang / Opsi'}
          </span>
        </div>
        <button 
          onClick={handleBooking}
          className="py-3 px-8 rounded-2xl text-white font-bold text-xs uppercase tracking-wide active:scale-95 transition-transform shadow-md"
          style={primaryBg}
        >
          {translate('book_now', language)}
        </button>
      </div>"""

bottom_bar_new = """      <div className="fixed bottom-0 left-0 right-0 bg-white border-t border-slate-200 p-4 pb-6 sm:pb-4 flex flex-col sm:flex-row justify-between sm:items-center gap-3 z-50">
        
        <div className="flex justify-between sm:justify-start items-center gap-4 w-full sm:w-auto">
          <div className="flex items-center gap-3 bg-slate-50 border border-slate-100 rounded-xl p-1 px-2">
            <button 
              onClick={() => setQuantity(prev => Math.max(pkg.min_pax || 1, prev - 1))}
              className="w-7 h-7 rounded-full bg-slate-200 text-slate-600 flex items-center justify-center font-bold active:scale-95"
            >
              -
            </button>
            <div className="flex flex-col items-center">
              <span className="text-xs font-bold min-w-[20px] text-center">{quantity}</span>
              <span className="text-[8px] text-slate-400 font-bold uppercase tracking-widest leading-none">Pax</span>
            </div>
            <button 
              onClick={() => setQuantity(prev => prev + 1)}
              className="w-7 h-7 rounded-full text-white flex items-center justify-center font-bold active:scale-95"
              style={primaryBg}
            >
              +
            </button>
          </div>
          <div>
            <span className="text-slate-900 font-bold text-base block leading-none mb-1">
              Rp {(quantity * displayPrice).toLocaleString('id-ID')}
            </span>
            <span className="text-[9px] font-medium text-slate-400 block uppercase tracking-wider">
              Total ({quantity}x)
            </span>
          </div>
        </div>
        
        <button 
          onClick={handleBooking}
          className="w-full sm:w-auto py-3 px-8 rounded-2xl text-white font-bold text-xs uppercase tracking-wide active:scale-95 transition-transform shadow-md"
          style={primaryBg}
        >
          {translate('book_now', language)}
        </button>
      </div>"""

content = content.replace(bottom_bar_old, bottom_bar_new)

with open('src/views/PackageDetailView.tsx', 'w') as f:
    f.write(content)
