import re

with open('src/context/AppContext.tsx', 'r') as f:
    content = f.read()

# Remove the duplicate CartItem type definition
matches = list(re.finditer(r'export type CartItem = \{.*?\};', content, re.DOTALL))
if len(matches) > 1:
    m2 = matches[1]
    content = content[:m2.start()] + content[m2.end():]

with open('src/context/AppContext.tsx', 'w') as f:
    f.write(content)
