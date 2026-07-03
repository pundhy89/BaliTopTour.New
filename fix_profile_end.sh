sed -i '265,275c\
                    <p className="text-xs font-bold text-slate-500">a.n. <span className="text-slate-700">{settings.bank_paypal_name || '"'"'-'"'"'}</span></p>\
                  </>\
                )}\
              </div>\
            </div>\
          </div>\
        )}\
\
        {/* Admin Portal Nav option */}' src/views/ProfileView.tsx
