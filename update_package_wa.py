with open('src/views/PackageDetailView.tsx', 'r') as f:
    content = f.read()

target = """    } else {
      textMsg = `${baseMsg}${tourName}${optionStr}. ${translate('wa_price', language)}: ${priceStr}`;
    }"""

replacement = """    } else {
      if (settings.wa_template_package) {
        textMsg = settings.wa_template_package
          .replace('[NAMA_PAKET]', tourName)
          .replace('[OPSI]', selectedOptionName)
          .replace('[HARGA]', priceStr);
      } else {
        textMsg = `${baseMsg}${tourName}${optionStr}. ${translate('wa_price', language)}: ${priceStr}`;
      }
    }"""

if target in content:
    content = content.replace(target, replacement)
else:
    print("Not found")

with open('src/views/PackageDetailView.tsx', 'w') as f:
    f.write(content)
