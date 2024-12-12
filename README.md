Directory Structure Explanation





data/newimage_cropped/

Contains two subdirectories:

approved: Stores approved images.

declined: Stores declined images.

Files:

newimage.csv: Metadata file containing information about all images.

newimage_undersampled.csv: Metadata file created by performing undersampling on the approved and declined images, ensuring balanced ratios for expiry and general images to prevent overfitting.

11th_train_practice.ipynb

The most recent Python code file used for training.

Augmentation.ipynb

A Python notebook that was previously used for data augmentation.

Includes techniques such as:

Grayscale conversion.

Noise addition.

Rotation.

Flip-flop transformations.

Enhances the dataset by creating varied image representations.

cropimage.py

A Python script designed to remove unnecessary gray masking at the bottom of images in bulk.

EDA_new.ipynb & EDA.ipynb

These files are used for exploratory data analysis.

They also include functionality to create the newimage_undersampled.csv file by performing undersampling.

EDA.ipynb: Legacy code but retained for its ability to visualize the decline_reason column using matplotlib.

make_new_directory_structure.ipynb

A script to reorganize images originally grouped by job_no into a new structure categorized by image_status (approved or declined).

Restructuring was done for convenience, especially for the latest batch of images not organized under job_no folders.

SmokeAlarm_OCR.ipynb

The most recent task for processing images to extract text using OCR.

Details:

Utilizes a pre-trained model, as the images feature only English printed text (no handwritten characters).

Mitigates out-of-memory errors by batching and saving intermediate results.

Designed to resume from a specific index if interrupted.

Results are saved as .txt files on Google Drive.
