def main():
    filename = input("File name: ").strip().lower()
    print(determine_media_type(filename))

def determine_media_type(filename):
    media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }
    for extension, media_type in media_types.items():
        if filename.endswith(extension):
            return media_type
    return "application/octet-stream"

main()
