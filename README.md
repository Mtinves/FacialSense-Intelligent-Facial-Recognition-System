# FacialSense-Intelligent-Facial-Recognition-System
FacialSense is an advanced facial recognition system that leverages intelligent algorithms to accurately identify individuals. With real-time image capture, facial feature extraction, and secure authentication, it provides seamless user verification for enhanced security and streamlined access control.

# Abstract
The Face Recognition project is an application that leverages computer vision and machine learning techniques to perform facial recognition tasks. The project provides functionality for user registration, login using facial recognition, and user data management. It utilizes popular libraries such as OpenCV, tkinter, Pillow (PIL), NumPy, and face_recognition to implement the core functionalities. 

The application allows users to register new users by capturing their facial images and associating them with unique names and IDs. These registered user data are stored in a designated folder. For login, the application uses the webcam to capture the user's face in real-time and compares it with the registered user data. If a match is found, the user is successfully logged in; otherwise, a login failure message is displayed. 

The project demonstrates the usage of fundamental computer vision techniques like image capturing, image processing, and facial feature extraction. It also showcases the power of machine learning algorithms in face recognition by utilizing the face_recognition library for face encoding and matching. The graphical user interface (GUI) is implemented using tkinter to provide a user-friendly interaction experience.

The documentation provides detailed instructions on the installation, usage, dependencies, and directory structure of the project. It also highlights the limitations of the current implementation and suggests potential future enhancements such as multi-face recognition and additional features for user management.

This Face Recognition project serves as a practical demonstration of facial recognition technology and provides a foundation for further exploration and development in the field of computer vision and biometric authentication systems.

# Dependencies
The following dependencies are required to run the application:
- Python 3.x
- OpenCV
- tkinter
- Pillow (PIL)
- NumPy
- face_recognition

# Installation

Install the required dependencies using pip:
   ```
   pip install opencv-python
   pip install opencv-contrib-python
   pip install tkinter
   pip install Pillow
   pip install numpy
   pip install face_recognition
   ```

# Underlying Technologies:

OpenCV: OpenCV (Open Source Computer Vision Library) is a popular computer vision library that provides tools and functions for image and video processing. It is used in this project for tasks such as capturing images from the webcam, color space conversions, and image manipulation.

tkinter: tkinter is a Python library for creating graphical user interfaces (GUIs). It is used in the project to build the user interface, allowing users to interact with the application easily.

Pillow (PIL): Pillow, also known as PIL (Python Imaging Library), is a library for image processing tasks. It provides functionalities such as image format conversions, resizing, and manipulation. In the project, Pillow is used to convert images captured by OpenCV to a format compatible with tkinter.

NumPy: NumPy is a powerful library for numerical computing in Python. It is widely used for array manipulation and processing. In the project, NumPy is utilized for efficient handling and processing of image data.

face_recognition: The face_recognition library is a Python wrapper for the dlib library, which is a popular library for machine learning and computer vision tasks. face_recognition provides facial recognition functionalities, including face detection, facial feature extraction, face encoding, and face matching. It plays a vital role in the project's implementation of facial recognition.

# Files and Directory Structure
- `main.py`: Main script to run the application.
- `req.py`: Contains helper functions for GUI elements and messagebox handling.
- `datasets/`: Directory to store registered user data images.

# Features:
1.	User Registration: The application allows users to register new users by capturing their facial images and associating them with unique names and IDs. The registered user data is stored in a designated folder.
2.	Facial Recognition Login: Users can log in using facial recognition. The application captures real-time images from the webcam and compares them with the registered user data. If a match is found, the user is successfully logged in.
3.	User Data Management: The project provides functionality for managing user data, including adding new users, deleting user data, and updating user information.

# Implementation Details:
The Face Recognition project is structured using object-oriented programming principles. It consists of multiple classes, each responsible for specific functionalities. Here are the key components of the implementation:

*App class: The App class serves as the main application class and handles the GUI, user interactions, and high-level application flow. It utilizes the tkinter library to create the application window, buttons, labels, and entry fields. It also interacts with other classes to perform tasks such as image capturing, facial recognition, and user data management.*

*Image capturing: The project utilizes the OpenCV library to capture real-time images from the webcam. The captured images are then processed and converted to a suitable format for display in the GUI.*

*User Registration: When registering a new user, the application captures their facial image using the webcam. The captured image is then saved in a designated folder along with associated user information such as name and ID.*

*Facial Recognition: During the login process, the application captures real-time images from the webcam and compares them with the registered user data. The face_recognition library is used to extract facial features, encode faces, and perform face matching. If a match is found, the user is successfully logged in.*

*User Data Management: The project provides functionality for managing user data, including adding new users, deleting user data, and updating user information. User data is stored in a designated folder, and the application interacts with the file system to perform these operations.*


# Usage
1. Run the `main.py` script to launch the application.
2. The application window will open with two options: "LOGIN" and "REGISTER NEW USER".
3. Click on the "LOGIN" button to proceed with facial recognition login.
4. The webcam feed will be displayed, and the application will attempt to recognize the user's face.
5. If a match is found in the registered user database, a successful login message will be displayed.
6. If no match is found, a login failure message will be displayed.
7. To register a new user, click on the "REGISTER NEW USER" button.
8. The webcam feed will be displayed, and the user can capture their image.
9. Enter the user's name and ID in the provided text fields.
10. Click the "REGISTER" button to save the user's data.
11. A confirmation message will be displayed, and the user's image will be saved in the `datasets` folder.
12. To delete user data, click on the "DELETE YOUR DATA" button.
13. A confirmation message will be displayed, and all user data will be deleted from the `datasets` folder.
14. To log out of the application, click on the "LOG OUT" button.


# Limitations
- The facial recognition accuracy may vary depending on lighting conditions, pose, and other factors.
- The application currently supports single-face recognition. Multiple faces in the webcam feed may result in inaccurate results.
- The application relies on the `datasets` folder to store user data images. Ensure the folder is present and accessible.

# Future Enhancements
- Implement multi-face recognition to handle multiple faces in the webcam feed.
- Improve the accuracy of facial recognition by using more advanced techniques and algorithms.
- Add additional features such as password protection, user management, and user-specific functionality.

The Face Recognition application provides a basic implementation of facial recognition for user login and registration. It demonstrates the use of computer vision and machine learning techniques to perform facial recognition tasks. By following the provided documentation, users can run the application, register new users, and perform facial recognition login.
