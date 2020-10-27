import wget

f = open("DataBaseImages.txt", "r")

while True:
    try:
        url = f.readline()

        print(url)

        wget.download(url, "/home/guillem/Desktop/Padel_Image_Recognition_Analisis_(PIRA)/ImagesTennisBall")
    except:
        print("Error " + url)
f.close()
