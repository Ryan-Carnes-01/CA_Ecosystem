import imageio
import os
import sys

def create_gif_from_directory(directory_path, output_filename, duration=0.5):
    images = []
    for file_name in sorted(os.listdir(directory_path)):
        if file_name.endswith('.png'):
            file_path = os.path.join(directory_path, file_name)
            images.append(imageio.imread(file_path))

    if images:
        imageio.mimsave(output_filename, images, duration=duration)
        print(f"GIF created at {output_filename}")
    else:
        print("No images found to create a GIF.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python create_gif.py <directory> <output_gif_name>")
        sys.exit(1)

    directory = sys.argv[1]
    output_gif = sys.argv[2]
    create_gif_from_directory(directory, output_gif)
