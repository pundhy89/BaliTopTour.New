import re

with open('src/context/AppContext.tsx', 'r') as f:
    content = f.read()

# I will find everything between the first `const [cart, setCart]` and `const clearCart = () => setCart([]);\n` and delete one of them.
matches = list(re.finditer(r'  const \[cart, setCart\] = useState<CartItem\[\]>\(\(\) => \{.*?\n  const clearCart = \(\) => setCart\(\[\]\);\n', content, re.DOTALL))
if len(matches) > 1:
    # Remove the second match
    m2 = matches[1]
    content = content[:m2.start()] + content[m2.end():]

# Check if there are other duplicates like userName
username_matches = list(re.finditer(r'  const \[userName, setUserNameState\] = useState<string>\(\(\) =>[\s\S]*?localStorage\.getItem\(\'bali_tour_user_name\'\) \|\| \'\'[\s\S]*?\);', content))
if len(username_matches) > 1:
    m2 = username_matches[1]
    content = content[:m2.start()] + content[m2.end():]

with open('src/context/AppContext.tsx', 'w') as f:
    f.write(content)
