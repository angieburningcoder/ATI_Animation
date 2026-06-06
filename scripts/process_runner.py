import os
from PIL import Image

def process_runner(src_path, dst_path):
    print(f"Processing runner image: {src_path}")
    img = Image.open(src_path).convert("RGBA")
    datas = img.getdata()
    new_data = []
    
    for item in datas:
        r, g, b, a = item
        # Remove white background
        if r > 248 and g > 248 and b > 248:
            new_data.append((255, 255, 255, 0))
        elif r > 240 and g > 240 and b > 240:
            # Semi-transparent transition for antialiasing
            factor = (min(r, g, b) - 240) / 8.0
            alpha = int(255 * (1.0 - factor))
            new_data.append((r, g, b, alpha))
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
        
    img.save(dst_path, "PNG")
    print(f"Saved transparent runner to {dst_path}")

def copy_founder(src_path, dst_path):
    print(f"Copying founder image to {dst_path}")
    img = Image.open(src_path)
    img.save(dst_path)
    print("Done copying.")

if __name__ == "__main__":
    # Source paths (from artifact directory)
    runner_src = "/Users/yu1025/.gemini/antigravity/brain/51cde15d-6077-42ea-a5ef-513374a2c518/doris_runner_clay_1780733313933.png"
    founder_src = "/Users/yu1025/.gemini/antigravity/brain/51cde15d-6077-42ea-a5ef-513374a2c518/founder_shusheng_clay_1780733336553.png"
    
    # Destination paths
    runner_dst = "/Users/yu1025/Dev-Project/ATI animation/runner.png"
    founder_dst = "/Users/yu1025/Dev-Project/ATI animation/assets/shu-sheng-photo.png"
    
    process_runner(runner_src, runner_dst)
    copy_founder(founder_src, founder_dst)
