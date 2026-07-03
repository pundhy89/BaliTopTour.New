import re
with open('src/views/ActivityDetailView.tsx', 'r') as f:
    content = f.read()

target = """          {activePrices.length === 0 ? (
            <div className="text-center py-4 bg-slate-50 rounded-2xl">
              <p className="text-slate-400 text-xs font-semibold">{translate('activity_no_packages', language)}</p>
            </div>
          ) : ("""

replacement = """          {activePrices.length === 0 ? (
            <div className="w-full p-4 rounded-2xl text-left border border-slate-50 bg-slate-50/40 flex justify-between items-center transition-all">
              <div className="flex items-center gap-2.5">
                <span className="text-slate-800 text-xs font-bold">
                  {translate('per_person', language)}
                </span>
              </div>
              <div className="flex flex-col items-end gap-2">
                <span className="font-bold text-xs" style={primaryText}>
                  Rp {activity.price_per_person_idr?.toLocaleString('id-ID')}
                </span>
                <div className="flex items-center gap-3">
                  <button 
                    onClick={() => setQuantities(prev => ({...prev, default: Math.max(1, (prev['default'] || 1) - 1)}))}
                    className="w-6 h-6 rounded-full bg-slate-200 text-slate-600 flex items-center justify-center font-bold active:scale-95"
                  >
                    -
                  </button>
                  <span className="text-xs font-bold w-4 text-center">{quantities['default'] || 1}</span>
                  <button 
                    onClick={() => setQuantities(prev => ({...prev, default: (prev['default'] || 1) + 1}))}
                    className="w-6 h-6 rounded-full text-white flex items-center justify-center font-bold active:scale-95"
                    style={primaryBg}
                  >
                    +
                  </button>
                </div>
              </div>
            </div>
          ) : ("""

content = content.replace(target, replacement)

with open('src/views/ActivityDetailView.tsx', 'w') as f:
    f.write(content)
