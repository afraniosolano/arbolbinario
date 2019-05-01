
class Nodo():
    izq , der, dato = None, None, 0
 
    def __init__(self, dato):
        # crea un nodo
        self.izq = None
        self.der = None
        self.dato = dato

    def __str__(self) -> str:
        v_response = {}
        v_response["izq"] = str(self.izq)
        v_response["der"] = str(self.der)
        v_response["dato"] = str(self.dato)
        return str(v_response)

    def to_dict(self) -> dict:

        v_response = {}

        if self.izq:
            v_response["izq"] = self.izq.to_dict()
        
        if self.der:
            v_response["der"] = self.der.to_dict()

        v_response["dato"] = self.dato
        return v_response

    def tiene_hijo(self, num) -> bool:
        v_res = False

        if self.izq:
            if self.izq.dato == num:
                v_res = True
        
        elif self.der:
            if self.der.dato == num:
                v_res = True

        return v_res
