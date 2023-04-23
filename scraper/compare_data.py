import pandas as pd

#!CHANGE THIS TO THE FILENAME OF THE CSV FILE YOU WANT TO COMPARE WITH

#Read in the data from 'Rumah.comdataset.csv' -> final dataset
final = pd.read_csv('Rumah.comdataset_v1.csv')
#Read in the data from 'Rumah.com3.csv'
df3 = pd.read_csv('Rumah.com3.csv')

#Print out the count of rows which are in df3 but not in final
print(len(df3[~df3['ID'].isin(final['ID'])]))
#Print out the count of rows which are in df3 but not in final (by using Property Link) -> DONT USE PROPERTY LINK
print(len(df3[~df3['Property Link'].isin(final['Property Link'])]))
#Save the count of rows which are in df3 but not in final to a dataframe
df3_not_in_final = df3[~df3['ID'].isin(final['ID'])]
#Check for each row in df3_not_in_final, if there is a row in final which has the same Price, Street Address, Bed, Bath, Listing Area, Certificate, Jakarta Division
#If there is, add to count
count = 0
for index, row in df3_not_in_final.iterrows():
    if len(final[(final['Price'] == row['Price']) & (final['Street Address'] == row['Street Address']) & (final['Bed'] == row['Bed']) & (final['Bath'] == row['Bath']) & (final['Listing Area'] == row['Listing Area']) & (final['Certificate'] == row['Certificate']) & (final['Jakarta Division'] == row['Jakarta Division'])]) != 0:
        #Print out the row ID of both final and df3_not_in_final
        count += 1
        #Remove the row from df3_not_in_final
        df3_not_in_final = df3_not_in_final.drop(index)
print(count, "rows removed since they are basically duplicates")
#Print the current length of df3_not_in_final
print(len(df3_not_in_final), "rows left in df3_not_in_final")

#Add the rows in df3_not_in_final to RUmah.comdataset.csv
final = final.append(df3_not_in_final, ignore_index=True)
#Save the final dataframe to a csv file -> latest version: v2, updated on 04/13/2023
final.to_csv('Rumah.comdataset_v2.csv', index=False)