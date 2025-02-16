import json

class Calc_probality():
    
    def control_input(self, c_info, d_info, e_info, f_info, e_info_alpha, f_info_alpha, x_info, y_info, z_info, head_info, body_info):

        self.c_info = c_info
        self.d_info = d_info
        self.e_info = e_info
        self.f_info = f_info
        self.e_info_alpha = e_info_alpha.text
        self.f_info_alpha = f_info_alpha.text
        self.x_info = x_info.text
        self.y_info = y_info.text
        self.z_info = z_info.text
        self.head_info = head_info.text
        self.body_info = body_info.text


        positive_probality = '/home/salamat/ratingsays_offline/rs/utils/positive.json'
        negative_probality = '/home/salamat/ratingsays_offline/rs/utils/negative.json'

        with open(positive_probality, 'r', encoding='utf-8') as pos_file:
            self.pos_data = json.load(pos_file)

        with open(negative_probality, 'r', encoding='utf-8') as neg_file:
            self.neg_data = json.load(neg_file)

        self.instance_c = 0
        self.instance_d = 0
        self.instance_e = 0
        self.instance_f = 0

        self.c = 0
        self.d = 0
        self.e = 0
        self.f = 0

        try:
            try: 
                self.e_alpha = int(self.e_info_alpha)
                self.f_alpha = int(self.f_info_alpha)
            except ValueError | TypeError as e: 
                print(e)
            
            if int(self.e_alpha) and int(self.f_alpha) or float(self.e_alpha) and float(self.f_alpha):
                if self.e_alpha and self.f_alpha < 11 or 0:
                    self.get_c()
                    self.get_d()
                    self.get_e()
                    self.get_f()
                    self.is_instance()
                else:
                    print('Most be beetwen 0-10')

            else: 
                print(f'Type error')

        except TypeError or ValueError as e:
            print(f'Error is : {e}')



    def get_c(self):

        c_info_lower = self.c_info.title()
        for key, value in self.pos_data.items():
            for word, _ in value.items():
                if word in c_info_lower:
                    
                    self.instance_c += 1  
                    self.c += int(key)
                    self.c /= self.instance_c
                    self.c /= 10

    def get_d(self):

        d_info_lower = self.d_info.title()
        for key, value in self.neg_data.items():
            for word, _ in value.items():
                if word in d_info_lower:
                    
                    self.instance_d += 1  
                    self.d += int(key)
                    self.d /= self.instance_d
                    self.d /= 10

    def get_e(self):

        e_info_lower = self.e_info.title()
        for key, value in self.pos_data.items():
            for word, _ in value.items():
                if word in e_info_lower:
                    
                    self.instance_e += 1  
                    self.e += int(key)
                    self.e /= self.instance_e
                    self.e /= 10

    def get_f(self):

        f_info_lower = self.f_info.title()
        for key, value in self.neg_data.items():
            for word, _ in value.items():
                if word in f_info_lower:
                    
                    self.instance_f += 1  
                    self.f += int(key)
                    self.f /= self.instance_f
                    self.f /= 10

    def is_instance(self):
        
        if self.x_info == 'Pes':
            self.x = 2

        elif self.x_info == 'Erbet dal':
            self.x = 4
        
        elif self.x_info == 'Onat':
            self.x = 6

        elif self.x_info == 'Yokary':
            self.x = 8

        elif self.x_info == 'Mejbur':
            self.x = 10

        
        if self.y_info == 'Pes':
            self.y = 2

        elif self.y_info == 'Erbet dal':
            self.y = 4
        
        elif self.y_info == 'Onat':
            self.y = 6

        elif self.y_info == 'Yokary':
            self.y = 8

        elif self.y_info == 'Mejbur':
            self.y = 10

        if self.z_info == '0%':
            self.z = 1

        elif self.z_info == '10%':
            self.z = 1.5

        elif self.z_info == '20%':
            self.z = 2

        elif self.z_info == '30%':
            self.z = 2.5
            
        elif self.z_info == '40%':
            self.z = 3

        elif self.z_info == '50%':
            self.z = 3.5

        elif self.z_info == '60%':
            self.z = 4

        elif self.z_info == '70%':
            self.z = 4.5

        elif self.z_info == '80%':
            self.z = 5

        elif self.z_info == '90%':
            self.z = 5.5

        elif self.z_info == '99%':
            self.z = 6


        if self.head_info == 'Yeterlik dal':
            self.g = 1

        elif self.head_info == 'Onat':
            self.g = 5
        
        elif self.head_info == 'Yeterlik':
            self.g = 10
        


        if self.body_info == 'Yeterlik dal':
            self.h = 1

        elif self.body_info == 'Onat':
            self.h = 5
        
        elif self.body_info == 'Yeterlik':
            print('worked')
            self.h = 10


        self.calc_result()

    def calc_result(self):

        from UI.frontend import Posibilyty_calc
        self.probability = Posibilyty_calc()

        a = self.c - self.d
        b = (self.e + self.e_alpha) - (self.f + self.f_alpha)
        instance = self.x - self.y
        first = a * instance
        second = b * instance
        first_result = first + second
        second_result = first_result / self.z

        health = self.g + self.h


        result = second_result * health
        result_str = str(result)

        if len(result_str) > 1:
            result / 1000

        print(result)

        if result > 99: 
            result = 99

        elif result < 1:
            result = 1

        self.probability.get_result(int(result))