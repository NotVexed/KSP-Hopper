from typing import List

class PhysicsBody():
    def __init__(self, mass):
        self.mass = mass
    
self.weight = mass * g

self.init_altitude     = 0
self.init_velocity     = 0
self.init_acceleration = 0
self.altitudes = []
self.velocities = []
self.accelerations = []
self.forces = []

def simulate(altitude, velocity, acceleration):
    return 0

def linear_func(max_value):
    return lambda value: value * max_value

class RocketBody(PhysicsBody):
    def __init__(self, mass, control_func, max_thrust, throttle_response_func = None, mdot_func = None, mdot = 0)
        PhysicsBody.__init__(mass)

        self.control_func = control_func
        self.mdot = mdot

        if !throttle_response_func:
            self.throttle_response_func = linear_func(max_thrust) 
        else:
            self.throttle_response_func = throttle_response_func

        if !mdot_func:
            self.mdot_func = linear_func(mdot) 
        else:
            self.mdot_func = mdot_func

    def simulate(altitude, velocity, acceleration):
        throttle = self.control_func(altitude, velocity, acceleration)

        self.mass -= mdot_func(throttle)

        return self.throttle_response_func(throttle)

class PhysicsSimulation():
    def __init__(self, body: PhysicsBody, dt: float, end_time: float):
        self.body = body
        self.dt = dt
    
        self.time = np.arange(0, end_time, dt)
        self.ground_hit = False

    def simulate(self) -> PhysicsBody:
        for t in time:
            altitudes = self.body.altitudes
            velocities = self.body.velocities
            accelerations = self.body.accelerations
            forces = self.body.forces

        altitude = self.body.altitudes[-1]
        velocity = self.body.velocities[-1]
        acceleration = self.body.accelerations[-1]

       external_force = self.body.simulate(altitude, velocity, acceleration)
       force = external_force - self.body.weight

       forces.append(force)

       accelerations.append(force / mass)

       # Ground detection
       if altitude <= altitudes[0] and velocity < 0:
         ground_hit = True

         altitudes.extend(np.full(len(time) - len(altitudes), array[0]))
         velocities.extend(np.full(len(time) - len(velocities), 0))
         accelerations.extend(np.full(len(time) - len(accelerations), 0))
         forces.extend(np.full(len(time) - len(forces), 0))

         break
       else:
         velocities.append(velocity + acceleration * dt)

       altitudes.append(altitude + velocity * dt + 0.5 * acceleration * dt**2)