class TestClass:
    def __init__(self):
        print('TestClass.__init__()')
        self.name = 'TestClass'

    def __str__(self):
        return self.name
