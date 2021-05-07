# decodeqrcode
decoding qrcode using opencv with python

## setup
Here opencv version 4.2.0 is used for image process

We will be using following packages:
- python-qrcode - standard installation includes pillow for generating images
- glob          - used to retrieve files

[use this link](https://betterprogramming.pub/how-to-generate-and-decode-qr-codes-in-python-a933bce56fd0)

When you press the space key then the screenshot will be taken from the video stream  automatically and image will be saved in your local directory and 
also when you want to exit the video stream you can press the esc key.

```python
  cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")

    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)

        k = cv2.waitKey(1)
        if k == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k == 32:
            # SPACE pressed
            img_name = "opencv_frame_{}.jpg".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
            ```
