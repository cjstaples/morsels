from pptx import Presentation
from pptx.util import Inches

img_path = 'resources/autolocale.png'

prs = Presentation()
blank_slide_layout = prs.slide_layouts[6]
slide = prs.slides.add_slide(blank_slide_layout)

left = top = Inches(1)
pic = slide.shapes.add_picture(img_path, left, top)

img_path = 'resources/subway.png'

left = Inches(4)
height = Inches(2.0)
pic = slide.shapes.add_picture(img_path, left, top, height=height)

top = Inches(3)
left = Inches(5)
height = Inches(2.0)
pic = slide.shapes.add_picture(img_path, left, top, height=height)

prs.save('test_picture.pptx')