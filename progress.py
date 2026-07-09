class ProgressBar:
    def __init__(self,total,width=40):
        import time
        self.total = total
        self.current = 0
        self.width = width
        self.last_out = ''
        self.fill = '█'
        self.empty = '░'
        self.start_time = time.time()
        self.update_display()


    def tick(self,amount=1):
        self.current = min(self.current + amount, self.total)
        self.update_display()
    def set(self,value):
        self.current = max(0,min(value,self.total))
        self.update_display()
    def update_display(self):
        solid = round((self.current/self.total)*(self.width-2))
        transparent = (self.width-2) - solid
        formatted_bar = f'{self.fill*solid}{self.empty*transparent}'
        percent = self.current/self.total * 100
        eta = 'N/A'
        if time.time()-self.start_time >= 0.1 and self.current > 0:
            speed = self.current/(time.time()-self.start_time)
            eta = (self.total-self.current)/speed
        progress = f'{percent:6.2f}% ({self.current}/{self.total}) ETA {eta:.3}s'
        output = f'[{formatted_bar}] {progress}'

        last_length = len(self.last_out)
        self.last_out = output
        output = output.ljust(last_length)
        print("\r"+output, end="", flush=True)
    def log(self,message):
        message = message.ljust(len(self.last_out))
        print("\r"+message, end="", flush=True)
        print()
        self.update_display()
    



if __name__ == '__main__':
    import time
    import random
    bar = ProgressBar(37)
    for i in range(1,38):
        bar.tick()
        bar.log(f'Step {i}')

        time.sleep(0.1 + (random.random()/2)+((1+random.random())**2)/4)
