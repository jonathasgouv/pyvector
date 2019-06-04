# pyvector

PT-BR
O objetivo desse módulo é criar um modo de lidar com vetores que seja o mais próximo possível de função built-in, quase como se o vetor se torna-se um novo tipo de variável dentro do Python. Eu busquei adicionar todas as operações com vetores existentes, todas as propriedades possíveis. Caso eu tenha esquecido algo por favor me avise e eu tentarei implementar.

Optei por não implementar a função de plot visto que é possível plotar facilmente utilizando a biblioteca matplotlin, tendo os parâmetros self.x e self.y como entrada. Caso vocês vejam utilidade e necessidade a função pode ser implementada em versões seguintes.

Observe que todos os métodos funcionam utilizando vetores representados com coordenadas, portanto se você tem um vetor representado como módulo e ângulo utilize primeiro o método estático Vector.decompose(), e só então use o vetor resultante com as demações funções. É possível retornar ao estado original utilizando o método self.compose, que retornará uma lista contendo o módulo e o ângulo original.

EN-US
The purpose of this module is to create a way of dealing with vectors that is as close to the built-in function as possible, almost as if the vector becomes a new type of variable within Python. I've tried adding all operations with existing vectors, all possible properties. If I have forgotten something please let me know and I will try to implement.

I chose not to implement the plot function since it is possible to easily plot using the matplotlin library, taking the parameters self.x and self.y as input. If you see utility and necessity the function can be implemented in subsequent versions.

Note that all methods work by using vectors represented with coordinates, so if you have a vector
represented as a module and angle, first use the static method Vector.decompose (), and then use the resultant vector with the functions. It is possible to return to the original state using the self.compose method, which will return a list containing the original module and angle.
