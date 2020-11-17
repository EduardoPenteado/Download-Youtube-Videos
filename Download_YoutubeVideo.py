#!/usr/bin/env python
# coding: utf-8

# In[8]:


from pytube import YouTube

class Download_Youtube():
    
    def __init__(self):
        self.link = input('Insert the video link: ' '[youtube.com/...]')
        index = self.link.index('=')
        self.link = 'https://youtu.be/'+self.link[index+1:]
    
    def Download(self):
        yt = YouTube(self.link)
        filename = yt.title
        check = ['360p','420p','720p','1080p']
        print('***IMPORTANT***\n In resoluion 360p, the video contains audio. In the other resolutions, the download will contains 2 archives: audio and video')
        options = input('Insert the resolution to download the video!: '+"['360p','420p','720p','1080p']")
        print('\n'+filename+'\nDOWNLOADING . . .')
        if options in check:
            try:
                if options == '360p':
                    yt.streams.filter(resolution=options).first().download(filename=filename+' [VIDEO]')
                    print('DOWNLOAD COMPLETE')
                    print('The video have been downloaded in the folder that contains this archive')
                else:
                    yt.streams.filter(resolution=options).first().download(filename=filename+' [VIDEO]')
                    yt.streams.filter(type='audio').first().download(filename=filename+' [ÁUDIO]')
                    print('DOWNLOAD COMPLETE')
                    print('The video have been downloaded in the folder that contains this archive')
            except Exception:
                print('The resolution '+options+' is not available to download, please insert other resolution!')
        else:
            print('Invalid Resoluion.')
        
video = Download_Youtube()
video.Download()

