import os
import shutil

class FileUtils:
    
    @staticmethod
    def file_list(dir):
        file_list = []
        
        for root, _, files in os.walk(dir):
            for f in files:
                file_list.append(os.path.join(root, f))

        return file_list
    
    @staticmethod
    def delete_file(file):
        os.remove(file)
        
    @staticmethod
    def delete_dir(dir):
        shutil.rmtree(dir)
    