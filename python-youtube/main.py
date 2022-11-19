from pytube import YouTube


def get_download_options(link):
    yt_obj = YouTube(link)
    for item in yt_obj.streams:
        print(item)
    while True:
        itag = input("Enter the itag to download: ")
        if itag.isdigit():
            return itag, yt_obj
        print("Please enter a valid itag integer from the list of options")
        
def download_high_res(link):
    yt_obj = YouTube(link)
    yt_obj = yt_obj.streams.get_highest_resolution()
    try:
        yt_obj.download()
    except:
        print("An error occured when downloading")
    print("Video Downloaded Successfully")

def download(itag, yt_obj):
    yt_obj = yt_obj.streams.get_by_itag(itag)
    yt_obj.download()


def main():
    yt_link = input("Enter the link of youtube video: ")
    print("\nChoice 1: Download video quality of your choice.\nChoice 2: Download Highest Resolution directly\n")
    choice = input("Enter the choice: ")
    match choice:
        case "1":
            itag, yt_obj = get_download_options(yt_link)
            download(itag, yt_obj)
        case "2":
            download_high_res(yt_link)
        case other:
            print("Wrong Choice")
if __name__ == "__main__":
    main()