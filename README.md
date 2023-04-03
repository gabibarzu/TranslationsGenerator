# TranslationsGenerator

This tool can be used to generate a list of translations based on an input csv file.

## Execution

### Parameters
- `area` -> Area for the resource
- `file_name` -> The input for the translations that should be generated
- `skip_header` -> Flag that will skip the header for the csv input file

Using the python command `python generator.py "Area"` and with an existing CSV file.

### Additional runnings example
- `python generator.py "Area"`
- `python generator.py "Area" "translations.csv"`
- `python generator.py "Area" "translations.csv" True`

The output will be placed in the `output.sql` file.