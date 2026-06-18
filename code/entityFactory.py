class EntityFactory:
    
    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):         
        if entity_name == "player":
            return Player(window, position)
        elif entity_name == "ball":
            return Ball(window, position)
        elif entity_name == "brick":
            return Brick(window, position)
        else:
            raise ValueError(f"Unknown entity type: {entity_name}")
    
    def __init__(self):
        pass