#!/usr/bin/env python3
"""
Codes to match countries to their alphanumeric 3 codes.
Want to work from short official English name to get name in pycountry or directly get alphanumeric 3 codes.
pycountry matches the countries to name on wikipedia i.e. https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3 .
"""
import os
from pathlib import Path
import sys

__projectdir__ = Path(os.path.dirname(os.path.realpath(__file__)) + '/')

# Convert Alternative Country Name into Short Official English Name OLD:{{{1
def commonalternatives_toname():
    d = {}

    # OLD THIS IS OLD

    d['Bolivia (Plurinational State of)'] = 'Bolivia, Plurinational State of'
    d['British Virgin Islands'] = 'Virgin Islands, British'
    d['China, Hong Kong Special Administrative Region'] = 'Hong Kong'
    d['China, Macao Special Administrative Region'] = 'Macao'
    d['Congo, Republic of'] = 'Congo'
    d['Democratic Republic of the Congo'] = 'Congo, The Democratic Republic of the'
    d['Czech Republic'] = 'Czechia'
    d['Faeroe Islands'] = 'Faroe Islands'
    d['Iran (Islamic Republic of)'] = 'Iran, Islamic Republic of'
    d['Micronesia (Federated States of)'] = 'Micronesia, Federated States of'
    d['Republic of Korea'] = 'Korea, Republic of'
    d['Republic of Moldova'] = 'Moldova, Republic of'
    d['Reunion'] = 'Réunion'
    d['Russia'] = 'Russian Federatin'
    d['Sint Maarten'] = 'Sint Maarten (Dutch part)'
    d['State of Palestine'] = 'Palestine, State of'
    d['The former Yugoslav Republic of Macedonia'] = 'Macedonia, Republic of'
    d['Venezuela'] = 'Venezuela, Bolivarian Republic of'
    d['Venezuela, Republica Bolivariana de'] = 'Venezuela, Bolivarian Republic of'

    return(d)

def un_na_alternatives_toname():
    """
    Non-ISO names contained within the UN National Accounts names which are unusual.
    """
    d = {}

    # OLD THIS IS OLD

    d['Ethiopia [up to 1993]'] = 'Ethiopia'
    d['Ethiopia [from 1993]'] = 'Ethiopia'
    # this is a bit simplistic since Sudan did change substantially when South Sudan seceded
    d['Sudan (up to 2011)'] = 'Sudan'
    d['Tanzania - Mainland'] = 'Tanzania, United Republic of'

    return(d)

# Country to Alpha3 Dicts Main Names:{{{1
def alpha3dict_official():
    """
    Get alpha3dict from pycountries
    """
    import pycountry
    alpha3dict = {}

    for country in pycountry.countries:
        alpha3dict[country.name] = country.alpha_3

    return(alpha3dict)


def getown_alpha3dict():
    d = {}

    # areas without codes yet
    d['Kosovo'] = 'XKX'

    # areas that are semi official
    d['Channel Islands'] = 'CHI'

    # countries that no longer exist
    d['Federal Republic of Germany'] = '!WESGER'
    d['Yemen Arab Republic'] = '!NORYEM'
    d['Serbia and Montenegro'] = '!SERMON'
    d['Democratic Yemen'] = '!SOUYEM'
    d['Union of Soviet Socialist Republics'] = '!USSRep'
    d['Yugoslavia'] = '!YUGOSL'

    # countries that changed a lot
    d['Netherlands Antilles'] = '!NETANT'

    return(d)


# Country to Alpha3 Dicts Other Names:{{{1
def commonalternatives(myown = False):
    d = {}

    d['Afghanistan, Islamic Republic of'] = 'AFG'
    d['Bahrain, Kingdom of'] = 'BHR'
    d['Bahamas, The'] = 'BHS'
    d['Bolivia'] = 'BOL'
    d['Bolivia (Plurinational State of)'] = 'BOL'
    d['China, P.R.: Mainland'] = 'CHN'
    d['Cote d\'Ivoire'] = 'CIV'
    d['Democratic Republic of the Congo'] = 'COD'
    d['Congo, Democratic Republic of'] = 'COD'
    d['Congo, Republic of'] = 'COG'
    d['Cape Verde'] = 'CPV'
    d['Curacao'] = 'CUW'
    d['Czech Republic'] = 'CZE'
    d['Faeroe Islands'] = 'FRO'
    d['Micronesia (Federated States of)'] = 'FSM'
    d['Gambia, The'] = 'GMB'
    d['China, Hong Kong Special Administrative Region'] = 'HKG'
    d['China, P.R.: Hong Kong'] = 'HKG'
    d['Iran (Islamic Republic of)'] = 'IRN'
    d['Kyrgyz Republic'] = 'KGZ'
    d['St. Kitts and Nevis'] = 'KNA'
    d['Republic of Korea'] = 'KOR'
    d['St. Lucia'] = 'LCA'
    d['China, Macao Special Administrative Region'] = 'MAC'
    d['China, P.R.: Macao'] = 'MAC'
    d['Moldova'] = 'MDA'
    d['Republic of Moldova'] = 'MDA'
    d['Macedonia, FYR'] = 'MKD'
    d['The former Yugoslav Republic of Macedonia'] = 'MKD'
    d['West Bank and Gaza'] = 'PSE'
    d['Reunion'] = 'REU'
    d['Russia'] = 'RUS'
    d['Serbia, Republic of'] = 'SRB'
    d['Slovak Republic'] = 'SVK'
    d['Sint Maarten'] = 'SXM'
    d['State of Palestine'] = 'PSE'
    d['Tanzania'] = 'TZA'
    d['St. Vincent and the Grenadines'] = 'VCT'
    d['Venezuela'] = 'VEN'
    d['British Virgin Islands'] = 'VGB'
    d['Venezuela, Republica Bolivariana de'] = 'VEN'
    d['Vietnam'] = 'VNM'
    d['Yemen, Republic of'] = 'YEM'

    # countries that no longer exist
    if myown is True:
        d['Germany, Federal Republic of'] = '!WESGER'
        d['Yemen Arab Republic [former]'] = '!NORYEM'
        d['Serbia and Montenegro'] = '!SERMON'
        d['Democratic Yemen [former]'] = '!SOUYEM'
        d['Union of Soviet Socialist Republics [former]'] = '!USSRep'
        d['Yugoslavia [former Socialist Federal Republic]'] = '!YUGOSL'

    return(d)

def un_na_alternatives():
    """
    Non-ISO names contained within the UN National Accounts names which are unusual.
    """
    d = {}

    d['Ethiopia [up to 1993]'] = 'ETH'
    d['Ethiopia [from 1993]'] = 'ETH'
    # this is a bit simplistic since Sudan did change substantially when South Sudan seceded
    d['Sudan (up to 2011)'] = 'SDN'
    # bit simplistic since probably ignores Zanzibar
    d['Tanzania - Mainland'] = 'TZA'

    return(d)

# Composite Alpha3 Functions:{{{1
def getalpha3list(myown = False):
    alpha3list = []
    alpha3dict_off = alpha3dict_official()
    alpha3list = alpha3list + [alpha3dict_off[country] for country in alpha3dict_off]
    if myown is True:
        ownalpha3dict = getown_alpha3dict()
        alpha3list = alpha3list + [ownalpha3dict[country] for country in ownalpha3dict]
    return(alpha3list)


def alpha3dict_all(myown = False, unusualalternatives = True):
    """
    I see no reason not to include unusual alternatives
    """
    alpha3dict = alpha3dict_official()

    if myown is True:
        alpha3dict.update(getown_alpha3dict())

    alternativenamesdict = commonalternatives(myown = myown)
    alternativenamesdict.update(un_na_alternatives())

    # check alpha3s from alternativenamesdict are still valid
    goodalpha3s = set([alpha3dict[countryname] for countryname in alpha3dict])
    badalpha3s = []
    for country in alternativenamesdict:
        if alternativenamesdict[country] not in goodalpha3s:
            badalpha3s.append(alternativenamesdict[country])
    if len(badalpha3s) > 0:
        print(badalpha3s)
        raise ValueError('Need to update alpha3 term in alternative names functions.')

    alpha3dict.update(alternativenamesdict)

    return(alpha3dict)


# Check Alpha3 Codes:{{{1
def checkalpha3(alpha3tocheck, alpha3ok = None, knownbadalpha3 = None, myown = False, raise_error = False):
    """
    Check alpha3 list to see whether correct.
    alpha3tocheck is list of alpha3 codes to check are ok.
    alpha3ok is a list of alpha3 codes which are ok.
    """
    if knownbadalpha3 is None:
        knownbadalpha3 = []

    # just use standard alpha3 if I haven't specified which alpha3 are ok
    if alpha3ok is None:
        alpha3ok = getalpha3list(myown = myown)

    goodalpha3 = []
    unknownbadalpha3 = []
    for alpha3 in alpha3tocheck:
        if alpha3 in alpha3ok:
            goodalpha3.append(alpha3)
        else:
            if alpha3 not in knownbadalpha3:
                unknownbadalpha3.append(alpha3)

    if len(unknownbadalpha3) > 0:
        if raise_error is True:
            print(unknownbadalpha3)
            raise ValueError('Some alpha3 country codes do not exist in alpha3ok.')
        else:
            print('Warning: The Following alpha3 country codes are not in alpha3ok.')
            print(unknownbadalpha3)

    return(goodalpha3)


def checkalpha3_df(df, alpha3column, alpha3ok = None, knownbadalpha3 = [], myown = False, raise_error = False, deletebad = False):
    alpha3tocheck = list(set(df[alpha3column]))
    # try to sort
    try:
        alpha3tocheck = sorted(alpha3tocheck)
    except Exception:
        None

    if alpha3ok is None:
        alpha3ok = getalpha3list(myown = myown)

    goodalpha3 = checkalpha3(alpha3tocheck, alpha3ok = alpha3ok, knownbadalpha3 = knownbadalpha3, myown = myown, raise_error = raise_error)

    if deletebad is True:
        df = df.loc[df[alpha3column].isin(goodalpha3)]

    return(df)

    
# Add Alpha3 From Country Names:{{{1
def checkcountrynames(countrynames, alpha3dict = None, knownbadnames = None, myown = False, raise_error = False):
    """
    Check all countrynames in list have an alpha3 equivalent in alpha3dict
    """
    if knownbadnames is None:
        knownbadnames = []

    # just use standard alpha3 if I haven't specified which alpha3 are ok
    if alpha3dict is None:
        alpha3dict = alpha3dict_all(myown = myown)

    goodnames = []
    unknownbadnames = []
    for name in countrynames:
        if name in alpha3dict:
            goodnames.append(name)
        else:
            if name not in knownbadnames:
                unknownbadnames.append(name)

    if len(unknownbadnames) > 0:
        if raise_error is True:
            print(unknownbadnames)
            raise ValueError('Some country names do not exist in alpha3dict.')
        else:
            print('Warning: The Following alpha3 country names are not in alpha3dict.')
            print(unknownbadnames)

    return(goodnames)


def convertnamestoalpha3_df(df, countrynamecolumn, alpha3column = None, replacecountrynamecolumn = False, alpha3dict = None, knownbadnames = [], myown = False, raise_error = False, deletebad = False):

    if replacecountrynamecolumn is True:
        alpha3column = countrynamecolumn
    else:
        if 'country' not in df.columns:
            alpha3column = 'country'
        else:
            raise ValueError('Need to specify alpha3column name. The default of country is already taken.')

    countrynames = sorted(list(set(df[countrynamecolumn])))

    if alpha3dict is None:
        alpha3dict = alpha3dict_all(myown = myown)

    goodnames = checkcountrynames(countrynames, alpha3dict = alpha3dict, knownbadnames = knownbadnames, myown = myown, raise_error = raise_error)

    if deletebad is True:
        # need to add .copy() otherwise get errors later
        df = df.loc[df[countrynamecolumn].isin(goodnames)].copy()

    # note that if there is no match, the map just gives NaN
    df[alpha3column] = df[countrynamecolumn].map(alpha3dict)

    return(df)

    
