with open('src/views/PackageDetailView.tsx', 'r') as f:
    content = f.read()

content = content.replace("    trackAction\n  } = useApp();", "    trackAction,\n    userName\n  } = useApp();")

with open('src/views/PackageDetailView.tsx', 'w') as f:
    f.write(content)
