const sharp = require('sharp');
const jobs = [
  ['C:/Users/DELL/Downloads/jackery-solar-generator-1000-v2refurbished-9638983.webp', 'src/assets/products/jackery-1000v2.webp'],
  ['C:/Users/DELL/Downloads/AC200L_200L.webp', 'src/assets/products/bluetti-ac200l.webp'],
  ['C:/Users/DELL/Downloads/ecoflow-us-ecoflow-delta-3-plus-portable-power-station-standalone-delta-3-plus-1232540118.webp', 'src/assets/products/ecoflow-delta3plus.webp'],
];
(async () => {
  for (const [src, dst] of jobs) {
    await sharp(src).resize({ width: 400 }).webp({ quality: 80 }).toFile(dst);
    console.log('OK:', dst);
  }
})();
