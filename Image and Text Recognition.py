import cv2
import pytesseract

# Path of image
image = cv2.imread("sample.jpg")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Extract text
text = pytesseract.image_to_string(gray)

print("Recognized Text:")
print(text)

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()