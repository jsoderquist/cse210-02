from simulation.simulating.simulator import Simulator

def main():
    simulator = Simulator()
    simulator.start_simulation()

if __name__ == "__main__":
    main()

'''
from numpy import cos, sin, arcsin, arange
#variables
n_air = 1.00029
n_aluminum = 1.37289+7.617691j
n_silicon = 3.88163+0.01896923j

#Fresnel equations
theta_1 = arange(0,5,0.001)
theta_2 = arcsin(n_air*sin(theta_1)/n_aluminum)
theta_3 = arcsin(n_aluminum*sin(theta_2)/n_silicon)

#first boundary reflection
r_s_1 = (n_air*cos(theta_1) - n_aluminum*cos(theta_2))/(n_air*cos(theta_1) + n_aluminum*cos(theta_2))
r_p_1 = (n_air*cos(theta_2) - n_aluminum*cos(theta_1))/(n_air*cos(theta_2) + n_aluminum*cos(theta_1))
r_1 = (r_s_1 + r_p_1)/2

#second boundary reflection
r_s_1 = (n_air*cos(theta_1) - n_aluminum*cos(theta_2))/(n_air*cos(theta_1) + n_aluminum*cos(theta_2))
r_p_1 = (n_air*cos(theta_2) - n_aluminum*cos(theta_1))/(n_air*cos(theta_2) + n_aluminum*cos(theta_1))
r_1 = (r_s_1 + r_p_1)/2

#first boundary transmission of reflection


#phase shift


#add together
'''
