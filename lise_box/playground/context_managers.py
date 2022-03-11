# %%
class Manager:
    def __enter__(self):
        print("Entering")
    def __exit__(self, ty, val, tb):
        print("Exiting", ty, val, tb)

m = Manager()

with m:
    print("hello world")