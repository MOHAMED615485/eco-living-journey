from PIL import Image
import os

# Create output folder
os.makedirs('medium-images', exist_ok=True)

# Get all webp files
webp_files = [f for f in os.listdir('src/assets') if f.endswith('.webp')]

print(f'Converting {len(webp_files)} WebP images to JPG...\n')

for webp_file in webp_files:
    try:
        # Open WebP
        img = Image.open(f'src/assets/{webp_file}')
        
        # Convert to RGB (JPG doesn't support transparency)
        if img.mode in ('RGBA', 'LA', 'P'):
            img = img.convert('RGB')
        
        # Save as JPG
        jpg_filename = webp_file.replace('.webp', '.jpg')
        img.save(f'medium-images/{jpg_filename}', 'JPEG', quality=95)
        
        print(f'✅ {webp_file} → {jpg_filename}')
    except Exception as e:
        print(f'❌ Failed: {webp_file} - {e}')

print(f'\n✨ All images converted to medium-images/ folder!')
print('\nYou can now upload these JPG files to Medium.')
