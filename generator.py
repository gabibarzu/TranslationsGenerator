import csv


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


def generateTranslations(file_name, area, skip_header=True):
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
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
                line_count += 1


file_name = 'translations.csv'
area = 'Area'
generateTranslations(file_name, area)
