#coding=utf-8
class MoneyFmt(float):
    def __init__(self, value = 0.0):
        super(MoneyFmt, self).__init__()
        self.value = float(value)
    def update(self, value = None):
        self.value = float(value)
    def __repr__(self):
        return repr(self.value)
    def __str__(self):
        return '%f' % self.value
    def __nonzero__(self):
        return bool(self.value)
if __name__ == '__main__':
    fValue = MoneyFmt('1234.567')
    print fValue
    fValue.update('1234')
    print fValue
    newfValue = MoneyFmt('12323.25465')
    print newfValue + fValue