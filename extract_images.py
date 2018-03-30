import zipfile

def extract_images(filename):
    EmbeddedFiles = zipfile.ZipFile(filename).namelist()
    ImageFiles = [F for F in EmbeddedFiles if F.count('.png')]

    for Image in ImageFiles:
        zipfile.ZipFile(filename).extract(Image)
