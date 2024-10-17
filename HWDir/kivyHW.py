from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup



def ask_for_id():
    global isikukood
    while True:
        idcode = input('Please enter your national id or "stop" to exit: ')
        if idcode.lower() == 'stop':
            quit()
        if idcode.isdecimal():
            if len(idcode) != 11:
                if len(idcode) < 11:
                    print('ID you entered is too short.')
                    continue
                else:
                    print('ID you entered is too long.')
                    continue
            else:
                isikukood = idcode
                break
        else:
            print('ID you entered is not numeric!')
            continue


def get_gender():
    n = isikukood[0]
    if n not in '09':
        if int(n) % 2 == 0:
            print('you are female')
        else:
            print('you are male')
    else:
        print('something wrong with your id')


def get_date_of_birth():
    day = isikukood[5:7]
    month = isikukood[3:5]
    year = isikukood[1:3]
    bcent = ''

    n = isikukood[0]
    if n not in '09':
        if n in '12':
            bcent= '18'
        elif n in '34':
            bcent = '19'
        elif n in '56':
            bcent = '20'
        elif n in '78':
            bcent = '21'
        print(f'{day}.{month}.{bcent}{year}')

    else:
        print('something wrong with your id')

def get_birth_of_region():
    birth_number = int(isikukood[7:10])
    if birth_number in range (1,11):
        print('You were born in "Kuressaare haigla"')
    elif birth_number in range (11,20):
        print('You were born in "Tartu Ülikooli Naistekliinik"')
    elif birth_number in range (21,151):
        print('You were born in "Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)"')
    elif birth_number in range (151,161):
        print('You were born in "Keila haigla"')
    elif birth_number in range (161,221):
        print('You were born in "Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)"')
    elif birth_number in range(221,271):
        print('You were born in "Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)"')
    elif birth_number in range (271,371):
        print('You were born in "Maarjamõisa kliinikum (Tartu), Jõgeva haigla"')
    elif birth_number in range (371,421):
        print('You were born in "Narva haigla"')
    elif birth_number in range (421,471):
        print('You were born in "Pärnu haigla"')
    elif birth_number in range (471,491):
        print('You were born in "Haapsalu haigla"')
    elif birth_number in range (491,521):
        print('You were born in "Järvamaa haigla (Paide)"')
    elif birth_number in range (521,571):
        print('You were born in "Rakvere haigla, Tapa haigla"')
    elif birth_number in range (571,601):
        print('You were born in "Valga haigla"')
    elif birth_number in range (601,651):
        print('You were born in "Viljandi haigla"')
    elif birth_number in range (651,701):
        print('You were born in "Lõuna-Eesti haigla (Võru), Põlva haigla"')
    else:
        print('Unknown birth region')


def get_validation():
    val_kood = [int(val) for val in isikukood]
    # print(val_kood)
    kaal1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    kaal2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    sum1 = sum(val_kood[i] * kaal1[i] for i in range(10))
    left1 = sum1 % 11

    if left1 < 10:
        control_num = left1
    else:
        sum2 = sum(val_kood[i] * kaal2[i] for i in range(10))
        left2 = sum2 % 11
        if left2 < 10:
            control_num = left2
        else:
            control_num = 0
    if control_num == int(isikukood[10]):
        print('Your id is valid')
    else:
        print('Your id is invalid')


# idcode = '38803160272'

def menu():
    ask_for_id()
    # if ask_for_id == '0':
    while True:
        user_choice = input('Please choose: \n'
                            '1. Gender\n'
                            '2. Date of birth\n'
                            '3. birth region\n'
                            '4. Validation\n'
                            '5. change ID\n'
                            '0. Exit\n'
                            '-->')
        if user_choice == '1':
            get_gender()
        elif user_choice == '2':
            get_date_of_birth()
        elif user_choice == '3':
            get_birth_of_region()
        elif user_choice == '4':
            get_validation()
        elif user_choice == '5':
            ask_for_id()
        elif user_choice == '0' or user_choice == 'stop':
            break
        else:
            print('Choice out of range')

isikukood = ''
# menu()

class MyApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        #ввод ID
        self.id_input = TextInput(hint_text="Enter your ID", multiline=False)
        self.layout.add_widget(self.id_input)

        self.layout.add_widget(self.create_button("Get Gender", self.show_gender))
        self.layout.add_widget(self.create_button("Get Date of Birth", self.show_date_of_birth))
        self.layout.add_widget(self.create_button("Get Birth Region", self.show_birth_region))
        self.layout.add_widget(self.create_button("Validate ID", self.show_validation))

        return self.layout





    def create_button(self, text, action):
        button = Button(text=text, size_hint=(1, 0.2))
        button.bind(on_press=action)
        return button

    def show_popup(self, title, message):
        popup_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        popup_layout.add_widget(Label(text=message))
        close_button = Button(text='Close', size_hint=(1, 0.2))
        popup_layout.add_widget(close_button)
        popup = Popup(title=title, content=popup_layout, size_hint=(0.8, 0.4))
        close_button.bind(on_press=popup.dismiss)
        popup.open()

    def show_gender(self, instance):
        global isikukood
        isikukood = self.id_input.text
        if len(isikukood) == 11 and isikukood.isdigit():
            gender = get_gender()
            self.show_popup('Gender', f'You are {gender}')
        else:
            self.show_popup('Error', 'Please enter a valid 11-digit ID code')

    def show_date_of_birth(self, instance):
        global isikukood
        isikukood = self.id_input.text
        if len(isikukood) == 11 and isikukood.isdigit():
            dob = get_date_of_birth()
            self.show_popup('Date of Birth', f'Your date of birth is {dob}')
        else:
            self.show_popup('Error', 'Please enter a valid 11-digit ID code')

    def show_birth_region(self, instance):
        global isikukood
        isikukood = self.id_input.text
        if len(isikukood) == 11 and isikukood.isdigit():
            region = get_birth_of_region()
            self.show_popup('Birth Region', f'You were born in {region}')
        else:
            self.show_popup('Error', 'Please enter a valid 11-digit ID code')

    def show_validation(self, instance):
        global isikukood
        isikukood = self.id_input.text
        if len(isikukood) == 11 and isikukood.isdigit():
            validation = get_validation()
            self.show_popup('Validation', validation)
        else:
            self.show_popup('Error', 'Please enter a valid 11-digit ID code')

if __name__ == "__main__":
    MyApp().run()
