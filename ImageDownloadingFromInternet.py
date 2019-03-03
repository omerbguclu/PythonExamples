import urllib.request

url1 = "https://www.safaribooksonline.com/library/view/java-by-comparison/9781680505887/f_0002.xhtml"
url2 = "http://www.agac.gen.tr/images/agac-isimleri.jpg"


urllib.request.urlretrieve(url1,"Page"+".pdf")
inc=1
list=[url1,url2]

