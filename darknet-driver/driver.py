import subprocess
import os

def run_darknet_detection(image_path, output_file):
    command = f"./darknet detect cfg/yolov3.cfg yolov3.weights {image_path}"

    try:
        output = subprocess.check_output(command, shell=True)
        print("Command executed successfully for:", image_path)
        output_text = output.decode('utf-8')
        print(output_text) 
        with open(output_file, 'a') as f:
            f.write(f"Output for {image_path}:\n")
            f.write(output_text)
            f.write('\n\n')
    except subprocess.CalledProcessError as e:
        print("Error executing the command for:", image_path)
        print(e)
        
if __name__ == "__main__":
    directory_path = input("Enter the path to the directory with images (for example 'data')': ")
    file_extension = input("Enter the extension for the filetype of the images (for example '.jpg')': ")
    output_file = f"../driver-output_{directory_path}.txt"
    with open(output_file, 'w') as file:
        pass
    image_files = []
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path) and filename.endswith(file_extension):
            image_files.append(f"{directory_path}/{filename}")
    print(image_files)
    for image_file in image_files:
        run_darknet_detection(image_file, output_file)
