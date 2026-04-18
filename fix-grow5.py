import os

# The correct Grow script with is:inline to prevent Astro from wrapping it
grow_script = """<script is:inline data-grow-initializer="">!(function(){window.growMe||((window.growMe=function(e){window.growMe._.push(e);}),(window.growMe._=[]));var e=document.createElement("script");(e.type="text/javascript"),(e.src="https://faves.grow.me/main.js"),(e.defer=!0),e.setAttribute("data-grow-faves-site-id","U2l0ZTo1ZmZlMDAzMS1jMTliLTRkNDktOWVlYy1jYTA1YWRmNjAyNTU=");var t=document.getElementsByTagName("script")[0];t.parentNode.insertBefore(e,t);})();</script>"""

files = [
    "src/pages/index.astro",
    "src/pages/blog/index.astro",
    "src/layouts/BlogPost.astro",
    "src/components/BaseHead.astro",
]

for filepath in files:
    if not os.path.exists(filepath):
        print(f"NOT FOUND: {filepath}")
        continue

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove ALL previous grow script attempts
    lines = content.split("\n")
    clean_lines = []
    for line in lines:
        if "grow.me" in line or "growMe" in line or "data-grow" in line or "faves.grow" in line:
            continue
        clean_lines.append(line)
    clean_content = "\n".join(clean_lines)

    # Only add to files that have </head>
    if "</head>" in clean_content:
        new_content = clean_content.replace("</head>", grow_script + "\n</head>", 1)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"SUCCESS: {filepath}")
    else:
        # For BaseHead which has no </head>, just append
        new_content = clean_content.rstrip() + "\n" + grow_script + "\n"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"SUCCESS (appended): {filepath}")
