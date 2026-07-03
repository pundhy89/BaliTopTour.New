with open('src/views/AdminView.tsx', 'r') as f:
    content = f.read()

start_str = "canvas.width = width || 100;"
end_str = "} catch (err) {"

start_idx = content.find(start_str)
end_idx = content.find(end_str, start_idx)

new_content = content[:start_idx] + """canvas.width = width || 100;
              canvas.height = height || 100;
              const ctx = canvas.getContext('2d');
              
              if (ctx) {
                const outputType = (file.type === 'image/png' || file.type === 'image/webp' || file.type === 'image/gif') ? 'image/webp' : 'image/jpeg';
                ctx.drawImage(img, 0, 0, width, height);
                const compressedBase64 = canvas.toDataURL(outputType, quality);
                onChange(compressedBase64);
              } else {
                onChange(reader.result as string);
              }
            """ + content[end_idx:]

with open('src/views/AdminView.tsx', 'w') as f:
    f.write(new_content)
