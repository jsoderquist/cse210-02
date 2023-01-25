from constants import *
from simulation.scripting.action import Action


class FresnelCalculation(Action):

    def __init__(self):
        pass
        
    def execute(self, things):
        materials = things.get_objects(MATERIAL_GROUP)
        
        print(materials[0].get_index_of_refraction())
        print(materials[0].get_index_of_refraction_real_part())
        print(materials[0].get_index_of_refraction_imaginary_part())
        '''
        n_air = 1.00029
        n_1 = n_air
        theta_initial = arange(0,5,0.001)
        theta_1 = theta_initial
        i = 1
        for material in materials:
            #Fresnel equations
            n_2 = material.get_index_of_refraction()
            theta_2 = arcsin(n_1*sin(theta_1)/n_2)

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

            theta_1 = theta_2
            i += 1
            '''