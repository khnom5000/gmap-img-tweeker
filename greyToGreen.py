from PIL import Image
import numpy as np

green = [187,226,198]
blue = [156,192,249]

# Open image
im = Image.open('3.png').convert('RGB')

# Make into Numpy array
imnp = np.array(im)

# Make all Light Grey pixels Green 
imnp[(imnp[:,:,0]==232) & (imnp[:,:,1]==234) & (imnp[:,:,2]==237)] = green

# Make all Dark Green pixels Green 
imnp[(imnp[:,:,0]==168) & (imnp[:,:,1]==218) & (imnp[:,:,2]==181)] = green

# Make all Dark Blue pixels Blue
imnp[(imnp[:,:,0]==102) & (imnp[:,:,1]==157) & (imnp[:,:,2]==246)] = blue

# Make all Light Yellow pixels Green - this is the same values as inside the roads :(
#imnp[(imnp[:,:,0]==254) & (imnp[:,:,1]==239) & (imnp[:,:,2]==195)] = green

# Convert back to PIL and save
Image.fromarray(imnp).save('3e.png')
