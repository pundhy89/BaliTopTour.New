import re

with open('src/App.tsx', 'r') as f:
    content = f.read()

if "import { CartView }" not in content:
    content = content.replace("import { PackageDetailView } from './views/PackageDetailView';", "import { PackageDetailView } from './views/PackageDetailView';\nimport { CartView } from './views/CartView';")

if "ShoppingCart" not in content:
    content = content.replace("import { Home, Search, Map, Image, User } from 'lucide-react';", "import { Home, Search, Map, Image, User, ShoppingCart } from 'lucide-react';")

with open('src/App.tsx', 'w') as f:
    f.write(content)
