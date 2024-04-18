import imageio.v2 as imageio
import os
import sys

def create_gif_from_directory(directory_path, output_filename, duration=1):
    #collect all images
    images = []
    for file_name in sorted(os.listdir(directory_path), key=lambda x: int(x.split('_')[1].split('.')[0])):
        if file_name.endswith('.png'):
            file_path = os.path.join(directory_path, file_name)
            images.append(imageio.imread(file_path))
            print(file_path)

    #create gif from images
    if images:
        imageio.mimsave(output_filename, images, duration=duration)
        print(f"GIF created at {output_filename}")
    else:
        print("No images found to create a GIF.")

#get arguments when called, pass to function
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python gif_creator.py <directory> <output_gif_name>")
        sys.exit(1)

    directory = sys.argv[1]
    output_gif = sys.argv[2]
    create_gif_from_directory(directory, output_gif)
