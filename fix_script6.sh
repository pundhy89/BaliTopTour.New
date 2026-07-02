cat << 'INNER_EOF' > /tmp/ImageUpload.tsx
function ImageUploadOrUrl({
  value,
  onChange,
  label,
  placeholder = "https://...",
  id = "image-input",
  maxSize = 480,
  quality = 0.55
}: {
  value: string;
  onChange: (val: string) => void;
  label: string;
  placeholder?: string;
  id?: string;
  maxSize?: number;
  quality?: number;
}) {
  const [mode, setMode] = useState<'url' | 'upload'>(value?.startsWith('data:') ? 'upload' : 'url');
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      const reader = new FileReader();
      reader.onloadend = () => {
        if (typeof reader.result === 'string') {
          const img = new window.Image();
          img.src = reader.result;
          img.onload = () => {
            try {
              const canvas = document.createElement('canvas');
              let width = img.width;
              let height = img.height;

              if (width > height) {
                if (width > maxSize) {
                  height *= maxSize / width;
                  width = maxSize;
                }
              } else {
                if (height > maxSize) {
                  width *= maxSize / height;
                  height = maxSize;
                }
              }

              canvas.width = width || 100;
              canvas.height = height || 100;
              const ctx = canvas.getContext('2d');
              
              if (ctx) {
                ctx.drawImage(img, 0, 0, width, height);
                const compressedBase64 = canvas.toDataURL('image/jpeg', quality);
                onChange(compressedBase64);
              } else {
                onChange(reader.result as string);
              }
            } catch (err) {
              console.warn('Canvas compression failed:', err);
              onChange(reader.result as string);
            }
          };
          img.onerror = () => {
            onChange(reader.result as string);
          };
        }
      };
      reader.readAsDataURL(file);
    }
  };

  const isBase64 = value ? value.startsWith('data:') : false;

  return (
    <div className="flex flex-col gap-2 bg-slate-50 border border-slate-150 p-3 rounded-2xl">
      <div className="flex items-center justify-between">
        <label className="text-[9px] font-black text-slate-500 uppercase tracking-widest">{label}</label>
        
        {/* Toggle Mode Buttons */}
        <div className="flex bg-slate-200/60 p-0.5 rounded-lg border border-slate-200 text-[9px] font-bold">
          <button
            type="button"
            onClick={() => setMode('url')}
            className={`px-2 py-0.5 rounded-md transition-all ${
              mode === 'url' ? 'bg-white text-slate-800 shadow-xs' : 'text-slate-400'
            }`}
          >
            URL
          </button>
          <button
            type="button"
            onClick={() => setMode('upload')}
            className={`px-2 py-0.5 rounded-md transition-all ${
              mode === 'upload' ? 'bg-white text-slate-800 shadow-xs' : 'text-slate-400'
            }`}
          >
            Upload
          </button>
        </div>
      </div>

      {mode === 'url' ? (
        <input
          type="text"
          placeholder={placeholder}
          value={!isBase64 ? value : ''}
          onChange={e => onChange(e.target.value)}
          className="w-full bg-white border border-slate-200 outline-none text-[10px] font-semibold text-slate-800 rounded-xl py-2 px-3 focus:border-indigo-300 focus:ring-2 focus:ring-indigo-100 transition-all"
        />
      ) : (
        <div className="flex flex-col gap-2">
          {/* File Input */}
          <input
            type="file"
            accept="image/*"
            ref={fileInputRef}
            onChange={handleFileChange}
            className="hidden"
            id={id}
          />
          <div className="flex gap-2">
            <button
              type="button"
              onClick={() => fileInputRef.current?.click()}
              className="flex-1 bg-white border border-slate-200 text-slate-600 font-bold py-2 rounded-xl text-[10px] hover:bg-slate-100 transition-all flex items-center justify-center gap-1.5"
            >
              <Upload size={14} />
              Pilih Foto
            </button>
            {isBase64 && (
              <button
                type="button"
                onClick={() => onChange('')}
                className="px-3 bg-red-50 text-red-600 hover:bg-red-100 rounded-xl transition-all"
              >
                <Trash2 size={12} />
              </button>
            )}
          </div>
          
          {/* Preview Image */}
          {value && isBase64 && (
            <div className="relative w-full aspect-video rounded-xl overflow-hidden bg-slate-200 border border-slate-200 mt-1 group">
              <img src={value} className="w-full h-full object-cover" alt="Preview" />
              <div className="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center text-[9px] text-white font-bold tracking-wider">
                PREVIEW
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
INNER_EOF

# Replace lines 13 to 208 with the content of /tmp/ImageUpload.tsx
sed -i -e '13,208c\' -e "$(cat /tmp/ImageUpload.tsx)" src/views/AdminView.tsx
