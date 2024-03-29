import cv2
import os
import matplotlib
def find_faces(image_path):
    image =cv2.imread(image_path)
    color_img =image.copy()
    filename= os.path.basename(image_path)
    gray_img =cv2.cvtColor(color_img,cv2.COLOR_BGR2GRAY)
    haar_classifier =cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    smile_cascade =cv2.CascadeClassifier('haarcascade_smile.xml')
    faces=haar_classifier.detectMultiScale(gray_img,scaleFactor=1.1,minNeighbors=5)
    print('Number of faces found: {faces}'.format(faces=len(faces)))
    for(x,y,width,height) in faces:
        cv2.rectangle(color_img,(x,y),(x+width,y+height),(0,255,0),2)
        roi_gray =gray_img[y:y+height,x:x+width]
        roi_color =color_img[y:y+height,x:x+width]
        smile =smile_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in smile:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv2.imshow(filename,color_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__=='__main__':
    find_faces('smile.jpg')
