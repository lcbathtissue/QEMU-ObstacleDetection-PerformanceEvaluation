import csv

def parse_to_csv(filepath, output_csv_file):
    with open(filepath, 'r') as file:
        lines = file.readlines()
    data = [] 
    for line in lines:
        if line.startswith("Output for "):
            filename = line.split(":")[0].replace("Output for ", "").strip()
            time = None
            for subline in lines:
                if subline.startswith(filename + ": Predicted in "):
                    time = float(subline.split(" ")[-2])
                    break
            if time is not None:
                data.append((filename, time))
    with open(output_csv_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Filename', 'Time'])
        csv_writer.writerows(data)
        

filepath = input("Enter the path to the output file containing filenames and timestamps: ")
split_filename = filepath.rsplit('.', 1)
split_filenames = [split_filename[0], split_filename[1] if len(split_filename) == 2 else '']
output_csv_file = f"csv-parsed_{split_filenames[0]}.csv"
print(filepath, output_csv_file)
parse_to_csv(filepath, output_csv_file)