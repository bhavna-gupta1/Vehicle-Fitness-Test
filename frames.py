import tkinter as tk
from PIL import Image, ImageTk
import requests
from threading import Thread
import time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style
from handlers import Image1
from config import settings
from handlers import api_model, mqtt_handler
from Find_Directory_Path import resource_path


m_base_url = settings.m_base_url

class VFTApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1000x1000')
        self.root.title('VFT')
        self.root['bg'] = '#0E0E0E'

        # Create a single frame
        self.frame = tk.Frame(root, bg="#0E0E0E")
        self.frame.pack(expand=True,fill='both')

        # Display the background image
        # self.show_image('Images/crbg2.png', 1400, 750, 0, 0, "black")
        Image1.image_handler(self.frame, 'Images/crbg2.png', 2200, 1030, -100, 0)

        # Set up the initial content (vft head, welcome heading, etc.)
        self.setup_initial_content()

    def setup_initial_content(self):
        Image1.image_handler(self.frame, resource_path('Images/vftgft.png'), 1210, 180, 60, 60)
        Image1.image_handler(self.frame, resource_path('Images/WVT.png'), 630, 130, 100, 350)

        notrgstr = tk.Label(self.frame, text='New user ?', bg="#0E0E0E", fg='white', font=('Helvetica', 20))
        notrgstr.place(x=120, y=530)

        fgtpsd = tk.Label(self.frame, text='Setup', bg="#0E0E0E", fg='yellow', font=('Helvetica', 20))
        fgtpsd.place(x=270, y=530)
        fgtpsd.bind("<Button-1>", self.on_setup_click)

        loginbtn = Image.open(resource_path('Images/login.png'))
        width, height = 270, 65
        loginbtn_resize = loginbtn.resize((width, height))
        self.loginbtn_head = ImageTk.PhotoImage(loginbtn_resize)

        button = tk.Button(self.frame, image=self.loginbtn_head, bg="#0E0E0E", command=self.switch_to_signin,
                           borderwidth=0, relief='flat', activebackground="#0E0E0E", activeforeground='#0E0E0E')
        button.place(x=630, y=700)

    def on_setup_click(self, event):
        print('SETUP')

    def switch_to_signin(self):
        # Destroy the current frame
        self.frame.destroy()

        # Create and display the SignInApp frame
        signin_frame = SignInApp(self.root)

class SignInApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1000x1000')
        self.root.title('VFT')
        self.root['bg'] = '#0E0E0E'

        # Create a frame
        self.frame = tk.Frame(root,bg="#0E0E0E")
        self.frame.pack(expand=True,fill='both')

        # Load and display the background image
        Image1.image_handler(self.frame, 'Images/crbg2.png', 4000, 2000, -1000, -500)

        # Set up the initial content (VFT heading, Let's go fitness, etc.)
        self.setup_initial_content()

    def setup_initial_content(self):
        Image1.image_handler(self.frame, 'Images/Vehicle Fitness Test.png',1120, 100, 60, 70)
        Image1.image_handler(self.frame, 'Images/getftgo.png',700, 50, 10, 200)
        Image1.image_handler(self.frame, 'Images/signin.png', 240, 100, 80, 260)
        Image1.image_handler(self.frame, 'Images/userid.png',450, 80, 80, 400)
        Image1.image_handler(self.frame, 'Images/psswrd.png', 450, 80, 80, 500)
        Image1.image_handler(self.frame, 'Images/signbtn.png', 265, 60, 190, 620, self.on_SIGNIN_click)

        # Create Entry fields
        self.entryFieldid = tk.Entry(self.frame, width=20, font=('Helvetica', 20), fg='black', bg='#E5E5E5')
        self.entryFieldid.place(x=105, y=430)

        self.entryField = tk.Entry(self.frame, width=20, font=('Helvetica', 20), fg='black', bg='#E5E5E5', show='*')
        self.entryField.place(x=105, y=530)

        # Create labels for 'Not Registered?' and 'Forgot Password?'
        notrgstr = tk.Label(self.frame, text='Not Registered ?', bg="#0E0E0E", fg='white', font=('Helvetica', 18))
        notrgstr.place(x=90, y=800)
        notrgstr.bind("<Button-1>", self.on_text_click1)

        fgtpsd = tk.Label(self.frame, text='Forgot Password ?', bg="#0E0E0E", fg='yellow', font=('Helvetica', 18))
        fgtpsd.place(x=280, y=800)
        fgtpsd.bind("<Button-1>", self.on_text_click2)

    def on_SIGNIN_click(self):
        # Get username and password from entry fields
        username = 'amzad'
        apassword = 'abc123'
        center = "CTI1"

        # Make an API request with the provided username and password
        api_url = f'{m_base_url}/user/loginpc/{username}/{apassword}/{center}'  # Replace with your actual API endpoint
        payload = {'username': username, 'password': apassword, 'center': 'CTI1'}
        print(username,"user")
        print(api_url,"url")
        try:
            response = requests.get(api_url, data=payload)

            if response.status_code == 200:
                print('Signed in successfully!')
                
        # Destroy the current frame
                self.frame.destroy()

        # Create and display the SignInApp frame
                ScanApp(self.root)

                # You can handle further actions here, e.g., navigate to a new frame
            else:
                print(f'Error: {response.status_code,response.text}')
        except requests.RequestException as e:
            print(f'Error: {e}')

    def on_text_click1(self, event):
        print('Not registered')

    def on_text_click2(self, event):
        print('Forgot password')


class ScanApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1000x1000')
        self.root.title('VFT')
        self.root['bg'] = '#0E0E0E'

        # Create a frame
        self.frame = tk.Frame(root,bg="#0E0E0E" )
        self.frame.pack(expand=True,fill='both')

        # Load and display the background image
        Image1.image_handler(self.frame, 'Images/crbg2.png', 4000, 2000, -1000, -500)

        # Set up the initial content (VFT heading, Let's go fitness, etc.)
        self.setup_scan_content()

    def setup_scan_content(self):
        

        # VFT heading for scanning page
        Image1.image_handler(self.frame, 'Images/Vehicle Fitness Test.png', 1120, 100, 60, 70)
        Image1.image_handler(self.frame, 'Images/getftgo.png',700, 50, 10, 200)
        Image1.image_handler(self.frame, 'Images/waiting.png', 700, 70, 60, 350)
        Image1.image_handler(self.frame, 'Images/dot.png', 90, 20, 360, 420 )
        Image1.image_handler(self.frame, 'Images/scan.png', 240, 50, 70, 590 , self.on_scan_click)
        Image1.image_handler(self.frame, 'Images/userid.png', 470, 80,60, 740 )
        Image1.image_handler(self.frame, 'Images/search.png',  240, 50,550,770 , self.on_search_click)
         # Start scanning text
        self.scaningtext_scan = tk.Label(self.frame, text='Start Scanning Vehicle Number Plate', bg='#0E0E0E', fg='white', font=('Helvetica', 18))
        self.scaningtext_scan.place(x=60, y=530)
       #  enter manually 
        scaningtext = tk.Label(self.frame,text='or Enter Manually',bg='#0E0E0E',fg='white',font=('Helvetica',18))
        scaningtext.place(x=60,y=675)
       # vehicleidid entry field
        self.entryField = tk.Entry(self.frame, width=25, font=('Helvetica',18), fg='black', bg='#E5E5E5')
        self.entryField.place(x=85, y=770)

    def on_scan_click(self):
        print('Scanning...')  # Add your scanning logic here

    def on_search_click(self):
        # vehicalnumber=  str(self.entryField.get())
        vehicalnumber='HR NC 12 2918'
        vehicaltype = '4'
        id = 'A1'

        testcenter = "CTI1"
        name="Rahul"
        fueltype = "Diesel"
        date= "Sat, 18 Nov 2023 15:30:45 GMT"
        appointmentscol= "no"


      # Make an API request with the provided username and password
        api_url = f'{m_base_url}/authorize/vehicle/{vehicalnumber}'  # Replace with your actual API endpoint
        payload = {'vehicalnumber':vehicalnumber}
         
        
        try:
            response = requests.get(api_url,data=payload)
            print(response.text,"api")
            if response.status_code == 200:
                print('Searched successfully!') 
                datas = response.json()
                print(datas)
                 # Destroy the current frame
                self.frame.destroy()

        # Create and display the SignInApp frame
                vehicleDetail(self.root,datas)
            else:
                print(f'Error: Not Found')
                # print(f'Error: {response.status_code,response.text}')
                self.scaningtext_scan.config(text="Appointment Not Found", fg="red", font=('',20))

        except requests.RequestException as e:
            print(f'Error: {e}')

class vehicleDetail:
    def __init__(self, root,datas):
        self.root = root
        self.root.geometry('1000x1000')
        self.root.title('VFT')
        self.root['bg'] = '#0E0E0E'
        
     # Create a frame
        self.frame = tk.Frame(root,bg="#0E0E0E" )
        self.frame.pack(expand=True,fill='both')
    # Load and display the background image
        Image1.image_handler(self.frame, 'Images/crbg2.png', 3900, 1900, -1000, -580)
        

        #Extract data
        self.name = datas['payload']['name']
        self.regnNo = datas['payload']['vehicalnumber']
        self.regdUpto = datas['payload']['date']
        self.RC = datas['payload']['rcstatus']
        self.fuel = datas['payload']['fueltype']
        self.chassis = datas['payload']['chassis']
        self.engNo = datas['payload']['enginenumber']
        self.mfg = datas['payload']['mfgdate']
        self.wt = datas['payload']['wt']
        self.vtype = datas['payload']['vehicaltype']
        self.mfr = datas['payload']['mfr']
        self.model = datas['payload']['model']
        self.id = datas['payload']['id'] 
        self.center = datas['payload']['testcenter']
        print(self.center)
    # Set up the initial content (VFT heading, Let's go fitness, etc.)
        self.setup_scan_content(datas)

    def setup_scan_content(self,datas):
       # VFT heading for scanning page
   
        Image1.image_handler(self.frame, 'Images/Vehicle RC .png', 1120, 100, 60, 70)
        Image1.image_handler(self.frame, 'Images/getftgo.png', 700, 50, 10, 200)
        Image1.image_handler(self.frame, 'Images/Vehicledetail.png', 700, 70, 60, 310)
        Image1.image_handler(self.frame, 'Images/whitebord.png', 800, 520, 20, 450 )
        self.show_image1(resource_path('Images/redline.png'), 550,20,50,640)
        Image1.image_handler(self.frame, 'Images/strttesting.png',240, 50,1300,850, command=lambda:self.on_strttesting_click(datas=datas))
        
       
       # Text on white board
        # 1st line
        maintext = tk.Label(self.frame,text='Following are the details:',bg='#E5E5E5',fg='black',font=('Helvetica',18))
        maintext.place(x=50,y=480)

        # 2nd line
        text1 = tk.Label(self.frame,text='Owner name:',bg='#E5E5E5',fg='#D70226',font=('Helvetica',16,'italic'))
        text1.place(x=50,y=520)
        self.text1_input = tk.Label(self.frame,text=self.name,bg='#E5E5E5',fg='black',font=('Helvetica',16,'italic','bold'))
        self.text1_input.place(x=200,y=520)
        # # 3rd line
        text2 = tk.Label(self.frame,text='Regn. No:',bg='#E5E5E5',fg='#D70226',font=('Helvetica',16,'italic'))
        text2.place(x=50,y=550)
        self.text2_input = tk.Label(self.frame,text=self.regnNo,bg='#E5E5E5',fg='black',font=('Helvetica',16,'italic','bold'))
        self.text2_input.place(x=200,y=550)
        # # 4th line
        text3 = tk.Label(self.frame,text='Regd. upto:',bg='#E5E5E5',fg='#D70226',font=('Helvetica',16,'italic'))
        text3.place(x=50,y=580)
        self.text3_input = tk.Label(self.frame,text=self.regdUpto,bg='#E5E5E5',fg='black',font=('Helvetica',16,'italic','bold'))
        self.text3_input.place(x=200,y=580)
        # # 5th line
        text4 = tk.Label(self.frame,text='RC status:',bg='#E5E5E5',fg='#D70226',font=('Helvetica',16,'italic'))
        text4.place(x=50,y=610)
        self.text4_input = tk.Label(self.frame,text=self.RC,bg='#E5E5E5',fg='black',font=('Helvetica',16,'italic','bold'))
        self.text4_input.place(x=200,y=610)
       

        # # 6th line
        text5 = tk.Label(self.frame,text='Fuel Type:',bg='#E5E5E5',fg='#D70226',font=('Helvetica',16,'italic'))
        text5.place(x=50,y=670)
        self.text5_input = tk.Label(self.frame,text=self.fuel,bg='#E5E5E5',fg='black',font=('Helvetica',16,'italic','bold'))
        self.text5_input.place(x=200,y=670)
        # # 7th line
        text6 = tk.Label(self.frame,text='Chassis No:',bg='#E5E5E5',fg='#D70226',font=('Helvetica',16,'italic'))
        text6.place(x=50,y=700)
        self.text6_input = tk.Label(self.frame,text=self.chassis,bg='#E5E5E5',fg='black',font=('Helvetica',16,'italic','bold'))
        self.text6_input.place(x=200,y=700)
        # #  # 8th line
        text7 = tk.Label(self.frame,text='Engine No.:',bg='#E5E5E5',fg='#D70226',font=('Helvetica',16,'italic'))
        text7.place(x=50,y=730)
        self.text7_input = tk.Label(self.frame,text=self.engNo,bg='#E5E5E5',fg='black',font=('Helvetica',16,'italic','bold'))
        self.text7_input.place(x=200,y=730)
        # # # 9th line
        text8 = tk.Label(self.frame,text='MFG. DT. No.:',bg='#E5E5E5',fg='#D70226',font=('Helvetica',16,'italic'))
        text8.place(x=50,y=760)
        self.text8_input = tk.Label(self.frame,text=self.mfg,bg='#E5E5E5',fg='black',font=('Helvetica',16,'italic','bold'))
        self.text8_input.place(x=200,y=760)
        # # 10th line
        text9 = tk.Label(self.frame,text='Unladen WT:',bg='#E5E5E5',fg='#D70226',font=('Helvetica',16,'italic'))
        text9.place(x=50,y=790)
        self.text9_input = tk.Label(self.frame,text=self.wt,bg='#E5E5E5',fg='black',font=('Helvetica',16,'italic','bold'))
        self.text9_input.place(x=200,y=790)
        # # # 11th line
        text10 = tk.Label(self.frame,text='Vehicle Type:',bg='#E5E5E5',fg='#D70226',font=('Helvetica',16,'italic'))
        text10.place(x=50,y=820)
        self.text10_input = tk.Label(self.frame,text=self.vtype,bg='#E5E5E5',fg='black',font=('Helvetica',16,'italic','bold'))
        self.text10_input.place(x=200,y=820)
        # # # 12th line
        text11 = tk.Label(self.frame,text='MFR:',bg='#E5E5E5',fg='#D70226',font=('Helvetica',16,'italic'))
        text11.place(x=50,y=850)
        self.text11_input = tk.Label(self.frame,text=self.mfr,bg='#E5E5E5',fg='black',font=('Helvetica',16,'italic','bold'))
        self.text11_input.place(x=200,y=850)
        # # # # 13th line
        text12 = tk.Label(self.frame,text='Model:',bg='#E5E5E5',fg='#D70226',font=('Helvetica',16,'italic'))
        text12.place(x=50,y=880)
        self.text12_input = tk.Label(self.frame,text=self.model,bg='#E5E5E5',fg='black',font=('Helvetica',16,'italic','bold'))
        self.text12_input.place(x=200,y=880) 

    def show_image1(self, image_path, width, height, x, y):
            img = Image.open(image_path)
            img = img.resize((width, height))
            img_tk = ImageTk.PhotoImage(img)

            img_label = tk.Label(self.frame, image=img_tk, bg='#E5E5E5')
            img_label.image = img_tk
            img_label.place(x=x, y=y)

            
    def on_strttesting_click(self, datas):
        
        api_url = f'{m_base_url}/test/check/{self.id}/{self.center}'  # Replace with your actual API endpoint
        # payload = {}
         
        
        try:
            response = requests.post(api_url) #,data=payload)
            print(response.text,"api")
            if response.status_code == 200:
                print('Searched successfully!') 
                # datas = response.json()
                # print(datas)
                 # Destroy the current frame
                self.frame.destroy()

        # Create and display the SignInApp frame
                start_testing(self.root, datas)
            else:
                print(f'Error: Not Found')
                # self.manual_label =tk.Label(self.frame,text="Manual Test is Running...",bg='#E5E5E5',fg='red',font=('Helvetica',14,'bold','italic'))
                # self.manual_label.place(x=300,y=275)
                # print(f'Error: {response.status_code,response.text}')
                # self.scaningtext_scan.config(text="Appointment Not Found", fg="red", font=('',14))
                self.frame.destroy()
                start_testing(self.root, datas)

        except requests.RequestException as e:
            print(f'Error: {e}')

class start_testing:
    def __init__(self, root, datas):
        self.root = root
        self.root.geometry('1000x1000')
        self.root.title('VFT')
        self.root['bg'] = '#0E0E0E'
        
     # Create a frame
        self.frame = tk.Frame(root,bg="#0E0E0E"  )
        self.frame.pack(expand=True,fill='both')
    # Load and display the background image
        # Image1.image_handler(self.frame, 'Images/blackbg.png', 1400, 750, 0, 0) 
        # EXTRACT DATA
        self.id = datas['payload']['id'] 
        self.center = datas['payload']['testcenter']

     # Set up the initial content (VFT heading, Let's go fitness, etc.)
        self.setup_test_content(datas=datas)

        self.start_thread()
    def Go_next(self,datas):
        self.frame.destroy()
        print("ssssssssssssssssssssssssnext click")
        start_testing2(self.root, datas)


    def setup_test_content(self, datas):
       # VFT heading for scanning page
   
        Image1.image_handler(self.frame, 'Images/Vehicle Fitness Test.png', 980, 50, 40, 50)
        Image1.image_handler(self.frame, 'Images/getftgo.png', 600, 30, 50, 130)
        Image1.image_handler(self.frame, 'Images/logocompleting.png', 700, 80, 60, 180)
        Image1.image_handler(self.frame, 'Images/whiteline.png', 27, 698, 850, 265)
        # Image1.image_handler(self.frame, 'Images/strttesting.png', 240, 50, 1600, 920, command=lambda:self.stop_thread())
        Image1.image_handler(self.frame, 'Images/next.png', 240, 50, 1600, 920,command=lambda:(self.stop_thread(), self.Go_next(datas)))
        
        labels=['Headlamp Assembly','Top Light','Stop light','Parking light','Fog Lamp','Warning light','Number Plate','Marker Lamp','Direction Indicator','Hazard Warning Signal']
        # Create labels dynamically
        label_y_position = 304
        for label_text in labels:
            label = tk.Label(self.frame, text=label_text, font=('Helvetica', 14, 'bold'), fg='#FFF846', bg='#0E0E0E')
            label.place(x=140, y=label_y_position)
            label_y_position += 70
       
    #      # Print 'wheel.png' images 10 times at different y positions
        for i in range(10):
            y_position = 300 + i * 70# Adjust the spacing as needed
            Image1.image_handler(self.frame, 'Images/wheel.png', 40, 40, 70, y_position)
        
    #     # Print 'DETAILS.png' button 10 times at different y positions
        # for i in range(13):
        #     y_position = 290 + i * 60  # Adjust the spacing as needed
        #     Image1.image_handler(self.frame,'Images/DETAILS.png', 130, 30, 390, y_position, command=lambda:self.on_detail_click(x=500, y=y_position, datas=datas))
    # # SECOND PART
        for j in range(9):
            y_position = 300 + j * 70  # Adjust the spacing as needed
            Image1.image_handler(self.frame, 'Images/wheel.png', 40, 40,950, y_position)
        # for j in range(4):
        #     y_position =270 + j * 70  # Adjust the spacing as needed
        #     self.show_image('DETAILS.png', 130, 30, 1130, y_position, command=lambda:self.on_detail_click(x=1130, y=y_position, datas=datas))
        #  Create labels2 dynamically
        labels2=['Supressure Cap','Rear View Mirror','Safety Glass','Horn','Exhaust','Wiper Blades','Wiper System','Dashboard','Silencer']
        label_y_position = 304
        for label_text in labels2:
            label = tk.Label(self.frame, text=label_text, font=('Helvetica', 12, 'bold'), fg='#FFF846', bg='#0E0E0E')
            label.place(x=1020, y=label_y_position)
            label_y_position += 70  
    
    
    # #  detail function
    def m_param_detail(self, datas, m_test_name, id, topHeading):
        topHeading = topHeading
        try:
            self.stop_thread()
            self.frame.destroy()
            Detail_page(self.root, datas=datas, topHeading=topHeading, m_test_name = m_test_name, id = id)
        except requests.RequestException as e:
            print(f'Error: {e}')
    

        
    

    def automatic_fetching(self, id, center):
        
        api_url = f'{m_base_url}/test/checkdata/{id}/{center}'  # Replace with your actual API endpoint
        # payload = {}
        # print('datas',datas)
        
        try:
            response = requests.post(api_url) #,data=payload)
            print(response.text,"api")
            if response.status_code == 200:
                print('Searched successfully!') 
                datas = response.json()
                #Manualy insert the data in response back datas
                datas['payload']['testcenter'] = center
                print(datas)
                print(datas['payload']['testheadlamp'])
               
    #         # TEST CASE 1:
                if datas['payload']['testheadlamp'] == 'pass':
                    Image1.image_handler(self.frame,'Images/blnkbox.png',  35, 35, 510, 300, image_path_02='Images/right.png')
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 590, 298,command=lambda:self.m_param_detail(datas=datas, m_test_name='headlamp', id=self.id, topHeading='Headlamp Assembly'))
                elif datas['payload']['testheadlamp'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png',  165, 45, 590, 300,command=lambda:self.m_param_detail(datas=datas, m_test_name='headlamp', id=self.id, topHeading='Headlamp Assembly'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 298, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png',  35, 35, 510, 298)
    #         # TEST CASE 2:
                if datas['payload']['testtoplight'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 590, 370,command=lambda:self.m_param_detail(datas=datas, m_test_name='toplight', id=self.id, topHeading='Top Light'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 368, image_path_02='Images/right.png')
                elif datas['payload']['testtoplight'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 590, 370,command=lambda:self.m_param_detail(datas=datas, m_test_name='toplight', id=self.id, topHeading='Top Light'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 368, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 300, 368)
    # # #          # TEST CASE 3:
                if datas['payload']['teststoplight'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 590, 440,command=lambda:self.m_param_detail(datas=datas, m_test_name='stoplight', id=self.id, topHeading=' Stop Light'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 438, image_path_02='Images/right.png')
                elif datas['payload']['teststoplight'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 590, 440,command=lambda:self.m_param_detail(datas=datas, m_test_name='stoplight', id=self.id, topHeading='Stop Light'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 438, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 438)
    # #          # TEST CASE 4:
                if datas['payload']['testparkinglight'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 590, 510,command=lambda:self.m_param_detail(datas=datas, m_test_name='parkinglight', id=self.id, topHeading='Parking Light'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 508, image_path_02='Images/right.png')
                elif datas['payload']['testparkinglight'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 590, 510,command=lambda:self.m_param_detail(datas=datas, m_test_name='parkinglight', id=self.id, topHeading='Parking Light '))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 508, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 508)
    #         # TEST CASE 5:
                if datas['payload']['testfoglight'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 590, 580,command=lambda:self.m_param_detail(datas=datas, m_test_name='foglight', id=self.id, topHeading='Fog Lamp '))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 578, image_path_02='Images/right.png')
                elif datas['payload']['testfoglight'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 590, 580,command=lambda:self.m_param_detail(datas=datas, m_test_name='foglight', id=self.id, topHeading='Fog Lamp'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 578, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 578)
            # # TEST CASE 6:
                if datas['payload']['testwarninglight'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 590, 650,command=lambda:self.m_param_detail(datas=datas, m_test_name='warninglight', id=self.id, topHeading=' Warning Light'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 648, image_path_02='Images/right.png')
                elif datas['payload']['testwarninglight'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 590, 650,command=lambda:self.m_param_detail(datas=datas, m_test_name='warninglight', id=self.id, topHeading=' Warning Light'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 648, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 648)
            # # TEST CASE 7:
                if datas['payload']['testnumberplatelight'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 590, 720,command=lambda:self.m_param_detail(datas=datas, m_test_name='numberplatelight', id=self.id, topHeading=' Number Plate'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 718, image_path_02='Images/right.png')
                elif datas['payload']['testnumberplatelight'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 590, 720,command=lambda:self.m_param_detail(datas=datas, m_test_name='numberplatelight', id=self.id, topHeading=' Number Plate'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 718, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 718)
            #  # TEST CASE 8:
                if datas['payload']['testoutlinemarkerlight'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 590, 790,command=lambda:self.m_param_detail(datas=datas, m_test_name='outlinemarkerlight', id=self.id, topHeading='Marker Light '))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 788, image_path_02='Images/right.png')
                elif datas['payload']['testoutlinemarkerlight'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 590, 790,command=lambda:self.m_param_detail(datas=datas, m_test_name='outlinemarkerlight', id=self.id, topHeading='Marker Light '))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 788, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 788)   
             # TEST CASE 9:
                if datas['payload']['testdirectionlight'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 590, 860,command=lambda:self.m_param_detail(datas=datas, m_test_name='directionlight', id=self.id, topHeading=' Direction Light'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 858, image_path_02='Images/right.png')
                elif datas['payload']['testdirectionlight'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 590, 860,command=lambda:self.m_param_detail(datas=datas, m_test_name='directionlight', id=self.id, topHeading=' Direction Light'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 858, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 858)

                    # TEST CASE 10:
                if datas['payload']['testhazardlight'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 590, 930,command=lambda:self.m_param_detail(datas=datas, m_test_name='hazardlight', id=self.id, topHeading=' Hazard Light'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 928, image_path_02='Images/right.png')
                elif datas['payload']['testhazardlight'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 590, 930,command=lambda:self.m_param_detail(datas=datas, m_test_name='hazardlight', id=self.id, topHeading=' Hazard Light'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 928, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 928)

            # SECOND PART DETAIL BTN

                # TEST CASE 1:
                if datas['payload']['testsupressor'] == 'pass':
                    Image1.image_handler(self.frame,'Images/blnkbox.png',  35, 35, 1390, 300, image_path_02='Images/right.png')
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 1470, 298,command=lambda:self.m_param_detail(datas=datas, m_test_name='supressor', id=self.id, topHeading='Supressor'))
                elif datas['payload']['testsupressor'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png',  165, 45, 1470, 300,command=lambda:self.m_param_detail(datas=datas, m_test_name='supressor', id=self.id, topHeading='Supressor'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 298, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png',  35, 35, 1390, 298)

                # TEST CASE 2:
                if datas['payload']['testrearmirror'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 1470, 368,command=lambda:self.m_param_detail(datas=datas, m_test_name='rearmirror', id=self.id, topHeading='Rear View Mirror'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 368, image_path_02='Images/right.png')
                elif datas['payload']['testrearmirror'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 1470, 368,command=lambda:self.m_param_detail(datas=datas, m_test_name='rearmirror', id=self.id, topHeading='Rear View Mirror'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 368, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 368)
    # # #          # TEST CASE 3:
                if datas['payload']['testsafetyglass'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 1470,438,command=lambda:self.m_param_detail(datas=datas, m_test_name='safetyglasses', id=self.id, topHeading='Safety  Glass'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 438, image_path_02='Images/right.png')
                elif datas['payload']['testsafteyglass'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 1470,438,command=lambda:self.m_param_detail(datas=datas, m_test_name='safetyglasses', id=self.id, topHeading='Safety Glass'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 438, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 438)
    # #          # TEST CASE 4:
                if datas['payload']['testhorn'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 1470, 508,command=lambda:self.m_param_detail(datas=datas, m_test_name='horn', id=self.id, topHeading='Horn '))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 508, image_path_02='Images/right.png')
                elif datas['payload']['testhorn'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 1470, 508,command=lambda:self.m_param_detail(datas=datas, m_test_name='horn', id=self.id, topHeading='Horn '))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 508, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 508)
    #         # TEST CASE 5:
                if datas['payload']['testexhaust'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 1470, 578,command=lambda:self.m_param_detail(datas=datas, m_test_name='exhaust', id=self.id, topHeading='Exhaust '))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 578, image_path_02='Images/right.png')
                elif datas['payload']['testexhaust'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 1470, 578,command=lambda:self.m_param_detail(datas=datas, m_test_name='exhaust', id=self.id, topHeading='Exhaust '))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 578, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 578)
            # # TEST CASE 6:
                if datas['payload']['testwiperblade'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 1470, 648,command=lambda:self.m_param_detail(datas=datas, m_test_name='wiperblade', id=self.id, topHeading=' Wiper Blade'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 648, image_path_02='Images/right.png')
                elif datas['payload']['testwiperblade'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 1470, 648,command=lambda:self.m_param_detail(datas=datas, m_test_name='wiperblade', id=self.id, topHeading=' Wiper Blade'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 648, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 648)
            # # TEST CASE 7:
                if datas['payload']['testwipersystem'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 1470, 718,command=lambda:self.m_param_detail(datas=datas, m_test_name='wipersystem', id=self.id, topHeading=' Wiper System'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 718, image_path_02='Images/right.png')
                elif datas['payload']['testwipersystem'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 1470, 718,command=lambda:self.m_param_detail(datas=datas, m_test_name='wipersystem', id=self.id, topHeading=' Wiper System'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 718, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 718)
            #  # TEST CASE 8:
                if datas['payload']['testdashboard'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 1470, 788,command=lambda:self.m_param_detail(datas=datas, m_test_name='dashboard', id=self.id, topHeading='Dashboard '))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 788, image_path_02='Images/right.png')
                elif datas['payload']['testdashboard'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 1470, 788,command=lambda:self.m_param_detail(datas=datas, m_test_name='dashboard', id=self.id, topHeading='Dashboard '))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 788, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 788)   
                # TEST CASE 9:
                if datas['payload']['testsilencer'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 1470, 858,command=lambda:self.m_param_detail(datas=datas, m_test_name='silencer', id=self.id, topHeading=' Silencer'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 858, image_path_02='Images/right.png')
                elif datas['payload']['testsilencer'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 1470, 858,command=lambda:self.m_param_detail(datas=datas, m_test_name='silencer', id=self.id, topHeading=' Silencer'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 858, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 858)

            

                
    #            
    #             # How next button after completed manual test
                if datas['payload']['stage'] != 2:
                    # Manual Test Not completed label
                    m_test_not_completed = tk.Label(self.frame, text="Manual test is Ongoing",bg='#0E0E0E',font=('arial',24,'bold'),fg="yellow")
                    m_test_not_completed.place(x=1300, y=200)
                
                  # Destroy the current frame
        #         self.frame.destroy()
        # # Create and display the SignInApp frame
        #         start_testing(self.root)
            else:
                print(f'Error: Not Found')
                # print(f'Error: {response.status_code,response.text}')
                # self.scaningtext_scan.config(text="Appointment Not Found", fg="red", font=('',14))

        except requests.RequestException as e:
            print(f'Error: {e}')
    
    def start_thread(self):
        self.is_running = True  # Set the flag to start the thread
        self.thread = Thread(target=self.run_thread)
        self.thread.start()

    def stop_thread(self):
        self.is_running = False  # Set the flag to stop the thread

    def run_thread(self):
        while self.is_running:
            print("Thread is running...")
            self.thread = Thread(target=self.automatic_fetching(id=self.id, center=self.center))
            time.sleep(2)
        
        print("Thread is stopped.")
    
    def Go_To_Break_Test(self):
        self.frame.destroy()
        Break_Test(self.root, self.id, self.center)


# STARTING TESTING PAGE 2 (REST OF THE MANUAL TEST)
class start_testing2:
    def __init__(self, root, datas):
        self.root = root
        self.root.geometry('1000x1000')
        self.root.title('VFT')
        self.root['bg'] = '#0E0E0E'
        
     # Create a frame
        self.frame = tk.Frame(root,bg="#0E0E0E"  )
        self.frame.pack(expand=True,fill='both')
    # Load and display the background image
        # Image1.image_handler(self.frame, 'Images/blackbg.png', 1400, 750, 0, 0) 
        # EXTRACT DATA
        self.id = datas['payload']['id'] 
        self.center = datas['payload']['testcenter']

     # Set up the initial content (VFT heading, Let's go fitness, etc.)
        self.setup_test_content(datas=datas)

        self.start_thread()
    def Go_back(self,datas):
        self.frame.destroy()
        start_testing(self.root, datas)
        print('BACK')   

    def setup_test_content(self, datas):
       # VFT heading for scanning page
   
        Image1.image_handler(self.frame, 'Images/Vehicle Fitness Test.png', 980, 50, 40, 50)
        Image1.image_handler(self.frame, 'Images/getftgo.png', 600, 30, 50, 130)
        Image1.image_handler(self.frame, 'Images/logocompleting.png', 700, 80, 60, 180)
        Image1.image_handler(self.frame, 'Images/whiteline.png', 27, 698, 850, 265)
        # Image1.image_handler(self.frame, 'Images/strttesting.png', 240, 50, 1600, 920, command=lambda:self.stop_thread())
        Image1.image_handler(self.frame, 'Images/back.png', 240, 50, 1350, 920,command=lambda:(self.stop_thread(), self.Go_back(datas)))
        
        labels=['Service Brakes','Parking Brakes','Steering Gear','Joint Play','Speedometer','RUPD','LUPD','FASTag','Others','Wheel Chair']
         
        # Create labels dynamically
        label_y_position = 304
        for label_text in labels:
            label = tk.Label(self.frame, text=label_text, font=('Helvetica', 14, 'bold'), fg='#FFF846', bg='#0E0E0E')
            label.place(x=140, y=label_y_position)
            label_y_position += 70
       
    #      # Print 'wheel.png' images 10 times at different y positions
        for i in range(10):
            y_position = 300 + i * 70# Adjust the spacing as needed
            Image1.image_handler(self.frame, 'Images/wheel.png', 40, 40, 70, y_position)
        
    #     # Print 'DETAILS.png' button 10 times at different y positions
        # for i in range(13):
        #     y_position = 290 + i * 60  # Adjust the spacing as needed
        #     Image1.image_handler(self.frame,'Images/DETAILS.png', 130, 30, 390, y_position, command=lambda:self.on_detail_click(x=500, y=y_position, datas=datas))
    # # SECOND PART
        for j in range(9):
            y_position = 300 + j * 70  # Adjust the spacing as needed
            Image1.image_handler(self.frame, 'Images/wheel.png', 40, 40,950, y_position)
        # for j in range(4):
        #     y_position =270 + j * 70  # Adjust the spacing as needed
        #     self.show_image('DETAILS.png', 130, 30, 1130, y_position, command=lambda:self.on_detail_click(x=1130, y=y_position, datas=datas))
        #  Create labels2 dynamically
        labels2=['VLT','HSRP','Battery','Seat Belt','Speed Governor','Spray Suppression','Tyres','Reflective Tapes']
        label_y_position = 304
        for label_text in labels2:
            label = tk.Label(self.frame, text=label_text, font=('Helvetica', 12, 'bold'), fg='#FFF846', bg='#0E0E0E')
            label.place(x=1020, y=label_y_position)
            label_y_position += 70  
    
    
    # #  detail function
    def m_param_detail(self, datas, m_test_name, id, topHeading):
        topHeading = topHeading
        try:
            self.stop_thread()
            self.frame.destroy()
            Detail_page(self.root, datas=datas, topHeading=topHeading, m_test_name = m_test_name, id = id)
        except requests.RequestException as e:
            print(f'Error: {e}')
    

        
    

    def automatic_fetching(self, id, center):
        
        api_url = f'{m_base_url}/test/checkdata/{id}/{center}'  # Replace with your actual API endpoint
        # payload = {}
        # print('datas',datas)
        
        try:
            response = requests.post(api_url) #,data=payload)
            print(response.text,"api")
            if response.status_code == 200:
                print('Searched successfully!') 
                datas = response.json()
                #Manualy insert the data in response back datas
                datas['payload']['testcenter'] = center
                print(datas)
                print(datas['payload']['testheadlamp'])
               
    #         # TEST CASE 1:
                if datas['payload']['testbrakingmaual'] == 'pass':
                    Image1.image_handler(self.frame,'Images/blnkbox.png',  35, 35, 510, 300, image_path_02='Images/right.png')
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 590, 298,command=lambda:self.m_param_detail(datas=datas, m_test_name='beakingmanual', id=self.id, topHeading='Service Brake'))
                elif datas['payload']['testbrakingmanual'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png',  165, 45, 590, 300,command=lambda:self.m_param_detail(datas=datas, m_test_name='brakingmanual', id=self.id, topHeading='Service Brake'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 298, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png',  35, 35, 510, 298)
    #         # TEST CASE 2:
                if datas['payload']['testtestparkingbrakingmanual'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 590, 370,command=lambda:self.m_param_detail(datas=datas, m_test_name='parkingbrakingmanual', id=self.id, topHeading='Parking Brakes'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 368, image_path_02='Images/right.png')
                elif datas['payload']['testtestparkingbrakingmanual'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 590, 370,command=lambda:self.m_param_detail(datas=datas, m_test_name='parkingbrakingmanual', id=self.id, topHeading='Parking Brakes'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 368, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 300, 368)
    # # #          # TEST CASE 3:
                if datas['payload']['teststeering'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 590, 440,command=lambda:self.m_param_detail(datas=datas, m_test_name='steering', id=self.id, topHeading=' Steering Gear'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 438, image_path_02='Images/right.png')
                elif datas['payload']['teststeering'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 590, 440,command=lambda:self.m_param_detail(datas=datas, m_test_name='Steering', id=self.id, topHeading=' Steering Gear'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 438, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 438)
    # #          # TEST CASE 4:
                if datas['payload']['testjointplay'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 590, 510,command=lambda:self.m_param_detail(datas=datas, m_test_name='jointplay', id=self.id, topHeading='Joint Play'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 508, image_path_02='Images/right.png')
                elif datas['payload']['testjointplay'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 590, 510,command=lambda:self.m_param_detail(datas=datas, m_test_name='jointplay', id=self.id, topHeading='Joint Play'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 508, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 508)
    #         # TEST CASE 5:
                if datas['payload']['testspeedometermanual'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 590, 580,command=lambda:self.m_param_detail(datas=datas, m_test_name='speedometermanual', id=self.id, topHeading='Speedometer'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 578, image_path_02='Images/right.png')
                elif datas['payload']['testspeedometermanual'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 590, 580,command=lambda:self.m_param_detail(datas=datas, m_test_name='speedometermanual', id=self.id, topHeading='Speedometer'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 578, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 578)
            # # TEST CASE 6:
                if datas['payload']['testrupd'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 590, 650,command=lambda:self.m_param_detail(datas=datas, m_test_name='rupd', id=self.id, topHeading=' RUPD'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 648, image_path_02='Images/right.png')
                elif datas['payload']['testrupd'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 590, 650,command=lambda:self.m_param_detail(datas=datas, m_test_name='rupd', id=self.id, topHeading=' RUPD'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 648, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 648)
            # # TEST CASE 7:
                if datas['payload']['testlupd'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 590, 720,command=lambda:self.m_param_detail(datas=datas, m_test_name='lupd', id=self.id, topHeading=' LUPD'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 718, image_path_02='Images/right.png')
                elif datas['payload']['testlupd'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 590, 720,command=lambda:self.m_param_detail(datas=datas, m_test_name='lupd', id=self.id, topHeading=' LUPD'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 718, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 718)
            #  # TEST CASE 8:
                if datas['payload']['testfastag'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 590, 790,command=lambda:self.m_param_detail(datas=datas, m_test_name='fastag', id=self.id, topHeading='FASTag'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 788, image_path_02='Images/right.png')
                elif datas['payload']['testfastag'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 590, 790,command=lambda:self.m_param_detail(datas=datas, m_test_name='fastag', id=self.id, topHeading='FASTag'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 788, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 788)   
             # TEST CASE 9:
                if datas['payload']['testothers'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 590, 860,command=lambda:self.m_param_detail(datas=datas, m_test_name='others', id=self.id, topHeading='Others'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 858, image_path_02='Images/right.png')
                elif datas['payload']['testothers'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 590, 860,command=lambda:self.m_param_detail(datas=datas, m_test_name='others', id=self.id, topHeading=' Others'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 858, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 858)

                    # TEST CASE 9:
                if datas['payload']['testwheel'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 590, 930,command=lambda:self.m_param_detail(datas=datas, m_test_name='wheel', id=self.id, topHeading='Wheel Chair'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 928, image_path_02='Images/right.png')
                elif datas['payload']['testwheel'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 590, 930,command=lambda:self.m_param_detail(datas=datas, m_test_name='wheel', id=self.id, topHeading=' Wheel Chair'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 928, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 510, 928)

            # SECOND PART DETAIL BTN

                # TEST CASE 1:
                if datas['payload']['testvlt'] == 'pass':
                    Image1.image_handler(self.frame,'Images/blnkbox.png',  35, 35, 1390, 300, image_path_02='Images/right.png')
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 1470, 298,command=lambda:self.m_param_detail(datas=datas, m_test_name='vlt', id=self.id, topHeading='VLT'))
                elif datas['payload']['testvlt'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png',  165, 45, 1470, 300,command=lambda:self.m_param_detail(datas=datas, m_test_name='vlt', id=self.id, topHeading='VLT'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 298, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png',  35, 35, 1390, 298)

                # TEST CASE 2:
                if datas['payload']['testhsrp'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 1470, 368,command=lambda:self.m_param_detail(datas=datas, m_test_name='hsrp', id=self.id, topHeading='HSRP'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 368, image_path_02='Images/right.png')
                elif datas['payload']['testhsrp'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 1470, 368,command=lambda:self.m_param_detail(datas=datas, m_test_name='hsrp', id=self.id, topHeading='HSRP'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 368, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 300, 368)
    # # #          # TEST CASE 3:
                if datas['payload']['testbattery'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 1470,438,command=lambda:self.m_param_detail(datas=datas, m_test_name='battery', id=self.id, topHeading='Battery'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 438, image_path_02='Images/right.png')
                elif datas['payload']['testbattery'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 1470,438,command=lambda:self.m_param_detail(datas=datas, m_test_name='battery', id=self.id, topHeading='Battery'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 438, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 438)
    # #          # TEST CASE 4:
                if datas['payload']['testsafetybelt'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 1470, 508,command=lambda:self.m_param_detail(datas=datas, m_test_name='safetybelt', id=self.id, topHeading='Safety Belt'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 508, image_path_02='Images/right.png')
                elif datas['payload']['testsafetybelt'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 1470, 508,command=lambda:self.m_param_detail(datas=datas, m_test_name='safetybelt', id=self.id, topHeading='Safety Belt'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 508, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 508)
    #         # TEST CASE 5:
                if datas['payload']['testspeedgovermer'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 1470, 578,command=lambda:self.m_param_detail(datas=datas, m_test_name='speedgovermer', id=self.id, topHeading='Speed Governor'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 578, image_path_02='Images/right.png')
                elif datas['payload']['testspeedgovermer'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 1470, 578,command=lambda:self.m_param_detail(datas=datas, m_test_name='speedgovermer', id=self.id, topHeading='Speed Governor'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 578, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 578)
            # # TEST CASE 6:
                if datas['payload']['testspray'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 1470, 648,command=lambda:self.m_param_detail(datas=datas, m_test_name='spray', id=self.id, topHeading='Spray Supression'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 648, image_path_02='Images/right.png')
                elif datas['payload']['testspray'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 1470, 648,command=lambda:self.m_param_detail(datas=datas, m_test_name='spray', id=self.id, topHeading=' Spray Supression'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 648, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 648)
            # # TEST CASE 7:
                if datas['payload']['testtyres'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 1470, 718,command=lambda:self.m_param_detail(datas=datas, m_test_name='tyres', id=self.id, topHeading=' Tyres'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 718, image_path_02='Images/right.png')
                elif datas['payload']['testtyres'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 1470, 718,command=lambda:self.m_param_detail(datas=datas, m_test_name='tyres', id=self.id, topHeading=' Tyres'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 718, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 718)
            #  # TEST CASE 8:
                if datas['payload']['testretro'] == 'pass':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 1470, 788,command=lambda:self.m_param_detail(datas=datas, m_test_name='retro', id=self.id, topHeading='Reflective Tape'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 788, image_path_02='Images/right.png')
                elif datas['payload']['testretro'] == 'fail':
                    Image1.image_handler(self.frame, 'Images/DETAILS.png', 165, 45, 1470, 788,command=lambda:self.m_param_detail(datas=datas, m_test_name='retro', id=self.id, topHeading='Reflective Tape'))
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 788, image_path_02='Images/cross.png')
                else:
                    Image1.image_handler(self.frame,'Images/blnkbox.png', 35, 35, 1390, 788)   
                

            

                
    #             # How next button after completed manual test
                if datas['payload']['stage'] == 2:
                    Image1.image_handler(self.frame, 'Images/strttesting.png',240, 50, 1600, 920 ,command=lambda: [self.stop_thread(), self.Go_To_Break_Test()])
                else:
                    # Manual Test Not completed label
                    m_test_not_completed = tk.Label(self.frame, text="Manual test is Ongoing",bg='#0E0E0E',font=('arial',24,'bold'),fg="yellow")
                    m_test_not_completed.place(x=1400, y=100)
                
                  # Destroy the current frame
        #         self.frame.destroy()
        # # Create and display the SignInApp frame
        #         start_testing(self.root)
            else:
                print(f'Error: Not Found')
                # print(f'Error: {response.status_code,response.text}')
                # self.scaningtext_scan.config(text="Appointment Not Found", fg="red", font=('',14))

        except requests.RequestException as e:
            print(f'Error: {e}')
    
    def start_thread(self):
        self.is_running = True  # Set the flag to start the thread
        self.thread = Thread(target=self.run_thread)
        self.thread.start()

    def stop_thread(self):
        self.is_running = False  # Set the flag to stop the thread

    def run_thread(self):
        while self.is_running:
            print("Thread is running...")
            self.thread = Thread(target=self.automatic_fetching(id=self.id, center=self.center))
            time.sleep(2)
        
        print("Thread is stopped.")
    
    def Go_To_Break_Test(self):
        self.frame.destroy()
        Break_Test(self.root, self.id, self.center)

class Detail_page:
    def __init__(self, root, datas, topHeading, m_test_name, id):
        self.root = root
        self.root.geometry('1000x1000')
        self.root.title('VFT')
        self.root['bg'] = '#0E0E0E'
        
    # Create a frame
        self.frame = tk.Frame(root,bg='#0E0E0E')
        self.frame.pack(expand=True,fill='both')

        # print("Data is Here: ", hdlp_datas)

        # top Heading variable defined
        self.topHeading = topHeading

    # Load and display the background image        
        Image1.image_handler(self.frame, 'Images/blackbg.png', 1400, 750, 0, 0)
        # self.setup_test_content(datas=datas, hdlp_datas=hdlp_datas)
        self.setup_test_content(datas=datas, m_test_name = m_test_name, id = id)

    def setup_test_content(self, datas, m_test_name, id):
    #    # VFT heading for scanning page

        # Text Image for info
        Image1.image_handler(self.frame, 'Images/Vehicle Fitness Test.png', 980, 50, 40, 50)
        Image1.image_handler(self.frame, 'Images/getftgo.png', 600, 30, 50, 130)

        # Parameters image
        # self.show_image('Images/wheel.png', 40, 40, 50, 190)
        Image1.image_handler(self.frame, 'Images/wheel.png', 45, 45, 80, 230)
        
        Image1.image_handler(self.frame, 'Images/addtional.png', 400, 400, 970,300)
        # self.show_image('Images/back.png', 180, 42, 950,550, command=lambda:self.on_back_click(datas=datas))
        Image1.image_handler(self.frame, 'Images/back.png', 240, 50, 1400, 800, command=lambda:self.on_back_click(datas=datas))


        self.label1 = tk.Label(self.frame,text=self.topHeading,font=('Helvetica',24,'bold'),fg='#FFF846',bg='#0E0E0E')
        self.label1.place(x=130,y=230) 
        
        if m_test_name == 'headlamp':
            # Dict for parameters details
            headings=[('1.Bulb should be working', ('Helvetica', 18, 'bold'), 'white'),
            ('2.Head lamp operating switch working', ('Helvetica', 18, 'bold'), 'white'),
            ('3.No broken lens', ('Helvetica', 18, 'bold'), 'white'),
            ('4.Lens of the lamp should not be painted with colour', ('Helvetica', 18, 'bold'), 'white'),
            ('5.No moisture deposition on the inside surface of the lens', ('Helvetica', 18, 'bold'), 'white')
            ]
        
        elif m_test_name == 'toplight':
            # Dict for parameters details
            headings=[('1. Coloured lens shall not be faded', ('Helvetica', 18, 'bold'), 'white'),
            ('2.Lens should not be broken', ('Helvetica', 18, 'bold'), 'white'),
            ('3.Lamp shall be working', ('Helvetica', 18, 'bold'), 'white'),
            ('4.Rear: red, front: white for dual-lens lamps', ('Helvetica', 18, 'bold'), 'white'),
            ('5.No moisture deposition on the inside surface of the lens', ('Helvetica', 18, 'bold'), 'white'),
            ('6.Secured fitment of the lamps', ('Helvetica', 18, 'bold'), 'white'),
            ]
        
        elif m_test_name == 'supressor':
            # Dict for parameters details
            headings=[('1.Suppressor cap shall be in good condition', ('Helvetica', 18, 'bold'), 'white'),
            ('2.High Tension cable shall beproperly insulated', ('Helvetica', 18, 'bold'), 'white'),
            ('3.Are terminals connected on bothside ?', ('Helvetica', 18, 'bold'), 'white'),
            ]
        
        elif m_test_name == 'horn':
            # Dict for parameters details
            headings=[('1.Restrict harsh or alarming noise devices', ('Helvetica', 18, 'bold'), 'white'),
            ('2.Horn shall be securely fitted', ('Helvetica', 18, 'bold'), 'white'),
            ('3.Horn shall be functioning', ('Helvetica', 18, 'bold'), 'white'),
            ('4.Is horn sound compliant with IS:15796', ('Helvetica', 18, 'bold'), 'white')
            ]
        
        elif m_test_name == 'exhaust':
            # Dict for parameters details
            headings=[('1.Ensure no leakage', ('Helvetica', 18, 'bold'), 'white'),
            ('2.Secured fitment of silencer', ('Helvetica', 18, 'bold'), 'white'),
            ('3.Is silencer rust-free and functionally sound', ('Helvetica', 18, 'bold'), 'white'),
            ('4.Stationary noise test as per IS10399:1998', ('Helvetica', 18, 'bold'), 'white'),
            ]
        
        elif m_test_name == 'wiperblade':
            # Dict for parameters details
            headings=[('1.Ensure presence of wiper blades', ('Helvetica', 18, 'bold'), 'white'),
            ('2.Wiper blade shall be in good condition', ('Helvetica', 18, 'bold'), 'white'),
            ]
        
        elif m_test_name == 'wipersystem':
            # Dict for parameters details
            headings=[('1.Do wipers cover the entire windshield', ('Helvetica', 18, 'bold'), 'white'),
            ('2.Do each split windshield wipers operate securely', ('Helvetica', 18, 'bold'), 'white'),
            ]
        
        elif m_test_name == 'dashboard':
            # Dict for parameters details
            headings=[('1.Ensure secured mounting', ('Helvetica', 18, 'bold'), 'white'),
            ('2.Wiring shall be insulated', ('Helvetica', 18, 'bold'), 'white'),
            ('3. Dashboard illumination shall be functioning', ('Helvetica', 18, 'bold'), 'white'),
            ('4.Do warning lights turn off correctly', ('Helvetica', 18, 'bold'), 'white'),
            ]
        
        elif m_test_name == 'safetyglasses':
            # Dict for parameters details
            headings=[('1.Is the windscreen glass transparent, excluding stickers', ('Helvetica', 18, 'bold'), 'white'),
            ('2.Does windscreen have required safety markings', ('Helvetica', 18, 'bold'), 'white'),
            ('3.Is glass undamaged, free from films', ('Helvetica', 18, 'bold'), 'white'),
            ]
        elif m_test_name == 'stoplight':
            # Dict for parameters details
           headings=[('1.Coloured lens shall not be faded', ('Helvetica', 18, 'bold'), 'white'),
            ('2.Lens should not be broken', ('Helvetica', 18, 'bold'), 'white'),
            ('3.Lamp shall be working on actuation of the brake', ('Helvetica', 18, 'bold'), 'white'),
            ('4.No moisture deposition on the inside surface of the lens', ('Helvetica', 18, 'bold'), 'white'),
            ('5.Secured fitment of the lamps', ('Helvetica', 18, 'bold'), 'white')]
        elif m_test_name == 'parkinglight':
            # Dict for parameters details
            headings=[('1.Coloured lens shall not be faded', ('Helvetica', 18, 'bold'), 'white'),
            ('2.Lens should not be broken', ('Helvetica', 18, 'bold'), 'white'),
            ('3.Lamp shall be working', ('Helvetica', 18, 'bold'), 'white'),
            ('4.No moisture deposition on the inside surface of the lens', ('Helvetica', 18, 'bold'), 'white'),
            ('5.Secured fitment of the lamps', ('Helvetica', 18, 'bold'), 'white')
            ]   
        elif m_test_name == 'foglight':
            # Dict for parameters details
             headings=[('1. Coloured lens shall not be faded', ('Helvetica', 18, 'bold'), 'white'),
            ('2.Lens should not be broken', ('Helvetica', 18, 'bold'), 'white'),
            ('3.Lamp shall be working', ('Helvetica', 18, 'bold'), 'white'),
            ('4.No moisture deposition on the inside surface of the lens', ('Helvetica', 18, 'bold'), 'white'),
            ('5.Secured fitment of the lamps', ('Helvetica', 18, 'bold'), 'white')
            ]
        elif m_test_name == 'numberplatelight':
            # Dict for parameters details
            headings=[('1.White light shall be used for illuminating number plate', ('Helvetica', 18, 'bold'), 'white'),
            ('2.Lens should not be broken', ('Helvetica', 18, 'bold'), 'white'),
            ('3.Lamps shall be working', ('Helvetica', 18, 'bold'), 'white'),
             ('4.No moisture deposition on the inside surface of the lens', ('Helvetica', 18, 'bold'), 'white'),
             ('5.Secured fitment of the lamps', ('Helvetica', 18, 'bold'), 'white')
            ]
        elif m_test_name == 'outlinemarkerlight':
            # Dict for parameters details
            headings=[('1.Ensure secured fitment of end-outline marker lamps', ('Helvetica', 18, 'bold'), 'white'),
            ('2.Coloured lens shall not be faded', ('Helvetica', 18, 'bold'), 'white'),
            ('3.Lens should not be broken', ('Helvetica', 18, 'bold'), 'white'),
            ('4.No moisture deposition on the inside surface of the lens', ('Helvetica', 18, 'bold'), 'white'),
            ('5.Corrected Orientation:Red lens-rear,White-front', ('Helvetica', 18, 'bold'), 'white'),
            ]
        elif m_test_name == 'directionlight':
            # Dict for parameters details
            headings=[('1.Flashing light emitted shall be Amber in colour', ('Helvetica', 18, 'bold'), 'white'),
            ('2.Lens should not be broken', ('Helvetica', 18, 'bold'), 'white'),
            ('3.Lamps shall be working', ('Helvetica', 18, 'bold'), 'white'),
            ('4.No moisture deposition on the inside surface of the lens ', ('Helvetica', 18, 'bold'), 'white'),
            ('5.Secured fitment of the lamps', ('Helvetica', 18, 'bold'), 'white'),
            ]
        elif m_test_name == 'warninglight':
            # Dict for parameters details
            headings=[('1.Coloured lens shall not be faded', ('Helvetica', 18, 'bold'), 'white'),
            ('2.Lens should not be broken', ('Helvetica', 18, 'bold'), 'white'),
            ('3.Lamp shall be working', ('Helvetica', 18, 'bold'), 'white'),
             ('4.No moisture deposition on the inside surface of the lens', ('Helvetica', 18, 'bold'), 'white'),
             ('5.Secured fitment of the lamps', ('Helvetica', 18, 'bold'), 'white')
            ] 
       
        elif m_test_name == 'hazardlight':
            # Dict for parameters details
            headings=[('1.Flashing light emitted shall be Amber in colour', ('Helvetica', 18, 'bold'), 'white'),
            ('2.Does switch ensure synchronize indicator operation ? ', ('Helvetica', 18, 'bold'), 'white'),
             ]
        elif m_test_name == 'rearmirror':
            # Dict for parameters details
            headings=[('1.Is the windscreen glass transparent, excluding stickers', ('Helvetica', 18, 'bold'), 'white'),
            ('2.Does windscreen have required safety markings', ('Helvetica', 18, 'bold'), 'white'),
            ('3.Is glass undamaged, free from films', ('Helvetica', 18, 'bold'), 'white'),
            ] 
        elif m_test_name == 'silencer':
            # Dict for parameters details
            headings=[('1.Is the windscreen glass transparent, excluding stickers', ('Helvetica', 18, 'bold'), 'white'),
            ('2.Does windscreen have required safety markings', ('Helvetica', 18, 'bold'), 'white'),
            ('3.Is glass undamaged, free from films', ('Helvetica', 18, 'bold'), 'white'),
            ] 
        elif m_test_name == 'brakingmanual':
            # Dict for parameters details
            headings=[('1.Fittings shall be secured', ('Helvetica', 18, 'bold'), 'white'),
            ('2. Brake hoses shall not be damaged or cracked', ('Helvetica', 18, 'bold'), 'white'),
            ('3.No leakage of brake fluid', ('Helvetica', 18, 'bold'), 'white'),
            ] 
        elif m_test_name == 'parkingbrakingmanual':
            # Dict for parameters details
            headings=[('1.Fittings shall be secured', ('Helvetica', 18, 'bold'), 'white'),
            ('2. Brake hoses shall not be damaged or cracked', ('Helvetica', 18, 'bold'), 'white'),
            ('3.No leakage of brake fluid', ('Helvetica', 18, 'bold'), 'white'),
            ] 
        elif m_test_name == 'steering':
            # Dict for parameters details
            headings=[('1.Is steering backlash limited to 30 degrees?', ('Helvetica', 18, 'bold'), 'white'),
            
            ]
        elif m_test_name == 'jointplay':
            # Dict for parameters details
            headings=[('1.Are springs and shocks securely attached?', ('Helvetica', 18, 'bold'), 'white'),
            ('2.Springs shall not be damaged or fractured', ('Helvetica', 18, 'bold'), 'white'),
            ('3.) Shock absorber dampers shall not have any oil leakage', ('Helvetica', 18, 'bold'), 'white'),
             ('4.Is excessive wear prevented in swivel components?', ('Helvetica', 18, 'bold'), 'white'),
             ('5.In case of Air suspension,ensure no audible system leakage', ('Helvetica', 18, 'bold'), 'white')
            ] 
        elif m_test_name == 'speedometermanual':
            # Dict for parameters details
            headings=[('1.Securely fitted', ('Helvetica', 18, 'bold'), 'white'),
            ('2.Sufficiently illuminated', ('Helvetica', 18, 'bold'), 'white'),
            ('3.Dial cover shall not be broken', ('Helvetica', 18, 'bold'), 'white'),
             ('4.Indicator needle operational', ('Helvetica', 18, 'bold'), 'white'),
            ]
        elif m_test_name == 'rupd':
            # Dict for parameters details
            headings=[('1.Rear Underride Protection Device shall be fitted', ('Helvetica', 18, 'bold'), 'white'),
            ('2.Is the rear underride protection undamaged?', ('Helvetica', 18, 'bold'), 'white'),
            ('3.Are rear underride dimensions compliant with IS-14812-2005?', ('Helvetica', 18, 'bold'), 'white'),
             ] 
        elif m_test_name == 'lupd':
            # Dict for parameters details
            headings=[('1. Lateral under run protection device shall be fitted', ('Helvetica', 18, 'bold'), 'white'),
            ('2.Is lateral underrun protection free from damage?', ('Helvetica', 18, 'bold'), 'white'),
            ('3.Are lateral underrun dimensions compliant with IS-14682-2004?', ('Helvetica', 18, 'bold'), 'white'),
             ]
        elif m_test_name == 'fastag':
            # Dict for parameters details
            headings=[('1. To be affixed on the front windscreen', ('Helvetica', 18, 'bold'), 'white'),
            ('2.FASTag shall not be damaged.', ('Helvetica', 18, 'bold'), 'white'),
          ]
        elif m_test_name == 'others':
            # Dict for parameters details
            headings=[('1.Are priority seat pictograms visible as required?', ('Helvetica', 18, 'bold'), 'white'),
            ('2.A pictogram shall be placed internally adjacent to the priority seat', ('Helvetica', 18, 'bold'), 'white'),
            ('3.Do Type I buses meet disability seating requirements?', ('Helvetica', 18, 'bold'), 'white'),
            ('4.Are priority seats behind the forward-facing driver?', ('Helvetica', 18, 'bold'), 'white'),
            ('5.Are priority seats equipped for securing mobility aids?', ('Helvetica', 18, 'bold'), 'white'),
            ('6.Is there a handrail at Type I bus entrance?', ('Helvetica', 18, 'bold'), 'white'),
             ('7.Are Type I NDX buses equipped with stop-request controls?', ('Helvetica', 18, 'bold'), 'white'),
             ('8.Are communication devices near priority seats installed?', ('Helvetica', 18, 'bold'), 'white')
             ]
        elif m_test_name == 'wheel':
            # Dict for parameters details
            headings=[('1.Are there visible wheelchair pictograms on the bus?', ('Helvetica', 18, 'bold'), 'white'),
            ('2.Is there an internal pictogram indicating wheelchair orientation?', ('Helvetica', 18, 'bold'), 'white'),
            ('3.Is there a wheelchair space with a capable restraint system?', ('Helvetica', 18, 'bold'), 'white'),
            ('4.Is there enough space for a wheelchair user to maneuver independently?', ('Helvetica', 18, 'bold'), 'white'),
            ('5.Does Type I vehicles have designated space for a wheelchair user?', ('Helvetica', 18, 'bold'), 'white'),
            ('6.Are communication devices located in the wheelchair area?', ('Helvetica', 18, 'bold'), 'white'),
         
             ]
        else:
            print("Error: m_test_name hasn't passed...")
        
        y_position = 290
        for text, font_params, fg_color in headings:
            label = tk.Label(self.frame, text=text, font=font_params, fg=fg_color, bg='#0E0E0E')
            label.place(x=170, y=y_position)

            y_position += 70
        
        api_model.m_test_parameters_handler(frame = self.frame, m_test_name = m_test_name, id = id)
        
        

    
    # function to resize the image
    def detail_page_resize_image(self, image_path, width, height):
        try:
            img = Image.open(image_path)
            img = img.resize((width, height))
            img_tk = ImageTk.PhotoImage(img)

            return img_tk
        except Exception as e:
            print(f"Error loading {image_path}: {e}") 
    
    
    def on_back_click(self, datas):
        self.frame.destroy()
        start_testing(self.root, datas)
        print('BACK')

# Break Test and Axle weight test frame for page(GUI)
class Break_Test:
    def __init__(self, root, id, centre):
        self.root = root
        self.root.geometry('1000x1000')
        self.root.title('VFT')
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        # Create a frame
        self.frame = tk.Frame(root)
        self.frame.pack(expand=True, fill='both')

        # Load and display the background image        
        # Image1.image_handler(self.frame, 'Images/blackbg.png', 1400, 750, 0, 0)
        
        # Variable defines for parameters
        self.id = id
        self.centre = centre
        
        # self.setup_test_content(datas=datas, hdlp_datas=hdlp_datas)
        self.setup_test_content()
        self.start_thread1()
        self.start_thread2()
    
    
    def on_close(self):
        # Stop the thread
        self.stop_thread1()
        self.stop_thread2()
        # Destroy the Tkinter window
        self.root.destroy()
    
    # FUNCTION FOR BUTTONS
    def on_prev10_click(self):
        # self.buttonprev.config(bg='red', fg='white')
        self.buttonnext.config(bg='white', fg='red')
        

    def on_next10_click(self):
        # self.buttonprev.config(bg='white', fg='red')
        self.buttonnext.config(bg='red',  fg='white')
    
    
    def setup_test_content(self):
        # carwtbg
        # Image1.image_handler(self.frame, 'Images/blackbg.png', 1400, 750, 0, 0)
        bg_img = Image.open('Images/blackbg.png')
        bg_img_tk = ImageTk.PhotoImage(bg_img)
        bg_img_label = tk.Label(self.frame, image=bg_img_tk)
        bg_img_label.image = bg_img_tk
        bg_img_label.pack(expand=True, fill='both')
        
        # Brake heading
        Image1.image_handler(self.frame, 'Images/brake.png', 600, 90, 10, 20)

        # Apply brake heading
        Image1.image_handler(self.frame, 'Images/applybreak.png', 500, 70, 80, 110)

        # SPEEDOMETER IMAGE 1
        MQTT = mqtt_handler.mqtt_object(frame=self.frame, id=self.id)
        
        # Image1.image_handler(self.frame, 'Images/speedo_base.png', 300, 60, 20, 468)
        
        # label 1 : left brake
        label1 = tk.Label(self.frame, text='Left Brake Force(kN)',font=('Helvetica',12,'bold'),bg="#0E0E0E",fg="#FFF846")
        label1.place(x=95 ,y=530)
        
        # entryfield left brake
        # leftbrake_entryField = tk.Label(self.frame, width=10,text='20', font=("Arial", 12), fg='black',bg='#FAFAFA',borderwidth=0,relief='flat')
        # leftbrake_entryField.place(x=125, y=480)

        # SPEEDOMETER IMAGE 2
        # Image1.image_handler(self.frame, 'Images/speedo_base.png', 230, 50, 400, 380)

        # label 2: left brake
        label2 = tk.Label(self.frame, text='Weight',font=('Helvetica',12,'bold'),bg="#0E0E0E",fg="#FFF846")
        label2.place(x=490 ,y=436)
        # entryfield WEIGHT
        # weight_entryfield = tk.Label(self.frame, width=8,text='30', font=("Arial", 12), fg='black',bg='#FAFAFA',borderwidth=0,relief='flat')
        # weight_entryfield.place(x=480, y=387)
        
        # SPEEDOMETER IMAGE 3
        # Image1.image_handler(self.frame, 'Images/speedo_base.png', 300, 60, 690, 468)
        
        # label 3 : left brake
        label3 = tk.Label(self.frame, text='Right Brake Force(kN)',font=('Helvetica',12,'bold'),bg="#0E0E0E",fg="#FFF846")
        label3.place(x=770 ,y=530)
        # # entryfield 
        # rightbrake_entryfield = tk.Label(self.frame,text='400', width=10, font=("Arial", 12), fg='black',bg='#FAFAFA',borderwidth=0,relief='flat')
        # rightbrake_entryfield.place(x=795, y=480)
        
        # Break Efficiency and test result
        break_efficiency = tk.Label(self.frame, text='Break Efficiency', font=("Times", "20", "bold italic"), fg='white', bg='#0E0E0E')
        break_efficiency.place(x=80, y=600)
        
        break_efficiency = tk.Label(self.frame, text='Test Result', font=("Times", "20", "bold italic"), fg='white', bg='#0E0E0E')
        break_efficiency.place(x=500, y=600)


        # info
        Image1.image_handler(self.frame, 'Images/info.png', 20, 20, 40, 670)

        procedure_label = tk.Label(self.frame, text='Procedure',font=('Helvetica',12),bg="#0E0E0E",fg="white")
        procedure_label.place(x=80 ,y=670)

        procedure1_label = tk.Label(self.frame, text='1.Wait for car to establish connection with sensor',font=('Helvetica',10),bg="#0E0E0E",fg="white")
        procedure1_label.place(x=80 ,y=700)

        procedure2_label = tk.Label(self.frame, text='2.Ask Driver to press accelerato',font=('Helvetica',10),bg="#0E0E0E",fg="white")
        procedure2_label.place(x=80 ,y=720)
        

        # white bg of graph
        Image1.image_handler(self.frame, 'Images/graphbg.png', 500, 500, 1050, 140)
        
        #  BUTTON PREV AND NEXT
        # self.buttonprev = tk.Button(self.frame, text="Prev",font=('Helvetica',12,'bold','italic'),width=13,height=1,fg='#D70226',bg='#FAFAFA',borderwidth=0,relief='flat',command=lambda: [self.on_prev10_click(), self.start_thread2()], activeforeground='white',)
        # self.buttonprev.place(x=1000,y=680)

        # self.buttonnext = tk.Button(self.frame, text="Next",font=('Helvetica',12,'bold','italic'),width=13,height=1,fg='#D70226',bg='#FAFAFA',borderwidth=0,relief='flat',command=lambda: [self.on_next10_click(), self.stop_thread2(), self.stop_thread1(), self.Go_To_Break_Test()],activeforeground='white')
        # self.buttonnext.place(x=1200,y=680)

        # status
        Image1.image_handler(self.frame, 'Images/status.png', 80, 20, 950, 70)

        # timer
        Image1.image_handler(self.frame, 'Images/timer.png', 40, 40, 950, 100)
        
        # timer1_label= tk.Label(self.frame,text='pass', bg="#0E0E0E",fg='yellow',font=(10))
        # timer1_label.place(x=1000, y=125)
        
        # Code to show variable data in graph
        style.use("ggplot")
        self.f = Figure(figsize=(5,5), dpi=77)
        self.a = self.f.add_subplot(111)

        # Adjust the appearance of axis labels
        self.a.tick_params(axis='x', labelsize=15)  # Set x-axis label size
        self.a.tick_params(axis='y', labelsize=15)  # Set y-axis label size

        self.canvas = FigureCanvasTkAgg(self.f)
        self.canvas.get_tk_widget().place(x=1110, y=195)
    
    
    
    # Function to update graph
    def animate(self):
        file_path1 = resource_path('Graph_Text_Files\\sampleText.txt')
        file_path2 = resource_path('Graph_Text_Files\\sampleText2.txt')
        pullData = open(file_path1,"r").read()
        pullData2 = open(file_path2,"r").read()
        dataList = pullData.split('\n')
        dataList2 = pullData2.split('\n')
        xList = []
        yList = []
        xList2 = []
        yList2 = []
        # print("Yes i am also execuring")
        for eachLine in dataList:
            if len(eachLine) > 1:
                x, y = eachLine.split(',')
                xList.append(float(x))
                yList.append(float(y))
                
        for eachLine2 in dataList2:
            if len(eachLine2) > 1:
                x, y = eachLine2.split(',')
                xList2.append(float(x))
                yList2.append(float(y))
        self.a.clear()
        self.a.plot(xList, yList, color='#CC0CA1')
        self.a.plot(xList2, yList2, color='#2BB3E1')
        self.a.tick_params(left = False)
        # Refresh the canvas to show the updated plot
        self.canvas.draw()
    
    # Show the next button after the completion on break force and axle weight test
    def NextButtonShow(self):
        
        api_url = f'{m_base_url}/test/checkdata/{self.id}/{self.centre}'  # Replace with your actual API endpoint
        # payload = {}
         
        
        try:
            response = requests.post(api_url) #,data=payload)
            # print(response.text,"api")
            if response.status_code == 200:
                # print('Searched successfully!') 
                datas = response.json()
                # print(datas)
                if datas['payload']['testbrake'] == 'fail' or datas['payload']['testbrake'] == 'pass':
                    self.buttonnext = tk.Button(self.frame, text="Next",font=('Helvetica',12,'bold','italic'),width=13,height=1,fg='#D70226',bg='#FAFAFA',borderwidth=0,relief='flat',activeforeground='white',command=lambda: [self.on_next10_click(), self.stop_thread2(), self.stop_thread1(), self.Go_To_Break_Test()])
                    self.buttonnext.place(x=1200,y=680)
                else:
                    pass
                 # Destroy the current frame
                # self.frame.destroy()

        # Create and display the SignInApp frame
                # start_testing(self.root, datas)
            else:
                print(f'Error: Not Found')
                # self.manual_label =tk.Label(self.frame,text="Manual Test is Running...",bg='#E5E5E5',fg='red',font=('Helvetica',14,'bold','italic'))
                # self.manual_label.place(x=300,y=275)
                # print(f'Error: {response.status_code,response.text}')
                # self.scaningtext_scan.config(text="Appointment Not Found", fg="red", font=('',14))
                # self.frame.destroy()
                # start_testing(self.root, datas)

        except requests.RequestException as e:
            print(f'Error: {e}')
    
    
    
    def start_thread1(self):
        self.is_running1 = True  # Set the flag to start the thread
        self.thread1 = Thread(target=self.run_thread1)
        self.thread1.start()

    def stop_thread1(self):
        self.is_running1 = False  # Set the flag to stop the thread

    def run_thread1(self):
        while self.is_running1:
            print("Thread1 is running...")
            self.thread1 = Thread(target=self.animate())
            time.sleep(2)
        
        print("Thread1 is stopped.")
    
    def start_thread2(self):
        self.is_running2 = True  # Set the flag to start the thread
        self.thread2 = Thread(target=self.run_thread2)
        self.thread2.start()

    def stop_thread2(self):
        self.is_running2 = False  # Set the flag to stop the thread

    def run_thread2(self):
        while self.is_running2:
            print("Thread2 is running...")
            self.thread2 = Thread(target=self.NextButtonShow())
            time.sleep(2)
        
        print("Thread2 is stopped.")
        
    
    def Go_To_Break_Test(self):
        self.frame.destroy()
        RPM_Test(self.root)



# Break Test and Axle weight test frame for page(GUI)
class RPM_Test:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1000x1000')
        self.root.title('VFT')
        # Create a frame
        self.frame = tk.Frame(root)
        self.frame.pack(expand=True, fill='both')

        # Load and display the background image        
        # Image1.image_handler(self.frame, 'Images/blackbg.png', 1400, 750, 0, 0)
        
        # self.setup_test_content(datas=datas, hdlp_datas=hdlp_datas)
        self.setup_test_content()
        # self.start_thread()
    
    
    # FUNCTION FOR BUTTONS
    def on_prev10_click(self):
        self.buttonprev.config(bg='red', fg='white')
        self.buttonnext.config(bg='white', fg='red')
        

    def on_next10_click(self):
        self.buttonprev.config(bg='white', fg='red')
        self.buttonnext.config(bg='red',  fg='white')
    
    
    def setup_test_content(self):
        # carwtbg
        # Image1.image_handler(self.frame, 'Images/blackbg.png', 1400, 750, 0, 0)
        bg_img = Image.open('Images/blackbg.png')
        bg_img_tk = ImageTk.PhotoImage(bg_img)
        bg_img_label = tk.Label(self.frame, image=bg_img_tk)
        bg_img_label.image = bg_img_tk
        bg_img_label.pack(expand=True, fill='both')
        
        # Speed heading
        Image1.image_handler(self.frame, 'Images/speed.png', 900, 90, 10, 20)

        # Accelerate heading
        Image1.image_handler(self.frame, 'Images/accelerate.png', 600, 80, 60, 170)

        # Status
        Image1.image_handler(self.frame, 'Images/status.png', 100, 20, 160, 280)
        
        # Timer
        Image1.image_handler(self.frame, 'Images/timer.png', 40, 40, 160, 320)
        status_input = tk.Label(self.frame, width=8,text='pass', font=(12), fg='yellow',bg="#0E0E0E",borderwidth=0,relief='flat')
        status_input.place(x=200, y=330)

        # Info
        Image1.image_handler(self.frame, 'Images/info.png', 25, 25, 40, 470)

        procedure_label = tk.Label(self.frame, text='Procedure',font=('Helvetica',12),bg="#0E0E0E",fg="white")
        procedure_label.place(x=80 ,y=473)

        procedure1_label = tk.Label(self.frame, text='1.Wait for car to establish connection with sensor',font=('Helvetica',12),bg="#0E0E0E",fg="white")
        procedure1_label.place(x=80 ,y=500)

        procedure2_label = tk.Label(self.frame, text='2.Ask Driver to press accelerato',font=('Helvetica',12),bg="#0E0E0E",fg="white")
        procedure2_label.place(x=80 ,y=530)

        procedure3_label = tk.Label(self.frame, text='3. .....(your own instructions)',font=('Helvetica',12),bg="#0E0E0E",fg="white")
        procedure3_label.place(x=80 ,y=560)
        
        # Speedometer Image
        Image1.image_handler(self.frame, 'Images/speedometer.png', 500, 450, 650, 100)

        # ENTRY FIELD IN SPEEDOMETER
        speedentryField = tk.Label(self.frame, width=20,text='80kmph', font=("Arial", 12), fg='black',bg='#FAFAFA',borderwidth=0,relief='flat')
        speedentryField.place(x=810, y=460)
        
        # BUTTON PREV AND NEXT
        buttonprev = tk.Button(self.frame, text="Prev",font=('Helvetica',12,'bold','italic'),width=15,height=1,fg='#D70226',bg='#FAFAFA',borderwidth=0,relief='flat',command=self.on_prev10_click, activeforeground='white',)
        buttonprev.place(x=850,y=580)

        buttonnext = tk.Button(self.frame, text="Next",font=('Helvetica',12,'bold','italic'),width=15,height=1,fg='#D70226',bg='#FAFAFA',borderwidth=0,relief='flat',command=self.on_next10_click,activeforeground='white')
        buttonnext.place(x=1050,y=580)

# Usage
root = tk.Tk()
app = VFTApp(root)
root.mainloop()
