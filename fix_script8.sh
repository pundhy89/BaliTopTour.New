sed -i '71,81c\
  const handleBooking = () => {\
    const activePkg = packages.find(p => p.id === activePackId);\
    const selectedPkgName = activePkg ? getEntityName(activePkg) : '"'"''"'"';\
    const selectedPrice = activePrices[selectedPriceIdx];\
    const num = settings.whatsapp_number || '"'"'6282143415254'"'"';\
    const baseMsg = translate('"'"'wa_message'"'"', language);\
    const actName = getEntityName(activity);\
    const pkgStr = selectedPkgName ? ` - ${selectedPkgName}` : '"'"''"'"';\
    const labelStr = selectedPrice ? ` (${selectedPrice.label})` : '"'"''"'"';\
    const priceStr = selectedPrice ? `Rp ${selectedPrice.price_idr.toLocaleString('"'"'id-ID'"'"')}` : `Rp ${activity.price_per_person_idr?.toLocaleString('"'"'id-ID'"'"')}`;\
    \
    let textMsg = '"'"''"'"';\
    \
    if (settings.receipt_company_name) {\
      textMsg += `==========================\\n`;\
      textMsg += `  *${settings.receipt_company_name.toUpperCase()}*\\n`;\
      textMsg += `==========================\\n\\n`;\
      textMsg += `*INVOICE / PESANAN*\\n`;\
      textMsg += `Aktivitas: ${actName}${pkgStr}${labelStr}\\n`;\
      textMsg += `Total: ${priceStr}\\n\\n`;\
      if (settings.receipt_footer) {\
        textMsg += `--------------------------\\n`;\
        textMsg += `${settings.receipt_footer}\\n`;\
        textMsg += `==========================`;\
      }\
    } else {\
      textMsg = `${baseMsg}${actName}${pkgStr}${labelStr}. ${translate('"'"'wa_price'"'"', language)}: ${priceStr}`;\
    }' src/views/ActivityDetailView.tsx
