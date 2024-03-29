# -*- coding: utf-8 -*-
"""Social Media Labelling.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P8fbNjsPYZfbiymVcotpcV7dcYsrx8l6

# Library
"""

pip install langdetect

import re
import numpy as np
import pandas as pd
from langdetect import detect

"""# Import"""

# Read data from Excel file
toyo = '/content/Hyundai Kona (EV).xlsx'  # Update with your file name
df = pd.read_excel(toyo)

"""# Bahasa"""

pip install langdetect

def detect_language(text):
    try:
        return detect(text)
    except:
        return 'unknown'

# Apply language detection to a specific column (e.g., 'TextColumn')
df['Language'] = df['message'].apply(detect_language)

# Count occurrences of all unique values in the specified column
value_counts = df['Language'].value_counts()

# Print the value counts
value_counts.head(50)

# Specify the column and the two specific keywords to split on
column_to_split = 'Language'  # Replace with the actual column name
specific_keyword = 'id'  # Replace with the first keyword

# Create two subsets based on the presence of the specific keyword
Indonesia = df[df[column_to_split].str.contains(specific_keyword, case=False, na=False)]
Others = df[~df[column_to_split].str.contains(specific_keyword, case=False, na=False)]

# Save the subsets to separate CSV files if needed
# subset_with_keyword.to_csv('path/to/your/output/subset_with_keyword.csv', index=False)
# subset_without_keyword.to_csv('path/to/your/output/subset_without_keyword.csv', index=False)

"""# Media Type"""

# Specify the columns for which you want to create a label
column1 = 'username'  # Replace with the actual column name
column2 = 'follower'  # Replace with the actual column name
column3 = "name"
# Define a list of acceptable values for column1
acceptable_values_column1 = ["hyundaimotorindonesia", "hyundaimotorid", "Hyundai Motors Indonesia", "Hyundai Motors Indonesia",
                             ]
# acceptable_values_column2 = ['hondaisme', 'Hondaisme', 'HONDAISME']

# Function to apply labels based on values from different columns
def label_based_on_columns(row):
    if row[column1] in acceptable_values_column1 or row[column3] in acceptable_values_column1:
        return 'Owned'
    elif row[column2] > 20000:
        return 'Paid'
    else:
        return 'Earned'

# Apply the labeling function to create a new 'LabelColumn'
Indonesia['Media Type'] = Indonesia.apply(label_based_on_columns, axis=1)

# Specify the columns for which you want to create a label
column1 = 'username'  # Replace with the actual column name
column2 = 'follower'  # Replace with the actual column name
column3 = "name"
# Define a list of acceptable values for column1
acceptable_values_column1 = ['hondaisme', 'Hondaisme', 'HONDAISME', 'Honda', 'honda','toyotaid', 'ToyotaID',
                             'ToyotaIndonesia', 'ToyotaID', 'toyotaid', 'Toyota Indonesia',
                             "mitsubishimotorsid", "Mitsubishi_ID", "Mitsubishi Motors Indonesia", "Mitsubishi Motors Indonesia", "mitsubishimotorsid",
                             "hyundaimotorindonesia", "hyundaimotorid", "Hyundai Motors Indonesia", "Hyundai Motors Indonesia",
                             "daihatsuind", "DaihatsuInd", "Daihatsu Sahabatku", "Astra Daihatsu",
                             "suzuki_id", "SuzukiIndonesia", "Suzuki Indonesia", "Suzuki Indonesia", "suzuki_id",
                             "wulingmotorsid", "WulingMotorsID", "Wuling MotorsID", "Wuling Motors Indonesia", "wulingmotorsid",
                             "mazdaid", "Mazda Indonesia", "Mazda Indonesia",
                             "dfskindonesia", "DFSK_indonesia", "DFSK Motors Indonesia", "DFSK Motors Indonesia",
                             "bmw_indonesia", "BMW_Indonesia", "BMW Indonesia"
                             "cherymotorindonesia", "Chery Motor Indonesia", "CheryMotorID",
                             "MercedesBenz", "mercedesbenzid", "Mercedes-Benz", "Mercedes-Benz Indonesia",
                             "mgmotor.id", "MG Motor Indonesia", "MGmotorId",
                             "nissanid", "Nissan", "NissanID", "Nissan Indonesia",
                             "protoncars", "Proton Cars Official"]
# acceptable_values_column2 = ['hondaisme', 'Hondaisme', 'HONDAISME']

# Function to apply labels based on values from different columns
def label_based_on_columns(row):
    if row[column1] in acceptable_values_column1 or row[column3] in acceptable_values_column1:
        return 'Owned'
    elif row[column2] > 20000:
        return 'Paid'
    else:
        return 'Earned'

# Apply the labeling function to create a new 'LabelColumn'
Indonesia['Media Type'] = Indonesia.apply(label_based_on_columns, axis=1)

# Specify the columns for which you want to create a label
column1 = 'username'  # Replace with the actual column name
column2 = 'follower'  # Replace with the actual column name
column3 = "name"
column4 = 'service'
# Define a list of acceptable values for column1
acceptable_values_column1 = ['hondaisme', 'Hondaisme', 'HONDAISME', 'Honda', 'honda','toyotaid', 'ToyotaID',
                             'ToyotaIndonesia', 'ToyotaID', 'toyotaid', 'Toyota Indonesia',
                             "mitsubishimotorsid", "Mitsubishi_ID", "Mitsubishi Motors Indonesia", "Mitsubishi Motors Indonesia", "mitsubishimotorsid",
                             "hyundaimotorindonesia", "hyundaimotorid", "Hyundai Motors Indonesia", "Hyundai Motors Indonesia",
                             "daihatsuind", "DaihatsuInd", "Daihatsu Sahabatku", "Astra Daihatsu",
                             "suzuki_id", "SuzukiIndonesia", "Suzuki Indonesia", "Suzuki Indonesia", "suzuki_id",
                             "wulingmotorsid", "WulingMotorsID", "Wuling MotorsID", "Wuling Motors Indonesia", "wulingmotorsid",
                             "mazdaid", "Mazda Indonesia", "Mazda Indonesia",
                             "dfskindonesia", "DFSK_indonesia", "DFSK Motors Indonesia", "DFSK Motors Indonesia",
                             "bmw_indonesia", "BMW_Indonesia", "BMW Indonesia"
                             "cherymotorindonesia", "Chery Motor Indonesia", "CheryMotorID",
                             "MercedesBenz", "mercedesbenzid", "Mercedes-Benz", "Mercedes-Benz Indonesia",
                             "mgmotor.id", "MG Motor Indonesia", "MGmotorId",
                             "nissanid", "Nissan", "NissanID", "Nissan Indonesia",
                             "protoncars", "Proton Cars Official"]
services = ['news', 'blogs']
# acceptable_values_column2 = ['hondaisme', 'Hondaisme', 'HONDAISME']

# Function to apply labels based on values from different columns
def label_based_on_columns(row):
    if row[column4] in services:
        return 'Paid'
    elif row[column1] in acceptable_values_column1 or row[column3] in acceptable_values_column1:
        return 'Owned'
    elif row[column2] > 20000:
        return 'Paid'
    else:
        return 'Earned'

# Apply the labeling function to create a new 'LabelColumn'
Indonesia['Media Type'] = Indonesia.apply(label_based_on_columns, axis=1)

constant_value = 'Earned'  # Replace with the value you want to assign
Others['Media Type'] = constant_value

# Count occurrences of all unique values in the specified column
value_counts = Indonesia['Media Type'].value_counts()

# Print the value counts
value_counts.head(50)

# Count occurrences of all unique values in the specified column
value_counts = Others['Media Type'].value_counts()

# Print the value counts
value_counts.head(50)

"""# Voice"""

# Specify the columns for which you want to create a label
columnV1 = 'Media Type'  # Replace with the actual column name
columnV2 = 'message'  # Replace with the actual column name
# columnV3 = "message"
# Define a list of acceptable values for column1
acceptable_values_columnV1 = ['Owned', 'Paid']
acceptable_values_columnV2 = ['Earned']
keywords_to_check  = ["Peluncuran", "Debut", "pemasaran", "Konferensi Pers", "Premier", "luncurkan", "diluncurkan", "uji coba", "Dealer", "showroom", "sponsor", "sponsorship", "kampanye", "iklan", "CSR",
              "amal", "donasi", "donatur", "penghargaan", "program", "informasi", "launching", "merilis", "meluncurkan", "lawan baru", "penantang baru", "iims", "lebih baik", "meluncur", "lengkap", "layanan",
              "acara", "pemerintah", "bersiaplah", "GIIAS", "exhibition", "show", "test drive", "kementrian", "G20", "bersiaplah", "diluncurkan", "launching", "jangan diragukan", "pelayanan",
              "award", "Komunitas", "meet", "modifikasi", "club", "Competitions", "Kompetisi", "quiz", "giveaway", "give away", "bagi-bagi", "pelatihan", "pameran", "otomotif"]
dealer = ['Dealer', 'Shop', 'Store', 'Toko', 'Online', 'Garasi', 'Garage', 'jual', 'beli',
          'honda', 'suzuki', 'daihatsu', 'mitsubishi', 'toyota', 'mazda']

# Function to apply labels based on values from different columns
def label_based_on_conditions(row):
    if row[columnV1] in acceptable_values_columnV1 and any(keyword in row[columnV2].lower() for keyword in keywords_to_check):
        return 'Brand'
    elif row[columnV1] in acceptable_values_columnV2 and any(keyword.lower() in row[column1].lower() for keyword in dealer or row[column3].lower() for keyword in dealer):
        return 'Dealer'
    elif row[columnV1] in acceptable_values_columnV2:
        return 'Customer'
    else:
        return 'Other'

# Apply the labeling function to create a new 'LabelColumn'
Indonesia['Voice'] = Indonesia.apply(label_based_on_conditions, axis=1)

constant_value = 'Other'  # Replace with the value you want to assign
Others['Voice'] = constant_value

# Count occurrences of all unique values in the specified column
value_counts = Indonesia['Voice'].value_counts()

# Print the value counts
value_counts.head(50)

# Count occurrences of all unique values in the specified column
value_counts = Others['Voice'].value_counts()

# Print the value counts
value_counts.head(50)

"""# Merge"""

merged_df = pd.concat([Indonesia, Others], ignore_index=True)

merged_df.info()

# Specify the column and the two specific keywords to split on
column_to_split = 'Voice'  # Replace with the actual column name
specific_keyword = 'Customer'  # Replace with the first keyword

# Create two subsets based on the presence of the specific keyword
Customer = merged_df[merged_df[column_to_split].str.contains(specific_keyword, case=False, na=False)]
Others = merged_df[~merged_df[column_to_split].str.contains(specific_keyword, case=False, na=False)]

# Define your groups and corresponding labels
SubAtt = {
    'D - Overall': {"fungsionalitas", "sustainability", "desain"},
    'D - Styles': {"Streamline", "futuristik", "klasik", "tradisional", "sederhana", "modern"},
    'D - Specific': {"roof rack", "rangka atap", "karpet", "floor mat"},
    'D - Sizes': {"panjang", "lebar", "tinggi", "kapasitas bagasi", "kapasitas",  "jarak", "sudut approach", "sudut departure", "sudut ramping", "turning radius", "mungil"},
    'D - Colors': {"warna", "cat", "metalik", "solid", "matte", "pastel"},
    'D - Weight': {"berat", "ringan", "ideal"},
    'D - Ground clearance': {"ground clearance", "rendah"},
    'D - Wheel': {"velg"},
    'D - Exterior': {"berkelas", "menawan", "estetis", "proporsional", "tangguh", "kuat", "elegan"},
    'D - Interior': {"menarik", "minimalis", "eksklusif", "estetika", "istimewa", "rumit", "keras", "sempit", "kecil"},
    'D - Material': {"Material" ,"mudah tergores", "plastik mudah pecah", "kulit cepat rusak", "bau", "sulit dibersihkan", "kualitas premium", "tahan cuaca ekstrem", "ringan", "ramah lingkungan"},
    'P - General': {"kencang", "mesin"},
    'P - Fuel tank capacity': {"kapasitas tangki", "tangki"},
    'P - Drivetrain': {"FWD", "RWD", "4WD", "AWD"},
    'P - Transmission': {"transmisi manual", "Transmisi otomatis", "CVT", "Transmisi Semi", "DCT"},
    'P - Suspension': {"suspensi", "Pegas", "Amortiser", "Stabilizer", "Wishbone", "Bushing", "Subframe"},
    'P - Power steering': {"hidraulik", "EPS", "power steering elektrik"},
    'P - Brake': {"cakram", "tromol", "ABS", "Anti-lock Braking System", "Rem Regeneratif", "E-Brake", "rem parkir"},
    'P - Fuel consumption': {"mpg", "km/L", "kilowatt", "kWh", "hemat"},
    'P - Speed': {"kecepatan", "cepat", "ngadat", "lambat", "ngebut", "lama"},
    'P - Soundproof': {"panel isolasi", "peredam suara", "kaca Laminasi", "rubber seals"},
    'P - Driving feeling': {"Torsi", "silent", "Smooth", "halus", "lincah", "responsifitas", "keseimbangan"},
    'E - Head lamp': {"head lamp", "lampu depan", "lampu sorot", "lampu utama", "light", "LED"},
    'E - Tail lamp': {"lampu belakang", "tail lamp", "light"},
    'E - Rearview mirrors': {"rearview mirror", "spion", "rear view", "rearview"},
    'E - Others': {"kaca", "wiper", "pintu", "bemper", "bumper", "rooftop", "jendela", "window", "body", "bodi","ukuran ban", "tire", "engsel penarik"},
    'I - Seat Material': {"jok", "seat", "kulit", "tempat duduk", "duduk"},
    'I - Seat function': {"kursi", "empuk", "nyaman", "penghangat kursi", "heated seats", "luas", "lega"},
    'I - Air Condicioner': {"ac", "air conditioner", "pendingin"},
    'I - Speedometer': {"speedometer", "spidometer", "indikator"},
    'I - Audio System': {"audio", "speaker", "pengeras suara", "radio", "stereo", "sound"},
    'S - Back Camera': {"back camera", "kamera", "kamera belakang"},
    'S - Parking Sensors': {"parking", "parkir", "sensor", "GPS", "sensor parkir"},
    'S - Airbag': {"airbag", "keamanan"},
    'S - Speed Control': {"isc", "idle", " speed control"},
    'S - Advance features': {"advance features", "fitur lanjutan"},
    'S - PIN': {"safety pin", "dongkrak"},
    'Q - Durabilities': {"durability", "durabilities", "durabilitas", "daya tahan", "kualitas", "fasilitas"},
    'SV - Sparepat': {"sparepart", "sperpat"},
    'SV - Warranty Service': {"warranty", "garasi", "servis", "service"},
    'Pr - General': {"mahal", "murah", "terjangkau", "ekonomis", "selangit"},
    'Pr - Depreciations': {"depresiasi", "depreciation", "penurunan harga", "turun harga","harga", "anjlok", "turun", "harga naik", "harga jual"},
    'B - Brand love': {"suka", "favorit",  "idaman", "terbaik", "jago", "terdepan", "gemar", "mewah"},
    'Br - Super Fast Charge': {"fast charging", "fast charge", "fast charger", "capacity"},
    'Br - Battery life': {"battery", "baterai", "batre"},
    'Br - Safety': {"Battery Safety"},
    'CS - Charging Station': {"charging station", "charging", "station", "ngecas", "ngeces"},

}

# Function to apply labels based on groups
def label_based_on_subatt(cell_value):
    for group, keywords in SubAtt.items():
        # Check for the presence of the keyword as a standalone word
        if any(re.search(rf'\b{re.escape(keyword)}\b', str(cell_value), flags=re.IGNORECASE) for keyword in keywords):
            return f'{group}'
    return 'Other'  # Default label if no group is matched
Customer['SubAtt'] = Customer['message'].apply(label_based_on_subatt)

# Count occurrences of all unique values in the specified column
value_counts = Customer['SubAtt'].value_counts()

# Print the value counts
value_counts.head(50)

# Define your groups and corresponding labels
Att = {
    'Design': {"fungsionalitas", "sustainability", "desain", "Streamline", "futuristik", "klasik", "tradisional", "sederhana", "modern", "roof rack", "rangka atap", "karpet", "floor mat", "panjang", "lebar", "tinggi", "kapasitas bagasi", "kapasitas",  "jarak", "sudut approach", "sudut departure", "sudut ramping", "turning radius", "mungil", "warna", "cat", "metalik", "solid", "matte", "pastel", "berat", "ringan", "ideal", "ground clearance", "rendah", "velg", "berkelas", "menawan", "estetis", "proporsional", "tangguh", "kuat", "elegan", "menarik", "minimalis", "eksklusif", "estetika", "istimewa", "rumit", "keras", "sempit", "kecil", "Material" ,"mudah tergores", "plastik mudah pecah", "kulit cepat rusak", "bau", "sulit dibersihkan", "kualitas premium", "tahan cuaca ekstrem", "ringan", "ramah lingkungan"},
    'Performance': {"kencang", "mesin", "kapasitas tangki", "tangki", "FWD", "RWD", "4WD", "AWD", "transmisi manual", "Transmisi otomatis", "CVT", "Transmisi Semi", "DCT", "suspensi", "Pegas", "Amortiser", "Stabilizer", "Wishbone", "Bushing", "Subframe", "hidraulik", "EPS", "power steering elektrik", "cakram", "tromol", "ABS", "Anti-lock Braking System", "Rem Regeneratif", "E-Brake", "rem parkir", "mpg", "km/L", "kilowatt", "kWh", "hemat", "kecepatan", "cepat", "ngadat", "lambat", "ngebut", "lama", "panel isolasi", "peredam suara", "kaca Laminasi", "rubber seals", "Torsi", "silent", "Smooth", "halus", "lincah", "responsifitas", "keseimbangan"},
    'Exterior': {"head lamp", "lampu depan", "lampu sorot", "lampu utama", "light", "LED", "lampu belakang", "tail lamp", "light", "rearview mirror", "spion", "rear view", "rearview", "kaca", "wiper", "pintu", "bemper", "bumper", "rooftop", "jendela", "window", "body", "bodi","ukuran ban", "tire", "engsel penarik"},
    'Interior': {"jok", "seat", "kulit", "tempat duduk", "duduk", "kursi", "empuk", "nyaman", "penghangat kursi", "heated seats", "luas", "lega", "ac", "air conditioner", "pendingin", "speedometer", "spidometer", "indikator", "audio", "speaker", "pengeras suara", "radio", "stereo", "sound"},
    'Safety': {"back camera", "kamera", "kamera belakang", "parking", "parkir", "sensor", "GPS", "sensor parkir", "airbag", "keamanan", "isc", "idle", " speed control", "advance features", "fitur lanjutan", "safety pin", "dongkrak"},
    'Quality': {"durability", "durabilities", "durabilitas", "daya tahan", "kualitas", "fasilitas"},
    'Service': {"sparepart", "sperpat", "warranty", "garasi", "servis", "service"},
    'Price': {"mahal", "murah", "terjangkau", "ekonomis", "selangit", "depresiasi", "depreciation", "penurunan harga", "turun harga","harga", "anjlok", "turun", "harga naik", "harga jual"},
    'Brand Image': {"suka", "favorit",  "idaman", "terbaik", "jago", "terdepan", "gemar", "mewah"},
    'Battery': {"fast charging", "fast charge", "fast charger", "capacity", "battery", "baterai", "batre", "Battery Safety"},
    'Charging Station': {"charging station", "charging", "station", "ngecas", "ngeces"},

}

# Function to apply labels based on groups
def label_based_on_Att(cell_value):
    for group, keywords in Att.items():
        # Check for the presence of the keyword as a standalone word
        if any(re.search(rf'\b{re.escape(keyword)}\b', str(cell_value), flags=re.IGNORECASE) for keyword in keywords):
            return f'{group}'
    return 'Other'  # Default label if no group is matched
Customer['Att'] = Customer['message'].apply(label_based_on_Att)

# Count occurrences of all unique values in the specified column
value_counts = Customer['Att'].value_counts()

# Print the value counts
value_counts.head(50)

Final = pd.concat([Customer, Others], ignore_index=True)

Final.info()

Final.to_excel('/content/EV PART 2.xlsx', index=False)