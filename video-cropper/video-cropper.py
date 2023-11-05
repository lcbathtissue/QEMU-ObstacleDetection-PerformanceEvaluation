import cv2

def extract_video_segment(input_video_path, output_video_path, start_time, end_time, fps):
    video_capture = cv2.VideoCapture(input_video_path)
    start_frame = int(start_time * fps)
    end_frame = int(end_time * fps)
    frame_width = int(video_capture.get(3))
    frame_height = int(video_capture.get(4))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))
    video_capture.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
    while True:
        ret, frame = video_capture.read()
        if not ret or video_capture.get(cv2.CAP_PROP_POS_FRAMES) > end_frame:
            break
        out.write(frame)
    video_capture.release()
    out.release()
    print("Video segment extraction completed.")

if __name__ == "__main__":
    input_video_file = input("Enter the input video file: ")
    video_fps = input("Enter the fps of the video file: ")
    split_filename = input_video_file.rsplit('.', 1)
    split_filenames = [split_filename[0], split_filename[1] if len(split_filename) == 2 else '']
    output_video_file = f"{split_filenames[0]}_cropped.{split_filenames[1]}"
    start_timestamp = input("Enter the start timestamp (in seconds): ")
    end_timestamp = input("Enter the end timestamp (in seconds): ")
    extract_video_segment(input_video_file, output_video_file, int(start_timestamp), int(end_timestamp), int(video_fps))
