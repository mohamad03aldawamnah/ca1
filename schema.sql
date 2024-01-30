DROP TABLE IF EXISTS users; 

CREATE TABLE users 
(  
    user_id TEXT PRIMARY KEY, 
    password TEXT NOT NULL 
);  
DROP TABLE IF EXISTS meals; 

CREATE TABLE meals 
( 
    meal_id INTEGER PRIMARY KEY AUTOINCREMENT,  
    name TEXT NOT NULL, 
    price REAL NOT NULL, 
    description TEXT, 
    type_of_meal TEXT,
    calories_per_meal INTEGER,
    allergic_nuts INTEGER,
    allergic_dairy INTEGER,
    allergic_eggs INTEGER,
    allergic_soy INTEGER,
    allergic_fish INTEGER,
    alergic_chicken INTEGER

); 
INSERT INTO meals (name, price, description,type_of_meal,calories_per_meal,allergic_nuts,allergic_dairy,allergic_eggs,allergic_soy,allergic_fish,alergic_chicken) 
VALUES 
    ('manooshat zatar', 16.5, 'Syrian oregano with some mozzeralla cheese spread on a circular dough','breakfast',100,0,0,0,0,0,0), 
    ('boiled egg', 17.99, 'boiled egg cut in 4 slices and served','breakfast',100,0,0,1,0,0,0),  
    ('fatirat cheese ', 12, 'a dough filled with mozerella cheese and seseme','breakfast',100,0,1,0,0,0,0),  
    ('mahmara ', 15.99, 'a very spicy sauce spread on a dough with seseme sprayed on it ','breakfast',100,1,0,0,1,0,0),
    ('Fava Beans', 8.99, 'beans squeshed and and mixed with olive oil and tomato','breakfast',100,0,0,0,1,0,0),  
	('samosa', 10.99, 'triangled fried South Asian pastry with a savoury filling','breakfast',100,1,0,0,0,0,1),
    ('kubba labania', 16.5, '3 balls of meet and nuts filled that is covered with cooked yougert ','lunch',100,1,1,0,0,0,0), 
    ('stuffed zucchini)', 17.99, '3 pieces of zucchini stuffed with rice and beef and tomato sauce ','lunch',100,1,0,0,0,0,0),  
    ('rocket chicken shawarma wrap ', 12, 'a chicken wrap from the middle of demascus taste','lunch',100,0,0,0,1,0,1),  
    ('grape leaves aka "waraq enab"', 15.99, 'meat and rice filled in a grape leave and rolled up','lunch',100,0,0,0,1,0,0),
    ('musakhan', 8.99, 'roasted chicken baked with onions, sumac, allspice, saffron, and fried pine nuts served over taboon bread.','lunch',100,1,0,0,1,0,0),  
	('chicken beryani', 10.99, 'rise and chicken  ','lunch',100,1,0,0,0,0,1),
    ('Falafel',10,'deep-fried balls or patties made from chickpeas or fava beans, sometimes both, plus fresh herbs and spices','dinner',100,0,0,0,0,0,0),
    ('Shish barak',10,'ravioli-like dumplings filled with seasoned lamb, onions, and pine nuts that are boiled, baked, or fried and served in a warm yogurt sauce with melted butter, mint, sumac, and more toasted pine nuts.','dinner',100,1,1,0,0,0,0),  
    ('Mujadara',10.5,'cooked lentils and rice and it can aslo be eaten with bulgur','dinner',100,1,0,0,0,0,0),  
    ('zataer and labnah sandwitch',22,'Syrian oregano with some type of cheese spread on a wrap type bread ','dinner',100,1,1,0,0,0,0),
    ('fattet makdous ',10,' Roasted Eggplant dish with ground beef, pita chips and yogurt sauce bursting with flavors and textures.','dinner',100,1,1,0,0,0,0),  
	('fattet humus',10,'Fattet hummus is a creamy, pine-nutty concoction often eaten in Palestine, Lebanon, and Syria for a satisfying weekend brunch','dinner',100,1,1,0,0,0,0);




DROP TABLE IF EXISTS new_menue; 

CREATE TABLE new_menue 
( 
    meal_id INTEGER PRIMARY KEY AUTOINCREMENT,  
    name TEXT NOT NULL 
    
); 

