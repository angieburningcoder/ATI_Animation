#!/usr/bin/env python3
"""
Generate clay 3D animation assets via Google Gemini (Nano Banana).

Usage:
  export GEMINI_API_KEY="your-key"
  pip install google-genai pillow
  python scripts/generate_assets.py

Get a key: https://aistudio.google.com/apikey
Docs: https://ai.google.dev/gemini-api/docs/image-generation
"""

import os
import sys
from pathlib import Path

ASSETS_DIR = Path(__file__).resolve().parent.parent / "assets"

PROMPTS = {
    "bg-main-scene.png": (
        "16:9 widescreen illustration, 3D claymation stop-motion vineyard countryside. "
        "Rolling moss-green clay hills, warm peach sunset sky, chunky rounded clay cobblestone "
        "path through grapevine rows, distant clay winery villa. Matte modeling-clay texture, "
        "soft rounded edges, Japanese clay animation style (Mumu pocket / kotatsu clay aesthetic). "
        "Visible handmade paper fiber grain texture across entire image. Warm palette: cream, "
        "terracotta, mustard, moss green. No text, no people."
    ),
    "bg-spotlight-winery.png": (
        "16:9 widescreen, 3D claymation winery interior courtyard. Grape vine trellis with chunky "
        "clay purple grape clusters, rounded stone wall, wooden clay barrels, cozy winery building "
        "with warm glowing windows. Matte clay texture, rounded forms, paper grain texture visible. "
        "Warm terracotta and moss green. No text, no people. Background plate."
    ),
    "clay-winery-building.png": (
        "Single isolated 3D claymation winery building on plain cream paper background. "
        "Chunky rounded clay forms, terracotta blank sign, mustard window glow, moss trim. "
        "Matte clay, soft shadow beneath. Paper grain texture. No text. Centered with empty space around."
    ),
    "clay-icons-sheet.png": (
        "2x2 grid of four 3D claymation icons on cream paper background: purple grape cluster, "
        "clay wine glass, clay notebook, clay folded map. Chunky matte clay, rounded edges. "
        "Paper fiber grain. No text."
    ),
}


def main() -> None:
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("Error: set GEMINI_API_KEY or GOOGLE_API_KEY", file=sys.stderr)
        sys.exit(1)

    try:
        from google import genai
        from google.genai import types
    except ImportError:
        print("Run: pip install google-genai", file=sys.stderr)
        sys.exit(1)

    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    client = genai.Client(api_key=api_key)

    # Nano Banana 2 — fast clay asset generation
    model = "gemini-2.5-flash-image"

    for filename, prompt in PROMPTS.items():
        out_path = ASSETS_DIR / filename
        print(f"Generating {filename}...")

        response = client.models.generate_content(
            model=model,
            contents=[prompt],
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE"],
            ),
        )

        saved = False
        for part in response.parts:
            if part.inline_data is not None:
                image = part.as_image()
                image.save(out_path)
                print(f"  -> {out_path}")
                saved = True
                break

        if not saved:
            print(f"  Warning: no image returned for {filename}", file=sys.stderr)

    print("Done.")


if __name__ == "__main__":
    main()
