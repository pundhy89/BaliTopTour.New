with open('src/views/ProfileView.tsx', 'r') as f:
    content = f.read()

content = content.replace(
    'className="h-10 mb-4 object-contain"',
    'className="w-full max-w-[140px] h-12 mb-4 object-contain drop-shadow-md"'
)

with open('src/views/ProfileView.tsx', 'w') as f:
    f.write(content)
