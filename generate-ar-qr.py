#!/usr/bin/env python3
"""Generate QR code for AR viewer."""
import argparse, os, sys

try:
    import qrcode
except ImportError:
    print("Install: pip install qrcode")
    sys.exit(1)

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--url', required=True)
    p.add_argument('--output', default='qr-ar.png')
    p.add_argument('--size', type=int, default=10)
    args = p.parse_args()

    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H,
                        box_size=args.size, border=3)
    qr.add_data(args.url)
    qr.make(fit=True)
    img = qr.make_image(fill_color=(240,192,64), back_color=(10,10,10))
    img.save(args.output)
    print(f"QR saved: {os.path.abspath(args.output)}")
    print(f"Points to: {args.url}")

if __name__ == '__main__':
    main()
