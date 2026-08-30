# AR Tiger Viewer

AR experience: scan QR → camera opens → video overlays on artwork.
Zero platforms, zero signup, self-hosted.

## Setup

### 1. Print the marker
Print `hiro_marker.png` at actual size (do not resize).
Place it in the **bottom-right corner** of your tiger artwork frame.
Size: ~1cm visible at exhibition distance — barely noticeable.

### 2. Deploy to HTTPS
AR requires HTTPS. Deploy to any static host:
- GitHub Pages
- Cloudflare Pages
- TrueNAS + nginx + Let's Encrypt

### 3. Generate QR code
```bash
cd ar-tiger-viewer
python3 generate-ar-qr.py --url https://your-domain/ar-tiger-viewer/
```

### 4. Print QR on placard
Place the QR code on the artwork display placard below the marker.

## How it works

```
User scans QR → HTTPS page → camera access
  → AR.js detects hiro marker on artwork frame
  → MiniMax video overlays exactly on marker plane
  → Video sticks to artwork — walk around to see from angles
```

## Device support

| Device | Status |
|--------|--------|
| Android Chrome | Full AR (WebAR-on-ARCore) |
| iOS Safari | Video plays directly (no AR) |
| Desktop | Video plays directly |

## Files

```
ar-tiger-viewer/
├── index.html          ← AR viewer page
├── hiro_marker.png     ← Print this on artwork frame
├── hiro_marker.patt    ← ARToolKit marker definition
├── generate-ar-qr.py   ← QR code generator
├── server.py           ← Local HTTPS test server
├── README.md
└── assets/
    ├── video.mp4       ← Optimized tiger video (~1.2MB)
    └── video.webm      ← VP9 WebM alternative (~750KB)
```

## Local testing

```bash
python server.py --gen-cert --port 8443
# Open https://localhost:8443 (accept security warning)
```
