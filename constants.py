#CONSTANTS AND COLORS
class Constants:
    from pygame import Rect
    from pygame.locals import USEREVENT
    WIDTH = 800
    HEIGHT = 600

    #COLORS:
    BLACK = [  0,  0,  0]
    WHITE = [255,255,255]
    BLUE =  [  0,  0,255]
    GREEN = [  0,255,  0]
    RED =   [255,  0,  0]
    PROTON_COLOR = [204,0,0]
    NEUTRON_COLOR = [204,153,0]
    ELECTRON_COLOR = [0,51,204]
    
    ELEMENT_LIST = "Hydrogen,Helium,Lithium,Beryllium,Boron,Carbon,Nitrogen,Oxygen,Fluorine,Neon,Sodium,Magnesium,Aluminum,Silicon,Phosphorus,Sulfur,Chlorine,Argon,Potassium,Calcium,Scandium,Titanium,Vanadium,Chromium,Manganese,Iron,Cobalt,Nickel,Copper,Zinc,Gallium,Germanium,Arsenic,Selenium,Bromine,Krypton,Rubidium,Strontium,Yttrium,Zirconium,Niobium,Molybdenum,Technetium,Ruthenium,Rhodium,Palladium,Silver,Cadmium,Indium,Tin,Antimony,Tellurium,Iodine,Xenon,Cesium,Barium,Lanthanum,Cerium,Praseodymium,Neodymium,Promethium,Samarium,Europium,Gadolinium,Terbium,Dysprosium,Holmium,Erbium,Thulium,Ytterbium,Lutetium,Hafnium,Tantalum,Tungsten,Rhenium,Osmium,Iridium,Platinum,Gold,Mercury,Thallium,Lead,Bismuth,Polonium,Astatine,Radon,Francium,Radium,Actinium,Thorium,Protactinium,Uranium,Neptunium,Plutonium,Americium,Curium,Berkelium,Californium,Einsteinium".split(',')
    
    screen_rect = Rect(0,0,WIDTH,HEIGHT)

    #events
    ADD_PARTICLE = USEREVENT+1 #add proton, neutron, or electron
    ADD_BLOCK = USEREVENT+2    #add normal block or magnet
    ADD_GENERATOR = USEREVENT+3#add a spark generator
    ADD_SPARK = USEREVENT+4    #add a spark
