# 🖼️ CartoonifyMe

Turn your photos into **fun, cartoon-style images** using **Python** and **OpenCV**! 🎨✨  

CartoonifyMe applies advanced image processing techniques to transform your ordinary photos into artistic cartoons — perfect for fun, social media, or creative projects.  

---

## 🚀 Features
- 🎯 **Simple GUI** to select images using a file dialog  
- 🖌️ Converts images into cartoon style with **smooth colors and sharp edges**  
- 👀 Displays all transformation steps:
  1. Original Image  
  2. Grayscale  
  3. Smoothed Grayscale  
  4. Edge Detection  
  5. Filtered Color  
  6. Final Cartoon  
- 📸 Works with standard image formats: `.jpg`, `.png`, `.jpeg`  

---

## 🧰 Technologies Used
- **Python 3.x**  
- **OpenCV** – Image processing  
- **Matplotlib** – Display images  
- **EasyGUI** – File chooser dialog  

---

## ⚡ How to Run
1. **Clone the repository**
```bash
git clone https://github.com/YOUR-USERNAME/CartoonifyMe.git
````

2. **Navigate to the project folder**

```bash
cd CartoonifyMe
```

3. **Install dependencies**

```bash
pip install opencv-python easygui matplotlib
```

4. **Run the script**

```bash
python cartoonify.py
```

5. **Select an image** from the file dialog and watch the cartoon magic happen! ✨



## 💡 How It Works

1. **Grayscale Conversion** – simplifies colors for easier edge detection
2. **Median Blur** – smooths the grayscale image to reduce noise
3. **Edge Detection** – uses adaptive thresholding to highlight edges
4. **Bilateral Filter** – smooths colors while keeping edges sharp
5. **Bitwise AND** – combines color and edges to produce the final cartoon

---

## 👨‍💻 Author

**SHAIK JAHEER AHMED**
Made with ❤️ using Python and OpenCV.


