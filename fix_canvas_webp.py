with open('src/views/AdminView.tsx', 'r') as f:
    content = f.read()

old_logic = """              if (ctx) {
                const isTransparent = file.type === 'image/png' || file.type === 'image/webp' || file.type === 'image/gif' || file.type === 'image/svg+xml';
                const outputType = isTransparent ? 'image/png' : 'image/jpeg';
                ctx.clearRect(0, 0, width, height);
                ctx.drawImage(img, 0, 0, width, height);
                const compressedBase64 = canvas.toDataURL(outputType, isTransparent ? undefined : quality);
                onChange(compressedBase64);
              } else {"""

new_logic = """              if (ctx) {
                const isTransparent = file.type === 'image/png' || file.type === 'image/webp' || file.type === 'image/gif' || file.type === 'image/svg+xml';
                const outputType = isTransparent ? 'image/webp' : 'image/jpeg';
                ctx.clearRect(0, 0, width, height);
                ctx.drawImage(img, 0, 0, width, height);
                const compressedBase64 = canvas.toDataURL(outputType, quality);
                onChange(compressedBase64);
              } else {"""

if old_logic in content:
    with open('src/views/AdminView.tsx', 'w') as f:
        f.write(content.replace(old_logic, new_logic))
    print("Updated to use image/webp for transparent files")
else:
    print("Could not find old logic")
