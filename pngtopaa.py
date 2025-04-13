import os
import subprocess

def convert_png_to_paa(png_file):
    # Define the output PAA file name by changing the extension
    paa_file = os.path.splitext(png_file)[0] + ".paa"
    
    # Path to ImagetoPAA (if it's not in your PATH, specify the full path)
    imagetopaa_path = r"D:\Steam\steamapps\common\DayZ Tools\Bin\ImageToPAA\ImageToPAA.exe"  # Adjust this if ImagetoPAA is in a specific folder
    
    # Use ImagetoPAA to convert PNG to PAA
    try:
        subprocess.run([imagetopaa_path, png_file, paa_file], check=True)
        print(f"Converted {png_file} to {paa_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error converting {png_file}: {e}")

def main():
    # Get the current working directory (where the script is located)
    current_dir = os.path.dirname(os.path.realpath(__file__))
    
    # List all files in the directory
    files_in_directory = os.listdir(current_dir)
    
    # Loop through all files and find the .png files
    for file in files_in_directory:
        if file.lower().endswith(".png"):
            png_file_path = os.path.join(current_dir, file)
            convert_png_to_paa(png_file_path)

if __name__ == "__main__":
    main()
