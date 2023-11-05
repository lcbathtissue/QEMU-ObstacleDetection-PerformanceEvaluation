import cv2
import os

def extract_video_frames(video_file, output_directory):
    os.makedirs(output_directory, exist_ok=True)
    cap = cv2.VideoCapture(video_file)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    for frame_number in range(frame_count):
        ret, frame = cap.read()
        if not ret:
            break
        frame_filename = os.path.join(output_directory, f'frame_{frame_number:04d}.jpg')
        cv2.imwrite(frame_filename, frame)
        print(f'Saved frame {frame_number}/{frame_count}')
    cap.release()
    print(f'Frames saved to {output_directory}')

if __name__ == "__main__":
    input_video_file = input("Enter the input video file: ")
    split_filename = input_video_file.rsplit('.', 1)
    split_filenames = [split_filename[0], split_filename[1] if len(split_filename) == 2 else '']
    output_video_file = f"{split_filenames[0]}_cropped.{split_filenames[1]}"
    output_directory = f"frames/{split_filename[0]}"
    extract_video_frames(input_video_file, output_directory)
