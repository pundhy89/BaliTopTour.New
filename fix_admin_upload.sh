sed -i '58,62c\
              canvas.width = width || 100;\
              canvas.height = height || 100;\
              const ctx = canvas.getContext('"'"'2d'"'"');\
              \
              if (ctx) {\
                const outputType = file.type === '"'"'image/png'"'"' || file.type === '"'"'image/webp'"'"' ? '"'"'image/webp'"'"' : '"'"'image/jpeg'"'"';\
                ctx.drawImage(img, 0, 0, width, height);\
                const compressedBase64 = canvas.toDataURL(outputType, quality);\
                onChange(compressedBase64);' src/views/AdminView.tsx
