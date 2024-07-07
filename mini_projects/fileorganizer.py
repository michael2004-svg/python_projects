import os
import shutil
folder_to_organize=input("enter the folder to organize  ").capitalize()
directory=os.path.join(os.path.expanduser("~"), folder_to_organize)
extensions={
    ".jpg":"Images",
    ".png":"Images",
    ".jpeg":"Images",
    ".zip":"Ziped Files",
    ".exe":"Apks",
    ".mp3":"Music",
    ".docx":"Documents",
    ".doc":"Documents",
    ".pdf":"Pdfs",
    ".csv":"Documents",
    ".mp4":"Videos",
    ".blend":"Blender objects",
    ".txt":"Text Files"
}
for filename in os.listdir(directory):
    file_path =os.path.join(directory, filename)
    
    if os.path.isfile(file_path):
        extension=os.path.splitext(filename)[1].lower()
        
        if extension in extensions:
            folder_name=extensions[extension]
            
            folder_path=os.path.join(directory,folder_name)
            os.makedirs(folder_path,exist_ok=True)
            
            destination_path=os.path.join(folder_path,filename)
            shutil.move(file_path,destination_path)
            
            print(f"moved {filename} to {folder_name}")
        else:
            print(f"skipped {filename} unknownfile extension")
    else:
        print(f"skipped {filename} is a directory")
print("file organization complete") 