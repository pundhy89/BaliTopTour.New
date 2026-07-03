with open('src/views/ActivityDetailView.tsx', 'r') as f:
    content = f.read()

target = """            <span className="text-[9px] font-medium text-white/80 block uppercase tracking-wider mt-0.5">
              {activePrices.length > 0 ? 'Total' : translate('per_person', language)}
            </span>
        </div>"""

replacement = """            <span className="text-[9px] font-medium text-slate-500 block uppercase tracking-wider mt-0.5">
              {activePrices.length > 0 ? 'Total' : translate('per_person', language)}
            </span>
          </span>
        </div>"""

content = content.replace(target, replacement)

with open('src/views/ActivityDetailView.tsx', 'w') as f:
    f.write(content)
