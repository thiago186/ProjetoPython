    import tkinter as tk
    import cv2
    from PIL import Image, ImageTk

    class App:
        def __init__(self):
            self.window = tk.Tk()
            self.window.title('Tela de Autenticação do programa')
            self.cap = cv2.VideoCapture(0) #código para ler a webcam
            self.canvas = tk.Canvas(self.window, width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH), height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            self.canvas.pack()
            self.delay = 15
            self.update()
            self.window.mainloop()

        def update(self):
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                self.photo = ImageTk.PhotoImage(image = Image.fromarray(frame))
                self.canvas.create_image(0, 0, image = self.photo, anchor = tk.NW)

            self.window.after(self.delay, self.update)

    App()