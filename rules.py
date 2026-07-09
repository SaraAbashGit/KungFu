import json
class Rules:

    def __init__(self):
        with open("rules.json") as file:
            self.rules = json.load(file)


    def get_rule(self, piece_type):
        return self.rules.get(piece_type)
    
# if __name__ == "__main__":
#     rules = Rules()
#     print(rules.get_rule("K"))