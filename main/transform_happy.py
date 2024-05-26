import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt




import pandas as pd

def transformar_datasets(happiness_2015, happy_2016, happier_2017, happiest_2018, happierness_2019):
    
        # Añadir columna de año
    happiness_2015['year'] = 2015
    happy_2016['year'] = 2016
    happier_2017['year'] = 2017
    happiest_2018['year'] = 2018
    happierness_2019['year'] = 2019

    # Eliminar valores nulos del dataset de 2018
    happiest_2018 = happiest_2018.dropna(subset=['Perceptions of corruption'])
    
    
    
    # Eliminar columnas innecesarias
    happiness_2015 = happiness_2015.drop(columns=['Region', 'Standard Error', 'Dystopia Residual'])
    happy_2016 = happy_2016.drop(columns=['Region', 'Lower Confidence Interval', 'Upper Confidence Interval', 'Dystopia Residual'])
    happier_2017 = happier_2017.drop(columns=['Whisker.high', 'Whisker.low', 'Dystopia.Residual'])

    # Renombrar columnas
    rename_dict_2017 = {
        'Country': 'country',
        'Happiness.Rank': 'happiness_rank',
        'Happiness.Score': 'happiness_score',
        'Economy..GDP.per.Capita.': 'economy',
        'Health..Life.Expectancy.': 'life_expectancy',
        'Freedom': 'freedom',
        'Generosity': 'generosity',
        'Trust..Government.Corruption.': 'government_corruption',
        'Family': 'social_support'
    }

    rename_dict_2018_2019 = {
        'Country or region': 'country',
        'Score': 'happiness_score',
        'GDP per capita': 'economy',
        'Social support': 'social_support',
        'Healthy life expectancy': 'life_expectancy',
        'Freedom to make life choices': 'freedom',
        'Generosity': 'generosity',
        'Perceptions of corruption': 'government_corruption',
        'Overall rank': 'happiness_rank'
    }

    happiness_2015.rename(columns={
        'Country': 'country',
        'Happiness Rank': 'happiness_rank',
        'Happiness Score': 'happiness_score',
        'Economy (GDP per Capita)': 'economy',
        'Health (Life Expectancy)': 'life_expectancy',
        'Freedom': 'freedom',
        'Generosity': 'generosity',
        'Trust (Government Corruption)': 'government_corruption',
        'Family': 'social_support'
    }, inplace=True)

    happy_2016.rename(columns={
        'Country': 'country',
        'Happiness Rank': 'happiness_rank',
        'Happiness Score': 'happiness_score',
        'Economy (GDP per Capita)': 'economy',
        'Health (Life Expectancy)': 'life_expectancy',
        'Freedom': 'freedom',
        'Generosity': 'generosity',
        'Trust (Government Corruption)': 'government_corruption',
        'Family': 'social_support'
    }, inplace=True)

    happier_2017.rename(columns=rename_dict_2017, inplace=True)
    happiest_2018.rename(columns=rename_dict_2018_2019, inplace=True)
    happierness_2019.rename(columns=rename_dict_2018_2019, inplace=True)




    # Concatenar los datasets
    happy_df = pd.concat([happiness_2015, happy_2016, happier_2017, happiest_2018, happierness_2019], ignore_index=True)

    # Agregar continente
    pais_a_continente = {
        'Switzerland': 'Europe',
        'Iceland': 'Europe',
        'Denmark': 'Europe',
        'Norway': 'Europe',
        'Canada': 'North America',
        'Finland': 'Europe',
        'Netherlands': 'Europe',
        'Sweden': 'Europe',
        'New Zealand': 'Oceania',
        'Australia': 'Oceania',
        'Israel': 'Asia',
        'Costa Rica': 'North America',
        'Austria': 'Europe',
        'Mexico': 'North America',
        'United States': 'North America',
        'Brazil': 'South America',
        'Luxembourg': 'Europe',
        'Ireland': 'Europe',
        'Belgium': 'Europe',
        'United Arab Emirates': 'Asia',
        'United Kingdom': 'Europe',
        'Oman': 'Asia',
        'Venezuela': 'South America',
        'Singapore': 'Asia',
        'Panama': 'North America',
        'Germany': 'Europe',
        'Chile': 'South America',
        'Qatar': 'Asia',
        'France': 'Europe',
        'Argentina': 'South America',
        'Czech Republic': 'Europe',
        'Uruguay': 'South America',
        'Colombia': 'South America',
        'Thailand': 'Asia',
        'Saudi Arabia': 'Asia',
        'Spain': 'Europe',
        'Malta': 'Europe',
        'Taiwan': 'Asia',
        'Kuwait': 'Asia',
        'Suriname': 'South America',
        'Trinidad and Tobago': 'North America',
        'El Salvador': 'North America',
        'Guatemala': 'North America',
        'Uzbekistan': 'Asia',
        'Slovakia': 'Europe',
        'Japan': 'Asia',
        'South Korea': 'Asia',
        'Ecuador': 'South America',
        'Bahrain': 'Asia',
        'Italy': 'Europe',
        'Bolivia': 'South America',
        'Moldova': 'Europe',
        'Paraguay': 'South America',
        'Kazakhstan': 'Asia',
        'Slovenia': 'Europe',
        'Lithuania': 'Europe',
        'Nicaragua': 'North America',
        'Peru': 'South America',
        'Belarus': 'Europe',
        'Poland': 'Europe',
        'Malaysia': 'Asia',
        'Croatia': 'Europe',
        'Libya': 'Africa',
        'Russia': 'Europe/Asia',
        'Jamaica': 'North America',
        'North Cyprus': 'Europe',
        'Cyprus': 'Europe',
        'Algeria': 'Africa',
        'Kosovo': 'Europe',
        'Turkmenistan': 'Asia',
        'Mauritius': 'Africa',
        'Hong Kong': 'Asia',
        'Estonia': 'Europe',
        'Indonesia': 'Asia',
        'Vietnam': 'Asia',
        'Turkey': 'Europe/Asia',
        'Kyrgyzstan': 'Asia',
        'Nigeria': 'Africa',
        'Bhutan': 'Asia',
        'Azerbaijan': 'Asia',
        'Pakistan': 'Asia',
        'Jordan': 'Asia',
        'Montenegro': 'Europe',
        'China': 'Asia',
        'Zambia': 'Africa',
        'Romania': 'Europe',
        'Serbia': 'Europe',
        'Portugal': 'Europe',
        'Latvia': 'Europe',
        'Philippines': 'Asia',
        'Somaliland region': 'Africa',
        'Morocco': 'Africa',
        'Macedonia': 'Europe',
        'Mozambique': 'Africa',
        'Albania': 'Europe',
        'Bosnia and Herzegovina': 'Europe',
        'Lesotho': 'Africa',
        'Dominican Republic': 'North America',
        'Laos': 'Asia',
        'Mongolia': 'Asia',
        'Swaziland': 'Africa',
        'Greece': 'Europe',
        'Lebanon': 'Asia',
        'Hungary': 'Europe',
        'Honduras': 'North America',
        'Tajikistan': 'Asia',
        'Tunisia': 'Africa',
        'Palestinian Territories': 'Asia',
        'Bangladesh': 'Asia',
        'Iran': 'Asia',
        'Ukraine': 'Europe',
        'Iraq': 'Asia',
        'South Africa': 'Africa',
        'Ghana': 'Africa',
        'Zimbabwe': 'Africa',
        'Liberia': 'Africa',
        'India': 'Asia',
        'Sudan': 'Africa',
        'Haiti': 'North America',
        'Congo (Kinshasa)': 'Africa',
        'Nepal': 'Asia',
        'Ethiopia': 'Africa',
        'Sierra Leone': 'Africa',
        'Mauritania': 'Africa',
        'Kenya': 'Africa',
        'Djibouti': 'Africa',
        'Armenia': 'Asia',
        'Botswana': 'Africa',
        'Myanmar': 'Asia',
        'Georgia': 'Asia/Europe',
        'Malawi': 'Africa',
        'Sri Lanka': 'Asia',
        'Cameroon': 'Africa',
        'Bulgaria': 'Europe',
        'Egypt': 'Africa',
        'Yemen': 'Asia',
        'Angola': 'Africa',
        'Mali': 'Africa',
        'Congo (Brazzaville)': 'Africa',
        'Comoros': 'Africa',
        'Uganda': 'Africa',
        'Senegal': 'Africa',
        'Gabon': 'Africa',
        'Niger': 'Africa',
        'Cambodia': 'Asia',
        'Tanzania': 'Africa',
        'Madagascar': 'Africa',
        'Central African Republic': 'Africa',
        'Chad': 'Africa',
        'Guinea': 'Africa',
        'Ivory Coast': 'Africa',
        'Burkina Faso': 'Africa',
        'Afghanistan': 'Asia',
        'Rwanda': 'Africa',
        'Benin': 'Africa',
        'Syria': 'Asia',
        'Burundi': 'Africa',
        'Togo': 'Africa',
        'Puerto Rico': 'North America',
        'Belize': 'North America',
        'Somalia': 'Africa',
        'Somaliland Region': 'Africa',
        'Namibia': 'Africa',
        'South Sudan': 'Africa',
        'Taiwan Province of China': 'Asia',
        'Hong Kong S.A.R., China': 'Asia',
        'Trinidad & Tobago': 'North America',
        'Northern Cyprus': 'Europe',
        'North Macedonia': 'Europe',
        'Gambia': 'Africa'
    }

    happy_df['continent'] = happy_df['country'].map(pais_a_continente)

    # Crear variables dummy para continentes
    if 'continent' in happy_df.columns:
        columns_to_drop = [col for col in happy_df.columns if col.startswith('continent_')]
        happy_df = happy_df.drop(columns=columns_to_drop)
        happy_df = pd.get_dummies(happy_df, columns=['continent'], drop_first=True)
        dummy_columns = happy_df.columns[happy_df.columns.str.startswith('continent_')]
        happy_df[dummy_columns] = happy_df[dummy_columns].astype(int)

    # Eliminar columnas innecesarias
    happy_df = happy_df.drop(columns=['country', 'happiness_rank'])

    return happy_df











