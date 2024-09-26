# WAP taking URL from user input in GUI

import requests

def download_file(url, file_name):

    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Open a local file in binary write mode and save the content
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"File '{file_name}' downloaded successfully.")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
        print(f"Status code: {response.status_code}")


if __name__ == "__main__":
    url = "https://www.cte.iup.edu/cte/Resources/PDF_TestPage.pdf"
    file_name = 'test.pdf'
    download_file(url,file_name)