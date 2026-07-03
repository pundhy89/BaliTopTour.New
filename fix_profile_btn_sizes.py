with open('src/views/ProfileView.tsx', 'r') as f:
    content = f.read()

content = content.replace(
    'className="h-5 mb-1 object-contain"',
    'className="w-full px-2 h-7 mb-1 object-contain drop-shadow-sm"'
)

with open('src/views/ProfileView.tsx', 'w') as f:
    f.write(content)
