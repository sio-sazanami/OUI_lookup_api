import csv

i = 1
oui_dic = {}

with open('oui.txt', encoding='UTF-8') as f:
    for row in f:
        if i >= 6:
            if i%6 == 0:# 社名
                oui = row[0:6]
                oui_dic[oui] = {}
            
                company_name = row[22:]
                company_name = company_name.replace('\n','')
                oui_dic[oui]['company_name'] = company_name
                
                if 'Private' in row and '(base 16)' in row:
                    i += 3
                    oui_dic[oui]['address_line'] = None
                    oui_dic[oui]['region'] = None
                
            if i%6 == 1:# 都市名以下
                address_line = row
                address_line = address_line.replace('\t','')
                address_line = address_line.replace('\n','')
                oui_dic[oui]['address_line'] = address_line
                
            if i%6 == 2:# 州・都道府県名と郵便番号
                region = row
                region = region.replace('\t','')
                region = region.replace('\n','')
                oui_dic[oui]['region'] = region
                
            if i%6 == 3:# 国名
                if 'Private' in row and '(base 16)' in row:
                    oui_dic[oui]['country'] = None
                else:
                    country = row
                    country = country.replace('\t','')
                    country = country.replace('\n','')
                    oui_dic[oui]['country'] = country
                    
        i+=1

    path = 'oui.csv'
    with open(path, mode='w') as csv_f:
        writer = csv.writer(csv_f)
        writer.writerow(['oui', 'company_name', 'address_line', 'region', 'country'])
    
    with open(path, mode='a', encoding='UTF-8') as csv_f:
        writer = csv.writer(csv_f)
        for oui in oui_dic:
            writer.writerow([oui, oui_dic[oui]['company_name'], oui_dic[oui]['address_line'], oui_dic[oui]['region'], oui_dic[oui]['country']])