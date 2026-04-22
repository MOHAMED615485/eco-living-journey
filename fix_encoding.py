import os
import re

blog_dir = 'src/content/blog'
fixed_count = 0

# Get all markdown files
md_files = [f for f in os.listdir(blog_dir) if f.endswith('.md')]

print('Fixing encoding in all blog posts...\n')

for filename in md_files:
    filepath = os.path.join(blog_dir, filename)
    
    # Read with UTF-8
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if it has broken stars
    if 'â˜…' in content or 'â˜†' in content or 'â^' in content:
        # Fix all star encoding issues
        content = content.replace('â˜…', '★')
        content = content.replace('â˜†', '☆')
        # Fix other common encoding issues
        content = content.replace('â€"', '—')
        content = content.replace('â€˜', ''')
        content = content.replace('â€™', ''')
        content = content.replace('â€œ', '"')
        content = content.replace('â€', '"')
        
        # Write back with UTF-8
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f'✅ Fixed: {filename}')
        fixed_count += 1

print(f'\n✨ Fixed {fixed_count} files!')
print('\nNow regenerating Medium posts with correct encoding...')
