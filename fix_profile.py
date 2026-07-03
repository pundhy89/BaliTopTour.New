import re

with open('src/views/ProfileView.tsx', 'r') as f:
    content = f.read()

# Add hasBca, hasSeabank, hasPaypal variables
inject_vars = """
  const navigate = useNavigate();

  const hasBca = !!(settings.bank_bca_number || settings.bank_bca_logo);
  const hasSeabank = !!(settings.bank_seabank_number || settings.bank_seabank_logo);
  const hasPaypal = !!(settings.bank_paypal_number || settings.bank_paypal_logo);
  const hasAnyBank = hasBca || hasSeabank || hasPaypal;
"""

content = re.sub(r'const navigate = useNavigate\(\);', inject_vars, content)

# Replace the Metode Pembayaran block
# Find the start
start_str = '{/* Metode Pembayaran */}'
end_str = '{selectedBank && ('

start_idx = content.find(start_str)
end_idx = content.find(end_str)

if start_idx != -1 and end_idx != -1:
    new_block = """{/* Metode Pembayaran */}
        {hasAnyBank && (
        <div className="bg-white rounded-3xl border border-slate-100 p-5 shadow-sm">
          <h4 className="text-slate-800 font-bold text-xs mb-1.5 flex items-center gap-2">
            <Landmark size={15} style={primaryText} />
            Metode Pembayaran
          </h4>
          <p className="text-slate-400 text-[10px] font-semibold mb-4 leading-relaxed">
            Pilih metode pembayaran untuk melihat informasi rekening
          </p>
          <div className="flex gap-2">
            {hasBca && (
            <button
              onClick={() => setSelectedBank('bca')}
              className={`flex-1 py-2 px-1 h-12 border rounded-xl flex items-center justify-center transition-all hover:bg-slate-50 border-slate-100 bg-white`}
            >
              {settings.bank_bca_logo ? (
                <img src={settings.bank_bca_logo} alt="BCA" className="w-full h-full object-contain drop-shadow-sm" />
              ) : (
                <img src="https://mgoutxmbncyoeeisosrx.supabase.co/storage/v1/object/public/cgve9jbd8q9t_tour_images/uploads/bca-logo.png" alt="BCA" className="w-full h-full object-contain grayscale-[0.2] opacity-80 mix-blend-multiply" onError={(e) => e.currentTarget.style.display = 'none'} />
              )}
            </button>
            )}
            {hasSeabank && (
            <button
              onClick={() => setSelectedBank('seabank')}
              className={`flex-1 py-2 px-1 h-12 border rounded-xl flex items-center justify-center transition-all hover:bg-slate-50 border-slate-100 bg-white`}
            >
              {settings.bank_seabank_logo ? (
                <img src={settings.bank_seabank_logo} alt="SeaBank" className="w-full h-full object-contain drop-shadow-sm" />
              ) : (
                <img src="https://mgoutxmbncyoeeisosrx.supabase.co/storage/v1/object/public/cgve9jbd8q9t_tour_images/uploads/seabank-logo.png" alt="SeaBank" className="w-full h-full object-contain grayscale-[0.2] opacity-80 mix-blend-multiply" onError={(e) => e.currentTarget.style.display = 'none'} />
              )}
            </button>
            )}
            {hasPaypal && (
            <button
              onClick={() => setSelectedBank('paypal')}
              className={`flex-1 py-2 px-1 h-12 border rounded-xl flex items-center justify-center transition-all hover:bg-slate-50 border-slate-100 bg-white`}
            >
              {settings.bank_paypal_logo ? (
                <img src={settings.bank_paypal_logo} alt="PayPal" className="w-full h-full object-contain drop-shadow-sm" />
              ) : (
                <img src="https://mgoutxmbncyoeeisosrx.supabase.co/storage/v1/object/public/cgve9jbd8q9t_tour_images/uploads/paypal-logo.png" alt="PayPal" className="w-full h-full object-contain grayscale-[0.2] opacity-80 mix-blend-multiply" onError={(e) => e.currentTarget.style.display = 'none'} />
              )}
            </button>
            )}
          </div>
        </div>
        )}
        
        """
    content = content[:start_idx] + new_block + content[end_idx:]

with open('src/views/ProfileView.tsx', 'w') as f:
    f.write(content)
print("Updated ProfileView.tsx")
