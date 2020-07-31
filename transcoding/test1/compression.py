import subprocess
from subprocess import run
from ffmpy3 import FFmpeg
import ffmpy3
import os
from django.urls import reverse
# code for video compression only.
def compression(request):
    for subdirs,dirs,files in os.walk(media):
        for file in files:
            input_file=subdirs+"/"+file
            output_file=subdirs+"compression_"+file
            print(output_file)
            extension=os.path.splitext(file)[-1].lower()
            if extension== '.mp4':
                print(extension)
                ff = FFmpeg(
                        inputs={input_file: None},
                        outputs={output_file: '-crf 44'}
                            )
            elif extension== '.AVI':
                print(extension)
                ff = FFmpeg(
                        inputs={input_file: None},
                        outputs={output_file: '-crf 44'}
                            )
                print("done")
            else:
                pass
    
    return media



    '''FUNCTION FOR TRANSCODING FOR FILES'''
def transcoding(self):
    '''GETTING ALL FILES,DIRS,SUBDIRS'''
    for subdirs,dirs,files in os.walk(data):
        for file in files:
            
            '''SETTIGN A PATH FOR INPUT FILES AND COMPRESSED FILE'''
            input_file=subdirs+"/"+file
            output_file=subdirs.replace('documents','compressed')+"/"+"compresssed_"+file
            extension=os.path.splitext(file)[-1].lower()

            '''FINDIG .MP4 FILES IN CURRENT DIRS'''
            if extension=='.mp4':

                '''GIVING THE FILES FOR TRANSCODING'''
                ff = FFmpeg(
                        inputs={input_file: None},
                        outputs={output_file: '-crf 44'}
                            )
                ff.run()          
    return data