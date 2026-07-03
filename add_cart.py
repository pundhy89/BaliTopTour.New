import re

with open('src/context/AppContext.tsx', 'r') as f:
    content = f.read()

cart_types = """
export type CartItem = {
  id: string;
  type: 'package' | 'activity';
  itemId: string;
  name: string;
  options: string;
  price: number;
  quantity: number;
  cover_image_url?: string;
};

interface AppContextType {"""

content = content.replace("interface AppContextType {", cart_types)

cart_context_types = """  // Cart
  cart: CartItem[];
  addToCart: (item: Omit<CartItem, 'id'>) => void;
  removeFromCart: (id: string) => void;
  updateCartQuantity: (id: string, qty: number) => void;
  clearCart: () => void;
  
  // Track action
"""

content = content.replace("  // Track action\n", cart_context_types)

cart_state = """  const [userName, setUserNameState] = useState<string>(() => 
    localStorage.getItem('bali_tour_user_name') || ''
  );

  const [cart, setCart] = useState<CartItem[]>(() => {
    try {
      const saved = localStorage.getItem('bali_tour_cart');
      return saved ? JSON.parse(saved) : [];
    } catch {
      return [];
    }
  });

  useEffect(() => {
    localStorage.setItem('bali_tour_cart', JSON.stringify(cart));
  }, [cart]);

  const addToCart = (item: Omit<CartItem, 'id'>) => {
    setCart(prev => {
      // Check if same item + option exists
      const existing = prev.find(i => i.itemId === item.itemId && i.options === item.options);
      if (existing) {
        return prev.map(i => i.id === existing.id ? { ...i, quantity: i.quantity + item.quantity } : i);
      }
      return [...prev, { ...item, id: Math.random().toString(36).substr(2, 9) }];
    });
  };

  const removeFromCart = (id: string) => {
    setCart(prev => prev.filter(i => i.id !== id));
  };

  const updateCartQuantity = (id: string, qty: number) => {
    if (qty <= 0) {
      removeFromCart(id);
      return;
    }
    setCart(prev => prev.map(i => i.id === id ? { ...i, quantity: qty } : i));
  };

  const clearCart = () => setCart([]);
"""

content = content.replace("  const [userName, setUserNameState] = useState<string>(() => \n    localStorage.getItem('bali_tour_user_name') || ''\n  );", cart_state)

cart_exports = """    updateCartQuantity,
    clearCart,
    userName,"""

content = content.replace("    userName,", "    cart,\n    addToCart,\n    removeFromCart,\n" + cart_exports)

with open('src/context/AppContext.tsx', 'w') as f:
    f.write(content)
