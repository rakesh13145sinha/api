from django.shortcuts import render,HttpResponse,HttpResponseRedirect
import subprocess
from subprocess import run
from ffmpy3 import FFmpeg
import ffmpy3
import os
from django.urls import reverse
from test1.forms import File_Upload_Form,File_upload
from test1.models import File_Upload
from django.conf import settings
from test1.compression import transcoding
from django.core.files.storage import FileSystemStorage
import re
from django.http import JsonResponse
media=settings.MEDIA_ROOT

'''THIS IS HOME PAGE FUNCTION'''
def home(request):
    check()
    #save_uploaded_data()
    uploaded_data=File_Upload.objects.all()
    return render(request,'templates/test1/home.html',{'uploaded_data':uploaded_data})

'''DELETE FILES'''
def delete_file(request,id):
    uploaded_data=File_Upload.objects.get(id=id)
    uploaded_data.delete()
    return HttpResponseRedirect(reverse("home"))

'''UPLOADING THE FILES '''
def upload_file(request):
    form=File_Upload_Form()
    if request.method=='POST':
        form=File_Upload_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("home"))
    else:
        form=File_Upload_Form()
    return render(request,'templates/test1/com.html',{'form':form})

'''FUNCTION FOR TRANSCODING FOR FILES'''
def transcoding():
    for files in os.listdir(media):
        end=re.search(".mp4$",files)
        endavi=re.search(".avi$",files)
        endjpg=re.search(".jpeg$",files)
        start=re.search("^compresssed_",files)

        ''' for mp4 video format'''
        if end != None:
            if start!=None:
                print("yes")

            else:
                input_file=media+"/"+files
                output_file=media+"/encode"+"/"+"compresssed_"+files
                ff = FFmpeg(
                        inputs={input_file: None},
                        outputs={output_file: '-crf 44'}
                            )
                ff.run() 
                break   
        else:
        
            print("no mp4 file",files)

        '''for avi format video'''
        if endavi !=None:
            if start !=None:
                print("avi format file available ")
            else:
                input_file=media+"/"+files
                output_file=media+"/encode"+"/"+"compresssed_"+files
                ff = FFmpeg(
                            inputs={input_file: None},
                            outputs={output_file: '-crf 44'}
                                )
                ff.run() 
                break
        else:
            print("no avi format video")

        '''for jpeg image format'''
        if endjpg !=None:
            if start !=None:
                print("jpeg video format available")
            else:
                input_file=media+"/"+files
                output_file=media+"/encode"+"/"+"compresssed_"+files
                ff = FFmpeg(
                        inputs={input_file: None},
                        outputs={output_file: '-crf 44'}
                            )
                ff.run() 
                break
        else:
            print("no jpeg format available")
            
   
    return save_uploaded_data()


'''after transcoding data save into database'''

def save_uploaded_data():
    data=settings.MEDIA_ROOT+"\encode"
            
    for files in os.listdir(data):
        if File_Upload.objects.filter(document__iexact=files).exists():
            print("file already exsits")
            
        else:
            obj,created=File_Upload.objects.get_or_create(document=files)
            obj.save()
            print("file uploaded successfully")
            break
    return 

'''UPLOAD TEMPORARY DATA '''
def temp_file_store(request): 
    if request.method == 'POST':
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        transcoding()
        return render(request, 'templates/test1/testing.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request,'templates/test1/testing.html')


'''checking file is available or not'''
def check():

    for files in os.listdir(media):

        endmp4=re.search(".mp4",files)
        endavi=re.search(".avi",files)
        endjpeg=re.search(".jpeg",files) 
        if endmp4!=None:
            print(os.remove(media+"/"+files))
        
        else:
            print("not exists")
    return

