from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import os
//give any text as input as for petta image i gave the inputs the youtube comments for petta trailer petta songs
//text i edited that one
// like this text="now i can able to speak in the english words so do not worry about the things i have in the hand let have talk about loves and singles and mingles they are very issues cirulating her therm facing manyproblems in the day to day life"

ormask=np.array(Image.open('petta.jpg'))
cloud=WordCloud(background_color="black", mask=ormask, contour_width=10, contour_color='white').generate(text)
cloud.to_file(path.join('wc1.png'))
plt.imshow(cloud)
plt.axis('off')
plt.show()
