import json
import arbol.nodo as nodo

class Arbol():
    """ Arbol class """

    def __init__(self):
        # inicializa la raiz
        self.raiz = None
 
    def agregarNodo(self, dato):
        return nodo.Nodo(dato)

    def existeDato(self, raiz, dato): 
        if raiz:
            if raiz.dato == dato:
                return True
            elif raiz.izq:
                v_temp = self.existeDato(raiz.izq, dato)
                if not v_temp and raiz.der:
                    v_temp = self.existeDato(raiz.der, dato)
                return v_temp
        return False

    def insertar(self, raiz, dato):
        # inserta un dato nuevo en el árbol
        if raiz == None:
            # si no hay nodos en el árbol lo agrega
            v_nuevo_nodo = self.agregarNodo(dato)
            return v_nuevo_nodo
        elif not self.existeDato(raiz, dato):
            # si hay nodos en el árbol lo recorre
            if dato < raiz.dato:
                # si el dato ingresado es  menor que el dato guardado va al subárbol izquierdo
                raiz.izq = self.insertar(raiz.izq, dato)
            else:
                # si no, procesa el subárbol derecho
                raiz.der = self.insertar(raiz.der, dato)
        return raiz

    def get_path(self, num, raiz):

        if raiz:

            if raiz.tiene_hijo(num) or raiz.dato == num:
                v_result = []
                if raiz.dato != num:
                    v_result.append(raiz.dato)                
                return v_result
            if self.existeDato(raiz.izq, num):
                v_result = self.get_path(num, raiz.izq)
                v_result.append(raiz.dato)
                return v_result

            elif self.existeDato(raiz.der, num):
                v_result = self.get_path(num, raiz.der)
                v_result.append(raiz.dato)
                return v_result
            else:
                return None

        return None

    def get_ancestor(self, num_1, num_2):
        v_path_1 = self.get_path(num_1, self.raiz)
        v_path_2 = self.get_path(num_2, self.raiz)

        v_result = {}
        v_result["ancestor"] = "No tiene"

        if v_path_1:
            v_path_1.reverse()
        
        if v_path_2:
            v_path_2.reverse()

        if v_path_1 and v_path_2 and len(v_path_1) > 0 and len(v_path_2) > 0:
            if v_path_1 == v_path_2:
                v_result["ancestor"] = v_path_1[len(v_path_1) - 1]
            else:
                i = 0
                if len(v_path_1) < len(v_path_2):
                    v_limit = len(v_path_1)
                else:
                    v_limit = len(v_path_2)

                while ( i < v_limit ):
                    if v_path_1[i] == v_path_2[i]:    
                        v_result["ancestor"] = v_path_1[i]
                    else:
                        break
                    i = i + 1

        return v_result


    def __str__(self) -> str:
        return str(self.raiz)

    def to_dict(self) -> dict:
        if self.raiz:
            return self.raiz.to_dict()
        else:
            return {}