import toml


class IrisWatcher:
    config_file = "./app.toml"

    def __init__(self):
        parsed_config = toml.load(self.config_file)
        self.frequency = parsed_config["config"]["frequency"]

    def watch(self, product_name: str):
        print(self.websites)
        print(self.frequency)


if __name__ == '__main__':
    iw = IrisWatcher()
    iw.watch("Hello")
