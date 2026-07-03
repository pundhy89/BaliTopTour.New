with open('src/types.ts', 'r') as f:
    content = f.read()

if 'wa_template_package' not in content:
    content = content.replace("receipt_paper_size?: '58mm' | '80mm';", "receipt_paper_size?: '58mm' | '80mm';\n  wa_template_package?: string;\n  wa_template_activity?: string;")
    with open('src/types.ts', 'w') as f:
        f.write(content)
