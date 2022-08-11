from tkinter import *
import random
import csv


class GUI:
    '''
    Class for setting the information of the GUI window
    '''
    def __init__(self, window):
        """
        - This function is for creating the frames of the window, entries, buttons and setting their dimensions.
        """

        self.window = window
         
        self.name_frame=Frame(self.window)
        self.entry_name=Entry(self.name_frame, width=16, font=10)
        self.label_name = Label(self.name_frame, text='Name', font=10)
        self.name_frame.pack(anchor='w', pady=6)
        self.entry_name.pack(padx=14, side='right')
        self.label_name.pack(padx=14, side='right')
        
        self.age_frame=Frame(self.window)
        self.entry_age=Entry(self.age_frame, width=16, font=10)
        self.label_age=Label(self.age_frame, text='Age', font=10)
        self.age_frame.pack(anchor='w', pady=6)
        self.entry_age.pack(padx=20,side='right')
        self.label_age.pack(padx=20, side='right')
        
        self.carMake_frame=Frame(self.window) 
        self.entry_car_make=Entry(self.carMake_frame, width=16, font=10)
        self.label_car_make=Label(self.carMake_frame, text='Car make', font=10)
        self.carMake_frame.pack(anchor='w', pady=6)
        self.entry_car_make.pack(padx=3, side='right')
        self.label_car_make.pack(padx=3, side='right')
            
        self.carModel_frame=Frame(self.window)
        self.entry_car_model=Entry(self.carModel_frame, width=16, font=10)
        self.label_car_model=Label(self.carModel_frame, text='Car model', font=10)
        self.carModel_frame.pack(anchor='w', pady=6)
        self.entry_car_model.pack(padx=2, side='right')
        self.label_car_model.pack(padx=2, side='right')
        
        self.carYear_frame=Frame(self.window)
        self.entry_car_year=Entry(self.carYear_frame, width=16, font=10)
        self.label_car_year=Label(self.carYear_frame, text='Car year', font=10)
        self.carYear_frame.pack(anchor='w', pady=6)
        self.entry_car_year.pack(padx=6, side='right')
        self.label_car_year.pack(padx=6, side='right')

        self.buttonFrame=Frame(self.window)
        
        self.buttonQuote=Button(self.window,text='Get Quote!', font=16, width = 12, command=self.clicked)
        self.buttonReset=Button(self.window,text='Reset', font=16, width = 12, command=self.reset)
        
        self.buttonFrame.pack(anchor='w', pady=6)
        self.buttonQuote.pack(padx=0,pady=6)
        self.buttonReset.pack(padx=0,pady=6)
    def clicked(self):
        '''
        This function is called when the 'Get quote' button is clicked. It is meant to get the user input and check if the data is not valid with showing error message.
        If data is valid, the function determines the price of insurance based on user's data and display it to them as quote in a new window.
        '''
        #List of car makes eligible to choose from.
        car_makes=['kia', 'toyota', 'chevrolet', 'nissan','ford', 'honda', 'hyundai']
        
        #List of car models eligible to choose from.
        car_models=['carnival', 'rio', 'soul', 'camry', 'corolla','avalon', 'malibu',
                    'corvette', 'sillverado', 'altima', 'maxima',
                    'sentra', 'focus', 'edge', 'mustang', 'accord', 'odyssey', 'civic',
                    'Sonata', 'accent', 'elantra']
        #List of cars whose insurance is more expensive.
        exp_cars=['mustang', 'accord', 'odyssey', 'camry', 'corvette', 'sillverado']
        
        #Getting the user inputs
        name=self.entry_name.get()
        age=self.entry_age.get()
        car_make=self.entry_car_make.get()
        car_model=self.entry_car_model.get()
        car_year=self.entry_car_year.get()
        
        try:
            #Meant to invoke the exception handler to catch data types error.
            name=(str(self.entry_name.get()))+''
            age=(int(self.entry_age.get()))+0
            car_make=(str(self.entry_car_make.get()))+''
            car_model=(str(self.entry_car_model.get()))+''
            car_year=(int(self.entry_car_year.get()))+0
            
            # Default insurance price
            price=50.00
            
            #Comparing user data with factors that affect the price.
            if age <25:
                price=price+20
            if age>50:
                price=price-7.00
            if car_year>2010 and car_year<=2016:
                price=price+10.00
            if car_year>2001 and car_year<=2010:
                price=price-5.00
            if car_year>=1995 and car_year>=2000:
                price=price-10.0
            if car_year>2016 and car_year<=2022:
                price=price+17.0
            if car_model.lower() in exp_cars:
                price=price+random.uniform(10.0, 15.5)
        
            #Checking if types of data entered are correct, whether car make and model are vaild, age(18-100), and car_year(1995-2022).
            if name.isalpha()==True and car_make.isalpha()==True and car_model.isalpha()==True and str(age).isdigit()==True and str(car_year).isdigit()==True and (str(car_make)).lower() in car_makes and (str(car_model)).lower() in car_models and int(car_year)>1995 and int(car_year)<=2022 and age<100 and age>=18:
                quoteMsg=f"Hello {name}! You can get your {car_make.title()} {car_model.title()} {car_year} insurance for {price:.2f}$/monthly or {price*6-50:.2f}$ for 6 months if you pay today! To get this done call us on 1-800-XAL-XAL or visit our website https://xal.com"
                messagebox.showinfo('Message', quoteMsg)
            else:
                raise(ValueError, TypeError)
        #Catching the errors expected with showing an error message.
        except(ValueError, TypeError):
            print('Oops there is something wrong!')
            errorMsg=f"Something went wrong!\nAge: 18-100\nCar year:1995-2022\nDo not leave any entries empty!\nCar makes eligible:Kia, Toyota, Chevrolet, Nissan, Ford, Honda, Hyundai\nCar models eligible: Carnival, Rio, Soul, Camry, Corolla, Avalon, Malibu,Corvette, Sillverado, Altima, Maxima, Sentra, Focus, Edge, Mustang, Accord, odyssey, Civic Sonata, Accent, Elantra"
                      
            messagebox.showerror('Error', errorMsg)
           
           
        #Resetting the entries after user presses the 'Get quote' button and get their quote.       
        self.entry_name.delete(0, END)
        self.entry_age.delete(0,END)
        self.entry_car_make.delete(0, END)
        self.entry_car_model.delete(0, END)
        self.entry_car_year.delete(0, END)
            
    def reset(self):
        '''
        This function is called when the user presses the 'Reset' button and it is meant to reset the entries.
        '''
        self.entry_name.delete(0, END)
        self.entry_age.delete(0,END)
        self.entry_car_make.delete(0, END)
        self.entry_car_model.delete(0, END)
        self.entry_car_year.delete(0, END)