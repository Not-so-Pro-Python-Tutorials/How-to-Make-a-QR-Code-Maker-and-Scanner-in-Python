import qrcode
import cv2

text = input("Enter text/url: ")

img = qrcode.make(text)
img.save("text.jpg")

detector = cv2.QRCodeDetector()
decoded, _, _ = detector.detectAndDecode(cv2.imread("text.jpg"))

print("Decoded text:", decoded)
