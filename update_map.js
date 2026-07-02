const fs = require('fs');
const content = fs.readFileSync('src/views/MapView.tsx', 'utf-8');

const mapPinsConfig = `
  const pinConfigs: Record<string, { num: number; x: number; y: number; color: string; bgColor: string; borderColor: string }> = {
    'Waterboom Park': { num: 1, x: 48, y: 82, color: 'text-blue-700', bgColor: 'bg-blue-100', borderColor: 'border-blue-300' },
    'ATV Adventure': { num: 2, x: 52, y: 55, color: 'text-orange-700', bgColor: 'bg-orange-100', borderColor: 'border-orange-300' },
    'Elephant Ride': { num: 3, x: 53, y: 50, color: 'text-yellow-700', bgColor: 'bg-yellow-100', borderColor: 'border-yellow-300' },
    'Bali Bird Park & Reptile Park': { num: 4, x: 55, y: 65, color: 'text-green-700', bgColor: 'bg-green-100', borderColor: 'border-green-300' },
    'Bali Hai Cruise': { num: 5, x: 55, y: 85, color: 'text-pink-700', bgColor: 'bg-pink-100', borderColor: 'border-pink-300' },
    'Mount Batur Sunrise Trekking': { num: 6, x: 60, y: 35, color: 'text-purple-700', bgColor: 'bg-purple-100', borderColor: 'border-purple-300' },
    'Paragliding Bali': { num: 7, x: 42, y: 92, color: 'text-cyan-700', bgColor: 'bg-cyan-100', borderColor: 'border-cyan-300' },
    'Rafting': { num: 8, x: 51, y: 53, color: 'text-blue-700', bgColor: 'bg-blue-100', borderColor: 'border-blue-300' },
    'Mount Batur Jeep Sunrise': { num: 9, x: 61, y: 36, color: 'text-orange-700', bgColor: 'bg-orange-100', borderColor: 'border-orange-300' },
    'Horse Riding': { num: 10, x: 45, y: 75, color: 'text-yellow-700', bgColor: 'bg-yellow-100', borderColor: 'border-yellow-300' },
    'Cycling Adventure': { num: 11, x: 54, y: 45, color: 'text-pink-700', bgColor: 'bg-pink-100', borderColor: 'border-pink-300' },
    'Water Sport': { num: 12, x: 56, y: 86, color: 'text-cyan-700', bgColor: 'bg-cyan-100', borderColor: 'border-cyan-300' },
    'Bali Safari Park': { num: 13, x: 65, y: 65, color: 'text-green-700', bgColor: 'bg-green-100', borderColor: 'border-green-300' },
    'Bali Zoo': { num: 14, x: 54, y: 64, color: 'text-purple-700', bgColor: 'bg-purple-100', borderColor: 'border-purple-300' },
    'Diving': { num: 15, x: 85, y: 30, color: 'text-blue-700', bgColor: 'bg-blue-100', borderColor: 'border-blue-300' },
    'Marine Safari Bali': { num: 16, x: 66, y: 66, color: 'text-orange-700', bgColor: 'bg-orange-100', borderColor: 'border-orange-300' }
  };
`;
