#!/usr/bin/env python

import os
import youtube_dl
import pickle
import time
from soundcloudbot import SoundCloudBot

class MyLogger(object):
    def debug(self, msg):
        print("Debug:" + msg)

    def warning(self, msg):
        print("Warning:" + msg)

    def error(self, msg):
        print(msg)

def my_hook(d):
    # if d['status'] == 'downloading':
    #     print('Downloading video!')
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

# ydl_opts = {
#     'format': 'bestaudio/best',
#     'postprocessors': [{
#         'key': 'FFmpegExtractAudio',
#         'preferredcodec': 'wav',
#     }],
#     'logger': MyLogger(),
#     'progress_hooks': [my_hook],
# }

externalDrive = '/Volumes/Tat SSD/Music Lib/SoundCloud Lib/'
externalDriveYT = '/Volumes/Tat SSD/Music Lib/Youtube Lib/'
ydl_opts = {
    # 'format': format_string,
    'format': 'bestaudio/best',
    'outtmpl': externalDrive + '%(title)s.%(ext)s',
    # 'outtmpl': externalDriveYT + '%(title)s.%(ext)s',

    # 'download_archive': download_archive,
    # 'outtmpl': outtmpl,
    'default_search': 'ytsearch',
    # 'noplaylist': True,
    # 'no_color': False,
    'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        },
        {'key': 'FFmpegMetadata'}
    ],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

ydl_playlist_opts = {
    # 'format': format_string,
    'format': 'bestaudio/best',
    'outtmpl': externalDriveYT + '%(title)s.%(ext)s',
    # 'outtmpl': externalDriveYT + '%(title)s.%(ext)s',

    'download_archive': externalDriveYT + 'download_archive',
    # 'outtmpl': outtmpl,
    'default_search': 'ytsearch',
    # 'noplaylist': True,
    # 'no_color': False,
    'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        },
        {'key': 'FFmpegMetadata'}
    ],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}


'''
* Try downloading a given file
* After download finishes, move it to the right folder
* Also save successfully downloaded files to a pickle file to keep track of lib
* Save everything in one folder
* Symlink files into organized libraries??
'''


# if __name__ == '__main__':
#
#     # outtmpl = f"{file_path}.%(ext)s"
#
#     SCBot = SoundCloudBot()
#     tracks = SCBot.tracks
#     indexFile = externalDrive + 'lib_index.pickle'
#
#     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#         infile = None
#         written_titles = set()
#         try:
#             with open(indexFile, 'rb') as infile:
#                 written_titles = pickle.load(infile)
#         except (FileNotFoundError, EOFError, TypeError, ValueError) as e:
#             print(e)
#             written_titles = set()
#
#         titles = list(map(lambda t: tracks[t]['user'] + ' ' +
#                                     tracks[t]['title'] + ' Radio Edit', tracks))
#         print(titles)
#         # titles = track['user'] + ' ' + track['title']
#         # ydl.download(titles)
#         to_download = set()
#         for title in titles:
#             if title in written_titles:
#                 continue
#             else:
#                 to_download.add(title)
#
#         for ind, title in enumerate(to_download):
#             print("Downloading", ind + 1, "of", len(to_download))
#             if title in written_titles:
#                 continue
#
#             try:
#                 ie_res = ydl.extract_info(title, False)
#                 if not(len(ie_res['entries']) > 0 and 'duration' in ie_res[
#                     'entries'][0] and ie_res['entries'][0]['duration'] < 500):
#                     continue
#
#                 dl_res = ydl.extract_info(title)
#                 time.sleep(2)
#
#                 written_titles.add(title)
#             except Exception as e:
#                 print(e)
#
#         # with open(indexFile, 'wb') as outfile:
#         #     print(written_titles)
#         #     pickle.dump(written_titles, outfile)
#
#         # result = ydl.extract_info(
#         #     # 'Swedish House Mafia - 19.30'
#         # #         'https://open.spotify.com/track/5aOpzm8W8zysk4asB9hxJw?si=361183683c6f41aa',
#         #         'https://soundcloud.com/officialswedishhousemafia/swedish-house-mafia-19-30',
#         # #         download=False # We just want to extract the info
#         #     )
#
#         # print(result.keys())
#         # if 'entries' in result:
#         #     # Can be a playlist or a list of videos
#         #     video = result['entries'][0]
#         #     print(result['entries'])
#         # else:
#         #     # Just a video
#         #     video = result
#         #
#         # if 'uploader' in result:
#         #     print(result['uploader'])
#         # if 'title' in result:
#         #     print(result['title'])


def downloadPlaylist(name, url):
    folder = externalDriveYT + '/' + name + '/'
    filepath = folder + '%(title)s.%(ext)s'
    archive = folder + 'download_archive'
    if not os.path.exists(folder):
        os.makedirs(folder)

    ydl_playlist_opts['outtmpl'] = filepath
    ydl_playlist_opts['download_archive'] = archive

    with youtube_dl.YoutubeDL(ydl_playlist_opts) as ydl:
        ydl.extract_info(url)


def downloadSong(url):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info(url)

if __name__ == '__main__':

    # outtmpl = f"{file_path}.%(ext)s"

    # SCBot = SoundCloudBot()
    # tracks = SCBot.tracks
    # indexFile = externalDrive + 'lib_index.pickle'
    # Lib deep house
    downloadPlaylist("House - Deep House",
                     "https://www.youtube.com/playlist?list=PLjDKD6CQUAffacoq4fNZMiRjTL9LBNkbi")
    # Lib House Catch Phrases
    downloadPlaylist("House - Catch Phrases",
                     "https://www.youtube.com/playlist?list=PL52JIFTmqtiVaebUu1pWaW9-GJU-xMz9q")

    # Lib House Tech house
    downloadPlaylist("House - Tech House",
                     "https://www.youtube.com/playlist?list=PLjDKD6CQUAfft_s3L4yHTxr-C2C3lIsGw")
    # Lib House - Bass House
    downloadPlaylist("House - Bass House",
                     "https://www.youtube.com/playlist?list=PL52JIFTmqtiXLqPAwiJ-s9schx2x1deDR")
    # Lib House - Progressive House
    downloadPlaylist("House - Progressive House",
                     "https://www.youtube.com/playlist?list=PL52JIFTmqtiVW6kN_JoyQH8717MalvKgP")
    # Lib House - G House
    downloadPlaylist("House - G House",
                     "https://www.youtube.com/playlist?list=PLjDKD6CQUAff_ce5x58PK2N6SKLi13wHs")
    # Lib minimal
    downloadPlaylist("House - Minimal House",
                     "https://www.youtube.com/playlist?list=PLjDKD6CQUAfdAe5Td4lkNRsFN6GwhWTBe")
    # Lib minimal tech afro
    downloadPlaylist("House - Minimal Tech Afro",
                     "https://www.youtube.com/playlist?list=PLjDKD6CQUAffN2lm99UIVMorJ9fP-tYEK")
    # Lib Organic
    downloadPlaylist("House - Organic House",
                     "https://www.youtube.com/playlist?list=PLjDKD6CQUAffn9jslU7R5NHc6CAAQwyz6")
    # Lib Bigroom / Rave
    # downloadPlaylist("House - Bigroom / Rave",
    #                  "https://www.youtube.com/playlist?list=PL52JIFTmqtiV__i2IDhbdXXud6KPD32C4")
    # Lib Bigroom / Rave
    downloadPlaylist("House - Dance Electronic Future",
                     "https://www.youtube.com/playlist?list=PLjDKD6CQUAfcMEOf1bJR8AwE_CX8xYQ6O")


    # Lib Hip hop
    downloadPlaylist("Hip Hop",
                     "https://www.youtube.com/playlist?list=PLjDKD6CQUAfdMn_rWnn_btnCSaQOSOrmi")
    # Trap
    downloadPlaylist("Trap",
                     "https://www.youtube.com/playlist?list=PLjDKD6CQUAfeUScKEFB8eTG4YWJm3wIia")

    # Desi
    downloadPlaylist("Desi",
                     "https://www.youtube.com/playlist?list=PLjDKD6CQUAfeC9FJLMinhjBzgQwD3GSks")

    # # downloadPlaylist()
    # Lib Acapellas
    downloadPlaylist("House - Fav Acapellas",
                     "https://www.youtube.com/playlist?list=PLjDKD6CQUAfeQAVV0I0qdKWKxPQ5PoZWm")
    # Lib iconic
    downloadPlaylist("House - Iconic",
                     "https://www.youtube.com/playlist?list=PL52JIFTmqtiVnDGGrANH8qi-loz7wkKjC")


    # Lib bass house
    downloadPlaylist("House - Bass House - Arnav",
                     "https://music.youtube.com/playlist?list=PL7kDOF7v0GUYiYIwJC1Grt1Jh5xQiMZn5")
    # Mixing Vibey
    downloadPlaylist("Mixing Vibey",
                     "https://music.youtube.com/playlist?list=PL7kDOF7v0GUYflI1bDY1fTBrj2_0ITTp4")

    # downloadSong("https://www.youtube.com/watch?v=yoIeg9B8EEg&list=RDJqzbsnwcRuc&index=2")

    # with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #     # infile = None
    #     # written_titles = set()
    #     # try:
    #     #     with open(indexFile, 'rb') as infile:
    #     #         written_titles = pickle.load(infile)
    #     # except (FileNotFoundError, EOFError, TypeError, ValueError) as e:
    #     #     print(e)
    #     #     written_titles = set()
    #     #
    #     # titles = list(map(lambda t: tracks[t]['user'] + ' ' +
    #     #                             tracks[t]['title'] + ' Radio Edit', tracks))
    #     # print(titles)
    #     # # titles = track['user'] + ' ' + track['title']
    #     ydl.extract_info("https://www.youtube.com/watch?v=ziDHaXj4IkE&ab_channel=Spinnin%27Records")
        # to_download = set()
        # for title in titles:
        #     if title in written_titles:
        #         continue
        #     else:
        #         to_download.add(title)
        #
        # for ind, title in enumerate(to_download):
        #     print("Downloading", ind + 1, "of", len(to_download))
        #     if title in written_titles:
        #         continue
        #
        #     try:
        #         ie_res = ydl.extract_info(title, False)
        #         if not(len(ie_res['entries']) > 0 and 'duration' in ie_res[
        #             'entries'][0] and ie_res['entries'][0]['duration'] < 500):
        #             continue
        #
        #         dl_res = ydl.extract_info(title)
        #         time.sleep(2)
        #
        #         written_titles.add(title)
        #     except Exception as e:
        #         print(e)

        # with open(indexFile, 'wb') as outfile:
        #     print(written_titles)
        #     pickle.dump(written_titles, outfile)

        # result = ydl.extract_info(
        #     # 'Swedish House Mafia - 19.30'
        # #         'https://open.spotify.com/track/5aOpzm8W8zysk4asB9hxJw?si=361183683c6f41aa',
        #         'https://soundcloud.com/officialswedishhousemafia/swedish-house-mafia-19-30',
        # #         download=False # We just want to extract the info
        #     )

        # print(result.keys())
        # if 'entries' in result:
        #     # Can be a playlist or a list of videos
        #     video = result['entries'][0]
        #     print(result['entries'])
        # else:
        #     # Just a video
        #     video = result
        #
        # if 'uploader' in result:
        #     print(result['uploader'])
        # if 'title' in result:
        #     print(result['title'])
