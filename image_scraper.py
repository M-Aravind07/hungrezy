from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()
absolute_image_path=response.download({"keywords":"dosa","limit":200,"chromedriver":"/home/aravind/chromedriver"})