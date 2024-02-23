class Smartphone:
    apps = []
    is_on = False

    def __init__(self, memory: int):
        self.memory = memory

    def power(self):
        self.is_on = True

    def install(self, app, app_memory):
        if not self.is_on:
            return f"Turn on your phone to install {app}"

        if self.memory >= app_memory:
            self.apps.append(app)
            self.memory -= app_memory
            return f"Installing {app}"
        else:
            return f"Not enough memory to install {app}"

    def status(self):
        total_apps_count = len(self.apps)
        return f"Total apps: {total_apps_count}. Memory left: {self.memory}"


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
