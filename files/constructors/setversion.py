class Version():

    def __init__(self,view) -> None:
        self.version = '1.0.2'
        self.label = view


    def set(self):
        self.label.setText(self.version)