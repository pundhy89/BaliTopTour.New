import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

content = content.replace("const showBottomNav = ['/', '/cart', '/map', '/gallery', '/profile'].includes(path);", "const showBottomNav = ['/', '/map', '/gallery', '/profile'].includes(path);")

with open('src/App.tsx', 'w') as f:
    f.write(content)

with open('src/views/CartView.tsx', 'r') as f:
    content2 = f.read()

content2 = content2.replace("const { cart, removeFromCart, updateCartQuantity, settings, language, userName, trackAction } = useApp();", "const { cart, removeFromCart, updateCartQuantity, clearCart, settings, language, userName, trackAction } = useApp();")
content2 = content2.replace("window.open(`https://wa.me/${num}?text=${encodeURIComponent(textMsg)}`, '_blank');\n  };", "window.open(`https://wa.me/${num}?text=${encodeURIComponent(textMsg)}`, '_blank');\n    clearCart();\n  };")

with open('src/views/CartView.tsx', 'w') as f:
    f.write(content2)

