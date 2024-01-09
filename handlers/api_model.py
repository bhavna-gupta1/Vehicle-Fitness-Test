# import sys
# sys.path.append("C:/Users/cti-2/OneDrive/Documents/Vehicle-Fitness-Test/bhavna_vft/handlers")

# import os
# current_dir = os.path.dirname(os.path.realpath(__file__))
# print(current_dir)


import requests
from io import BytesIO
from tkinter import Label
from PIL import Image
from handlers.Image1 import image_handler
from handlers.API_Handler import call_api

# result = call_api(vehiclenumber = 'HR NC 12 2918')
# print(result)

def get_image_from_url(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img


def m_test_parameters_handler(**kwargs):
    if 'm_test_name' in kwargs:
        response_datas = call_api(testname = kwargs['m_test_name'], id = kwargs['id'])
        
        #Image code for perticular manual test
        if response_datas['payload']['img'] != 'none':
            img_url = response_datas['payload']['img']
            img = get_image_from_url(img_url)
            image_handler(kwargs['frame'],'Images/blnkbox.png', 400, 400, 1490,300,direct_img=img)
        else:
            label_m_test_Img = Label(kwargs['frame'], text='Image not provided', fg='red', bg='#0E0E0E', font=('',24))
            label_m_test_Img.place(x=1530, y=500)
        
        #createing Label to show additional details for manual tests
        if response_datas['payload']['remark'] != None:
            label_additional_details = Label(kwargs['frame'],text=f"iiwjdiew oiwejofie oiwefiohe oiwefiewn woiehfiowehrf wiowehfiohewr woieehfiowehf: {response_datas['payload']['remark']}", wraplength=280, font=('',14))
            label_additional_details.place(x=1020, y=450)
        else:
            label_additional_details = Label(kwargs['frame'],text="You haven't mention the remarks")
            label_additional_details.place(x=1090, y=470)
        
        # For Parameter 1
        if response_datas['payload']['p1'] == '1':
            image_handler(kwargs['frame'],'Images/blnkbox.png', 40, 40, 110, 290, image_path_02='Images/right.png')
        elif response_datas['payload']['p1'] == '2':
            image_handler(kwargs['frame'],'Images/blnkbox.png', 40, 40,110, 290, image_path_02='Images/cross.png')
        else:
            image_handler(kwargs['frame'],'Images/blnkbox.png', 40, 40,110, 290)
            na_label = Label(kwargs['frame'], text='NA', font=('', 12, 'bold'), fg='black').place(x=113, y=293)
        
        # For Parameter 2
        if response_datas['payload']['p2'] == '1':
            image_handler(kwargs['frame'],'Images/blnkbox.png', 40, 40,110, 360, image_path_02='Images/right.png')
        elif response_datas['payload']['p2'] == '2':
            image_handler(kwargs['frame'],'Images/blnkbox.png', 40, 40,110, 360, image_path_02='Images/cross.png')
        else:
            image_handler(kwargs['frame'],'Images/blnkbox.png', 40, 40,110, 360)
            na_label = Label(kwargs['frame'], text='NA', font=('', 12, 'bold'), fg='black').place(x=113, y=363)
        
        if kwargs['m_test_name'] == 'headlamp' or kwargs['m_test_name'] == 'exhaust' or kwargs['m_test_name'] == 'dashboard' or kwargs['m_test_name'] == 'horn' or kwargs['m_test_name'] == 'safetyglasses' or kwargs['m_test_name'] == 'supressor' or kwargs['m_test_name'] == 'toplight' or kwargs['m_test_name'] == 'silencer' or kwargs['m_test_name'] == 'numberplatelight' or kwargs['m_test_name'] == 'directionlight' or kwargs['m_test_name'] == 'outlinemarkerlight' or kwargs['m_test_name'] == 'foglight' or kwargs['m_test_name'] == 'parkinglight' or kwargs['m_test_name'] == 'rearmirror' or kwargs['m_test_name'] == 'warninglight' :
            # For Parameter 3
            if response_datas['payload']['p3'] == '1':
                image_handler(kwargs['frame'],'Images/blnkbox.png', 40, 40,110, 430, image_path_02='Images/right.png')
            elif response_datas['payload']['p3'] == '2':
                image_handler(kwargs['frame'],'Images/blnkbox.png', 40, 40,110, 430, image_path_02='Images/cross.png')
            else:
                image_handler(kwargs['frame'],'Images/blnkbox.png', 40, 40,110, 430)
                na_label = Label(kwargs['frame'], text='NA', font=('', 12, 'bold'), fg='black').place(x=113, y=433)
            
            if kwargs['m_test_name'] == 'headlamp'or kwargs['m_test_name'] == 'toplight' or kwargs['m_test_name'] == 'dashboard' or kwargs['m_test_name'] == 'exhaust' or kwargs['m_test_name'] == 'horn' or kwargs['m_test_name'] == 'silencer' or kwargs['m_test_name'] == 'numberplatelight' or kwargs['m_test_name'] == 'directionlight' or kwargs['m_test_name'] == 'outlinemarkerlight' or kwargs['m_test_name'] == 'foglight' or kwargs['m_test_name'] == 'parkinglight' or kwargs['m_test_name'] == 'rearmirror' or kwargs['m_test_name'] == 'warninglight' :
                #For Parameter 4
                if response_datas['payload']['p4'] == '1':
                    image_handler(kwargs['frame'],'Images/blnkbox.png', 40, 40,110, 500, image_path_02='Images/right.png')
                elif response_datas['payload']['p4'] == '2':
                    image_handler(kwargs['frame'],'Images/blnkbox.png', 40, 40,110, 500, image_path_02='Images/cross.png')
                else:
                    image_handler(kwargs['frame'],'Images/blnkbox.png', 40, 40,110, 500)
                    na_label = Label(kwargs['frame'], text='NA', font=('', 12, 'bold'), fg='black').place(x=113, y=503)
                
                if kwargs['m_test_name'] == 'headlamp' or kwargs['m_test_name'] == 'toplight' or  kwargs['m_test_name'] == 'silencer' or kwargs['m_test_name'] == 'numberplatelight' or kwargs['m_test_name'] == 'directionlight' or kwargs['m_test_name'] == 'outlinemarkerlight' or kwargs['m_test_name'] == 'foglight' or kwargs['m_test_name'] == 'parkinglight' or kwargs['m_test_name'] == 'rearmirror' or kwargs['m_test_name'] == 'warninglight' :
                    #For Parameter 5
                    if response_datas['payload']['p5'] == '1' :
                        image_handler(kwargs['frame'],'Images/blnkbox.png', 40, 40,110, 570, image_path_02='Images/right.png')
                    elif response_datas['payload']['p5'] == '2':
                        image_handler(kwargs['frame'],'Images/blnkbox.png', 40, 40,110, 570, image_path_02='Images/cross.png')
                    else:
                        image_handler(kwargs['frame'],'Images/blnkbox.png', 40, 40,110, 570)
                        na_label = Label(kwargs['frame'], text='NA', font=('', 12, 'bold'), fg='black').place(x=113, y=576)
                    
                    if kwargs['m_test_name'] == 'toplight':
                        #For Parameter 6
                        if response_datas['payload']['p6'] == '1':
                            image_handler(kwargs['frame'],'Images/blnkbox.png', 40, 40,110, 640, image_path_02='Images/right.png')
                        elif response_datas['payload']['p6'] == '2':
                            image_handler(kwargs['frame'],'Images/blnkbox.png', 40, 40,110, 640, image_path_02='Images/cross.png')
                        else:
                            image_handler(kwargs['frame'],'Images/blnkbox.png', 40, 40,110, 640)
                            na_label = Label(kwargs['frame'], text='NA', font=('', 12, 'bold'), fg='black').place(x=113, y=643)

# m_test_parameters_handler(m_test_name = 'headlamp', id = 'A3')