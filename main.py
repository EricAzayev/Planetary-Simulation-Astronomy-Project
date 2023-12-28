Web VPython 3.2

MMoon = 7.342e22
MEarth = 5.972e24

earth = sphere(radius=6.356e6)
earth.texture = textures.earth

moon = sphere(radius=1.737e6, pos=vec(3.844e7, 0, 0))
moon.texture = {'file': "http://i.imgur.com/YPg4RPU.jpg"}

time = 0.0  # this is the starting time
dt = 0.01  # this is the time between each frame of animation
timelapse = 100
lapse = dt * timelapse
speedEarth = 0  # this is the speed of the object in meters per second
speedMoon = 10000
accEarth = 0
accMoon = 0


def getRadius(obj1, obj2):
    distance = sqrt((obj1.pos.x - obj2.pos.x) ** 2 + (obj1.pos.y - obj2.pos.y) ** 2 + (obj1.pos.z - obj2.pos.z) ** 2)
    return distance


def TwoBodyForce(obj1, obj2, Mass1, Mass2):  # The gravitational formula outputs the force subjected on both objects.
    F = 6.67e-11 * (Mass1 * Mass2) / (getRadius(obj1, obj2) ** 2)
    return F


def CenterOfGravity(obj1, obj2, Mass1, Mass2):
    divBy = Mass1 + Mass2  # Time Optimization, sacrifice Memory
    xcog = (obj1.pos.x * Mass1 + obj2.pos.x + Mass2) / (divBy)
    ycog = (obj1.pos.y * Mass1 + obj2.pos.y + Mass2) / (divBy)
    zcog = (obj1.pos.z * Mass1 + obj2.pos.z + Mass2) / (divBy)
    COG = sphere(radius=1e5, color=vec(1, 0, 0)), pos = vec(xcog, ycog, zcog)
    return COG


def checkForCollision(obj1, cog):
    if (obj1.pos.x = cog.pos.x and obj1.pos.y = cog.pos.y and obj.pos.z = cog.pos.z):
        return True
    else:
        return False


print(EarthAndMoonForce())
COGEarthMoon = CenterOfGravity(earth, moon, MEarth, MMoon)
y = input("Ready? - ")
while (True):
    rate(1 / dt)
    moon.pos.x -= speedMoon * lapse
    speedMoon += accMoon * lapse
    print(speedMoon)
    accMoon = (EarthAndMoonForce() / MMoon)
    # print(accMoon)
    earth.pos.x += speedEarth * dt
    speedEarth += accEarth * dt
    accEarth = EarthAndMoonForce() / MMoon

    time = time + dt
