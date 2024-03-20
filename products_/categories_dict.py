categories_subcategories = {
    ("Est", "Real Estate"): [("AP", "Apartments"), ("H", "Houses"), ("POF", "Plot Of Land"), ("G", "Garages")],
    ("TR", "Transport"): [("C", "Cars"), ("CP", "Car Parts"), ("TR", "Trucks"), ("PL", "Planes")],
    ("J", "Job"): [("TRA", "Trade"), ("RPC", "Restaurants, Pubs, Cafes"), ("TD", "Transport, Driver"), ("FS", "Fitness, Sport"), ("BS", "BabySitting")],
    ("EL", "Electronics"): [("CP", "Cell Phones"), ("LT", "Laptops"), ("MON", "Monitors"), ("TV", "TVs"), ("PS", "Printers, Scanners"), ("CAM", "Cameras")],
}


subcatigories = list(categories_subcategories.values())[0] +\
                list(categories_subcategories.values())[1] + \
                list(categories_subcategories.values())[2] + \
                list(categories_subcategories.values())[3]