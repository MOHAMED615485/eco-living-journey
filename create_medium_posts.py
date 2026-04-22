import os
import re
from pathlib import Path

# Create output directory for Medium posts
output_dir = 'medium-posts'
os.makedirs(output_dir, exist_ok=True)

# Article slug to title mapping (we'll extract from frontmatter)
blog_dir = 'src/content/blog'

# Get all markdown files
md_files = [f for f in os.listdir(blog_dir) if f.endswith('.md')]

print(f'Found {len(md_files)} articles to convert...\n')

for filename in md_files:
    filepath = os.path.join(blog_dir, filename)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title from frontmatter
    title_match = re.search(r'title:\s*["\']([^"\']+)["\']', content)
    title = title_match.group(1) if title_match else filename.replace('.md', '').replace('-', ' ').title()
    
    # Extract description
    desc_match = re.search(r'description:\s*["\']([^"\']+)["\']', content)
    description = desc_match.group(1) if desc_match else ''
    
    # Remove frontmatter (everything between --- markers)
    content_no_frontmatter = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
    
    # Create canonical URL
    slug = filename.replace('.md', '')
    canonical_url = f'https://ecoliving-journey.com/blog/{slug}/'
    
    # Build Medium post
    medium_post = f'''# {title}

{description}

---

{content_no_frontmatter}

---

**Originally published at** [{canonical_url}]({canonical_url})

*This article was written by Ethan Clarke, who field-tests portable power stations for 73+ days to bring you real-world backup power insights. Read more at [Eco Living Journey](https://ecoliving-journey.com).*
'''
    
    # Save Medium version
    output_file = os.path.join(output_dir, f'medium-{filename}')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(medium_post)
    
    print(f'✅ Created: {output_file}')

print(f'\n✨ All {len(md_files)} Medium posts created in /{output_dir}/ folder!')
print('\nNext steps:')
print('1. Go to medium.com and click "Write a story"')
print('2. Copy-paste each Medium post')
print('3. Add your hero images')
print('4. Click "Import a story" if Medium supports markdown import')
