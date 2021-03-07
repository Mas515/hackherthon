from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class CameraExample(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        # Create a camera object
        self.cameraObject            = Camera(play=False)
        self.cameraObject.play       = True
        self.cameraObject.resolution = (1000, 1000) # Specify the resolution
        # Create a button for taking photograph
        self.camaraClick = Button(text="Take Photo")
        self.camaraClick.size_hint=(.5, .2)
        self.camaraClick.pos_hint={'x': .25, 'y':.75}
        # bind the button's on_press to onCameraClick
        self.camaraClick.bind(on_press=self.onCameraClick)
        # add camera and button to the layout
        layout.add_widget(self.cameraObject)
        layout.add_widget(self.camaraClick)
        # return the root widget
        return layout
    # Take the current frame of the video as the photo graph
    def onCameraClick(self, *args):
        self.cameraObject.export_to_png('/Users/marine/hackherthon/bread-eating-jeddi/selfie.png')
        App.get_running_app().stop()

# Start the Camera App
if __name__ == '__main__':
     CameraExample().run()



     #Display the image 
from kivy.uix.image import Image

class MainApp(App):

# #This works to just display the image
     def build(self):
         img = Image(source='/Users/marine/hackherthon/bread-eating-jeddi/selfie.png',
                      size_hint=(2, 1),
                      pos_hint={'center_x':.5, 'center_y':.5})

         return img
if __name__ == '__main__':
     app = MainApp()
     app.run()

