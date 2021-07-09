class Provider(object):
    base_url = None
    def __init__(self, url: str) -> None:
        self.base_url = url
    
    def watch(self):
        pass