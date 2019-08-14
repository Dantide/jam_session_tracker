import csv
import os

from musicsessions.models import Tune, Style, Tempo, TuneRealBook, RealBook

# To run file, open shell using:
# /> py manage.py shell
# and run the code:
# >>> import db_csv_migrations
# >>> db_csv_migrations.main()

def main():
    """This function runs the core of the program."""
    import_song_list('exports.csv')

def import_song_list(filename : str) -> None:
    """
    Imports the list of songs defined in a csv file given in path.
    """
    print("\n\n\n\n")
    print("Running song list import on " + filename + ":\n")
    BASE_DIR = os.getcwd()
    import_count = 0
    failed_count = 0
    with open(filename) as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            _, tune_created = Tune.objects.get_or_create(
                name=row[0],
                composer=row[1],
                default_style=Style.objects.get(name=row[2]),
                default_tempo=Tempo.objects.get(name=row[3]),
            )
            _, tunerealbook_created = TuneRealBook.objects.get_or_create(
                real_book=RealBook.objects.get(name=row[4]),
                tune=Tune.objects.get(name=row[0]),
                page_num=row[5]
            )
            message = ""
            if (not tune_created):
                failed_count += 1
                message = "Failed: " + row[0] + " is already in the database." + ("Real Book entry added." if tunerealbook_created else "")
                if (not tunerealbook_created):
                    message = message + 
            else:
                import_count += 1
                message = "Passed: " + row[0] + "."
            print(message)
    print("\n\n")
    print("Sucessfully imported: " + str(import_count) + ", Failed: " + str(failed_count))