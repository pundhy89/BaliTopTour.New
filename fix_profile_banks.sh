sed -i '4c\
import { Globe, User, Phone, Settings as SettingsIcon, LogIn, ChevronRight, Edit2, ShieldAlert, Landmark, X, Copy } from '"'"'lucide-react'"'"';' src/views/ProfileView.tsx
sed -i '181,217c\
          <div className="flex gap-2">\
            <button\
              onClick={() => setSelectedBank('"'"'bca'"'"')}\
              className={`flex-1 py-2 border rounded-xl flex flex-col items-center justify-center font-extrabold text-[10px] transition-all hover:bg-slate-50 border-slate-100 text-slate-500`}\
            >\
              {settings.bank_bca_logo ? (\
                <img src={settings.bank_bca_logo} alt="BCA" className="h-5 mb-1 object-contain" />\
              ) : (\
                <img src="https://mgoutxmbncyoeeisosrx.supabase.co/storage/v1/object/public/cgve9jbd8q9t_tour_images/uploads/bca-logo.png" alt="BCA" className="h-4 mb-1 object-contain grayscale-[0.2] opacity-80 mix-blend-multiply" onError={(e) => e.currentTarget.style.display = '"'"'none'"'"'} />\
              )}\
              <span>BCA</span>\
            </button>\
            <button\
              onClick={() => setSelectedBank('"'"'seabank'"'"')}\
              className={`flex-1 py-2 border rounded-xl flex flex-col items-center justify-center font-extrabold text-[10px] transition-all hover:bg-slate-50 border-slate-100 text-slate-500`}\
            >\
              {settings.bank_seabank_logo ? (\
                <img src={settings.bank_seabank_logo} alt="SeaBank" className="h-5 mb-1 object-contain" />\
              ) : (\
                <img src="https://mgoutxmbncyoeeisosrx.supabase.co/storage/v1/object/public/cgve9jbd8q9t_tour_images/uploads/seabank-logo.png" alt="SeaBank" className="h-4 mb-1 object-contain grayscale-[0.2] opacity-80 mix-blend-multiply" onError={(e) => e.currentTarget.style.display = '"'"'none'"'"'} />\
              )}\
              <span>SEABANK</span>\
            </button>\
            <button\
              onClick={() => setSelectedBank('"'"'paypal'"'"')}\
              className={`flex-1 py-2 border rounded-xl flex flex-col items-center justify-center font-extrabold text-[10px] transition-all hover:bg-slate-50 border-slate-100 text-slate-500`}\
            >\
              {settings.bank_paypal_logo ? (\
                <img src={settings.bank_paypal_logo} alt="PayPal" className="h-5 mb-1 object-contain" />\
              ) : (\
                <img src="https://mgoutxmbncyoeeisosrx.supabase.co/storage/v1/object/public/cgve9jbd8q9t_tour_images/uploads/paypal-logo.png" alt="PayPal" className="h-4 mb-1 object-contain grayscale-[0.2] opacity-80 mix-blend-multiply" onError={(e) => e.currentTarget.style.display = '"'"'none'"'"'} />\
              )}\
              <span>PAYPAL</span>\
            </button>\
          </div>\
        </div>\
\
        {selectedBank && (\
          <div className="fixed inset-0 z-[100] flex items-center justify-center p-4 bg-slate-900/40 backdrop-blur-sm animate-in fade-in duration-200">\
            <div className="bg-white rounded-[28px] w-full max-w-sm overflow-hidden shadow-2xl animate-in zoom-in-95 duration-300">\
              <div className="p-5 border-b border-slate-100 flex items-center justify-between">\
                <h3 className="font-extrabold text-slate-800 text-sm flex items-center gap-2">\
                  <Landmark size={18} className="text-indigo-600" />\
                  Informasi Rekening\
                </h3>\
                <button onClick={() => setSelectedBank(null)} className="p-2 bg-slate-100 text-slate-500 hover:text-slate-700 rounded-full transition-colors">\
                  <X size={16} />\
                </button>\
              </div>\
              <div className="p-6 flex flex-col items-center">\
                {selectedBank === '"'"'bca'"'"' && (\
                  <>\
                    {settings.bank_bca_logo ? (\
                      <img src={settings.bank_bca_logo} alt="BCA" className="h-10 mb-4 object-contain" />\
                    ) : (\
                      <div className="w-16 h-16 bg-blue-100 text-blue-600 rounded-2xl flex items-center justify-center font-black text-xl mb-4">BCA</div>\
                    )}\
                    <p className="text-[10px] font-bold text-slate-400 uppercase tracking-widest mb-1">Nomor Rekening</p>\
                    <div className="flex items-center gap-2 mb-2">\
                      <p className="text-2xl font-black text-slate-800 tracking-tight">{settings.bank_bca_number || '"'"'-'"'"'}</p>\
                      <button onClick={() => navigator.clipboard.writeText(settings.bank_bca_number || '"'"''"'"')} className="p-1.5 text-slate-400 hover:text-indigo-600 transition-colors"><Copy size={16} /></button>\
                    </div>\
                    <p className="text-xs font-bold text-slate-500">a.n. <span className="text-slate-700">{settings.bank_bca_name || '"'"'-'"'"'}</span></p>\
                  </>\
                )}\
                {selectedBank === '"'"'seabank'"'"' && (\
                  <>\
                    {settings.bank_seabank_logo ? (\
                      <img src={settings.bank_seabank_logo} alt="SeaBank" className="h-10 mb-4 object-contain" />\
                    ) : (\
                      <div className="w-16 h-16 bg-orange-100 text-orange-600 rounded-2xl flex items-center justify-center font-black text-xl mb-4">SB</div>\
                    )}\
                    <p className="text-[10px] font-bold text-slate-400 uppercase tracking-widest mb-1">Nomor Rekening</p>\
                    <div className="flex items-center gap-2 mb-2">\
                      <p className="text-2xl font-black text-slate-800 tracking-tight">{settings.bank_seabank_number || '"'"'-'"'"'}</p>\
                      <button onClick={() => navigator.clipboard.writeText(settings.bank_seabank_number || '"'"''"'"')} className="p-1.5 text-slate-400 hover:text-indigo-600 transition-colors"><Copy size={16} /></button>\
                    </div>\
                    <p className="text-xs font-bold text-slate-500">a.n. <span className="text-slate-700">{settings.bank_seabank_name || '"'"'-'"'"'}</span></p>\
                  </>\
                )}\
                {selectedBank === '"'"'paypal'"'"' && (\
                  <>\
                    {settings.bank_paypal_logo ? (\
                      <img src={settings.bank_paypal_logo} alt="PayPal" className="h-10 mb-4 object-contain" />\
                    ) : (\
                      <div className="w-16 h-16 bg-sky-100 text-sky-600 rounded-2xl flex items-center justify-center font-black text-xl mb-4">PP</div>\
                    )}\
                    <p className="text-[10px] font-bold text-slate-400 uppercase tracking-widest mb-1">Akun PayPal</p>\
                    <div className="flex items-center gap-2 mb-2">\
                      <p className="text-xl font-black text-slate-800 tracking-tight">{settings.bank_paypal_number || '"'"'-'"'"'}</p>\
                      <button onClick={() => navigator.clipboard.writeText(settings.bank_paypal_number || '"'"''"'"')} className="p-1.5 text-slate-400 hover:text-indigo-600 transition-colors"><Copy size={16} /></button>\
                    </div>\
                    <p className="text-xs font-bold text-slate-500">a.n. <span className="text-slate-700">{settings.bank_paypal_name || '"'"'-'"'"'}</span></p>\
                  </>\
                )}\
              </div>\
            </div>\
          </div>\
        )}' src/views/ProfileView.tsx
