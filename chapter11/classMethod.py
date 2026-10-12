class maggi:
    a=1

    @classmethod
    def show(self):
        
        print(f"this is a code for show method {self.a}")

w=maggi()
w.a=45
w.show()