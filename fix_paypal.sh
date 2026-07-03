sed -i '260,268c\
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
        )}\
        {/* Admin Portal Nav option */}\
        <button\
          onClick={() => navigate(isAdminLoggedIn ? '"'"'/admin'"'"' : '"'"'/admin/login'"'"')}' src/views/ProfileView.tsx
