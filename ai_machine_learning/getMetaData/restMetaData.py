i = Image.open(image_path)

    for segment, content in i.applist:
        c = str(content).split("x00", 1)
        c[1] = c[1][:-1]
        if segment == 'APP1' and 'http://ns.adobe.com/xap/1.0/' in str(content):
            print (c[1])

    from bs4 import BeautifulSoup

    with open( image_path, "rb") as fin:
        img = fin.read()
    imgAsString=str(img)
    xmp_start = imgAsString.find('<x:xmpmeta')
    xmp_end = imgAsString.find('</x:xmpmeta')
    if xmp_start != xmp_end:
        xmpString = imgAsString[xmp_start:xmp_end+12]

        xmpAsXML = BeautifulSoup( xmpString )
        print(xmpAsXML.prettify())