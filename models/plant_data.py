from models.plant import PlantModel
from models.season import SeasonModel
from models.pollinator import PollinatorModel
from models.comment import CommentModel



# Added a seasons_list, which I have added all seasons to for the seeding

# seasons_list = [
#     SeasonModel(season="Summer"),
#     SeasonModel(season="Spring"),
#     SeasonModel(season="Winter"),
#     SeasonModel(season="Autumn")
# ]
summer_season = SeasonModel(season="Summer")
spring_season = SeasonModel(season="Spring")
winter_season = SeasonModel(season="Winter")
autumn_season = SeasonModel(season="Autumn")

bee = PollinatorModel(type="Bee")
hummingbird = PollinatorModel(type="Hummingbird")
bat = PollinatorModel(type="Bat")
butterfly = PollinatorModel(type="Butterfly")
ant = PollinatorModel(type="Ant")
wasp = PollinatorModel(type="Wasp")
moth = PollinatorModel(type="Moth")
hoverfly = PollinatorModel(type="Hoverfly")
mosquito = PollinatorModel(type="Mosquito")
bird = PollinatorModel(type="Bird")
fly = PollinatorModel(type="Fly")
beetle = PollinatorModel(type="Beetle")
other = PollinatorModel(type="Other")


plants_list = [
    PlantModel(name="Lavender", latinName="Lavandula", description="Bees, hoverflies and wasps will certainly thank you for planting these beautiful, perennial plants for pollinators and you will be rewarded with beautiful flowers and a garden alive with buzzing, fluttering insects", seasons=[summer_season], pollinators=[bee, wasp, hoverfly], image="https://res.cloudinary.com/dlxbte5xh/image/upload/v1654981600/pexels-pixabay-164470_rosbbz.jpg", user_id=1),
    PlantModel(name="Honeysuckle", latinName="Caprifoliaceae", description="A vigorous climber. Long, tubular flowers rich in sweet-scented nectar are visited by long-tongued bees like the Garden bumblebee and Carder bumblebee during the day, and moths at night.", seasons=[autumn_season], pollinators=[bee, moth], image="https://res.cloudinary.com/dlxbte5xh/image/upload/v1654977566/pexels-daka-12307150_tehhql.jpg", user_id=1),
    PlantModel(name="Mahonia", latinName="Berberidaceae", description="A hardy evergreen shrub. The nectar-rich bright yellow flowers help support overwintering bumblebees and honeybees.", seasons=[autumn_season], pollinators=[bee], image="https://res.cloudinary.com/dlxbte5xh/image/upload/v1654980047/pexels-micah-4946373_amyfat.jpg", user_id=1),
    PlantModel(name="Hawthorn", latinName="Crataegus Monogyna", description="Spiky branches make for a secure hedging plant. Bunches of open white May blossom are important for solitary bees such as the Red mason bee, Tawny mining bee, Ashy mining bee and the specialist Hawthorn mining bee. Birds also enjoy the fruits.", seasons=[autumn_season], pollinators=[bee, bird], image="https://res.cloudinary.com/dlxbte5xh/image/upload/v1654980287/pexels-ellie-burgin-4297568_mr8rl7.jpg", user_id=1),
    PlantModel(name="Crabapple", latinName="Malus Sylvestris", description="Bees are major pollinators of these trees, especially the Red mason bee. The attractive white or pink blossom hums with a variety of species, helping to produce tasty fruit for us.", seasons=[autumn_season], pollinators=[bee], image="https://res.cloudinary.com/dlxbte5xh/image/upload/v1654980400/pexels-eva-elijas-5500830_fr2zkk.jpg", user_id=1),
    PlantModel(name="Milkweed", latinName="Asclepias", description="Growing Milkweed plants will attract many pollinators and butterflies to your yard, and in particular the beautiful and colourful Monarch butterfly. Growing milkweed is easy and can have many benefits for the garden. Learn how to grow milkweed plants, and bring beneficial insects and beautiful butterflies into your pollinator garden.", seasons=[autumn_season], pollinators=[butterfly], image="https://res.cloudinary.com/dlxbte5xh/image/upload/v1654980997/pexels-hanna-tomany-8048054_sjtzhv.jpg", user_id=1),
    PlantModel(name="Coneflower", latinName="Echinacea", description="Coneflower, or echinacea, are a beautiful and popular wildflower native to central and eastern US. They are also loved by bees and butterflies, creating another dimension to their flowering display.", seasons=[autumn_season], pollinators=[butterfly, bee], image="https://res.cloudinary.com/dlxbte5xh/image/upload/v1654982437/pexels-rami-tayyem-3759375_cyqzim.jpg", user_id=1),
    PlantModel(name="Dandelion", latinName="Taraxacum", description="Dandelions are one of the easiest, hardiest plants that offer a surefire way to attract beneficial insects to your garden. Rather than getting rid of these bright yellow delights, we should be doing everything in our power to encourage them to grow!", seasons=[autumn_season], pollinators=[butterfly, bee, beetle], image="https://res.cloudinary.com/dlxbte5xh/image/upload/v1654989827/pexels-erik-mclean-4582572_b6t7jh.jpg", user_id=1),
    PlantModel(name="Snapdragon", latinName="Antirrhinum Majus", description="The snapdragon is the ultimate bumblebee attractor. It has evolved unique ways to attract these pollinators, adapting its scent, color, and physical form to perfectly suit all of the bumblebees needs", seasons=[autumn_season], pollinators=[bee, butterfly], image="https://res.cloudinary.com/dlxbte5xh/image/upload/v1654990026/pexels-faris-hamza-10629502_lnvrf1.jpg", user_id=1),
    PlantModel(name="Calendula", latinName="Calendula Officinalis", description="Shorter, bushy plants full of orange/yellow, daisy-like flowers that provide both pollen and nectar for pollinators. Note that calendula comes in colors other than the classic orange, like gorgeous Strawberry Blonde flowers", seasons=[autumn_season], pollinators=[butterfly, bee], image="https://res.cloudinary.com/dlxbte5xh/image/upload/v1659194406/pexels-pixabay-65255_y0wcka.jpg", user_id=1),
    PlantModel(name="Marigold", latinName="Tagetes", description="Marigolds are annual flowers that range from red to orange to yellow. Like calendula, they are excellent companion plants. They repel pest insects like cabbage moths. French marigolds are also reported to deter root-knot nematodes in soil.", seasons=[autumn_season], pollinators=[butterfly, moth], image="https://res.cloudinary.com/dlxbte5xh/image/upload/v1659194606/pexels-gm-rajib-3524048_owybof.jpg", user_id=1),
    PlantModel(name="Nasturtium", latinName="Tropaeolum", description="Easy to grow, sprawling, edible, lovely nasturtium! The peppery arugula-like leaves are edible, as well as the flowers. The blooms come in a variety of colors, and provide pollen and nectar for our garden friends.", seasons=[autumn_season], pollinators=[bee, bird, moth], image="https://res.cloudinary.com/dlxbte5xh/image/upload/v1659194791/pexels-jeffry-surianto-8974474_cpr9eu.jpg", user_id=1),
    PlantModel(name="Verbena", latinName="Vervain", description="Verbena is a huge family that includes over 250 species of both annual and perennial plants. Most of them produce flowers that pollinators go wild for!", seasons=[autumn_season], pollinators=[butterfly, bird], image="https://res.cloudinary.com/dlxbte5xh/image/upload/v1659194921/pexels-erik-karits-9181492_bgot4x.jpg", user_id=1),
    PlantModel(name="Pincushion", latinName="Scabiosa", description="ound, frilly, tufted flowers that appear in lavender, blues, pink and white. Most varieties are fairly short, averaging around a foot tall. Because they are compact, these cute plants for pollinators are well-suited for containers and borders.", seasons=[autumn_season], pollinators=[butterfly, bee], image="https://res.cloudinary.com/dlxbte5xh/image/upload/v1659195081/pexels-clayton-5732792_f3b7bi.jpg", user_id=1),
    PlantModel(name="Hibiscus", latinName="Malvaceae", description="Hibiscus flowers are loved by hummingbirds. Even though they attract other pollinators like butterflies, the exposed stamen allows for easy nectar collection.", seasons=[summer_season, autumn_season], pollinators=[butterfly, bee, hummingbird], image="https://res.cloudinary.com/dlxbte5xh/image/upload/v1659634327/pexels-philippe-donn-1133957_a5ngzd.jpg", user_id=1),
    PlantModel(name="Dahlia", latinName="Asteraceae", description="Dahlias are very good for bees because as they are a good source of pollen and they attract a lot of bees. This is why most people will advise that you locate your beehives very close to dahlia flowers", seasons=[summer_season, autumn_season], pollinators=[bee, hummingbird, beetle, bat, ant], image="https://res.cloudinary.com/dlxbte5xh/image/upload/v1659881040/pexels-amber-shadow-8585187_dg1iqr.jpg", user_id=1),
    PlantModel(name="Cherry Blossom", latinName="Prunus Cerasus", description="During the warm, summer months apple and cherry blossom trees are a fantastic choice for attracting bees. The majority of varieties perform well during the hotter weather and will keep bees interested during the earlier part of the growing season. Cherry blossom trees, in particular, make for a brilliant addition as they are usually quite large with lots of flower buds, attracting a large number of bees.", seasons=[spring_season, summer_season], pollinators=[bee, hummingbird, beetle, bat, bird], image="https://res.cloudinary.com/dlxbte5xh/image/upload/v1660167090/pexels-lukas-379926_wbofmp.jpg", user_id=2),
    PlantModel(name="Basil", latinName="Ocimum Basilicum", description="Basil is a tender annual that thrives outdoors in spring and summer, where the blooms will draw bees and other important pollinators. At night, basil attracts moths due to its scent", seasons=[spring_season, summer_season], pollinators=[bee, hummingbird, moth], image="https://res.cloudinary.com/dlxbte5xh/image/upload/v1660168900/pexels-abhishek-gaurav-1537265_dyxqfh.jpg", user_id=2),
    PlantModel(name="Borage", latinName="Boraginaceae", description="Borage is a hardy annual edible that is known for its beauty. It’s a domestic herbal remedy that has been used since ancient times. Some people use borage as a substitute for valerian as it dispels melancholy and induces euphoria. Both honeybees and bumblebees rub up to its rich nectar, as well as butterflies. It blooms from spring to autumn, which means pollinators have a long season of borage nectar each year", seasons=[spring_season, summer_season, autumn_season], pollinators=[bee, hummingbird, moth, butterfly], image="https://res.cloudinary.com/dlxbte5xh/image/upload/v1660168967/pexels-julz-5585748_u7gqol.jpg", user_id=2),
]

comments_list = [
    CommentModel(content="Beautiful flower that has attracted so many pollinators!", plant_id=1, user_id=1),
    CommentModel(content="Seen sooooo many butterflies on this plant in my garden!", plant_id=14, user_id=2)
    ]

