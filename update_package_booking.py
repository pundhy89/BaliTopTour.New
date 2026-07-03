import re

with open('src/views/PackageDetailView.tsx', 'r') as f:
    content = f.read()

handle_booking_regex = re.compile(r'  const handleBooking = \(\) => \{.*?\n  \};\n', re.DOTALL)

new_handle_booking = """  const { addToCart } = useApp();

  const handleBooking = () => {
    const selectedOptionName = activeOpt?.name || '';
    const tourName = getEntityName(pkg);
    
    addToCart({
      type: 'package',
      itemId: pkg.id,
      name: tourName,
      options: selectedOptionName,
      price: displayPrice,
      quantity: quantity,
      cover_image_url: pkg.cover_image_url
    });
    
    trackAction('add_to_cart', `Added package to cart: ${tourName} (${selectedOptionName})`);
    navigate('/cart');
  };
"""

content = handle_booking_regex.sub(new_handle_booking, content)

# Change button text from "Pesan Sekarang" (book_now) to "Tambah Keranjang"
content = content.replace("translate('book_now', language)", "language === 'en' ? 'Add to Cart' : language === 'zh' ? '加入购物车' : 'Tambah Keranjang'")

# Fix "useApp" destructuring
content = content.replace("    trackAction,\n    userName\n  } = useApp();", "    trackAction,\n    userName,\n    addToCart\n  } = useApp();")

# Remove unused variable if it causes lint errors (addToCart defined twice now?)
# Let's just fix the hook call directly

with open('src/views/PackageDetailView.tsx', 'w') as f:
    f.write(content)
