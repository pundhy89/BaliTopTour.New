import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

# Add CartView import
if "import { CartView }" not in content:
    content = content.replace("import { PackageDetailView } from './views/PackageDetailView';", "import { PackageDetailView } from './views/PackageDetailView';\nimport { CartView } from './views/CartView';")

# Add to renderCurrentView
cart_route = """
    if (currentPath === '/cart') {
      return <CartView onBack={() => navigate('/')} />;
    }
"""
if "currentPath === '/cart'" not in content:
    content = content.replace("    if (currentPath === '/admin' || currentPath === '/admin/login') {", cart_route + "    if (currentPath === '/admin' || currentPath === '/admin/login') {")

with open('src/App.tsx', 'w') as f:
    f.write(content)
