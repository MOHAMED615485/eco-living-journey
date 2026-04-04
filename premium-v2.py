c = open('src/styles/global.css', encoding='utf-8').read()

# Remove all previous table CSS we added
import re
c = re.sub(r'/\* Premium table styling \*/.*?/\* Gold stars.*?\}', '', c, flags=re.DOTALL)
c = re.sub(r'/\* Force gold.*?\}', '', c, flags=re.DOTALL)
c = re.sub(r'/\* Gold star.*?\}', '', c, flags=re.DOTALL)
c = re.sub(r'/\* Gold stars.*?\}', '', c, flags=re.DOTALL)

premium = '''
/* ============================================
   PREMIUM COMPARISON TABLE
   ============================================ */
.prose table {
  width: 100% !important;
  border-collapse: collapse !important;
  border-radius: 16px !important;
  overflow: hidden !important;
  box-shadow:
    0 20px 60px rgba(0,0,0,0.18),
    0 8px 20px rgba(0,0,0,0.12),
    0 2px 6px rgba(0,0,0,0.08) !important;
  border: none !important;
  font-family: "DM Sans", sans-serif !important;
}

.prose table thead tr {
  background: linear-gradient(135deg, #0d0d0d 0%, #1a1a2e 50%, #16213e 100%) !important;
}

.prose table thead th {
  color: #ffffff !important;
  font-weight: 700 !important;
  font-size: 0.78rem !important;
  letter-spacing: 1.5px !important;
  padding: 18px 20px !important;
  border: none !important;
  text-transform: uppercase !important;
  text-shadow: 0 1px 3px rgba(0,0,0,0.4) !important;
}

.prose table tbody tr {
  border-bottom: 1px solid #f0f0f0 !important;
  transition: all 0.2s ease !important;
}

.prose table tbody tr:nth-child(odd) {
  background: #ffffff !important;
}

.prose table tbody tr:nth-child(even) {
  background: #f8f9fa !important;
}

.prose table tbody tr:hover {
  background: #fff9f0 !important;
  transform: scale(1.005) !important;
  box-shadow: 0 2px 12px rgba(245,166,35,0.1) !important;
}

.prose table tbody tr:last-child {
  border-bottom: none !important;
}

.prose table td {
  padding: 14px 20px !important;
  color: #1a1a1a !important;
  font-size: 0.92rem !important;
  border: none !important;
  border-right: 1px solid #f0f0f0 !important;
  vertical-align: middle !important;
}

.prose table td:first-child {
  font-weight: 600 !important;
  color: #2d2d2d !important;
  background: inherit !important;
  border-right: 2px solid #e8e8e8 !important;
}

.prose table td:last-child {
  border-right: none !important;
}

/* Gold star cells */
.prose table td.star-cell {
  color: #e8940a !important;
  font-size: 1.15rem !important;
  letter-spacing: 2px !important;
  font-weight: 700 !important;
  text-shadow: 0 1px 3px rgba(232,148,10,0.25) !important;
}
'''

open('src/styles/global.css', 'w', encoding='utf-8').write(c + premium)
print('done')
