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
      
      // If nothing selected, add 1 of the first price option by default to prevent stuck UI
      if (itemsAdded === 0 && activePrices.length > 0) {
        const firstPrice = activePrices[0];
        addToCart({
          type: 'activity',
          itemId: activity.id,
          name: actName,
          options: `${selectedPkgName} - ${firstPrice.label}`,
          price: firstPrice.price_idr,
          quantity: 1,
          cover_image_url: activity.cover_image_url
        });
        itemsAdded += 1;
      }
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
    
    trackAction('add_to_cart', `Added ${itemsAdded} items of activity: ${actName} to cart`);
    navigate('/cart');
  };
"""

content = handle_booking_regex.sub(new_handle_booking, content)

with open('src/views/ActivityDetailView.tsx', 'w') as f:
    f.write(content)
