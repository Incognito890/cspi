import os
from pytube.cli import on_progress
from termcolor import colored, cprint
import requests
import argparse
from hurry.filesize import size, si
from pytube import YouTube

def banner():

  cprint(""" 

      .               .    
 .´  ·  .     .  ·  `.  cspi v1.0
 :  :  :  (¯)  :  :  :  a simple cli youtub video downloader
 `.  ·  ` /¯\ ´  ·  .´  Author: Mr.Rajeev kumar
   `     /¯¯¯\     ´    https://github.com/ """,'green') 


def check_dependencies():
   try:
       import requests
       import argparse
       from pytube import YouTube
       print(colored('[+]', 'blue'), colored('All dependencies are already install', 'white'))
   except ImportError:
       print('[!] Error: some dependencies are not installed')
       print('Type \'pip install -r requirements.txt\' to install all required packages')
       exit()

def checkinternet():
    res = False
    try:
        requests.get('https://www.google.com', verify=True)
        res = False
        print(colored('[+]', 'yellow'), colored('connection established successfully to youtube.com (172.217.174.238)', 'blue'))
    except Exception:
        res = True
    if res:
        print(colored('[!]','red'), colored('It seems That Your Internet Speed is Slow or You Are Using Proxies..','green'))
        print(colored('[!]','red',attrs=['blink']), colored('Your are not connected to the internate','green'))
        print('[-] Cspi  Will Stop Now...')
        exit()

def dowcspi(Url,Path,Format,Quality):

    mystreams = {

      "360p": 18,
      "720p": 22,
      
    }
    
    socketr = YouTube(Url, on_progress_callback=on_progress)

    if(Format == "video"):
         
         stream = socketr.streams.get_by_itag(mystreams[Quality])
         #stream.download(Path)
         
    else:
        if(Format == "audio"):
              stream = socketr.streams.filter(only_audio=True).first()
              #stream.download(Path) 
        else:
            print(colored('[!]','red'),colored('Your format is infalid try another..','blue')) 
    
    print(colored(f'{Format} info:','blue'))
    print(colored(f'From:','yellow'),colored(f'{socketr.author} youtub channel','white'))
    print(f"Title is {socketr.title} and length {socketr.length}...")
    print(f"Publish date: {socketr.publish_date}...\nTotal views {socketr.views}..\nRating of the {Format} is {socketr.rating}...")
    print(f"Thumbnail url of {Format} is {socketr.thumbnail_url}....\n")
    print(f"After this operation, {size(stream.filesize_approx,system=si)} of additional disk space will be used.")
    dis = input("Do you want to continue? [Y/n]") 
    
    if(dis == "Y" or dis == "y"):
         #socketr.prefetch()
         stream.download(Path) 
         print(f"conglations your {Format} file is successfully downloaded...")
    else:
        exit()
    
          


           
    
# argparse controle is started form now 



parser = argparse.ArgumentParser(prog='cspi',  description='The option [url] is required [other options] are optional.'
,usage='%(prog)s -u [url] [other options..] ', epilog='so sorry there is only to regulation are avalable[360p,720p]:)')

parser.version = 'cspi version 1.0'
parser.add_argument('-u','--url', action='store', help='set the download url for downloading',nargs = 1, metavar = '',default = None,required=True,type=str)
parser.add_argument('-p','--path', action='store',help='set the path for download[optional]',nargs = 1,metavar = '',default =['Download/'])
parser.add_argument('-f','--format',action='store',help='set the download format(default video)(optiona)',nargs = 1, metavar = '',default =['video'])
parser.add_argument('-q','--quality',action='store',help='set the download regulation(default 720p)(optional)',nargs = 1, metavar = '',default =['360p'])

parser.add_argument('-v','--version', action='version')

args = parser.parse_args()


check_dependencies()
checkinternet()

dowcspi(args.url[0],args.path[0],args.format[0],args.quality[0])

       







