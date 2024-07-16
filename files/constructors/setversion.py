class Version():

    def __init__(self,view) -> None:
        self.version = '1.0.3'
        self.label = view


    def set(self):
        self.label.setText(self.version)