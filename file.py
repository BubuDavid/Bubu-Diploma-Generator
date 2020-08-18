import os
# Definition of things
size = 450
x = (diploma.size[0])/2
y = 1170
font_path = os.environ.get("font_path") + "FredokaOne-Regular.ttf"


for name in data_names["names"][0:6]:
    # Definition of things
    numLetters = len(name)
    
    # Resizing
    new_size = size * 0.975**numLetters
    new_size = int(new_size)
    
    # Positioning
    pos_x = x - numLetters*new_size/2
    pos_y = y
        

    
    # Diploma writing.
    diploma01 = diploma.copy()
    draw = ImageDraw.Draw(diploma01)
    font = ImageFont.truetype(font_path, new_size)
    draw.text((pos_x,pos_y), name, (255, 206, 76), font=font)
    diploma01.save(f"./Diplomas/{name}.jpg")
#   diploma01.show()
#    plt.imshow(diploma01)