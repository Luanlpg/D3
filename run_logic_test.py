LIST_BIN = [
            [1,1,1,1],
            [0,1,1,0],
            [0,1,0,1],
            [0,1,9,1],
            [1,1,1,1]
            ]

class ElementCrawler():

    def __init__(self, list_bin):
        self.list_bin = list_bin
        self.element_line = None
        self._continue = True
        self.len = len(list_bin)
        self.response = []

    def find_element_line(self):
        """=====================================================================
        Método que retorna linha que se encontra elemento a ser encontrado.
        ====================================================================="""
        for i in range(self.len):
            if 9 in self.list_bin[i]:
                return i

    def set_line(self, line):
        """=====================================================================
        Método que mostra caminho na matriz e cria lista algoritimo necessário.
        ====================================================================="""
        continue_line = True

        for i in range(len(self.list_bin[line])):

            conditions = [  # condição para descer
                            all([
                                line != self.element_line,
                                self.list_bin[line][i] == 1,
                                self.list_bin[line + 1][i] == 1,
                                continue_line
                                ]),
                            # condição para virar a direita
                            all([
                                line != self.element_line,
                                self.list_bin[line][i] == 1,
                                self.list_bin[line + 1][i] != 1,
                                continue_line
                                ]),
                            # condição para virar a direita na linha do destino
                            all([
                                line == self.element_line,
                                self.list_bin[line][i] == 1,
                                continue_line
                                ]),
                            # condição de chegada
                            all([
                                line == self.element_line,
                                self.list_bin[line][i] == 9,
                                continue_line
                                ])
                        ]

            if conditions[0]:
                self.list_bin[line][i] = 'v'
                self.response.append('v')
                continue_line = False

            elif conditions[1]:
                self.list_bin[line][i] = '>'
                self.response.append('>')

            elif conditions[2]:
                self.list_bin[line][i] = '>'
                self.response.append('>')

            elif conditions[3]:
                self.response.append('x')
                self._continue = False
                continue_line = False


    def start(self):
        """=====================================================================
        Método que seta e mostra cada linha da matriz e enfim retorna algoritmo.
        ====================================================================="""
        self.element_line = self.find_element_line()
        for line in range(self.len):
            if self._continue:
                self.set_line(line)
            print(self.list_bin[line])
        return self.response


x = ElementCrawler(LIST_BIN)
print('Algoritimo para chegar até o elemento: ', x.start())
