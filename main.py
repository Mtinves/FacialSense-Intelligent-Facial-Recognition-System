import tkinter as tk
import cv2
from PIL import Image, ImageTk
import numpy as np
import face_recognition
import os

import req

path = 'datasets'
images = []
classNames = []
myList = os.listdir(path)
# print(myList)

class App:
    def __init__(self):
        self.mw = tk.Tk()
        self.mw.title("FACE RECOGNITION")
        self.mw.geometry("720x540")

        self.login_button = req.get_button(self.mw, "LOGIN", "green", self.login)
        self.login_button.place(x=300, y=450)

        self.register_new_user_button = req.get_button(self.mw, 'REGISTER NEW USER', 'gray', self.register_new_user, fg='black')
        self.register_new_user_button.place(x=500, y=450)

        self.webcam_label = req.get_img_label(self.mw)
        self.webcam_label.place(x=50, y=50, width=620, height=360)
        self.add_webcam(self.webcam_label)

    def add_webcam(self, label):
        if 'cap' not in self.__dict__:
            self.cap = cv2.VideoCapture(0)
            # address="http://192.168.1.9:8080/video"
            # self.cap.open(address)
        self._label = label
        self.process_webcam()
    
    def process_webcam(self):
        ret, frame = self.cap.read()
        self.most_recent_capture_arr = frame
        img_ = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)
        self.most_recent_capture_pil = Image.fromarray(img_)
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        self._label.imgtk = imgtk
        self._label.configure(image=imgtk)
        self._label.after(20, self.process_webcam)

    def login(self):
        self.mw.destroy()

        self.mw = tk.Tk()
        self.mw.title("LOGIN PAGE")
        self.mw.geometry("720x540")

        self.webcam_label = req.get_img_label(self.mw)
        self.webcam_label.place(x=50, y=50, width=620, height=360)
        self.add_webcam(self.webcam_label)

        self.check_button = req.get_button(self.mw, 'CHECK', 'gray', self.check, fg='black')
        self.check_button.place(x=500, y=450)

    def register_new_user(self):
        self.mw.destroy()

        self.mw = tk.Tk()
        self.mw.title("REGISTRATION PAGE")
        self.mw.geometry("720x540")

        self.capture_label = req.get_img_label(self.mw)
        self.capture_label.place(x=50, y=50, width=620, height=360)
        self.add_img_to_label(self.capture_label)

        self.reg_name_button = req.get_button(self.mw, 'REGISTER', 'green', self.user_register, fg='black')
        self.reg_name_button.place(x=50, y=450)

        self.name_text_label=req.get_text_label(self.mw,'ENTER USER NAME:')
        self.name_text_label.place(x=300, y=430)

        self.enter_name_new_user=req.get_entry_text(self.mw)
        self.enter_name_new_user.place(x=300, y=453)

        self.name_text_label=req.get_text_label(self.mw,'ENTER USER ID:')
        self.name_text_label.place(x=500, y=430)

        self.enter_id_new_user=req.get_entry_text(self.mw)
        self.enter_id_new_user.place(x=500, y=453)

    def add_img_to_label(self, label):
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        label.imgtk = imgtk
        label.configure(image=imgtk)
        self.register_new_user_capture=self.most_recent_capture_arr.copy()

    def user_register(self):
        name=self.enter_name_new_user.get(1.0, "end-1c")
        id=self.enter_id_new_user.get(1.0, "end-1c")
        cv2.imwrite('datasets/'+str(name)+"-"+str(id)+".jpg", self.register_new_user_capture)
        req.msg_box('Registration Successful', 'User Data Saved as \n{}'.format(name))
        self.mw.geometry("720x640")

        self.delete_user_button = req.get_button(self.mw, "DELETE YOUR DATA", "red", self.delete_user)
        self.delete_user_button.place(x=50, y=510)

        self.LogOut_button = req.get_button(self.mw, 'LOG OUT', 'gray', self.LogOut, fg='black')
        self.LogOut_button.place(x=50, y=550)
        
        self.login_button = req.get_button(self.mw, "LOG IN", "green", self.login)
        self.login_button.place(x=300, y=510)

    def check(self):
        for cl in myList:
            curImg = cv2.imread(f'{path}/{cl}')
            images.append(curImg)
            classNames.append(os.path.splitext(cl)[0])

        def findEncodings(images):
            encodeList = []
            for img in images:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                encode = face_recognition.face_encodings(img)[0]
                encodeList.append(encode)
            return encodeList
        encodeListKnown = findEncodings(images)
        unknown_image = self.most_recent_capture_arr
        unknown_image = cv2.cvtColor(unknown_image, cv2.COLOR_BGR2RGB)
        if len(face_recognition.face_encodings(unknown_image)) == 0:
            req.msg_box('Login Failed', 'No Face Detected')
            return
        
        unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
        matches = face_recognition.compare_faces(encodeListKnown, unknown_face_encoding)
        faceDis = face_recognition. face_distance(encodeListKnown,unknown_face_encoding)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            if True in matches:
                req.msg_box('Login Successful', 'This User Data Exists as {}'.format(name))

                self.delete_user_button = req.get_button(self.mw, "DELETE YOUR DATA", "red", self.delete_user)
                self.delete_user_button.place(x=300, y=450)

                self.LogOut_button = req.get_button(self.mw, 'LOG OUT', 'gray', self.LogOut, fg='black')
                self.LogOut_button.place(x=500, y=450)
            else:
                req.msg_box('Login Failed!', 'Register as a New User')

    def delete_user(name):
        data_path = 'datasets'
        files = os.listdir(data_path)
        for file in files:
            file_path = os.path.join(data_path, file)
            os.remove(file_path)
        req.msg_box('Deletion Success', 'Data for User ID deleted successfully.'.format(name))

    def LogOut(self):
        self.mw.destroy()

    def start(self):
        self.mw.mainloop()

if __name__ == "__main__":
    app=App()
    app.start()