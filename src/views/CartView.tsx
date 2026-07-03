import React from 'react';
import { useApp } from '../context/AppContext';
import { ArrowLeft, Trash2, Phone } from 'lucide-react';

export const CartView: React.FC<{ onBack: () => void }> = ({ onBack }) => {
  const { cart, removeFromCart, updateCartQuantity, clearCart, settings, language, userName, trackAction } = useApp();

  const totalHarga = cart.reduce((sum, item) => sum + (item.price * item.quantity), 0);

  const primaryBg = { backgroundColor: settings.theme_color };
  const primaryText = { color: settings.theme_color };

  const handleCheckout = () => {
    if (cart.length === 0) return;

    const num = settings.whatsapp_number || '6282143415254';
    const pemesan = userName || 'Guest';
    let textMsg = '';
    
    let baseMsg = `Halo, saya ${pemesan} ingin memesan:\n\n`;
    
    cart.forEach((item, idx) => {
      baseMsg += `${idx + 1}. ${item.name}\n`;
      if (item.options) baseMsg += `   Opsi: ${item.options}\n`;
      baseMsg += `   Harga: Rp ${(item.price * item.quantity).toLocaleString('id-ID')}\n\n`;
    });
    
    baseMsg += `Total Pembayaran: Rp ${totalHarga.toLocaleString('id-ID')}`;

    textMsg = baseMsg;

    if (settings.receipt_company_name) {
      let receipt = `\n\n==========================\n`;
      receipt += `  *${settings.receipt_company_name.toUpperCase()}*\n`;
      receipt += `==========================\n`;
      receipt += `*INVOICE / PESANAN*\n`;
      receipt += `Pemesan: ${pemesan}\n`;
      
      cart.forEach((item, idx) => {
        receipt += `${idx + 1}. ${item.name} (${item.options})\n`;
        receipt += `   Rp ${(item.price * item.quantity).toLocaleString('id-ID')}\n`;
      });
      
      receipt += `\nTotal: Rp ${totalHarga.toLocaleString('id-ID')}\n`;
      if (settings.receipt_footer) {
        receipt += `--------------------------\n`;
        receipt += `${settings.receipt_footer.replace('[NAMA_PEMESAN]', pemesan).replace('[NAMA PEMESAN]', pemesan)}\n`;
      }
      receipt += `==========================`;
      textMsg += receipt;
    }

    trackAction('checkout_cart', `Checkout ${cart.length} items with total Rp ${totalHarga}`);
    window.open(`https://wa.me/${num}?text=${encodeURIComponent(textMsg)}`, '_blank');
    clearCart();
  };

  return (
    <div className="flex-1 pb-28 overflow-y-auto bg-slate-50 relative min-h-screen">
      <div className="bg-white px-5 pt-8 pb-5 sticky top-0 z-40 border-b border-slate-100 shadow-sm flex items-center justify-between">
        <div className="flex items-center gap-3">
          <button 
            onClick={onBack}
            className="w-8 h-8 rounded-full bg-slate-50 flex items-center justify-center border border-slate-100 active:scale-95 transition-all text-slate-500"
          >
            <ArrowLeft size={16} />
          </button>
          <h2 className="text-slate-800 font-extrabold text-sm uppercase tracking-wider">
            {language === 'en' ? 'Shopping Cart' : language === 'zh' ? '购物车' : 'Keranjang'}
          </h2>
        </div>
      </div>

      <div className="p-5 flex flex-col gap-4">
        {cart.length === 0 ? (
          <div className="text-center py-10">
            <p className="text-slate-400 font-bold text-xs uppercase tracking-wider">
              {language === 'en' ? 'Your cart is empty' : language === 'zh' ? '您的购物车是空的' : 'Keranjang Anda kosong'}
            </p>
          </div>
        ) : (
          cart.map((item) => (
            <div key={item.id} className="bg-white rounded-3xl p-4 shadow-sm border border-slate-100 flex gap-4 items-center">
              {item.cover_image_url && (
                <div className="w-16 h-16 rounded-xl bg-slate-100 flex-shrink-0 overflow-hidden">
                  <img src={item.cover_image_url} className="w-full h-full object-cover" alt={item.name} />
                </div>
              )}
              <div className="flex-1 min-w-0">
                <h3 className="font-bold text-slate-800 text-xs truncate leading-tight mb-1">{item.name}</h3>
                {item.options && (
                  <p className="text-[10px] text-slate-500 font-bold mb-1 truncate">{item.options}</p>
                )}
                <p className="text-xs font-bold" style={primaryText}>
                  Rp {(item.price * item.quantity).toLocaleString('id-ID')}
                </p>
              </div>
              <div className="flex flex-col items-end gap-2 flex-shrink-0">
                <button 
                  onClick={() => removeFromCart(item.id)}
                  className="text-rose-400 p-1"
                >
                  <Trash2 size={14} />
                </button>
                <div className="flex items-center gap-2 bg-slate-50 border border-slate-100 rounded-lg p-0.5">
                  <button 
                    onClick={() => updateCartQuantity(item.id, item.quantity - 1)}
                    className="w-6 h-6 rounded bg-white text-slate-600 flex items-center justify-center font-bold shadow-sm"
                  >
                    -
                  </button>
                  <span className="text-[10px] font-bold w-4 text-center">{item.quantity}</span>
                  <button 
                    onClick={() => updateCartQuantity(item.id, item.quantity + 1)}
                    className="w-6 h-6 rounded bg-white text-slate-600 flex items-center justify-center font-bold shadow-sm"
                  >
                    +
                  </button>
                </div>
              </div>
            </div>
          ))
        )}
      </div>

      {cart.length > 0 && (
        <div className="fixed bottom-0 left-0 right-0 bg-white border-t border-slate-200 p-4 pb-6 z-50 flex justify-between items-center">
          <div>
            <span className="text-[9px] font-medium text-slate-400 block uppercase tracking-wider mb-1">
              Total
            </span>
            <span className="text-slate-900 font-bold text-base block leading-none">
              Rp {totalHarga.toLocaleString('id-ID')}
            </span>
          </div>
          <button 
            onClick={handleCheckout}
            className="py-3 px-6 rounded-2xl text-white font-bold text-xs uppercase tracking-wide active:scale-95 transition-transform shadow-md flex items-center gap-2"
            style={primaryBg}
          >
            <Phone size={14} />
            {language === 'en' ? 'Checkout' : language === 'zh' ? '结账' : 'Checkout WhatsApp'}
          </button>
        </div>
      )}
    </div>
  );
};
