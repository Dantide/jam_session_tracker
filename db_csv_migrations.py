import csv
import os

from musicsessions.models import Tune, Style, Tempo


def import_song_list(path):
    """
    Imports the list of songs defined in a csv file given in path.
    """
    print("\n\n\n\n")
    BASE_DIR = os.getcwd()
    import_count = 0
    failed_count = 0
    with open(path) as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            _, created = Tune.objects.get_or_create(
                name=row[0],
                composer=row[1],
                default_style=Style.objects.get(name=row[2]),
                default_tempo=Tempo.objects.get(name=row[3]),
            )
            if (not created):
                failed_count += 1
                print (row[0] + " is already in the database.")
            else:
                import_count += 1
    print("\n\n")
    print("Sucessfully imported: " + str(import_count) + ", Failed: " + str(failed_count))

import_song_list('exports.csv')