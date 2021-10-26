#pip install pillow
from PIL
import Image

imageColor = Image.open(yourPath)

imageBlackAndWhite = imageColor.convert('L')
imageBlackAndWhite.save(yourPath)