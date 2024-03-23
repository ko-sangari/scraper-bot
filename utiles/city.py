from pydantic import BaseModel


class City(BaseModel):
    id: int
    name: str


AVAILABLE_CITY = [
    City(id=24, name="Amsterdam"),
    City(id=320, name="Arnhem"),
    City(id=619, name="Capelle aan den IJssel"),
    City(id=26, name="Delft"),
    City(id=28, name="Den Bosch"),
    City(id=90, name="Den Haag"),
    City(id=110, name="Diemen"),
    City(id=620, name="Dordrecht"),
    City(id=29, name="Eindhoven"),
    City(id=545, name="Groningen"),
    City(id=616, name="Haarlem"),
    City(id=6099, name="Helmond"),
    City(id=6209, name="Maarssen"),
    City(id=6090, name="Maastricht"),
    City(id=6051, name="Nieuwegein"),
    City(id=6217, name="Nijmegen"),
    City(id=25, name="Rotterdam"),
    City(id=6224, name="Rijswijk"),
    City(id=6211, name="Sittard"),
    City(id=6093, name="Tilburg"),
    City(id=27, name="Utrecht"),
    City(id=6127, name="Waalre"),
    City(id=6098, name="Waddinxveen"),
    City(id=6145, name="Zeist"),
    City(id=6088, name="Zoetermeer"),
]
