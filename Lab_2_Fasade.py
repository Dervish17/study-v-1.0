class CarFacade:
    def __init__(self):
        self._engine = Engine()
        self._climate = ClimateControl()
        self._multimedia = Multimedia()
        self._headlight = Headlight()

    def engine(self, value):
        if value == 'start':
            self._engine.start()
        elif value == 'stop':
            self._engine.stop()

    def climate(self, value, intensity=None):
        if type(value) is int:
            self._climate.blowing(value)
        else:
            if value == 'on':
                self._climate.climate_on()
            elif value == 'off':
                self._climate.climate_off()
            self._climate.blowing(intensity)

    def multimedia(self, value, volume=0):
        if type(value) is int:
            self._multimedia.volume(value)
        else:
            if value == 'on':
                self._multimedia.music()
            elif value == 'off':
                self._multimedia.silence()
            self._multimedia.volume(volume)

    def light(self, value):
        if value == 'on':
            self._headlight.light()
        elif value == 'off':
            self._headlight.dark()


class Engine:
    def __init__(self):
        self.engine = False

    def start(self):
        self.engine = True
        print('Двигатель заведен')

    def stop(self):
        self.engine = False
        print('Двигатель заглушен')


class ClimateControl:
    def __init__(self):
        self.climate = False
        self.blowing_intensity = 0

    def climate_on(self):
        self.climate = True
        print('Климат включен')

    def blowing(self, intensity):
        if intensity:
            self.blowing_intensity = intensity
            print(f'Интенсивность обдува: {self.blowing_intensity}')

    def climate_off(self):
        self.climate = False
        print('Климат выключен')


class Multimedia:
    def __init__(self):
        self.multimedia = False
        self.volume_lvl = 0

    def music(self):
        self.multimedia = True
        print('Музыка включена')

    def volume(self, value):
        if value:
            self.volume_lvl = value
            print(f'Громкость на: {self.volume_lvl}')

    def silence(self):
        self.multimedia = False
        print('Музыка выключена')


class Headlight:
    def __init__(self):
        self.headlight = False

    def light(self):
        self.headlight = True
        print('Фары включены')

    def dark(self):
        self.headlight = False
        print('Фары выключены')


car = CarFacade()
car.climate('on', 30)
car.climate(40)
car.climate('off')
