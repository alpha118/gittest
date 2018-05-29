class StaffClass:

    def __init__(self):
        pass


    def StaffInfoDict(self, name_list):
        self.duty_info_dict = {}
        for staff_name in name_list:
            if self.duty_info_dict:
                self.duty_info_dict[max(self.duty_info_dict.keys()) + 1] = {'Name': staff_name, 'Duty_Times': 0}
            else:
                self.duty_info_dict[1] = {'Name': staff_name, 'Duty_Times': 0}