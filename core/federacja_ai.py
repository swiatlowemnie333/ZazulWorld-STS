import psutil

class RadaNajwyzsza:
    def __init__(self):
        self.departamenty = {
            "Departament Innowacji": ["Agent1", "Agent2", "Agent3"],
            "Departament Bezpieczenstwa": ["Agent4", "Agent5"],
            "Departament Operacyjny": ["Agent6", "Agent7", "Agent8"]
        }
    
    def licz_agentow(self):
        total = 0
        for dept, agenci in self.departamenty.items():
            total += len(agenci)
        return total
    
    def gotowosc_na_skalowanie(self):
        # Przykładowa implementacja
        return 85
