class employee:
    def __init__(self):
        print("employee created")

    def __del__(self):
        print("destructer called, employee deleted")

obj = employee()
del obj