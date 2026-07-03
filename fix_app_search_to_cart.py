import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Replace showBottomNav
content = content.replace("const showBottomNav = ['/', '/search', '/map', '/gallery', '/profile'].includes(path);", "const showBottomNav = ['/', '/cart', '/map', '/gallery', '/profile'].includes(path);")

# Remove SearchView rendering
if "if (currentPath === '/search')" in content:
    content = re.sub(r'    if \(currentPath === \'/search\'\) \{\n      return <SearchView navigate=\{navigate\} />;\n    \}\n', '', content)

# Remove Floating Cart Button since it will be in the nav bar
if "{/* Floating Cart Button */}" in content:
    content = re.sub(r'        \{/\* Floating Cart Button \*/\}.*?        \{/\* Persistent Bottom Nav Bar element \*/\}', '        {/* Persistent Bottom Nav Bar element */}', content, flags=re.DOTALL)

# Replace Search button with Cart button in bottom nav
cart_button = """            {/* Cart item (Floating Cart) - Re-positioned and styled like the reference photo */}
            <button
              onClick={() => navigate('/cart')}
              className="flex flex-col items-center justify-end flex-1 h-full pb-2 relative transition-all duration-200 active:scale-95 group"
            >
              <div 
                className="absolute -top-7 w-[64px] h-[64px] rounded-full flex items-center justify-center border-[4px] border-white shadow-[0_8px_20px_rgba(0,0,0,0.15)] transition-all duration-200 group-hover:scale-105"
                style={{ backgroundColor: settings.theme_color }}
              >
                <div className="relative">
                  <ShoppingCart size={22} className="stroke-[2.5px] text-white" />
                  {cart.length > 0 && (
                    <div className="absolute -top-2 -right-2 bg-red-500 text-white text-[10px] font-bold w-5 h-5 rounded-full flex items-center justify-center border-2 border-white">
                      {cart.reduce((sum, item) => sum + item.quantity, 0)}
                    </div>
                  )}
                </div>
              </div>
              <span 
                className="text-[10px] font-semibold tracking-wide transition-colors duration-200"
                style={path === '/cart' ? { color: settings.theme_color } : { color: '#8e9aa8' }}
              >
                {language === 'en' ? 'Cart' : language === 'zh' ? '购物车' : 'Keranjang'}
              </span>
            </button>"""

content = re.sub(r'            \{/\* Cari item.*?            </button>', cart_button, content, flags=re.DOTALL)

with open('src/App.tsx', 'w') as f:
    f.write(content)
