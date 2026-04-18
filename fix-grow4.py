import os

grow_script = """    <script data-grow-initializer="">!(function(){window.growMe||((window.growMe=function(e){window.growMe._.push(e);}),(window.growMe._=[]));var e=document.createElement("script");(e.type="text/javascript"),(e.src="https://faves.grow.me/main.js"),(e.defer=!0),e.setAttribute("data-grow-faves-site-id","U2l0ZTo1ZmZlMDAzMS1jMTliLTRkNDktOWVlYy1jYTA1YWRmNjAyNTU=");var t=document.getElementsByTagName("script")[0];t.parentNode.insertBefore(e,t);})();</script>"""

files = [
    "src/layouts/BlogPost.astro",
    "src/pages/index.astro",
    "src/pages/blog/index.astro",
]

for filepath in files:
    if not os.path.exists(filepath):
        print(f"NOT FOUND: {filepath}")
        continue

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if "data-grow-initializer" in content:
        print(f"ALREADY HAS IT: {filepath}")
        continue

    # Insert before </head>
    if "</head>" in content:
        new_content = content.replace("</head>", grow_script + "\n  </head>", 1)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"SUCCESS: {filepath}")
    else:
        print(f"NO </head> FOUND: {filepath}")
