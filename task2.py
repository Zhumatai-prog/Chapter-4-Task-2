class Airplane():
	def __init__(self, mark, model, year, max_speed):
		self.mark = mark
		self.model = model
		self.year = year
		self.max_speed = max_speed
		self.odometer = 0
		self.is_flying = False

	def take_off(self):
		self.is_flying = True

	def land(self):
		self.is_flying = False

	def fly(self):
		self.odometer += 5

	def result(self):
		return f"{self.mark} {self.model} {self.year} year is flying {self.odometer} km {self.is_flying} -- max speed {self.max_speed}"

trip = Airplane(
	'Boing', '747', '2010', '1200 kmph')
trip.take_off()
trip.fly()
trip.fly()
trip.fly()
trip.fly()
trip.fly()
trip.fly()

print(trip.result())
