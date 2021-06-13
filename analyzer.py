from os import listdir
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

#def convert_stars(stars):
    #return float(stars.split("/")[0].replace(",", "."))

pd.set_option("display.max_columns", None)

print(*[file_name.split(".")[0] for file_name in listdir("reviews")], sep="\n")
product_id = input("Podaj kod produktu: ")

reviews = pd.read_json(f"reviews/{product_id}.json")

reviews.stars = reviews.stars.map(lambda stars: float(stars.split("/")[0].replace(",", ".")))

reviews_count = len(reviews.index)
#reviews_count = reviews.review_id.count()
#reviews_count = reviews["review_id"].count()
#reviews_count = reviews.shape[0]

#pros_count = reviews.pros.astype(bool).sum()
pros_count = reviews.pros.map(bool).sum()
pros_count = reviews.pros.apply(bool).sum()
print(pros_count)

#cos_count = reviews.cons.astype(bool).sum()
cos_count = reviews.cons.map(bool).sum()
cos_count = reviews.cons.apply(bool).sum()
print(cos_count)

average_score = reviews.stars.mean().round(2)
print(average_score)

stars = reviews.stars.value_counts(dropna=False).reindex(np.arange(0, 5.5, 0.5), fill_value = 0)
stars.plot.bar(color="lightgreen")
plt.title("Gwiazdki")
plt.xlabel("Liczba gwiazdek")
plt.ylabel("Liczba opinii")
plt.show()
plt.savefig(f"plots/{product_id}.png")
plt.close()
