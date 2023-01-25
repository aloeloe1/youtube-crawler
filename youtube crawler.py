import pytube
import requests
from tqdm import tqdm
print('this one is made for fun')
while True:
    link1=input('\n\n\ninput your link:',)
    list1=[]
    list2=[]
    def kiezen1(link):

        yt=pytube.YouTube(link)
        video=yt.vid_info
        # print(type(video))
        # print(video)
        link_number=len(video['streamingData']['formats'])
        for i in range(link_number):

            # print(video['streamingData']['formats'][i],'\n')
            videos=video['streamingData']['formats'][i]
            itag=videos['itag']
            url=videos['url']
            qualitylabel=videos['qualityLabel']
            codes=videos['mimeType']
            if 'video/mp4' in codes:
                print('number=',itag)
                print('this is video')
                print('url=',url)
                print('type=',codes)
                print('qualitylabel=',qualitylabel,'\n\n\n')
                list1.append(str(itag))
                list2.append(url)
                # print(list1,list2)
            else:
                print('number=', itag)
                print('this is audio')
                print('url=', url)
                print('type=', codes)
                print('qualitylabel', qualitylabel, '\n\n\n')
                list1.append(str(itag))
                list2.append(url)
                # print(list1,list2)
    kiezen1(link1)
    dictkiezen=dict(zip(list1,list2))
    # print(dictkiezen)
    kiezen= input(str('which number do you want？:'))
    rsp=requests.get(dictkiezen[kiezen],stream=True)
    video_headers=rsp.headers.get('Content-Length')
    print(video_headers)
    videolang=tqdm(total=int(video_headers))
    print(rsp)
    with open(kiezen+'.mp4',mode='wb')as f:
        for videoss in rsp.iter_content(1024*1024*2):
            f.write(videoss)
            videolang.set_description(f'we are started with number{kiezen}...')
            videolang.update(1024*1024*2)
        videolang.set_description('finished')
        videolang.close()

