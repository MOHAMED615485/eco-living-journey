import os
import re

blog_dir = 'src/content/blog'
md_files = [f for f in os.listdir(blog_dir) if f.endswith('.md')]

replacements = {
    r'73[- ]day[s]?\s+(?:field[\s-])?test(?:ing|s|ed)?': 'real-world testing',
    r'for 73[- ]days': 'over several months',
    r'73[- ]day\s+(?:testing\s+)?protocol': 'testing process',
    r'after 73 days': 'after extended use',
    r'over 73 days': 'over time',
    r'73\+ days': 'extended period',
}

fixed_count = 0

for filename in md_files:
    filepath = os.path.join(blog_dir, filename)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Apply all replacements
    for pattern, replacement in replacements.items():
        content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
    
    # Check if anything changed
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'? Fixed: {filename}')
        fixed_count += 1

print(f'\n? Updated {fixed_count} files!')
print('All "73-day testing" mentions removed and replaced with natural language.')
