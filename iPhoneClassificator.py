import glob
import os
import shutil

base_dir = os.getcwd()

def check_folder_existance(folder_name):
    return os.path.isdir(os.path.join(base_dir, folder_name))

def move_to_folder(folder_name, files_to_classify):
    if not check_folder_existance(folder_name):
        os.mkdir(folder_name)
    for one_file in files_to_classify:
        full_path = os.path.join(base_dir, one_file)
        file_without_parent_folder = one_file.replace("unclassifiedPhotosAndVideos\\", "")
        new_full_path = os.path.join(base_dir, folder_name, file_without_parent_folder)
        shutil.move(full_path, new_full_path)

def process_files_matching_with_regex(destination_folder, regex ):
    common_regex = "**/unclassifiedPhotosAndVideos/"
    print(destination_folder)
    files = glob.glob(common_regex + regex, recursive=True)
    print(files)
    move_to_folder(destination_folder, files)
    print("================")


# The order we execute this process files is critical since some regex assumes that previous cases are already classified.
# order critical first wpp then camera
process_files_matching_with_regex("whatsapp-images", "*_*_*.JPG")
process_files_matching_with_regex("camera", "*_*.JPG")
process_files_matching_with_regex("camera-multi", "*.MOV")
process_files_matching_with_regex("screenshots", "*.PNG")
# order critical first wpp then tiktoks
process_files_matching_with_regex("whatsapp_videos_and_screenrecords", "*_*.MP4")
process_files_matching_with_regex("tiktoks", "*.MP4")
