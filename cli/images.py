from term_image.image import from_url

def get_image(url):
    try:
        img = from_url(url)
        return img
    except:
        print(f"Failed to fetch image from {url}")


def draw_image(img):
    img.height = 15
    img.draw(h_align="left", pad_height=-30)
    img.draw()