class add(int):
    # argument is typed as integer
    def __call__(self, number):
        return add(self + number)
        
    # Ref: https://stackoverflow.com/questions/9663562/what-is-the-difference-between-init-and-call
    
