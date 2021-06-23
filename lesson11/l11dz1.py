
class Date:
    def __init__(self, date_time):
        self.date_time = date_time

    @classmethod
    def to_int(cls, date_time):
        cur_dat = map(int, date_time.split('-'))
        return cur_dat

    @staticmethod
    def valid_date(cur_dat):
        d, m, y = cur_dat
        try:
            if d < 1 or d > 31:
                raise ValueError
            if m < 1 or m > 12:
                raise ValueError
            if len(str(y)) > 4:
                raise ValueError
        except ValueError:
            print('Дата введена некоректно!')


d_1 = Date.to_int('12-13-15')
Date.valid_date(d_1)
