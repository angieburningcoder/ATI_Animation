import shutil
import os

def copy_files():
    src_dir = "/Users/yu1025/.gemini/antigravity/brain/51cde15d-6077-42ea-a5ef-513374a2c518"
    
    mapping = {
        "bg_main_scene_mumu_green_grapes_1780738042168.png": "assets/bg-main-scene.png",
        "bg_spotlight_winery_mumu_green_grapes_1780738063627.png": "assets/bg-spotlight-winery.png",
        "clay_winery_building_mumu_green_grapes_1780738083071.png": "assets/clay-winery-building.png",
        "clay_icons_sheet_mumu_green_grapes_1780738102117.png": "assets/clay-icons-sheet.png"
    }
    
    for src_name, dst_relative in mapping.items():
        src_path = os.path.join(src_dir, src_name)
        dst_path = os.path.join("/Users/yu1025/Dev-Project/ATI animation", dst_relative)
        print(f"Copying {src_path} -> {dst_path}")
        shutil.copy(src_path, dst_path)
        
    print("All green grape clay background and UI assets copied successfully.")

if __name__ == "__main__":
    copy_files()
