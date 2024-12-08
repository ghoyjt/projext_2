class Weather:
    def __init__(self, location, day, day_part, temperature, wind_speed, rain_probability, humidity):
        self.location = location
        self.day = day
        self.day_part = day_part
        self.temperature = temperature
        self.wind_speed = wind_speed
        self.rain_probability = rain_probability
        self.humidity = humidity
        self.messages = []
        self.validate()

    def validate(self):
        # Reset messages
        self.messages = []

        if self.temperature < 0:
            self.messages.append('Слишком низкая температура')
        elif self.temperature > 35:
            self.messages.append('Слишком высокая температура')

        if self.wind_speed > 50:
            self.messages.append('Слишком быстрый ветер')

        if self.humidity < 20:
            self.messages.append('Слишком низкая влажность воздуха')

        if self.rain_probability > 70:
            self.messages.append('С большой вероятностью будет дождь')

        if not self.messages:
            self.messages.append('Всё отлично')

    def get_message(self):
        return " | ".join(self.messages)
