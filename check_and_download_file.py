import os
import urllib
	
def check_and_download_file(local_file, url):
    """ Python script that checks if the file local_file exists locally, and if not,
    downloads it from a specified URL

    Explanation:
    os.path.exists(local_file): Checks if the file already exists locally.
    urllib.request.urlretrieve(url, local_file): Downloads the file if it’s not available locally.


    Copyright notice: use as is, please cite the source and the author. No guarantees.
    (c) Gabriel Turinici 2021
    """

    #print('Check if the file exists locally')
    if not os.path.exists(local_file):
        print(f"{local_file} not found. Downloading from {url}...")
        # Download the file from the given URL
        urllib.request.urlretrieve(url, local_file)
        print(f"Downloaded {local_file}")
    else:
        print(f"{local_file} already exists locally.")

# Example usage
local_file = 'download_test.txt'
url='https://turinici.com/wp-content/uploads/data/download_test.txt'

check_and_download_file(local_file, url)
