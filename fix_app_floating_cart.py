import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Make sure ShoppingCart icon is imported
if "ShoppingCart" not in content:
    content = content.replace("import { Home, Search, Map, Image, User }", "import { Home, Search, Map, Image, User, ShoppingCart }")

# Add the floating button in MainApp
target = "        {/* Persistent Bottom Nav Bar element */}"
replacement = """
        {/* Floating Cart Button */}
        {cart.length > 0 && path !== '/cart' && !path.startsWith('/admin') && (
          <button
            onClick={() => navigate('/cart')}
            className="absolute bottom-28 right-4 w-14 h-14 rounded-full shadow-[0_8px_25px_rgba(0,0,0,0.2)] flex items-center justify-center text-white z-40 hover:scale-105 active:scale-95 transition-all"
            style={{ backgroundColor: settings.theme_color }}
          >
            <div className="relative">
              <ShoppingCart size={24} className="stroke-[2.5px]" />
              <div className="absolute -top-2 -right-2 bg-red-500 text-white text-[10px] font-bold w-5 h-5 rounded-full flex items-center justify-center border-2 border-white">
                {cart.reduce((sum, item) => sum + item.quantity, 0)}
              </div>
            </div>
          </button>
        )}

        {/* Persistent Bottom Nav Bar element */}"""

if "{/* Floating Cart Button */}" not in content:
    content = content.replace(target, replacement)

# Add cart destructured variable in MainApp
content = content.replace("const { settings, language, isAdminLoggedIn } = useApp();", "const { settings, language, isAdminLoggedIn, cart } = useApp();")

with open('src/App.tsx', 'w') as f:
    f.write(content)
