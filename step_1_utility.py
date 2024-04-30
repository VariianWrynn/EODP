import pandas as pd

# Expanded data for book series and authors
data = {
    "titles": [
        "Sherlock Holmes", "The Hobbit", "The Ring", "Foundation", 
        "Harry Potter", "A Song of Ice and Fire", "The Wheel of Time", "Discworld",
        "Outlander", "Percy Jackson & the Olympians", "His Dark Materials",
        "Bridget Jones", "The No. 1 Ladies' Detective Agency", "The Southern Vampire Mysteries",
        "Artemis Fowl", "Alex Cross", "Stephanie Plum", "The Dark Tower", "Anita Blake: Vampire Hunter",
        "The Chronicles of Narnia", "Tom Clancy's Op Center", "Dune", "The Princess Diaries",
        "Shopaholic series", "The Mitford Years", "Jack Reacher", "Redwall",
        "Foundation series", "The Saga of Darren Shan", "The Riftwar Cycle", "Temeraire",
        "In Death series", "The Left Behind", "Amelia Peabody", "The Bourne Series", "Mortal Instruments",
        "Maximum Ride", "The Tudor Court", "Kay Scarpetta", "Dirk Pitt", "Earth's Children",
        "Mars Trilogy", "Prey Series", "Rizzoli & Isles", "The Vampire Chronicles", "Incarnations of Immortality",
        "Guardians of Time", "The Spiderwick Chronicles", "Magic Tree House", "Warriors", "Ranger's Apprentice",
        "Gossip Girl", "Circle Trilogy", "The Dark is Rising", "The Keys to the Kingdom", "Young Wizards",
        "The Pendragon Adventure", "Shadow Children", "Ramona", "Septimus Heap", "Diary of a Wimpy Kid",
        "The Immortals", "The Belgariad", "Magic Circle", "Malory Towers", "The Uplift Saga",
        "Discworld", "The Night World", "The CHERUB Series", "The Sword of Truth", "The Godfather",
        "Maze Runner", "Wicked", "Animorphs", "Bone", "Wolves of Mercy Falls", "The Shannara Series",
        "The Sigma Force", "The Temperance Brennan Series", "The Repairman Jack Series", "Thursday Next",
        "The Alex Rider Series", "Hitchhiker's Guide to the Galaxy", "The Last Kingdom Series", "The Morganville Vampires",
        "The Inheritance Cycle", "The Hunger Games", "Robert Langdon Series", "The House of Night", "The 39 Clues",
        "The Women's Murder Club", "The Twilight Saga", "The Millennium Series", "Mistborn Series", "The Kingkiller Chronicle",
        "Fablehaven", "The Luxe Series", "Gone Series", "The Lorien Legacies", "The Dresden Files",
        "The Mercy Thompson Series", "The Sookie Stackhouse Series",
        "The Alex Delaware Series", "Virgil Flowers Series", "The Cork O'Connor Series", "The Demonata",
        "Cirque Du Freak", "The Kane Chronicles", "The Heroes of Olympus", "The Riyria Revelations",
        "The First Law", "The Riyria Chronicles", "Codex Alera", "The Hollows", "The Rain Wild Chronicles",
        "The Liveship Traders Trilogy", "The Farseer Trilogy", "The Tawny Man Trilogy", "The Fitz and The Fool Trilogy",
        "The Legend of Drizzt", "Nightside", "The Secret Histories", "The October Daye Series", "The Lockwood & Co. Series",
        "The Bartimaeus Trilogy", "The Edge Chronicles", "The Chronicles of Ancient Darkness"
    ],
    "Author": [
        "Arthur Conan Doyle", "George R.R. Martin", "George R.R. Martin", "Isaac Asimov",
        "J.K. Rowling", "George R.R. Martin", "Robert Jordan", "Terry Pratchett",
        "Diana Gabaldon", "Rick Riordan", "Philip Pullman", "Helen Fielding",
        "Alexander McCall Smith", "Charlaine Harris", "Eoin Colfer", "James Patterson",
        "Janet Evanovich", "Stephen King", "Laurell K. Hamilton", "C.S. Lewis", "Tom Clancy and Jeff Rovin",
        "Frank Herbert, Brian Herbert, Kevin J. Anderson", "Meg Cabot", "Sophie Kinsella",
        "Jan Karon", "Lee Child", "Brian Jacques", "Isaac Asimov", "Darren Shan", "Raymond E. Feist",
        "Naomi Novik", "J.D. Robb", "Tim LaHaye and Jerry B. Jenkins", "Elizabeth Peters", "Robert Ludlum, Eric Van Lustbader",
        "Cassandra Clare", "James Patterson", "Philippa Gregory", "Patricia Cornwell", "Clive Cussler", "Jean M. Auel",
        "Kim Stanley Robinson", "John Sandford", "Tess Gerritsen", "Anne Rice", "Piers Anthony", "Marianne Curley", 
        "Holly Black and Tony DiTerlizzi", "Mary Pope Osborne", "Erin Hunter", "John Flanagan",
        "Cecily von Ziegesar", "Nora Roberts", "Susan Cooper", "Garth Nix", "Diane Duane",
        "D.J. MacHale", "Margaret Peterson Haddix", "Beverly Cleary", "Angie Sage", "Jeff Kinney",
        "Tamora Pierce", "David Eddings", "Tamora Pierce", "Enid Blyton", "David Brin",
        "Terry Pratchett", "L.J. Smith", "Robert Muchamore", "Terry Goodkind", "Mario Puzo",
        "James Dashner", "Gregory Maguire", "K.A. Applegate", "Jeff Smith", "Maggie Stiefvater", "Terry Brooks",
        "James Rollins", "Kathy Reichs", "F. Paul Wilson", "Jasper Fforde", "Anthony Horowitz",
        "Douglas Adams", "Bernard Cornwell", "Rachel Caine", "Christopher Paolini", "Suzanne Collins",
        "Dan Brown", "P.C. Cast and Kristin Cast", "Various Authors", "James Patterson", "Stephenie Meyer",
        "Stieg Larsson", "Brandon Sanderson", "Patrick Rothfuss", "Brandon Mull", "Anna Godbersen",
        "Michael Grant", "Pittacus Lore", "Jim Butcher", "Patricia Briggs", "Charlaine Harris",
        "Jonathan Kellerman", "John Sandford", "William Kent Krueger", "Darren Shan", "Darren Shan",
        "Rick Riordan", "Rick Riordan", "Michael J. Sullivan", "Joe Abercrombie", "Michael J. Sullivan",
        "Jim Butcher", "Kim Harrison", "Robin Hobb", "Robin Hobb", "Robin Hobb", "Robin Hobb", "Robin Hobb",
        "R.A. Salvatore", "Simon R. Green", "Simon R. Green", "Seanan McGuire", "Jonathan Stroud",
        "Jonathan Stroud", "Paul Stewart and Chris Riddell", "Michelle Paver"
    ],
}

# Create a DataFrame
series_df = pd.DataFrame(data)

import re

def preprocess_title(title):
    
    # Remove leading articles: "the", "a", "an"
    title = re.sub(r'^\b(The|A|An)\s+', '', title)
    
    # Remove leading and trailing whitespace
    title = title.strip()
    
    return title

processed_titles = [preprocess_title(title) for title in data["titles"]]

series_df["Simplified-Title"] = processed_titles

# Save the DataFrame to a CSV file
csv_file_path = 'popular_titles.csv'
series_df.to_csv(csv_file_path, index=False)

print(f"CSV file saved as {csv_file_path}")
