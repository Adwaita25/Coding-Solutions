class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        
        kelvin = 273.15 + celsius
        fahrenheit = celsius * (9/5) + 32
        
        return [kelvin, fahrenheit]
