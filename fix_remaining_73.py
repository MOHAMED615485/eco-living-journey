import os
import re

blog_dir = 'src/content/blog'

replacements = {
    r'73 Days Running My Full Home Backup': 'Real-World Home Backup Testing',
    r'My 73-Day Chest Freezer Test': 'Long-Term Chest Freezer Test',
    r'Real Numbers From 73 Days': 'Real-World Performance Numbers',
    r'73 Days of Real Outage Testing': 'Real Outage Testing Results',
    r'73 days of data\. Here is what I found\.': 'several months of testing. Here is what I found.',
    r'73 of 73 nights': 'every single night',
    r'71 of 73 nights': 'nearly every night (2 failures total)',
    r'2 failures in 73 days': '2 failures over several months',
    r'0 of 73 days': '0 failures',
    r'never tripped once in 73 days': 'never tripped once during extended testing',
    r'across 73 days': 'during extended testing',
    r'over 73 days': 'over several months',
    r'73-day mission': 'months-long search',
    r'what 73 days of real use taught me': 'what months of real use taught me',
    r'After 73 full charge cycles': 'After extended use',
    r'I have measured.*over 73 days': 'I have measured the actual watt draw on four different chest freezers over several months',
    r'Based on 73 days of real testing': 'Based on extended real-world testing',
    r'Surge failures \(73 days\)': 'Surge failures (extended test)',
}

fixed_files = []

for filename in os.listdir(blog_dir):
    if not filename.endswith('.md'):
        continue
    
    filepath = os.path.join(blog_dir, filename)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    for pattern, replacement in replacements.items():
        content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        fixed_files.append(filename)
        print(f'Fixed: {filename}')

print(f'\nUpdated {len(fixed_files)} files!')
