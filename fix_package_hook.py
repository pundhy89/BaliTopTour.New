with open('src/views/PackageDetailView.tsx', 'r') as f:
    content = f.read()

content = content.replace("  const { addToCart } = useApp();\n\n  const handleBooking", "  const handleBooking")

with open('src/views/PackageDetailView.tsx', 'w') as f:
    f.write(content)
