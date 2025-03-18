import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break


    cv2.imshow('frame', frame)

    # 按'q'键退出循环
    if cv2.waitKey(1) == ord('q'):
        break

# 完成所有操作后，释放捕获器

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 将帧写入输出文件
    out.write(frame)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
    # 释放资源
cap.release()
out.release()
cv2.destroyAllWindows()