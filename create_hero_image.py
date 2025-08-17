#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFilter
import math

def create_iphone_frame(width=390, height=844):
    """Create an iPhone 15-style frame with rounded corners and notch"""
    # Create frame
    frame = Image.new('RGBA', (width + 40, height + 40), (0, 0, 0, 0))
    draw = ImageDraw.Draw(frame)
    
    # Phone body (dark gray)
    phone_color = (30, 30, 30, 255)
    draw.rounded_rectangle([10, 10, width + 30, height + 30], radius=25, fill=phone_color)
    
    # Screen area (black)
    screen_color = (0, 0, 0, 255)
    draw.rounded_rectangle([20, 20, width + 20, height + 20], radius=20, fill=screen_color)
    
    return frame

def add_shadow(image, offset=(10, 10), shadow_color=(0, 0, 0, 128)):
    """Add drop shadow to image"""
    shadow = Image.new('RGBA', (image.width + 20, image.height + 20), (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow)
    
    # Create shadow
    shadow_img = image.copy()
    shadow_img = shadow_img.filter(ImageFilter.GaussianBlur(5))
    
    # Paste shadow
    shadow.paste(shadow_img, offset, shadow_img)
    shadow.paste(image, (0, 0), image)
    
    return shadow

def resize_screenshot(image, target_width=370, target_height=824):
    """Resize screenshot to fit iPhone screen"""
    # Calculate aspect ratio
    aspect = image.width / image.height
    target_aspect = target_width / target_height
    
    if aspect > target_aspect:
        # Image is wider - fit to height
        new_height = target_height
        new_width = int(new_height * aspect)
    else:
        # Image is taller - fit to width
        new_width = target_width
        new_height = int(new_width / aspect)
    
    resized = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    
    # Crop to exact size
    if new_width > target_width:
        left = (new_width - target_width) // 2
        resized = resized.crop((left, 0, left + target_width, target_height))
    elif new_height > target_height:
        top = (new_height - target_height) // 2
        resized = resized.crop((0, top, target_width, top + target_height))
    
    return resized

def create_hero_image():
    """Create hero image with multiple app screenshots in iPhone frames"""
    
    # Hero image dimensions
    hero_width = 1200
    hero_height = 600
    
    # Create gradient background
    hero = Image.new('RGB', (hero_width, hero_height), (0, 0, 0))
    
    # Create gradient (dark blue to black)
    for y in range(hero_height):
        gradient_factor = y / hero_height
        r = int(0 * (1 - gradient_factor) + 0 * gradient_factor)
        g = int(20 * (1 - gradient_factor) + 0 * gradient_factor)
        b = int(40 * (1 - gradient_factor) + 0 * gradient_factor)
        
        draw = ImageDraw.Draw(hero)
        draw.line([(0, y), (hero_width, y)], fill=(r, g, b))
    
    # Screenshot files to use (best ones from each app)
    screenshots = [
        ('snapjigsaw_main.jpg', 150, 50),      # Position (x, y)
        ('clevercontacts_main.jpg', 380, 80),
        ('mapcred_main.jpg', 610, 50),
        ('cardswithphones_main.jpg', 840, 80)
    ]
    
    for screenshot_file, x, y in screenshots:
        try:
            # Load screenshot
            screenshot = Image.open(screenshot_file).convert('RGBA')
            
            # Resize to fit iPhone screen
            screenshot = resize_screenshot(screenshot)
            
            # Create iPhone frame
            frame = create_iphone_frame()
            
            # Paste screenshot into frame (accounting for frame border)
            frame.paste(screenshot, (20, 20), screenshot)
            
            # Add shadow
            framed_phone = add_shadow(frame)
            
            # Paste onto hero image
            hero.paste(framed_phone, (x, y), framed_phone)
            
            print(f"✓ Added {screenshot_file} at position ({x}, {y})")
            
        except Exception as e:
            print(f"✗ Failed to process {screenshot_file}: {e}")
    
    # Save hero image
    hero.save('hero-mockup.jpg', 'JPEG', quality=90)
    print(f"\n✓ Hero image saved as hero-mockup.jpg ({hero.width}x{hero.height})")

def main():
    print("Creating hero image mockup...")
    create_hero_image()
    print("Hero image creation complete!")

if __name__ == "__main__":
    main()