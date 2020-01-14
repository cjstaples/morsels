import collections
import os
import sys
import time
import glob
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3

#   todo:   sanitize tag data to prevent bad directory / file names (':' error)
#   todo:   fiz root directory issue
#   todo:   mutagen.id3._util.ID3NoHeaderError: '01 Far Cry.mp3' doesn't start with an ID3 tag

def create_m3u_playlist(dir="."):
    print('(playlist) create_m3u_playlist:', dir)
    try:
        print("---------- processing directory '%s'..." % dir)

        playlist = ''
        mp3s = []
        glob_pattern = "*.[mM][pP]3"

        os.chdir(dir)

        for file in glob.glob(glob_pattern):
            if playlist == '':
                playlist = EasyID3(file)['album'][0] + '.m3u'

            meta_info = {
                'filename': file,
                'length': int(MP3(file).info.length),
                'tracknumber': EasyID3(file)['tracknumber'][0].split('/')[0],
            }

            mp3s.append(meta_info)

        if len(mp3s) > 0:
            print("Writing playlist '%s'..." % playlist)
            print('----------------')
            print('')

            # open and write playlist
            of = open(playlist, 'w')
            of.write("#EXTM3U\n")

            # sorted by track number
            for mp3 in sorted(mp3s, key=lambda mp3: int(mp3['tracknumber'])):
                of.write("#EXTINF:%s,%s\n" % (mp3['length'], mp3['filename']))
                of.write(mp3['filename'] + "\n")

            of.close()
        else:
            print("---------- no MP3 files found in '%s'." % dir)
            print()

        print("---------- check for sub directories in '%s'..." % dir)
        subfolders = [f.path for f in os.scandir(dir) if f.is_dir()]
        print('subdirs = ',subfolders)
        print()

        for subdir in subfolders:
            create_m3u_playlist(subdir)

    except:
        raise
        print("ERROR occurred processing directory '%s'. Ignoring." % dir)
        print("info: ", sys.exc_info()[0])
        print()


def main(argv=None):
    print('(playlist) main:')
    print()

    if argv is None:
        argv = sys.argv

#    dirs = ['/Users/cstaples/MEDIA/MUSIC/test',
#            '/Users/cstaples/MEDIA/MUSIC/testempty',
#            '/Users/cstaples/MEDIA/MUSIC/testfiles']

#    dirs = ['/Users/cstaples/MEDIA/MUSIC/test']
#    dirs = ['D:\MEDIA.RETAG\MUSIC']

    if len(sys.argv) == 2 and sys.argv[1] == '-':
        # when no args, read from STDIN
        for line in sys.stdin:
            dirs.append(line.strip())
    else:
        # when there are dir args
        for argdir in sys.argv[1:]:
            dirs.append(argdir)

    # make a playlist for each dir
    for dir in dirs:
        create_m3u_playlist(dir)

    print()
    print('(playlist) end::')
    return 0


# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(result)
