import math 
import speedtest # pip install speedtest-cli


def bytes_to_mb(size_bytes):
    i = int(math.floor(math.log(size_bytes, 1024)))
    power = math.pow(1024,i)
    size = round(size_bytes / power , 2)
    return f"{size} Mbps"


ether = speedtest.Speedtest()

print('Getting download speed...')
download_speed = ether.download()

print('Getting upload speed...')
upload_speed = ether.upload()

print('Download Speed : ' , bytes_to_mb(download_speed))
print('Upload Speed : ' , bytes_to_mb(upload_speed))
