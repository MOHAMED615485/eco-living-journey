import re

# Read the file
with open('src/components/BaseHead.astro', 'r', encoding='utf-8') as f:
    content = f.read()

# The Clarity code
clarity_code = '''
<!-- Microsoft Clarity -->
<script type="text/partytown">
    (function(c,l,a,r,i,t,y){
        c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
        t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i+"?ref=bwt";
        y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    })(window, document, "clarity", "script", "wf28mimveg");
</script>
'''

# Find the gtag config script and add Clarity after it
pattern = r"(gtag\('config', 'G-R4DLNKRS96'\);\n</script>)"
replacement = r"\1\n" + clarity_code

if pattern in content or "gtag('config', 'G-R4DLNKRS96')" in content:
    content = re.sub(pattern, replacement, content)
    print('✅ Microsoft Clarity code added after Google Analytics')
else:
    print('❌ Could not find Google Analytics code')

# Write back
with open('src/components/BaseHead.astro', 'w', encoding='utf-8') as f:
    f.write(content)
