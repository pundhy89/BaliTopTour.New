import React, { useState, useRef, useMemo } from 'react';
import { useApp } from '../context/AppContext';
import { translate } from '../data/translations';
import { MapPin, Navigation, Star, ArrowRight, List, LayoutGrid } from 'lucide-react';
import mapBg from '../assets/images/bali_tourist_map_1782285564594.jpg';

export default function MapView({ navigate }: { navigate: (to: string | number) => void }) {
  const { settings, language, activities } = useApp();
  const scrollContainerRef = useRef<HTMLDivElement>(null);

  // All active activities sorted by sort_order
  const sortedActiveActivities = useMemo(() => {
    return [...activities]
      .filter(a => a.is_active)
      .sort((a, b) => (a.sort_order ?? 0) - (b.sort_order ?? 0));
  }, [activities]);

  // Filter activities that have coordinates and are active
  const mapActivities = useMemo(() => {
    return sortedActiveActivities.filter(a => a.latitude !== null && a.longitude !== null);
  }, [sortedActiveActivities]);

  const [selectedAct, setSelectedAct] = useState<any>(mapActivities[0] || null);
  const [viewMode, setViewMode] = useState<'list' | 'thumbnail'>('list');

  const getEntityName = (item: any) => {
    if (language === 'en') return item.name_en || item.name_id;
    if (language === 'zh') return item.name_zh || item.name_id;
    return item.name_id;
  };

  const getEntityDesc = (item: any) => {
    if (language === 'en') return item.description_en || item.description_id;
    if (language === 'zh') return item.description_zh || item.description_id;
    return item.description_id;
  };

  // Hardcoded positions and styles for the 16 map activities based on illustration map
  const getPinConfig = (name: string) => {
    const pinConfigs: Record<string, { num: number; x: number; y: number; colorClass: string }> = {
      'Waterboom Park': { num: 1, x: 39.5, y: 66.5, colorClass: 'bg-blue-500 border-white text-white' },
      'ATV Adventure': { num: 2, x: 45, y: 37.5, colorClass: 'bg-orange-500 border-white text-white' },
      'Elephant Ride': { num: 3, x: 61.5, y: 52, colorClass: 'bg-blue-500 border-white text-white' },
      'Bali Bird Park & Reptile Park': { num: 4, x: 52.5, y: 44, colorClass: 'bg-purple-500 border-white text-white' },
      'Bali Hai Cruise': { num: 5, x: 70, y: 77.5, colorClass: 'bg-purple-500 border-white text-white' },
      'Mount Batur Sunrise Trekking': { num: 6, x: 65, y: 24.5, colorClass: 'bg-orange-500 border-white text-white' },
      'Paragliding Bali': { num: 7, x: 84.5, y: 63.5, colorClass: 'bg-pink-500 border-white text-white' },
      'Rafting': { num: 8, x: 37.5, y: 34, colorClass: 'bg-cyan-500 border-white text-white' },
      'Mount Batur Jeep Sunrise': { num: 9, x: 74.5, y: 21.5, colorClass: 'bg-pink-500 border-white text-white' },
      'Horse Riding': { num: 10, x: 32.5, y: 47, colorClass: 'bg-blue-500 border-white text-white' },
      'Cycling Adventure': { num: 11, x: 58.5, y: 31.5, colorClass: 'bg-green-500 border-white text-white' },
      'Water Sport': { num: 12, x: 66, y: 68, colorClass: 'bg-blue-500 border-white text-white' },
      'Bali Safari Park': { num: 13, x: 45, y: 53, colorClass: 'bg-yellow-500 border-white text-white' },
      'Bali Zoo': { num: 14, x: 32, y: 8, colorClass: 'bg-purple-500 border-white text-white' },
      'Diving': { num: 15, x: 97, y: 45, colorClass: 'bg-blue-500 border-white text-white' },
      'Marine Safari Bali': { num: 16, x: 53, y: 81.5, colorClass: 'bg-blue-500 border-white text-white' }
    };

    const baseName = name || '';
    if (pinConfigs[baseName]) return pinConfigs[baseName];

    for (const [key, val] of Object.entries(pinConfigs)) {
      if (baseName.includes(key)) return val;
    }

    return { num: 0, x: 50, y: 50, colorClass: 'bg-white border-slate-300 text-slate-700' };
  };

  const selectAndScrollToTop = (act: any) => {
    setSelectedAct(act);
    if (scrollContainerRef.current) {
      scrollContainerRef.current.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    }
  };

  const handleOpenGmaps = (act: any) => {
    const url = `https://www.google.com/maps/search/?api=1&query=${act.latitude},${act.longitude}`;
    window.open(url, '_blank');
  };

  const primaryBg = { backgroundColor: settings.theme_color };
  const primaryText = { color: settings.theme_color };

  return (
    <div ref={scrollContainerRef} className="flex-1 pb-24 overflow-y-auto flex flex-col bg-slate-50 scroll-smooth">
      {/* Map Header with 2 View Choices Toggle */}
      <div className="px-5 pt-6 pb-3 bg-white border-b border-slate-100 flex justify-between items-center shrink-0">
        <div>
          <h2 className="text-slate-950 font-bold text-xl tracking-tight">
            {translate('map_title', language)}
          </h2>
          <p className="text-slate-400 text-xs font-semibold mt-0.5">
            {translate('all_activities', language)} ({sortedActiveActivities.length})
          </p>
        </div>

        {/* ONLY 2 choices as requested: List mode and Thumbnail mode */}
        <div className="bg-slate-100 p-1 rounded-full flex items-center gap-0.5 border border-slate-200/50 shadow-sm shrink-0">
          <button
            onClick={() => setViewMode('list')}
            className={`p-2 rounded-full transition-all duration-300 flex items-center justify-center ${
              viewMode === 'list'
                ? 'text-white shadow-sm'
                : 'text-slate-400 hover:text-slate-600'
            }`}
            style={viewMode === 'list' ? primaryBg : {}}
            title={language === 'zh' ? '列表视图' : language === 'en' ? 'List View' : 'Tampilan List'}
          >
            <List size={15} />
          </button>
          <button
            onClick={() => setViewMode('thumbnail')}
            className={`p-2 rounded-full transition-all duration-300 flex items-center justify-center ${
              viewMode === 'thumbnail'
                ? 'text-white shadow-sm'
                : 'text-slate-400 hover:text-slate-600'
            }`}
            style={viewMode === 'thumbnail' ? primaryBg : {}}
            title={language === 'zh' ? '网格视图' : language === 'en' ? 'Thumbnail View' : 'Tampilan Grid'}
          >
            <LayoutGrid size={15} />
          </button>
        </div>
      </div>

      {/* TOP SECTION: Always Active Interactive Vector Map on Bali */}
      <div className="bg-white p-4 border-b border-slate-100 flex flex-col items-center shrink-0">
        <div className="w-full max-w-[360px] aspect-[4/3] rounded-3xl bg-indigo-50/20 relative overflow-hidden border border-slate-100/80 shadow-md flex items-center justify-center">
          {/* Custom generated map background image */}
          <img
            src={settings.map_image_url || mapBg}
            alt="Bali Tourist Map"
            className="absolute inset-0 w-full h-full object-cover select-none brightness-[0.95] contrast-[1.05]"
            referrerPolicy="no-referrer"
          />

          {/* Semi-transparent overlay to help the interactive pins pop */}
          <div className="absolute inset-0 bg-slate-900/5 pointer-events-none" />

          {/* Circular Interactive Pins */}
          {mapActivities.map(act => {
            const fallbackPin = getPinConfig(act.name_id);
            const num = act.pin_number !== undefined ? act.pin_number : fallbackPin.num;
            const pinColor = act.pin_color || 'blue';
            
            const colorClass = pinColor === 'blue' ? 'bg-blue-500 border-white text-white' :
                               pinColor === 'teal' ? 'bg-teal-500 border-white text-white' :
                               pinColor === 'orange' ? 'bg-orange-500 border-white text-white' :
                               pinColor === 'pink' ? 'bg-pink-500 border-white text-white' :
                               pinColor === 'purple' ? 'bg-purple-500 border-white text-white' :
                               'bg-red-600 border-white text-white';

            const isSelected = selectedAct?.id === act.id;

            let left = 50;
            let top = 50;
            if (act.map_x !== undefined && act.map_y !== undefined) {
              left = act.map_x;
              top = act.map_y;
            } else {
              const minLng = 114.4;
              const maxLng = 115.7;
              const minLat = -8.05;
              const maxLat = -8.90;
              
              const xPercent = (((act.longitude || 0) - minLng) / (maxLng - minLng)) * 100;
              const yPercent = (((act.latitude || 0) - minLat) / (maxLat - minLat)) * 100;

              left = Math.min(Math.max(0, xPercent), 100);
              top = Math.min(Math.max(0, yPercent), 100);
            }

            return (
              <button
                key={act.id}
                onClick={() => selectAndScrollToTop(act)}
                className="absolute transition-all active:scale-125 z-10"
                style={{
                  left: `${left}%`,
                  top: `${top}%`,
                  transform: 'translate(-50%, -100%)'
                }}
              >
                <div className="flex flex-col items-center">
                  <div 
                    className={`p-1.5 min-w-[24px] h-[24px] rounded-full shadow-md flex items-center justify-center transition-all border-[1.5px] ${
                      isSelected 
                        ? `text-white scale-110 shadow-indigo-200 border-indigo-500 bg-indigo-500` 
                        : `${colorClass} hover:scale-105`
                    }`}
                    style={isSelected ? primaryBg : {}}
                  >
                    <span className="text-[11px] font-black leading-none" style={{ textShadow: '0px 1px 2px rgba(0,0,0,0.3)' }}>{num > 0 ? num : <MapPin size={12} />}</span>
                  </div>
                  {/* Subtle triangle point */}
                  <div 
                    className={`w-2 h-2 rotate-45 -mt-1.5 shadow-sm border-r border-b ${
                      isSelected ? 'border-indigo-500 bg-indigo-500' : colorClass.replace('text-white', '').replace('border-white', 'border-transparent')
                    }`}
                    style={isSelected ? primaryBg : {}}
                  />
                  
                  {/* Tiny text flag for selected landmarks */}
                  {isSelected && (
                    <div className="bg-slate-900/90 text-white font-bold text-[8px] py-1 px-2 rounded mt-1 shadow-md truncate max-w-[100px]">
                      {getEntityName(act)}
                    </div>
                  )}
                </div>
              </button>
            );
          })}
        </div>

        {/* Selected Activity Detail Box right below the map overlay */}
        {selectedAct && (
          <div className="w-full max-w-[360px] mt-4 animate-fade-in">
            <div className="bg-slate-50 border border-slate-100 rounded-2xl p-3 text-left">
              <div className="flex gap-3">
                <img
                  src={selectedAct.cover_image_url}
                  alt={getEntityName(selectedAct)}
                  className="w-14 h-14 rounded-xl object-cover bg-slate-100 flex-shrink-0"
                />
                <div className="flex-1 min-w-0 flex flex-col justify-between py-0.5">
                  <div>
                    <div className="flex items-center justify-between gap-1.5">
                      <span 
                        className="text-[8px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-md"
                        style={{ 
                          backgroundColor: `${settings.theme_color}10`,
                          color: settings.theme_color 
                        }}
                      >
                        {selectedAct.location_name || 'Bali'}
                      </span>
                      <div className="flex items-center gap-1">
                        <Star size={10} fill="#F59E0B" className="text-amber-500" />
                        <span className="text-amber-700 text-[9px] font-bold">
                          {selectedAct.rating || '5.0'}
                        </span>
                      </div>
                    </div>
                    <h3 className="font-bold text-slate-900 text-xs mt-1 truncate">
                      {getEntityName(selectedAct)}
                    </h3>
                  </div>

                  <div className="flex items-baseline justify-between mt-0.5">
                    <span 
                      style={{ color: settings.theme_color }} 
                      className="font-bold text-[11px]"
                    >
                      Rp {selectedAct.price_per_person_idr?.toLocaleString('id-ID') || '100000'} {selectedAct.price_mode === 'per_person' ? (language === 'zh' ? ' / 人' : language === 'en' ? ' / person' : ' / orang') : ''}
                    </span>
                  </div>
                </div>
              </div>

              {/* Action utilities */}
              <div className="grid grid-cols-2 gap-2 mt-2 pt-2 border-t border-slate-200/50">
                <button
                  onClick={() => handleOpenGmaps(selectedAct)}
                  className="w-full bg-white border border-slate-200 hover:bg-slate-50 text-slate-700 font-bold py-1.5 px-2 rounded-xl text-[9px] uppercase tracking-wider flex items-center justify-center gap-1 transition-all"
                >
                  <Navigation size={10} className="text-slate-500" />
                  {translate('map_open_maps', language)}
                </button>
                <button
                  onClick={() => navigate(`/activity/${selectedAct.id}`)}
                  className="w-full text-white font-bold py-1.5 px-2 rounded-xl text-[9px] uppercase tracking-wider flex items-center justify-center gap-1 shadow-sm"
                  style={primaryBg}
                >
                  {language === 'zh' ? '详情' : 'Detail'}
                  <ArrowRight size={10} />
                </button>
              </div>
            </div>
          </div>
        )}
      </div>

      {/* BOTTOM SECTION: Display all activities in selected Layout view */}
      {viewMode === 'list' && (
        <div className="p-5 flex flex-col gap-4">
          {sortedActiveActivities.map(act => (
            <div 
              key={act.id} 
              onClick={() => selectAndScrollToTop(act)}
              className={`bg-white rounded-[24px] p-3 border shadow-[0_4px_12px_rgba(0,0,0,0.02)] hover:shadow-md transition-all active:scale-[0.99] flex gap-4 cursor-pointer text-left ${
                selectedAct?.id === act.id ? 'ring-2 ring-slate-200 border-indigo-200 bg-indigo-50/10' : 'border-slate-100'
              }`}
            >
              <img 
                src={act.cover_image_url} 
                alt={getEntityName(act)} 
                className="w-20 h-20 rounded-2xl object-cover bg-slate-50 flex-shrink-0 shadow-sm"
              />
              <div className="flex-1 min-w-0 flex flex-col justify-between py-0.5">
                <div>
                  <div className="flex justify-between items-start gap-1">
                    <span 
                      className="text-[8px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-md"
                      style={{ 
                        backgroundColor: `${settings.theme_color}10`,
                        color: settings.theme_color 
                      }}
                    >
                      {act.location_name || 'Bali'}
                    </span>
                    <div className="flex items-center gap-1">
                      <Star size={10} fill="#F59E0B" className="text-amber-500" />
                      <span className="text-amber-700 text-[9px] font-bold">{act.rating || '5.0'}</span>
                    </div>
                  </div>
                  <h3 className="font-bold text-slate-900 text-xs mt-1.5 truncate">
                    {getEntityName(act)}
                  </h3>
                  <p className="text-slate-400 text-[10px] font-semibold leading-normal line-clamp-2 mt-0.5">
                    {getEntityDesc(act)}
                  </p>
                </div>
                <div className="flex justify-between items-center mt-2 pt-1.5 border-t border-slate-50">
                  <span 
                    style={{ color: settings.theme_color }} 
                    className="text-[11px] font-bold"
                  >
                    Rp {act.price_per_person_idr?.toLocaleString('id-ID')}
                  </span>
                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      navigate(`/activity/${act.id}`);
                    }}
                    className="text-[9px] text-slate-400 font-bold uppercase flex items-center gap-1 hover:text-slate-600 transition-colors"
                  >
                    Detail <ArrowRight size={10} style={primaryText} />
                  </button>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}

      {/* Grid Thumbnail View Mode (Styled exactly like Tour Packages on homepage) */}
      {viewMode === 'thumbnail' && (
        <div className="p-5 grid grid-cols-2 gap-4 content-start">
          {sortedActiveActivities.map(act => (
            <button 
              key={act.id} 
              onClick={() => selectAndScrollToTop(act)}
              className={`flex flex-col bg-white rounded-3xl overflow-hidden border shadow-[0_5px_15px_rgba(0,0,0,0.03)] hover:shadow-md transition-all active:scale-[0.98] text-left ${
                selectedAct?.id === act.id ? 'ring-2 ring-slate-200 border-indigo-200' : 'border-slate-100'
              }`}
            >
              <div className="relative aspect-[4/3] overflow-hidden bg-slate-100">
                <img 
                  src={act.cover_image_url} 
                  alt={getEntityName(act)} 
                  className="w-full h-full object-cover hover:scale-105 transition-all duration-300"
                />
                <div className="absolute top-2.5 right-2.5 bg-black/60 backdrop-blur-md py-1 px-2.5 rounded-full text-white text-[9px] font-bold shadow-sm flex items-center gap-0.5">
                  <Star size={9} fill="#fff" className="text-white fill-white" />
                  {act.rating || '5.0'}
                </div>
              </div>
              
              <div className="p-3.5 flex flex-col justify-between flex-1">
                <div>
                  <h4 className="font-bold text-slate-900 text-xs tracking-tight line-clamp-2 min-h-[32px]">
                    {getEntityName(act)}
                  </h4>
                  <p className="text-slate-400 text-[10px] line-clamp-1 mt-1 font-semibold">
                    {getEntityDesc(act)}
                  </p>
                </div>
                
                <div className="mt-3.5 pt-2.5 border-t border-slate-100 flex items-center justify-between">
                  <div className="flex flex-col">
                    <span className="text-slate-400 text-[9px] uppercase tracking-wider font-bold">
                      {translate('home_starting_from', language)}
                    </span>
                    <span 
                      style={{ color: settings.theme_color }} 
                      className="font-bold text-xs mt-0.5"
                    >
                      Rp {act.price_per_person_idr?.toLocaleString('id-ID')}
                    </span>
                  </div>
                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      navigate(`/activity/${act.id}`);
                    }}
                    className="p-1 px-2.5 rounded-lg text-[9px] text-indigo-600 bg-indigo-50 hover:bg-indigo-100 transition-all font-bold"
                  >
                    Detail
                  </button>
                </div>
              </div>
            </button>
          ))}
        </div>
      )}
    </div>
  );
}
