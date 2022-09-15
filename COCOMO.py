class Basic():
    def organic(self, a, b, c, d, KLOC):
        # E = a(KLOC) ^ b
        E = a*((KLOC) ^ b)
        time = c*((E) ^ d)
        person = E / time
        # self.w = Window()
        # self.w.show()
        # self.hide()
        return [E,time,person]


    def semiorganic(self):
        pass

    def embeded(self):
        pass
