import cv2

kamera = cv2.VideoCapture(0)

while (True):
    #Rectangle start point
    Rct_start_point = (100, 50)
    #Rectangle end point
    Rct_end_point = (550,400)


    #center rectangle's x and y value
    center_main_X=450
    center_main_y=125

    #target rectangle's x and y value
    target_x=325
    target_y=235

    #target coordinate information
    x1=400
    y1=100
    x2=500
    y2=150

    #target start point
    target_start_point=(x1, y1)
    #target end point
    target_end_point=(x2,y2)

   
    #calculate target center
    target_center=(int((x1+x2)/2),int((y1+y2)/2))

    #detection rectangle center coordinate
    main_center=(325,235)

    #read camera
    ret, videoGoruntu = kamera.read()

    #create target rectangle 
    target=cv2.rectangle(videoGoruntu,target_start_point,target_end_point,(0,255,0),5)
    #create target rectangle center
    aRtc_center=cv2.circle(videoGoruntu,target_center,10,(0,0,255),-1) 
    
    #create detection rectangle
    cv2.rectangle(videoGoruntu,Rct_start_point,Rct_end_point,(0,255,0),5)
    #create detection rertangle center
    Rtc_center_=cv2.circle(videoGoruntu,main_center,10,(0,0,255),-1) 
 
    #draw the distance between detection rectangle and target rectangle  
    cv2.line(videoGoruntu,target_center,main_center,(0,0,255),3)

    cv2.imshow("video", videoGoruntu)
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break


#the distance formul is ((target_x-center_main_x)^2+(target_y-center_main_y)^2)**1/2
distance_x=(center_main_X-target_x)^2

distance_y=(target_y-center_main_y)^2
#calculate distance
distance =int(distance_x)+int(distance_y)**1/2
print(int(distance))

kamera.release()
cv2.destroyAllWindows()








