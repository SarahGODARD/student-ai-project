
import pandas as pd

def open_csv(file_name, image_name, csv):
    """Open a csv file to write on it and create a dataframe containing images informations.
    Args:
        file_name (str): Path of the file to open.
        image_name (str): Name of the image to open.
        csv (str): name of a csv file to handle (in development)

    Returns:
        dictionary: containing to opended csv file and the dataframe containing the images names.

    """
    csvfile = open(file_name, 'w', newline="")
    df = pd.DataFrame({"image_name": [image_name]})
    return {"csv_file": csvfile, "df": df}

def write_in_csv(csvfile, df):
    """Write a dataframe in a csv file.
    Args:
        csvfile (file object): Path of the file to open.
        image_name (str): Name of the image to open.
        csv (str): name of a csv file to handle (in development)

    Returns:
        dictionary: containing to opended csv file and the dataframe containing the image name.

    """
    df.to_csv(csvfile, index= False)