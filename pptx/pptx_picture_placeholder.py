from pptx import Presentation
from PIL import Image


def make_square(im, min_size=256, fill_color=(0, 0, 0, 0)):
    x, y = im.size
    size = max(min_size, x, y)
    new_im = Image.new('RGBA', (size, size), fill_color)
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    return new_im

def create_squared_image(img_path):
    image_to_square = Image.open(img_path)
    new_image = make_square(image_to_square, min_size=64, fill_color=(64, 64, 64, 64))
    new_image.save('new_image.png')

def squared_image_path(img_path):
    # return 'resources/monoscope_728x410_squared.jpg'
    return 'new_image.png'


if __name__ == '__main__':

    img_path = 'resources/monoscope_728x410.jpg'
    save_path = 'test_placeholders.pptx'

    prs = Presentation()

    img_path = 'resources/monoscope_728x410.jpg'
    slide = prs.slides.add_slide(prs.slide_layouts[8])
    placeholder = slide.placeholders[1]
    # print('placeholder: ', placeholder.name)
    # print('format:', placeholder.placeholder_format.type)
    picture = placeholder.insert_picture(img_path)

    img_path = 'resources/monoscope_728x410.jpg'
    slide = prs.slides.add_slide(prs.slide_layouts[8])
    placeholder = slide.placeholders[1]
    create_squared_image(img_path)
    img_path = squared_image_path(img_path)
    picture = placeholder.insert_picture(img_path)

    img_path = 'resources/monoscope_728x410.jpg'
    slide = prs.slides.add_slide(prs.slide_layouts[8])
    print('picture shapes')
    for shape in slide.placeholders:
        print('%d %s %s %s' % (shape.placeholder_format.idx, shape.name, shape.is_placeholder, shape.placeholder_format))
        print('%d %d %d %d' % (shape.height, shape.width, shape.top, shape.left))
    placeholder = slide.placeholders[1]
    create_squared_image(img_path)
    img_path = squared_image_path(img_path)
    picture = placeholder.insert_picture(img_path)
    print('picture crop values')
    print('%s %s %s %s' % (picture.crop_left, picture.crop_right, picture.crop_top, picture.crop_bottom))
    print('picture name')
    print('%s' % (picture.name))
    picture.crop_top = 0

    img_path = 'resources/IMG_300x300_blue.png'
    slide = prs.slides.add_slide(prs.slide_layouts[8])
    placeholder = slide.placeholders[1]
    create_squared_image(img_path)
    img_path = squared_image_path(img_path)
    picture = placeholder.insert_picture(img_path)

    img_path = 'resources/IMG_600x300_blue.png'
    slide = prs.slides.add_slide(prs.slide_layouts[8])
    placeholder = slide.placeholders[1]
    create_squared_image(img_path)
    img_path = squared_image_path(img_path)
    picture = placeholder.insert_picture(img_path)

    img_path = 'resources/IMG_300x600_blue.png'
    slide = prs.slides.add_slide(prs.slide_layouts[8])
    placeholder = slide.placeholders[1]
    create_squared_image(img_path)
    img_path = squared_image_path(img_path)
    picture = placeholder.insert_picture(img_path)

    prs.save('test_placeholders.pptx')

