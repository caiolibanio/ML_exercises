
from numpy import *
import sys

def step_gradient(b_current, m_current, points, learningRate):
	b_gradient = 0
	m_gradient = 0
	N = float(len(points))
	for i in range(0, len(points)):
		x = points[i, 0]
		y = points[i, 1]
		b_gradient += -(2/N) * (y - ((m_current * x) + b_current))
		m_gradient += -(2/N) * x * (y - ((m_current * x) + b_current))
	new_b = b_current - (learningRate * b_gradient)
	new_m = m_current - (learningRate * m_gradient)
	return [new_b, new_m]


def compute_error_for_given_line(b, m, points):
	totalError = 0
	for i in range(0, len(points)):
		x = points[i, 0]
		y = points[i, 1]
		totalError += (y - (m * x + b)) ** 2
	return totalError / float(len(points))  

def gradient_descent(points, starting_b, starting_m, learning_rate, num_iterations, target_error):
	b = starting_b
	m = starting_m
	actual_error = sys.maxint
	num_count = 0
	#for i in range(num_iterations): #Condicao de parada original
	while actual_error > target_error: #Nova condicao de parada - questao 5.
		b, m = step_gradient(b, m, array(points), learning_rate)
		actual_error = compute_error_for_given_line(b, m, points)
		print 'Actual RSS is: ', actual_error
		num_count += 1
	return [b, m]
	
#y = mx + b
def run():
	points = genfromtxt('income.csv', delimiter=',')
	learning_rate = 0.001
	initial_b = 0 
	initial_m = 0
	num_iterations = 100000
	target_error = 29.9
	
	print "Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m, compute_error_for_given_line(initial_b, initial_m, points))
	print "Running..."
	[b, m] = gradient_descent(points, initial_b, initial_m, learning_rate, num_iterations, target_error)
	print "After {0} iterations b = {1}, m = {2}, error = {3}".format(num_iterations, b, m, compute_error_for_given_line(b, m, points))
	

if __name__ == '__main__':
    run()
    
"""RESPOSTAS AQUI
1 - DONE in line 42

2 - DONE in line 36

3 - O RSS diminui ao longo das iteracoes porque os coeficientes da reta estao, a cada iteracao, convergindo para
 uma inclinacao otima a representar os dados do conjunto. Quanto maior o tamanho dos passos (learning rate), 
 mais rapida se deu a convergencia.
 
4 - R: Learning rate: 0.001    Iterations: 100000

5 - Na linha 33, foi substituida a condicao de parada origial (numero de iteracoes) por um valor de erro desejado (target_error). Com isso, 
 a execucao sera interrompida quando esse limiar for atingido.
 
6 - Com a nova condicao de parada, o valor de tolerancia utilizado, para aproximar os resultados aos encontrados na questao 4, 
 foi de *target_error = 29.9*. Os valores para os coeficientes foram: b = -38.2249321767 e m = 5.5267799212.
 
7 - 
"""
