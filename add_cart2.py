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

cart_context_types = """  cart: CartItem[];
  addToCart: (item: Omit<CartItem, 'id'>) => void;
  removeFromCart: (id: string) => void;
  updateCartQuantity: (id: string, qty: number) => void;
  clearCart: () => void;
  
  // Visitor Logging"""

content = content.replace("  // Visitor Logging", cart_context_types)

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
      const existing = prev.find(i => i.itemId === item.itemId && i.options === item.options && i.type === item.type);
      if (existing) {
        return prev.map(i => i.id === existing.id ? { ...i, quantity: i.quantity + item.quantity } : i);
      }
      return [...prev, { ...item, id: Math.random().toString(36).substr(2, 9) }];
    });
  };

  const removeFromCart = (id: string) => setCart(prev => prev.filter(i => i.id !== id));

  const updateCartQuantity = (id: string, qty: number) => {
    if (qty <= 0) {
      removeFromCart(id);
      return;
    }
    setCart(prev => prev.map(i => i.id === id ? { ...i, quantity: qty } : i));
  };

  const clearCart = () => setCart([]);
"""

# Try to find the exact userName state declaration
username_decl_match = re.search(r'  const \[userName, setUserNameState\] = useState<string>\(\(\) =>[\s\S]*?localStorage\.getItem\(\'bali_tour_user_name\'\) \|\| \'\'[\s\S]*?\);', content)
if username_decl_match:
    content = content.replace(username_decl_match.group(0), cart_state)
else:
    print("Could not find username declaration")

exports_match = re.search(r'    userName,\n    setUserName,', content)
if exports_match:
    content = content.replace(exports_match.group(0), """    cart,
    addToCart,
    removeFromCart,
    updateCartQuantity,
    clearCart,
    userName,
    setUserName,""")
else:
    print("Could not find exports")

with open('src/context/AppContext.tsx', 'w') as f:
    f.write(content)
