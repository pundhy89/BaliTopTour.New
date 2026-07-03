with open('src/views/ActivityDetailView.tsx', 'r') as f:
    content = f.read()

target = """    } else {
      textMsg = `${baseMsg}${actName}${pkgStr}${labelStr}. ${translate('wa_price', language)}: ${priceStr}`;
    }"""

replacement = """    } else {
      if (settings.wa_template_activity) {
        textMsg = settings.wa_template_activity
          .replace('[NAMA_AKTIVITAS]', actName)
          .replace('[PAKET]', selectedPkgName)
          .replace('[OPSI]', selectedPrice ? selectedPrice.label : '')
          .replace('[HARGA]', priceStr);
      } else {
        textMsg = `${baseMsg}${actName}${pkgStr}${labelStr}. ${translate('wa_price', language)}: ${priceStr}`;
      }
    }"""

if target in content:
    content = content.replace(target, replacement)
else:
    print("Not found")

with open('src/views/ActivityDetailView.tsx', 'w') as f:
    f.write(content)
