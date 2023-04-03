import csv
import sys


def generateHeader(area):
    return f"""DECLARE @LanguageIdForEN INT = 1
DECLARE @LanguageIdForNL INT = 2
DECLARE @Area VARCHAR(50)
DECLARE @ResourceKey VARCHAR(50)

SET @Area = '{area}'

"""


def generateTranslation(label, en_translation, nl_translation, resource_key):
    return f"""SET @ResourceKey = '{resource_key}'
EXEC InsertResourceItem @Area, @ResourceKey, '{label}'
EXEC InsertOrUpdateResourceTranslation @LanguageIdForEN, @Area, @ResourceKey, '{en_translation}'
EXEC InsertOrUpdateResourceTranslation @LanguageIdForNL, @Area, @ResourceKey, '{nl_translation}'

"""


def generateTranslations(area, file_name='translations.csv', skip_header=True):
    try:
        with open(file_name) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            generated_translations = 0
            with open('output.sql', 'w') as f:
                f.write(generateHeader(area))
                for row in csv_reader:
                    if line_count == 0 and skip_header:
                        line_count += 1
                        continue
                    label = row[0]
                    en_translation = row[1]
                    nl_translation = row[2]
                    resource_key = row[3]
                    f.write(generateTranslation(
                        label, en_translation, nl_translation, resource_key))
                    generated_translations += 1
                    line_count += 1
        print(f"{generated_translations} translations generated.")
    except IOError:
        print("Please provide an existing input file.")


if (len(sys.argv) < 2):
    print("Please provide the area. The command should be *** python generator.py \"Area\" ***")
else:
    if (len(sys.argv) < 3):
        generateTranslations(sys.argv[1])
    elif (len(sys.argv) < 4):
        generateTranslations(sys.argv[1], sys.argv[2])
    else:
        skip_header = sys.argv[3].lower() == 'true'
        generateTranslations(sys.argv[1], sys.argv[2], skip_header)
