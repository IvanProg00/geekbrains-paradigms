class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


singlelon1 = Singleton()
singlelon2 = Singleton()

print(singlelon1 is singlelon2)
