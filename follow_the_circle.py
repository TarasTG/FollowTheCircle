import png #external module from project PyPng
import bz2
import urllib.request as URL

urladress = 'http://alcove.io/challenge.x.png'

###################################################################################
#1.get pixels from file
###################################################################################
with URL.urlopen(urladress) as circlefile:
#with open('test.png','rb') as circlefile:
    pixels = list(png.Reader(file = circlefile).read()[2])
###################################################################################



###################################################################################
#2.get height and width of image
###################################################################################
width = len(pixels[0])#width of image
height = len(pixels)#height of image
###################################################################################


###################################################################################
#3.calculate result
###################################################################################
result = bytes()#result of circles bytes
for rowindex in range(len(pixels)):#loop for image rows with circle pixels     
    
    row = pixels[rowindex]

    if not sum(row):#skip row with only black pixels
        continue

    #Get bytes from left and right part of crescents for row
    bytesfromleft = row[0:width//2].tobytes().strip(b'\x00')[1::3]
    bytesfromright = row[width//2:width].tobytes().strip(b'\x00')[1::3]
            
    #join result of left + right parts of crescents
    if rowindex <= (height // 2):#for top part of circle
        result = bytesfromleft + result + bytesfromright            
    elif rowindex > (height // 2):#for lower part of circle        
        result = bytesfromleft[::-1] + result + bytesfromright[::-1]

###################################################################################

###################################################################################
#4.print result
###################################################################################

#print simple text
print('Simple text: {}'.format(result[result.find(b'Congra'):result.find(b'BZh91AY',result.find(b'Congra'))]))

#print coded BZ2 phrase
b_bz2 = result[result.find(b'BZh91AY'):result.find(b'BZh91AY')+160]
print('{}\nBZ compressed: {}'.format('-'*40,b_bz2))

#print decoded phrase
print('{}\nBZ uncompressed: {}'.format('-'*40,bz2.decompress(b_bz2)))
###################################################################################