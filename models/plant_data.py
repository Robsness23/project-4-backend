from models.plant import PlantModel
from models.season import SeasonModel


# Added a seasons_list, which I have added all seasons to for the seeding
summer = SeasonModel(season="Summer")
spring = SeasonModel(season="Spring")
winter = SeasonModel(season="Winter")
autumn = SeasonModel(season="Autumn")

plants_list = [
    PlantModel(name="Lavender", latinName="Lavendula", description="a lovely plant which smells great and attracts bees", seasons=[summer], image="fjgharhgpairghorijg"),
    PlantModel(name="Honeysuckle", latinName="Honeysickelle", description="a lovely plant which looks great and attract butterflies", seasons=[spring], image="dkfgjoadifjgaodfigj")
]

