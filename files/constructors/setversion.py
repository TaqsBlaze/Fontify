class Version():

    def __init__(self,version_lable) -> None:
        self.version = '1.1.4'
        self.label = version_lable


    def set(self):
        self.label.setText(self.version)