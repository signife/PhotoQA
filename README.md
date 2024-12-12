# Photo-QA Project

This repository contains scripts, notebooks, and data for image classification and text extraction tasks, specifically related to fire alarm images.

---

## Directory Structure

### `data/newimage_cropped/`
- **Subdirectories:**
  - `approved/`: Stores approved images.
  - `declined/`: Stores declined images.
- **Files:**
  - `newimage.csv`: Metadata file containing information about all images.
  - `newimage_undersampled.csv`: Metadata file created by performing undersampling on approved and declined images, ensuring balanced ratios for expiry and general images to prevent overfitting.

---

## Notebooks and Scripts

### 1. `11th_train_practice.ipynb`
- The most recent Python notebook used for training the classification model.

---

### 2. `Augmentation.ipynb`
- A Python notebook previously used for data augmentation.
- Includes the following techniques:
  - Grayscale conversion.
  - Noise addition.
  - Rotation.
  - Flip-flop transformations.
- Enhances the dataset by creating varied image representations.

---

### 3. `cropimage.py`
- A Python script designed to bulk-remove unnecessary gray masking at the bottom of images.

---

### 4. `EDA_new.ipynb` & `EDA.ipynb`
- **Exploratory Data Analysis (EDA):**
  - `EDA_new.ipynb`: Focuses on data visualization and performing undersampling to create `newimage_undersampled.csv`.
  - `EDA.ipynb`: Legacy code used for visualizing the `decline_reason` column with `matplotlib`.

---

### 5. `make_new_directory_structure.ipynb`
- A script to reorganize images originally grouped by `job_no` into a new structure categorized by `image_status` (approved or declined).
- Useful for organizing the latest batch of images not already grouped under `job_no`.

---

### 6. `SmokeAlarm_OCR.ipynb`
- The most recent task for processing images to extract text using OCR.
- **Details:**
  - Utilizes a pre-trained OCR model, as the images feature only printed English text (no handwritten characters).
  - Mitigates out-of-memory errors by batching and saving intermediate results.
  - Designed to resume processing from a specific index if interrupted.
  - Results are saved as `.txt` files on Google Drive.

---

## How to Use

1. **Data Preparation:**
   - Ensure that the `data/newimage_cropped/` directory is populated with the `approved` and `declined` subdirectories and relevant metadata files (`newimage.csv` and `newimage_undersampled.csv`).

2. **Running Scripts:**
   - Use `11th_train_practice.ipynb` to train the classification model.
   - Use `Augmentation.ipynb` to perform data augmentation if additional variability in images is required.
   - Use `cropimage.py` to preprocess images by removing gray masks.
   - Use `EDA_new.ipynb` for exploratory data analysis and to create a balanced dataset.

3. **OCR Text Extraction:**
   - Run `SmokeAlarm_OCR.ipynb` for extracting printed text from images. Ensure you have sufficient memory or use batching to avoid crashes.

4. **Reorganizing Files:**
   - Use `make_new_directory_structure.ipynb` to restructure image files for convenience.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Contact
For any issues or questions, please create an issue in this repository or contact the maintainer directly.
