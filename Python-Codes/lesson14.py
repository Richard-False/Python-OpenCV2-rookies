import cv2

# 创建VideoCapture对象
cap = cv2.VideoCapture(0)

# 加载Haar特征分类器
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# 公众号《计算机视觉之光》回复【xml】获取上述'haarcascade_frontalface_default.xml'文件
while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
