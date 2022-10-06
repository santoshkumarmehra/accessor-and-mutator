class mobile:
    fp="yes"
    @classmethod
    def show_model(cls,r):
        cls.ram=r
        print("fingerprint: ",cls.fp)
        print("Ram: ",cls.ram)

# realme=mobile()
mobile.show_model("8gb")