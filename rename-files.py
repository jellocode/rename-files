import zipfile
import os

def rename_files(zip_file_path, new_prefix='new_name_'):
    # opens existing zip file in read
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # get list of files in zip
        file_list = zip_ref.namelist()

        # rename files sequentially and create a new zip file
        
        # replace 'renamed_files.zip' with name of new folder
        with zipfile.ZipFile('renamed_files.zip', 'w') as new_zip_ref:
            for i, old_file_name in enumerate(file_list):
                # replace 'new_prefix' with name of your choice
                new_file_name = f"{new_prefix}{i + 1}{os.path.splitext(old_file_name)[1]}"
                
                # read the file content
                file_content = zip_ref.read(old_file_name)
                
                # write file with new name to the new zip file
                new_zip_ref.writestr(new_file_name, file_content)

    print('Files have been renamed :3 ...')

# replace 'example.zip' with path to your existing zip file
rename_files(r'example.zip')