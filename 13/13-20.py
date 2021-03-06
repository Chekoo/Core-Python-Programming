#codiing=utf-8
class Time60(object):
    def __init__(self, *args1):
        if type(args1[0]) is tuple:
            self.hr = args1[0][0]
            self.min = args1[0][1]
        elif type(args1[0]) is dict:
            self.hr = args1[0]['hr']
            self.min = args1[0]['min']
        elif type(args1[0]) is str:
            self.hr = int(args1[0].split(':')[0])
            self.min = int(args1[0].split(':')[1])
        elif type(args1) is tuple:
            self.hr = args1[0]
            self.min = args1[1]
    def __str__(self):
        return '%02d:%02d' % (self.hr, self.min)
    def __repr__(self):
        return repr('%02d:%02d' % (self.hr, self.min))
    def __add__(self, other):
        hour = self.hr + other.hr
        min = self.min + other.min
        if min >= 60:
            min -= 60
            hour += 1
        return self.__class__(hour, min)
    def __radd__(self, other):
        self.hr += other.hr
        self.min += other.min
        if self.min >= 60:
            self.min -= 60
            self.hr += 1
        return self
    def __iadd__(self, other):
        self.hr += other.hr
        self.min += other.min
        if self.min >= 60:
            self.min -= 60
            self.hr += 1
        return self

if __name__ == '__main__':
    thu = Time60(10, 30)
    fri = Time60(8, 35)
    print thu + fri
    thu = Time60((10, 30))
    fri = Time60({'hr': 8, 'min': 35})
    mon = Time60('10:30')
    print thu + fri
    print fri + mon
    print thu




