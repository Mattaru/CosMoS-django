import random

from app.models import Product, Ingredient
from .handlers import get_ingredients_names_list_from_string


INGREDIENTS = 'Water, Glycerin, Dipropylene Glycol, Triethylhexanoin, Lactobacillus/Soybean Ferment Extract,' \
       ' Squalane, Isostearyl Isostearate, Camellia Japonica Seed Oil, 1,2-Hexanediol, Dimethicone,' \
       ' Niacinamide, Glyceryl Glucoside, Cetearyl Alcohol, Hydrogenated Olive Oil,' \
       ' Saccharomyces/Barley Seed Ferment Filtrate, Saccharomyces/Potato Extract Ferment Filtrate,' \
       ' Myristica Fragrans (Nutmeg) Extract, Panthenol, Saccharomyces/Grape Ferment Extract,' \
       ' Lactobacillus/Wasabia Japonica Root Ferment Extract, Lactobacillus/Water Hyacinth Ferment,' \
       ' Lactobacillus/Ginseng Root Ferment Filtrate, Lactobacillus/Rye Flour Ferment, Monascus/Rice Ferment,' \
       ' Saccharomyces/Xylinum/Black Tea Ferment, Withania Somnifera Root Extract,' \
       ' Rosmarinus Officinalis (Rosemary) Leaf Extract, Thymus quinquecostatus var. japonica leaf extract,' \
       ' Salvia Officinalis (Sage) Leaf Extract, Lactobacillus/Pear Juice Ferment Filtrate,' \
       ' Lactobacillus/Pumpkin Ferment Extract, Glycyrrhiza Glabra (Licorice) Root Extract,' \
       ' Diospyros Kaki Fruit Extract, Actinidia Polygama Fruit Extract, Cassia Obtusifolia Seed Extract,' \
       ' Ipomoea Batatas Root Extract, Trichosanthes Kirilowii Root Extract, Lycium Chinense Fruit Extract,' \
       ' Citrus Unshiu Peel Extract, Lonicera Japonica (Honeysuckle) Flower Extract, Millet Extract,' \
       ' Glechoma Hederacea Extract, Platycodon Grandiflorum Root Extract, Acer Palmatum Leaf Extract,' \
       ' Daucus Carota Sativa (Carrot) Root Extract, Codonopsis Lanceolata Root Extract,' \
              ' Camellia Japonica Leaf Extract,' \
       ' Rubus Idaeus (Raspberry) Fruit Extract, Melissa Officinalis Extract,' \
       ' Lippia Citriodora Leaf Extract, Allium Sativum (Garlic) Bulb Extract, Portulaca Oleracea Extract,' \
       ' Chaenomeles Sinensis Fruit Extract, Daikon Extract, Ficus Carica (Fig) Fruit Extract,' \
       ' Musa Sapientum (Banana) Fruit Extract, Ocimum Basilicum (Basil) Leaf Extract, ' \
       'Citrus Aurantium Bergamia (Bergamot) Leaf Extract, Centella Asiatica Extract,' \
       ' Prunus Persica (Peach) Fruit Extract, Beta Vulgaris (Beet) Root Extract, Eriobotrya Japonica Leaf Extract,' \
       ' Apple Extract, Morus Bombycis Leaf Extract, Prunus Armeniaca (Apricot) Fruit Extract,' \
       ' Centella Asiatica Extract [repeated], Prunus Persica (Peach) Fruit Extract [repeated],' \
       ' Beta Vulgaris (Beet) Root Extract [repeated], Eriobotrya Japonica Leaf Extract [repeated],' \
       ' Apple Extract [repeated], Morus Bombycis Leaf Extract [repeated],' \
       ' Prunus Armeniaca (Apricot) Fruit Extract [repeated], Zingiber Officinale (Ginger) Root Extract,' \
       ' Taraxacum Officinale (Dandelion) Leaf Extract, Equisetum Arvense Extract,' \
       ' Citrullus Lanatus (Watermelon) Fruit Extract, Brassica Rapa (Turnip) Leaf Extract,' \
       ' Spinacia Oleracea (Spinach) Leaf Extract, Artemisia Princeps Leaf Extract,' \
       ' Brassica Oleracea Capitata (Cabbage) Leaf Extract, Allium Cepa (Onion) Bulb Extract,' \
       ' Houttuynia cordata extract, Sasa Veitchii Leaf Extract,' \
       ' Nelumbo Nucifera Root Extract, Cucumis Sativus (Cucumber) Fruit Extract, Plantago Major Seed Extract,' \
       ' Hemerocallis Fulva Flower Extract, Citrus Junos Fruit Extract, Akebia Quinata Extract,' \
       ' Ginkgo Biloba Nut Extract, Crataegus Cuneata Fruit Extract, Grifola Frondosa Fruiting Body Extract,' \
       ' Prunus Salicina Fruit Extract, Perilla Frutescens Leaf Extract, Geranium Robertianum Extract,' \
       ' Anemarrhena Asphodeloides Root Extract, Rehmannia Chinensis Root Extract,' \
       ' Sesamum Indicum (Sesame) Seed Extract, Undaria Pinnatifida Extract, Acorus Calamus Root Extract,' \
       ' Cichorium Intybus (Chicory) Root Extract, Anthemis Nobilis Flower Extract,' \
       ' Carica Papaya (Papaya) Fruit Extract, Phaseolus Angularis Seed Extract,' \
       ' Mentha Piperita (Peppermint) Flower/Leaf/Stem Extract, Corthellus Shiitake (Mushroom) Extract,' \
       ' Helianthus Annuus (Sunflower) Seed Extract, Schizonepeta Tenuifolia Extract, Cucurbita Pepo (Pumpkin) Powder,' \
       ' Carthamus Tinctorius (Safflower) Flower Extract, Populus Nigra Bark/Bud/Leaf/Twig Extract,' \
       ' Lavandula Angustifolia (Lavender) Flower Extract, Rosa Canina Fruit Extract, Vinegar, Wine Extract,' \
       ' Honey Extract, Saccharomyces Ferment Filtrate, Curcuma Longa (Turmeric) Root Extract,' \
       ' Butyrospermum Parkii (Shea) Butter, C14-22 Alcohols, Phytosqualane, Glyceryl Stearate,' \
       ' Polymethylsilsesquioxane, Methyl Hydrogenated Rosinate, Stearic Acid, PEG-100 Stearate,' \
       ' Hydrogenated Lecithin, Polysilicone-11, Glycosphingolipids, Ceramide 3, Arachidyl Glucoside, Butylene Glycol,' \
       ' Tocopherol, Phospholipids, Lecithin, Olea Europaea (Olive) Oil Unsaponifiables, Lactobacillus Ferment,' \
       ' Acrylates/C10-30 Alkyl Acrylate Crosspolymer, Hydroxyethyl Acrylate/Sodium Acryloyldimethyl Taurate Copolymer,' \
       ' Xanthan Gum, Phytosphingosine, Mica, Titanium Dioxide, Glyceryl Acrylate/Acrylic Acid Copolymer, Carbomer,' \
       ' Cholesterol, Beta-Glucan, Ferric Oxide, Olea Europaea (Olive) Fruit Oil, Macadamia Integrifolia Seed Oil,' \
       ' Trisodium EDTA, Tromethamine, Fragrance'

INGREDIENT_DESCRIPTION = 'Safe, neutral, harmful'


# def _get_random_value_from_ingredient_safety_classification() -> str:
#     """Get random value from the ingredient safety classification."""
#     value = random.choice(Ingredient.SafetyClassification.choices)
#     if value:
#         return value


def _create_ingredients(names: list[str], instance) -> None:
    """Create the ingredient with a name from the names list."""
    for name in names:
        try:
            ingredient = Ingredient.objects.get(name=name)
            instance.ingredients_list.add(ingredient)
        except Ingredient.DoesNotExist:
            ingredient = Ingredient(
                name=name,
                description=INGREDIENT_DESCRIPTION,
                safety_classification=random.choice(Ingredient.SafetyClassification.choices),
                approved=True
            )
            ingredient.save()
            instance.ingredients_list.add(ingredient)


def create_products(name: str, quantity: int) -> None:
    """Enter a product by name and how many you wont to create. Then will be created ingredients from product
    ingredients and they will be added to the product ingredients list."""
    for number in range(quantity):
        product = Product(
            brand='MISSHA',
            name=f'{name} - {number}',
            ingredients="One, two, three",
            approved=True
        )
        product.save()

