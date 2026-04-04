c = open('src/styles/global.css', encoding='utf-8').read()

old = """/* Gold star ratings in tables */
td:has(\u2605), td:has(\u2606) {
  color: #f5a623;
  font-size: 1.2rem;
  letter-spacing: 3px;
}"""

new = """/* Gold star ratings in tables */
table td:last-child {
  color: #f5a623;
  font-size: 1.2rem;
  letter-spacing: 2px;
}"""

if old in c:
    c = c.replace(old, new)
    print('CSS updated')
else:
    c += new
    print('CSS appended')

open('src/styles/global.css', 'w', encoding='utf-8').write(c)
print('done')
