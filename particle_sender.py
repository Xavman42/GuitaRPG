from Particle import Particle

Particle.message = "test message"
Particle.area = "A"
Particle.region = "A"

my_particle = Particle("placeholder", "A", "A")
print(my_particle.message)
my_particle.message = "test message"
print(my_particle.message)
my_particle.send_particle()