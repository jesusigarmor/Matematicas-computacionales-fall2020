# Escribe aquí la clase GA
import numpy as np
from Cromosoma import BitCromosoma
import random


class GA:
    def __init__(
            self, tamaño_poblacion, tasa_mutacion,
            tasa_crossover, max_generaciones, fitness,
            num_elites
    ):
        self.tamaño_poblacion = tamaño_poblacion
        self.tasa_mutacion = tasa_mutacion
        self.tasa_crossover = tasa_crossover
        self.max_generaciones = max_generaciones
        self.fitness = fitness
        self.poblacion = []
        self.generacion = 0
        self.mejor_solucion_historica = ''
        self.mejor_solucion_actual = ''
        self.num_elites = num_elites

    def run(self):
        fitness_arr = []
        self.poblacion.sort(reverse=True, key=self.fitness)
        # Evaluación del fitness de toda la poblacion
        for i in self.poblacion:
            fitness_arr.append(self.fitness(i))
        # Encontramos la mejor solución de la generación.
        self.mejor_solucion_actual = \
            self.poblacion[fitness_arr.index(max(fitness_arr))]
        # Comparamos con la mejor solución que hemos encontrado y actualizamos.
        if self.fitness(self.mejor_solucion_historica) < max(fitness_arr):
            self.mejor_solucion_historica = self.mejor_solucion_actual
        # Hacemos la siguiente generación de los genes
        self.poblacion = self.crear_poblacion(fitness_arr)
        # Evaluamos condición de paro
        if self.condicion():
            return self.mejor_solucion_actual
        else:
            return False

    def crear_poblacion(self, fitness_arr):
        
        pass

    def crossover(self, i, j):
        crossover_point = random.randint(0, i.length)
        pass

    def seleccionar(self, fitness_arr):
        new_gen = self.poblacion[1:self.num_elites]
        fitness_poblacion = sum(fitness_arr)
        for i in range(len(self.poblacion) - self.num_elites):
            num_azar = np.random.uniform(low=0, high=fitness_poblacion)
            suma_fitness = 0
            for j in self.poblacion:
                suma_fitness += self.fitness(j)
                if suma_fitness > num_azar:
                    new_gen.append(j)
        return new_gen

    def plot():
        pass

    def fitness():
        pass

    def poblar(self):
        for i in range(0, self.tamaño_poblacion):
            self.poblacion.append(BitCromosoma())

    def __str__(self):
        return ("Población Actual" + self.poblacion +
                "\nMejor Solución Histórica" +
                str(self.mejor_solucion_ghistorica) +
                "\nMejor Solución de la Generación" +
                str(self.mejor_solucion_actual) +
                "\nNúmero de generación" + str(self.generacion))


    # def seleccionar(self):
    # #self.poblacion.sort(reverse=True, key=self.fitness)
    # fitness_poblacion = sum(self.fitness_arr)
    # num_azar = np.random.uniform(low=0, high=fitness_poblacion)
    # suma_fitness = 0
    # for i in self.poblacion:
    #     suma_fitness += self.fitness(i)
    #     if suma_fitness > num_azar:
    #         return i
