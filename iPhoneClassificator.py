import glob
import os
import shutil

base_dir = os.getcwd()

def checkear_si_existe_carpeta(nombre_de_la_carpeta):
    return os.path.isdir(os.path.join(base_dir, nombre_de_la_carpeta))

def move_to_folder(nombre_de_la_carpeta, archivos_a_mover):
    if not checkear_si_existe_carpeta(nombre_de_la_carpeta):
        os.mkdir(nombre_de_la_carpeta)
    for un_archivo in archivos_a_mover:
        full_path = os.path.join(base_dir, un_archivo)
        un_archivo_sin_su_carpeta_padre = un_archivo.replace("unclassifiedPhotosAndVideos\\", "")
        new_full_path = os.path.join(base_dir, nombre_de_la_carpeta, un_archivo_sin_su_carpeta_padre)
        shutil.move(full_path, new_full_path)

def process_files_matching_with_regex(destination_folder, regex ):
    common_regex = "**/unclassifiedPhotosAndVideos/"
    print(destination_folder)
    files = glob.glob(common_regex + regex, recursive=True)
    print(files)
    move_to_folder(destination_folder, files)
    print("================")


process_files_matching_with_regex("whatsapp-images", "*_*_*.JPG")
process_files_matching_with_regex("camera", "*_*.JPG")
process_files_matching_with_regex("camera-multi", "*.MOV")
process_files_matching_with_regex("screenshots", "*.PNG")
process_files_matching_with_regex("whatsapp_videos_and_screenrecords", "*_*.MP4")
# # MOVER TODO LO DE WPP Y GRABACIONES DE PANTALLA PREVIO A BUSCAR EL RESTO DE .MP4 QUE VAN A SER A TIKTOKS
process_files_matching_with_regex("tiktoks", "*.MP4")
