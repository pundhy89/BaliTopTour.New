import React, { useState } from 'react';
import { useApp } from '../context/AppContext';
import { translate } from '../data/translations';
import { Globe, User, Phone, Settings as SettingsIcon, LogIn, ChevronRight, Edit2, ShieldAlert, Landmark, X, Copy } from 'lucide-react';

export default function ProfileView({ navigate }: { navigate: (to: string | number) => void }) {
  const {
    settings,
    language,
    setLanguage,
    userName,
    setUserName,
    isAdminLoggedIn,
    logoutAdmin
  } = useApp();

  const [isEditingName, setIsEditingName] = useState(false);
  const [nameInput, setNameInput] = useState(userName);
  const [selectedBank, setSelectedBank] = useState<string | null>(null);
  const hasBca = !!(settings.bank_bca_number || settings.bank_bca_logo);
  const hasSeabank = !!(settings.bank_seabank_number || settings.bank_seabank_logo);
  const hasPaypal = !!(settings.bank_paypal_number || settings.bank_paypal_logo);
  const hasAnyBank = hasBca || hasSeabank || hasPaypal;


  const handleNameSave = () => {
    if (nameInput.trim()) {
      setUserName(nameInput.trim());
    }
    setIsEditingName(false);
  };

  const handleWhatsAppContact = () => {
    const num = settings.whatsapp_number || '6282143415254';
    const msg = encodeURIComponent(`Halo Bali Top Tour, saya ingin bertanya lebih lanjut tentang paket wisata Bali.`);
    window.open(`https://wa.me/${num}?text=${msg}`, '_blank');
  };

  const languages: { code: 'id' | 'en' | 'zh'; label: string }[] = [
    { code: 'id', label: 'Indonesian (ID)' },
    { code: 'en', label: 'English (EN)' },
    { code: 'zh', label: 'Chinese (中)' }
  ];

  const primaryBg = { backgroundColor: settings.theme_color };
  const primaryText = { color: settings.theme_color };
  const primaryBorder = { borderColor: settings.theme_color };

  return (
    <div className="flex-1 pb-24 overflow-y-auto px-5 pt-6 bg-slate-50/50">
      {/* Header */}
      <div className="mb-6">
        <h2 className="text-slate-950 font-bold text-xl tracking-tight">
          {translate('nav_profile', language)}
        </h2>
      </div>

      {/* User Info Card */}
      <div className="bg-white rounded-[28px] border border-slate-100 p-5 shadow-sm mb-6 flex flex-col items-center mt-8">
        
        {/* Floating Speech Bubble & Profile Image */}
        <div className="relative flex justify-center mb-3">
          <div className="absolute -top-12 animate-bounce bg-white px-3 py-2 border border-slate-100 shadow-sm rounded-2xl text-[10px] font-semibold text-slate-600 max-w-[200px] w-max text-center z-10 before:content-[''] before:absolute before:bottom-[-6px] before:left-1/2 before:-translate-x-1/2 before:w-3 before:h-3 before:bg-white before:border-r before:border-b before:border-slate-100 before:rotate-45">
            {language === 'zh' ? settings.profile_speech_text_zh : language === 'en' ? settings.profile_speech_text_en : settings.profile_speech_text_id}
          </div>

          <div className="w-24 h-24 rounded-full bg-slate-100 border-4 border-white flex items-center justify-center text-slate-400 text-xl font-bold shadow-md overflow-hidden relative z-0">
            {settings.profile_logo_url ? (
              <img src={settings.profile_logo_url} alt="Profile" className="w-full h-full object-cover" />
            ) : (
              <User size={32} />
            )}
          </div>
        </div>

        {isEditingName ? (
          <div className="flex gap-2 w-full max-w-[240px] mt-1">
            <input
              type="text"
              value={nameInput}
              onChange={e => setNameInput(e.target.value)}
              className="flex-1 bg-slate-50 border border-slate-200 outline-none text-xs font-bold text-slate-800 rounded-xl px-2.5 py-1.5 focus:border-indigo-500 text-center"
              maxLength={30}
            />
            <button
              onClick={handleNameSave}
              className="text-white text-[10px] font-bold px-3 rounded-xl transition-all shadow-sm uppercase active:scale-95"
              style={primaryBg}
            >
              Simpan
            </button>
          </div>
        ) : (
          <div className="flex items-center gap-1.5 mt-1">
            <h3 className="text-slate-800 font-bold text-sm">
              {userName || 'Guest'}
            </h3>
            <button
              onClick={() => {
                setNameInput(userName);
                setIsEditingName(true);
              }}
              className="p-1 hover:text-indigo-600 text-slate-400 transition-all"
            >
              <Edit2 size={12} />
            </button>
          </div>
        )}

        <span 
          className="text-[9px] font-bold mt-1.5 tracking-wide text-center leading-relaxed" 
          style={primaryText}
        >
          {language === 'zh' ? '您的名字将自动显示在WhatsApp消息中 (预订者)' : language === 'en' ? 'Your name will automatically appear in WhatsApp messages (Booker)' : 'Nama Anda akan muncul otomatis di pesan whatsapp (Pemesan)'}
        </span>
      </div>

      {/* Menu Sections Grid */}
      <div className="flex flex-col gap-4">
        {/* Language Selection Setting */}
        <div className="bg-white rounded-3xl border border-slate-100 p-5 shadow-sm">
          <h4 className="text-slate-800 font-bold text-xs mb-1.5 flex items-center gap-2">
            <Globe size={15} style={primaryText} />
            {translate('profile_language', language)}
          </h4>
          <p className="text-slate-400 text-[10px] font-semibold mb-4 leading-relaxed">
            {translate('select_language_desc', language)}
          </p>
          <div className="bg-slate-50 border border-slate-100 p-1 rounded-2xl flex items-center w-full gap-1 shadow-inner">
            {languages.map(lang => {
              const isSelected = language === lang.code;
              return (
                <button
                  key={lang.code}
                  onClick={() => setLanguage(lang.code)}
                  className={`flex-1 py-2.5 rounded-xl text-xs font-black transition-all duration-250 text-center cursor-pointer ${
                    isSelected
                      ? 'bg-white text-slate-900 shadow-[0_3px_12px_rgba(0,0,0,0.04)] scale-[1.02]'
                      : 'text-slate-450 hover:text-slate-700 hover:bg-slate-100/50'
                  }`}
                  style={isSelected ? { color: settings.theme_color } : {}}
                >
                  {lang.code === 'id' ? '🇺🇩 ID' : lang.code === 'en' ? '🇬🇧 EN' : '🇨🇳 ZH'}
                </button>
              );
            })}
          </div>
        </div>

        {/* Contact Support Option */}
        <button
          onClick={handleWhatsAppContact}
          className="bg-white rounded-3xl border border-slate-100 p-4.5 shadow-sm text-left flex items-center justify-between hover:bg-slate-50/50 active:scale-[0.99] transition-all"
        >
          <div className="flex items-center gap-3">
            <div className="p-2.5 bg-emerald-50 rounded-2xl text-emerald-600">
              <Phone size={16} />
            </div>
            <div>
              <h4 className="text-slate-800 font-bold text-xs">
                {translate('profile_contact', language)}
              </h4>
              <p className="text-slate-400 text-[10px] font-bold mt-0.5">
                +{settings.whatsapp_number || '6282143415254'}
              </p>
            </div>
          </div>
          <ChevronRight size={16} className="text-slate-400" />
        </button>

        {/* Metode Pembayaran */}
        {hasAnyBank && (
        <div className="bg-white rounded-3xl border border-slate-100 p-5 shadow-sm">
          <h4 className="text-slate-800 font-bold text-xs mb-1.5 flex items-center gap-2">
            <Landmark size={15} style={primaryText} />
            {translate('payment_method', language)}
          </h4>
          <p className="text-slate-400 text-[10px] font-semibold mb-4 leading-relaxed">
            {translate('payment_method_desc', language)}
          </p>
          <div className="flex gap-2">
            {hasBca && (
            <button
              onClick={() => setSelectedBank('bca')}
              className={`flex-1 py-2 px-1 h-12 border rounded-xl flex items-center justify-center transition-all hover:bg-slate-50 border-slate-100 bg-white`}
            >
              {settings.bank_bca_logo ? (
                <img src={settings.bank_bca_logo} alt="BCA" className="h-5 w-auto object-contain drop-shadow-sm" />
              ) : (
                <img src="https://mgoutxmbncyoeeisosrx.supabase.co/storage/v1/object/public/cgve9jbd8q9t_tour_images/uploads/bca-logo.png" alt="BCA" className="h-5 w-auto object-contain grayscale-[0.2] opacity-80 mix-blend-multiply" onError={(e) => e.currentTarget.style.display = 'none'} />
              )}
            </button>
            )}
            {hasSeabank && (
            <button
              onClick={() => setSelectedBank('seabank')}
              className={`flex-1 py-2 px-1 h-12 border rounded-xl flex items-center justify-center transition-all hover:bg-slate-50 border-slate-100 bg-white`}
            >
              {settings.bank_seabank_logo ? (
                <img src={settings.bank_seabank_logo} alt="SeaBank" className="h-5 w-auto object-contain drop-shadow-sm" />
              ) : (
                <img src="https://mgoutxmbncyoeeisosrx.supabase.co/storage/v1/object/public/cgve9jbd8q9t_tour_images/uploads/seabank-logo.png" alt="SeaBank" className="h-5 w-auto object-contain grayscale-[0.2] opacity-80 mix-blend-multiply" onError={(e) => e.currentTarget.style.display = 'none'} />
              )}
            </button>
            )}
            {hasPaypal && (
            <button
              onClick={() => setSelectedBank('paypal')}
              className={`flex-1 py-2 px-1 h-12 border rounded-xl flex items-center justify-center transition-all hover:bg-slate-50 border-slate-100 bg-white`}
            >
              {settings.bank_paypal_logo ? (
                <img src={settings.bank_paypal_logo} alt="PayPal" className="h-5 w-auto object-contain drop-shadow-sm" />
              ) : (
                <img src="https://mgoutxmbncyoeeisosrx.supabase.co/storage/v1/object/public/cgve9jbd8q9t_tour_images/uploads/paypal-logo.png" alt="PayPal" className="h-5 w-auto object-contain grayscale-[0.2] opacity-80 mix-blend-multiply" onError={(e) => e.currentTarget.style.display = 'none'} />
              )}
            </button>
            )}
          </div>
        </div>
        )}
        
        {selectedBank && (
          <div className="fixed inset-0 z-[100] flex items-center justify-center p-4 bg-slate-900/40 backdrop-blur-sm animate-in fade-in duration-200">
            <div className="bg-white rounded-[28px] w-full max-w-sm overflow-hidden shadow-2xl animate-in zoom-in-95 duration-300">
              <div className="p-5 border-b border-slate-100 flex items-center justify-between">
                <h3 className="font-extrabold text-slate-800 text-sm flex items-center gap-2">
                  <Landmark size={18} className="text-indigo-600" />
                  Informasi Rekening
                </h3>
                <button onClick={() => setSelectedBank(null)} className="p-2 bg-slate-100 text-slate-500 hover:text-slate-700 rounded-full transition-colors">
                  <X size={16} />
                </button>
              </div>
              <div className="p-6 flex flex-col items-center">
                {selectedBank === 'bca' && (
                  <>
                    {settings.bank_bca_logo ? (
                      <img src={settings.bank_bca_logo} alt="BCA" className="w-full max-w-[140px] h-12 mb-4 object-contain drop-shadow-md" />
                    ) : (
                      <div className="w-16 h-16 bg-blue-100 text-blue-600 rounded-2xl flex items-center justify-center font-black text-xl mb-4">BCA</div>
                    )}
                    <p className="text-[10px] font-bold text-slate-400 uppercase tracking-widest mb-1">Nomor Rekening</p>
                    <div className="flex items-center gap-2 mb-2">
                      <p className="text-2xl font-black text-slate-800 tracking-tight">{settings.bank_bca_number || '-'}</p>
                      <button onClick={() => navigator.clipboard.writeText(settings.bank_bca_number || '')} className="p-1.5 text-slate-400 hover:text-indigo-600 transition-colors"><Copy size={16} /></button>
                    </div>
                    <p className="text-xs font-bold text-slate-500">a.n. <span className="text-slate-700">{settings.bank_bca_name || '-'}</span></p>
                  </>
                )}
                {selectedBank === 'seabank' && (
                  <>
                    {settings.bank_seabank_logo ? (
                      <img src={settings.bank_seabank_logo} alt="SeaBank" className="w-full max-w-[140px] h-12 mb-4 object-contain drop-shadow-md" />
                    ) : (
                      <div className="w-16 h-16 bg-orange-100 text-orange-600 rounded-2xl flex items-center justify-center font-black text-xl mb-4">SB</div>
                    )}
                    <p className="text-[10px] font-bold text-slate-400 uppercase tracking-widest mb-1">Nomor Rekening</p>
                    <div className="flex items-center gap-2 mb-2">
                      <p className="text-2xl font-black text-slate-800 tracking-tight">{settings.bank_seabank_number || '-'}</p>
                      <button onClick={() => navigator.clipboard.writeText(settings.bank_seabank_number || '')} className="p-1.5 text-slate-400 hover:text-indigo-600 transition-colors"><Copy size={16} /></button>
                    </div>
                    <p className="text-xs font-bold text-slate-500">a.n. <span className="text-slate-700">{settings.bank_seabank_name || '-'}</span></p>
                  </>
                )}
                {selectedBank === 'paypal' && (
                  <>
                    {settings.bank_paypal_logo ? (
                      <img src={settings.bank_paypal_logo} alt="PayPal" className="w-full max-w-[140px] h-12 mb-4 object-contain drop-shadow-md" />
                    ) : (
                      <div className="w-16 h-16 bg-sky-100 text-sky-600 rounded-2xl flex items-center justify-center font-black text-xl mb-4">PP</div>
                    )}
                    <p className="text-[10px] font-bold text-slate-400 uppercase tracking-widest mb-1">Akun PayPal</p>
                    <div className="flex items-center gap-2 mb-2">
                      <p className="text-xl font-black text-slate-800 tracking-tight">{settings.bank_paypal_number || '-'}</p>
                      <button onClick={() => navigator.clipboard.writeText(settings.bank_paypal_number || '')} className="p-1.5 text-slate-400 hover:text-indigo-600 transition-colors"><Copy size={16} /></button>
                    </div>
                    <p className="text-xs font-bold text-slate-500">a.n. <span className="text-slate-700">{settings.bank_paypal_name || '-'}</span></p>
                  </>
                )}
              </div>
            </div>
          </div>
        )}

        {/* Admin Portal Nav option */}
        <button
          onClick={() => navigate(isAdminLoggedIn ? '/admin' : '/admin/login')}
          className="bg-white rounded-3xl border border-slate-100 p-4.5 shadow-sm text-left flex items-center justify-between hover:bg-slate-50/50 active:scale-[0.99] transition-all"
        >
          <div className="flex items-center gap-3">
            <div 
              className="p-2.5 rounded-2xl"
              style={{ backgroundColor: `${settings.theme_color}08`, color: settings.theme_color }}
            >
              {isAdminLoggedIn ? <SettingsIcon size={16} /> : <LogIn size={16} />}
            </div>
            <div>
              <h4 className="text-slate-800 font-bold text-xs">
                {isAdminLoggedIn 
                  ? (language === 'zh' ? '管理面板' : language === 'en' ? 'Admin Dashboard' : 'Dashboard Admin')
                  : translate('profile_admin_panel', language)}
              </h4>
            </div>
          </div>
          <ChevronRight size={16} className="text-slate-400" />
        </button>

        {/* Log Out Admin Option if logged in */}
        {isAdminLoggedIn && (
          <button
            onClick={logoutAdmin}
            className="w-full bg-red-50 hover:bg-red-100 border border-red-100 text-red-600 font-bold py-3 px-4 rounded-2xl text-xs uppercase tracking-wider flex items-center justify-center gap-2 transition-all active:scale-95 shadow-sm"
          >
            <ShieldAlert size={15} />
            {language === 'zh' ? '退出管理员' : language === 'en' ? 'Logout Admin' : 'Keluar Sebagai Admin'}
          </button>
        )}

        {/* Version Footer */}
        <div className="text-center mt-6">
          <span className="text-[10px] text-slate-400 font-bold uppercase tracking-wider">
            {translate('profile_version', language)} 3.0.0 (BaliTopTour)
          </span>
        </div>
      </div>
    </div>
  );
}