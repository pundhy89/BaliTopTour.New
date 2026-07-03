import re

with open('src/views/ActivityDetailView.tsx', 'r') as f:
    content = f.read()

handle_booking_regex = re.compile(r'  const handleBooking = \(\) => \{.*?\n  \};\n', re.DOTALL)

new_handle_booking = """  const handleBooking = () => {
    const activePkg = packages.find(p => p.id === activePackId);
    const selectedPkgName = activePkg ? getEntityName(activePkg) : '';
    const actName = getEntityName(activity);
    
    let itemsAdded = 0;
    
    if (activePrices.length > 0) {
      activePrices.forEach(pr => {
        const q = quantities[pr.id] || 0;
        if (q > 0) {
          addToCart({
            type: 'activity',
            itemId: activity.id,
            name: actName,
            options: `${selectedPkgName} - ${pr.label}`,
            price: pr.price_idr,
            quantity: q,
            cover_image_url: activity.cover_image_url
          });
          itemsAdded += q;
        }
      });
    } else {
      const q = quantities['default'] || 1;
      if (q > 0) {
        addToCart({
          type: 'activity',
          itemId: activity.id,
          name: actName,
          options: selectedPkgName,
          price: activity.price_per_person_idr || 0,
          quantity: q,
          cover_image_url: activity.cover_image_url
        });
        itemsAdded += q;
      }
    }
    
    if (itemsAdded === 0) {
      alert("Silakan pilih jumlah tiket terlebih dahulu");
      return;
    }
    
    trackAction('add_to_cart', `Added ${itemsAdded} items of activity: ${actName} to cart`);
    navigate('/cart');
  };
"""

content = handle_booking_regex.sub(new_handle_booking, content)

# Change button text from "Pesan Sekarang" (activity_book_now) to "Tambah Keranjang"
content = content.replace("translate('activity_book_now', language)", "language === 'en' ? 'Add to Cart' : language === 'zh' ? '加入购物车' : 'Tambah Keranjang'")

# Fix "useApp" destructuring
content = content.replace("    userName,\n    trackAction\n  } = useApp();", "    userName,\n    trackAction,\n    addToCart\n  } = useApp();")

with open('src/views/ActivityDetailView.tsx', 'w') as f:
    f.write(content)
