sed -i '13,56c\
function ImageUploadOrUrl({\
  value,\
  onChange,\
  label,\
  placeholder = "https://...",\
  id = "image-input",\
  maxSize = 480,\
  quality = 0.55\
}: {\
  value: string;\
  onChange: (val: string) => void;\
  label: string;\
  placeholder?: string;\
  id?: string;\
  maxSize?: number;\
  quality?: number;\
}) {\
  const [mode, setMode] = useState<'"'"'url'"'"' | '"'"'upload'"'"'>(value?.startsWith('"'"'data:'"'"') ? '"'"'upload'"'"' : '"'"'url'"'"');\
  const fileInputRef = useRef<HTMLInputElement>(null);\
\
  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {\
    const file = e.target.files?.[0];\
    if (file) {\
      const reader = new FileReader();\
      reader.onloadend = () => {\
        if (typeof reader.result === '"'"'string'"'"') {\
          const img = new window.Image();\
          img.src = reader.result;\
          img.onload = () => {\
            try {\
              const canvas = document.createElement('"'"'canvas'"'"');\
              let width = img.width;\
              let height = img.height;\
              if (width > height) {\
                if (width > maxSize) {\
                  height *= maxSize / width;\
                  width = maxSize;\
                }\
              } else {\
                if (height > maxSize) {\
                  width *= maxSize / height;\
                  height = maxSize;\
                }\
              }\
              canvas.width = width || 100;\
              canvas.height = height || 100;\
              const ctx = canvas.getContext('"'"'2d'"'"');\
              if (ctx) {\
                ctx.drawImage(img, 0, 0, width, height);\
                const compressedBase64 = canvas.toDataURL('"'"'image/jpeg'"'"', quality);\
                onChange(compressedBase64);\
              } else {\
                onChange(reader.result as string);\
              }\
            } catch (err) {\
              console.warn('"'"'Canvas compression failed, falling back to raw base64:'"'"', err);\
              onChange(reader.result as string);\
            }\
          };\
          img.onerror = () => {\
            onChange(reader.result as string);\
          };\
        }\
      };\
      reader.readAsDataURL(file);\
    }\
  };\
' src/views/AdminView.tsx
