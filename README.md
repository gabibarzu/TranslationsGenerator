# TranslationsGenerator

This tool can be used to generate a list of translations based on an input csv file.

## Execution

Using the python command `python generator.py` and with an existing CSV file.
For the csv file, the first line will the csv header, but i can be skyped without if parameter `skip_header` will be set to `False`

In the `generator.py` file, set the parameters:
```
file_name = 'translations.csv'
area = 'Area'
```

The output will be placed in the `output.sql` file.