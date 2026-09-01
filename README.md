
# Histogram Equalization Using OpenCV (Grayscale & Color Images)

---

## Aim

To write a Python program using OpenCV to perform histogram equalization on both grayscale and color images to enhance image contrast and brightness.

The program performs the following operations:

- Read and display a grayscale image.
- Plot histogram of the grayscale image.
- Apply histogram equalization on the grayscale image.
- Read and display a color image.
- Convert the image to HSV color space.
- Apply histogram equalization on the Value (V) channel.
- Convert the enhanced image back to BGR format.
- Display original and enhanced images along with their histograms.

---

## Software Used

- Anaconda – Python 3.7
- Jupyter Notebook
- OpenCV (`cv2`)
- NumPy
- Matplotlib

---

## Algorithm

### Step 1:
Import the required libraries: OpenCV, NumPy, and Matplotlib.

### Step 2:
Read the input image in grayscale mode.

### Step 3:
Display the grayscale image.

### Step 4:
Plot the histogram of the grayscale image.

### Step 5:
Apply histogram equalization using `cv2.equalizeHist()`.

### Step 6:
Display the equalized histogram and enhanced grayscale image.

### Step 7:
Read the same image in color mode.

### Step 8:
Convert the image from BGR to HSV color space.

### Step 9:
Apply histogram equalization to the V (Value) channel.

### Step 10:
Convert the enhanced HSV image back to BGR format.

### Step 11:
Display the original color image, equalized image, and their histograms.

---

# Program

### Developed By:
**Name:** SUPRIYA PRABHU

### Register No:
**212224240165**

---

## 1. Import the required libraries and read the grayscale image.

```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('parrot.jpg', cv2.IMREAD_GRAYSCALE)

plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.show()
```

---

## 2. Plot the histogram of the grayscale image.

```python
plt.hist(img.ravel(), 256, range=[0,256])
plt.title('Original Image Histogram')
plt.show()
```

---

## 3. Apply histogram equalization.

```python
img_eq = cv2.equalizeHist(img)
```

---

## 4. Display the histogram of the equalized image.

```python
plt.hist(img_eq.ravel(), 256, range=[0,256])
plt.title('Equalized Histogram')
plt.show()
```

---

## 5. Display the equalized grayscale image.

```python
plt.imshow(img_eq, cmap='gray')
plt.title('Equalized Image')
plt.show()
```

---

## 6. Read the image in color mode and convert to HSV.

```python
img = cv2.imread('parrot.jpg', cv2.IMREAD_COLOR)

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
```

---

## 7. Apply histogram equalization to the V channel.

```python
img_hsv[:, :, 2] = cv2.equalizeHist(img_hsv[:, :, 2])
```

---

## 8. Convert the enhanced HSV image back to BGR.

```python
img_eq = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
```

---

## 9. Display the original and equalized color images.

```python
plt.subplot(121)
plt.imshow(img[:, :, ::-1])
plt.title('Original Color Image')

plt.subplot(122)
plt.imshow(img_eq[:, :, ::-1])
plt.title('Equalized Image')

plt.show()
```

---

## 10. Display the original and equalized images along with their histograms.

```python
plt.figure(figsize=[12,10])

plt.subplot(221)
plt.imshow(img[:, :, ::-1])
plt.title('Original Color Image')

plt.subplot(222)
plt.imshow(img_eq[:, :, ::-1])
plt.title('Equalized Image')

plt.subplot(223)
plt.hist(img.ravel(), 256, range=[0,256])
plt.title('Original Histogram')

plt.subplot(224)
plt.hist(img_eq.ravel(), 256, range=[0,256])
plt.title('Histogram Equalized')

plt.show()
```

---

## Output

### Grayscale Histogram Equalization

- Original grayscale image is displayed.
- <img width="704" height="468" alt="image" src="https://github.com/user-attachments/assets/b72bac36-0004-49b2-b659-2b5e55c19a87" />

- Histogram of the original grayscale image is plotted.
- <img width="731" height="548" alt="image" src="https://github.com/user-attachments/assets/46bc8853-283d-49cb-9f75-26aad0b6334a" />

- Equalized grayscale image is displayed.
- <img width="788" height="528" alt="image" src="https://github.com/user-attachments/assets/a05cf959-7265-4a91-9de9-25baf778b0ba" />

- Histogram of the equalized image shows improved contrast.
- 
<img width="727" height="498" alt="image" src="https://github.com/user-attachments/assets/7954119b-91cf-4391-9f2b-843e3cd3ffdb" />

### Color Image Histogram Equalization

<img width="1230" height="443" alt="image" src="https://github.com/user-attachments/assets/7968a380-ff96-4bc5-a521-401d62491f7c" />

<img width="1253" height="530" alt="image" src="https://github.com/user-attachments/assets/7f1c147d-7cfe-4f1a-813a-783fc2fe143e" />


## Result

Thus, histogram equalization was successfully performed on both grayscale and color images using OpenCV. The contrast of the images was enhanced, improving the overall visual quality.
