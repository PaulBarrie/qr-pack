from graphene import ObjectType, Int, String, Float, Boolean

class Container(ObjectType):
    id = Int(required=True)
    type = String()
    weight_g = Float(min=0)
    max_use = Int(min=0)
    nb_use = Int(min=0, max = max_use)
    clean = Boolean()
    used = Boolean()
