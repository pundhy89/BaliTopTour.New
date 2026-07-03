with open('src/views/AdminView.tsx', 'r') as f:
    content = f.read()

btn = """
          {/* Template Pesan */}
          <button
            onClick={() => setActiveTab('wa-template')}
            className={`p-3.5 rounded-[24px] border flex flex-col items-center justify-center text-center transition-all duration-200 active:scale-95 cursor-pointer shadow-sm ${
              activeTab === 'wa-template' 
                ? 'bg-fuchsia-600 border-fuchsia-600 text-white shadow-md' 
                : 'bg-white border-slate-100 text-slate-700 hover:bg-slate-50'
            }`}
          >
            <div className={`w-9 h-9 rounded-2xl flex items-center justify-center mb-2 transition-colors ${
              activeTab === 'wa-template' ? 'bg-white/10 text-white' : 'bg-fuchsia-50 text-fuchsia-600'
            }`}>
              <MessageCircle size={18} className="stroke-[2.2px]" />
            </div>
            <span className="text-[10px] font-extrabold uppercase tracking-wide block leading-none truncate w-full">
              Template Pesan
            </span>
          </button>
"""

target = "          {/* Printer & Struk */}"

if target in content:
    content = content.replace(target, btn + "\n" + target)
    with open('src/views/AdminView.tsx', 'w') as f:
        f.write(content)
    print("Button added!")
else:
    print("Target not found!")
