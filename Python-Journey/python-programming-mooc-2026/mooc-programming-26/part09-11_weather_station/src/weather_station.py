# WRITE YOUR SOLUTION HERE:
class WeatherStation:
    def __init__(self, name:str):
        self.__name = name
        self.__observations = []

    def __str__(self):
        return f"{self.__name}, {len(self.__observations)} observations"

    # @property
    # def name(self):
    #     return self.__name

    # @name.setter
    # def name(self,name):
    #     if name != "":
    #         self._name = _name
    #     else:
    #         raise ValueError("The weather name shouldn't be empty")
    
    def add_observation(self,observation:str):
        if observation != "":
            self.__observations.append(observation)
        else:
            raise ValueError("The observation name shouldn't be empty")

    def latest_observation(self):
        if len(self.__observations) == 0:
            return f"No observations in {self.__name} yet"
        else:
            return self.__observations[-1]
    
    def number_of_observations(self):
        return len(self.__observations)