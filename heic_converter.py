#!/usr/bin/env python3
"""
HEIC to JPEG Converter
Converts all HEIC files in a source folder to JPEG format in a destination folder.
"""

import os
import sys
from pathlib import Path
from PIL import Image
import pillow_heif


def setup_heif_support():
    """Register HEIF opener with Pillow."""
    pillow_heif.register_heif_opener()


def convert_heic_to_jpeg(source_folder, destination_folder, quality=95):
    """
    Convert all HEIC files in source folder to JPEG in destination folder.

    Args:
        source_folder (str): Path to folder containing HEIC files
        destination_folder (str): Path to folder where JPEG files will be saved
        quality (int): JPEG quality (1-100, default 95)

    Returns:
        tuple: (successful_conversions, failed_conversions)
    """
    # Setup HEIF support
    setup_heif_support()

    # Convert paths to Path objects
    source_path = Path(source_folder)
    dest_path = Path(destination_folder)

    # Check if source folder exists
    if not source_path.exists():
        print(f"Error: Source folder '{source_folder}' does not exist.")
        return 0, 0

    # Create destination folder if it doesn't exist
    dest_path.mkdir(parents=True, exist_ok=True)

    # Find all HEIC files (case insensitive)
    heic_files = []
    for ext in ["*.heic", "*.HEIC", "*.heif", "*.HEIF"]:
        heic_files.extend(source_path.glob(ext))

    if not heic_files:
        print(f"No HEIC files found in '{source_folder}'")
        return 0, 0

    print(f"Found {len(heic_files)} HEIC file(s) to convert...")

    successful = 0
    failed = 0

    for heic_file in heic_files:
        try:
            # Open HEIC file
            with Image.open(heic_file) as img:
                # Convert to RGB if necessary (HEIC might be in different color mode)
                if img.mode != "RGB":
                    img = img.convert("RGB")

                # Create output filename with .jpg extension
                output_filename = heic_file.stem + ".jpg"
                output_path = dest_path / output_filename

                # Save as JPEG
                img.save(output_path, "JPEG", quality=quality, optimize=True)

                print(f"✓ Converted: {heic_file.name} → {output_filename}")
                successful += 1

        except Exception as e:
            print(f"✗ Failed to convert {heic_file.name}: {str(e)}")
            failed += 1

    return successful, failed


def main():
    """Main function with predefined folder paths."""
    print("HEIC to JPEG Converter")
    print("=" * 30)

    # Predefined folder paths
    source_folder = r"C:\Users\Username\Downloads\OldPhotos"
    destination_folder = r"C:\Users\Username\Downloads\NewPhotos"

    # Get quality setting (optional command line argument)
    quality = 95
    if len(sys.argv) > 1:
        try:
            quality = int(sys.argv[1])
            quality = max(1, min(100, quality))  # Clamp between 1-100
        except ValueError:
            print("Invalid quality value, using default (95)")

    print(f"\nSource: {source_folder}")
    print(f"Destination: {destination_folder}")
    print(f"JPEG Quality: {quality}")
    print("-" * 30)

    # Perform conversion
    successful, failed = convert_heic_to_jpeg(
        source_folder, destination_folder, quality
    )

    # Summary
    print("-" * 30)
    print(f"Conversion complete!")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Total processed: {successful + failed}")


if __name__ == "__main__":
    main()
