# -*- coding: UTF-8 -*-

import os
import subprocess
from glob import glob

if __name__ == '__main__':
    path = input("path: ")
    num = input("num per second: ")
    file_list = glob(path + "\\*.jpg")
    video_name = input("video name: ")
    encode_type = int(input("encode type (1 - nvidia, 2 - intel): "))
    with open(path + "\\input.txt", "w") as f:
        for i in file_list:
            file_name = i.split('\\')[-1]
            if file_name.__contains__("thumbnail"):
                continue
            f.write("file " + file_name + "\n")
            f.write("duration {}\n".format(1 / int(num)))
    command = '''ffmpeg -f concat -i {}\input.txt -c:v {} -r 25 -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2" -loglevel error -y {}\{}.mp4'''.format(
        path, "h264_qsv" if 2 == encode_type else "h264_nvenc", path, video_name)
    print("executing command: " + command)
    code = subprocess.call(command, shell=True)
    print("subprocess exit code: {}".format(code))
    del_pic = int(input("delete pics? 1 or 0: "))
    if (del_pic):
        print("deleting...")
        for i in file_list:
            os.remove(i)
        print("delete finished")
# damn noob things
# ffmpeg -f concat -i input.txt -c:v h264_qsv -r 25 -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2" -loglevel error -y output.mp4
# h264_nvenc
# ffmpeg -framerate 8 -i happy%d.jpg -s 1280x720 -vf format=yuv420p -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -r 30 output.mp4
#
# cat *.jpg | ffmpeg -framerate 8 -i - -s 1280x720 -vf format=yuv420p -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -r 30 output.mp4
#
# ls *.jpg | perl -ne 'print "file $_"' | ffmpeg -framerate 8 -i - -s 1280x720 -vf format=yuv420p -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -r 30 output.mp4
#
# ls *.jpg | % { $n = $_.name; "file '$n'" } | out-file -Encoding UTF8NoBOM input.txt
# ffmpeg -f concat -i input.txt -framerate 8 -s 1280x720 -vf format=yuv420p -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -r 30 output.mp4
#
# ffmpeg -r 60 -f image2 -s 1920x1080 -i pic%04d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p test.mp4
#
# ffmpeg -framerate 30 -pattern_type glob -i '*.jpg' -c:v libx264 -pix_fmt yuv420p out.mp4
# ffmpeg -f concat -i input.txt -framerate 8 -vf format=yuv420p -vf scale=-1:1280 -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -r 30 -loglevel error output.mp4
# ffmpeg -f concat -i input.txt -framerate 15 -vf format=yuv420p -vf scale=-1:1280 -c:v libx264 -r 30 -loglevel error output.mp4
# ffmpeg -f concat -i input.txt -framerate 15 -vf format=yuv420p -vf scale="1280:-2" -c:v libx264 -r 30 -vcodec h264_qsv -loglevel error output.mp4
# ffmpeg -f concat -i input.txt -framerate 15 -vf format=yuv420p -vf scale="1280:-2" -c:v hevc_qsv -r 30 -vcodec h264_qsv -loglevel error output.mp4
# ffmpeg -f concat -i input.txt -framerate 5 -r 30 -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2" -c:v h264_qsv -loglevel error output.mp4
# ffmpeg -f concat -i input.txt -framerate 5 -r 60 -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2" -c:v hevc_qsv -loglevel error output.mp4
