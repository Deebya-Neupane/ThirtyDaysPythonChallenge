# Example file for retrieving data from the internet.

import urllib.request

def main():
    webUrl = urllib.request.urlopen("https://www.youtube.com/")
    print("result code: " + str(webUrl.getcode())  + "\n")
    data = webUrl.read()
    print(data)

if __name__=="__main__":
    main()