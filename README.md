# Padel-Image-Recognition-Analisis-PIRA-


PIRA is a Machine Learning project based on Computer Vision that by watching Padel matches tries to get stats of the match in real time.

To create the dataset, we have we have downloaded some matches of the tournament World Padel Tour using youtube-dl and ffmpeg to transform the video to a dataset of images. 

# Installation
First of all we will need to install these packages:
```sh
$ sudo apt install youtube-dl
$ sudo apt install ffmpeg
```

Once we have them installed, we will start the download of the video:
```sh
$ youtube-dl <video-link(Youtube)
```

When it's done we will process it to make it into images:
```sh
$ ffmpeg -i <input.mp4> -vf fps=<numFps> out%d.png
```




