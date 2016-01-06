#!/usr/bin/python
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import requests, json, sys

item_name = sys.argv[1]
value = sys.argv[2]


final_result = {}

try:
    f = open("Sources/" + item_name + ".txt", "r")

    html = f.read()
    f.close()

    soup = BeautifulSoup(html)




    ################## GRAB COMPANY NAME #####################
    comp_table = soup.find("td", {"width":"100%", "bgcolor":"#FFFFFF"})
    company_name =  comp_table.get_text().replace("Company Name: ", '').strip()


    ####################   Grab Data from Market Information    #########################
    table_params = {'width':'100%', 'border':'0', 'cellpadding':'0', 'bgcolor':'#C0C0C0'}
    market_info_tables = soup.find_all("table", table_params)
    ###################    First Table ####################################
    #m_i_table_params ={'width':"100%", 'border':'0', 'cellpadding':'0', 'cellspacing':'1', 'bgcolor':'#C0C0C0'}
    m_i_table = market_info_tables[0]
    values=[]
    for td in m_i_table.find_all("tr"):
        values.append(td.text)


    lastTrade = str(values[1])
    lastTrade = lastTrade.replace("Last Trade:", "").strip()
    change_num = str(values[4]).strip()
    change_percentage = str(values[5]).strip()
    open_price = str(values[7]).replace("Open Price", "").strip()
    adjust_open_price = str(values[8]).replace("Adjusted Open Price", "").strip()
    yesterday_close_price = str(values[9]).replace("Yesterday Close Price", "").strip()

    ######### GRAB DATA FROM SECOND TABLE(Market Info Continue) ##################

    second_table = market_info_tables[1]
    values_second_table=[]
    for td in second_table.find_all("tr"):
        values_second_table.append(td.text)


    closePrice = str(values_second_table[1]).replace("Close Price",'').strip()
    daysRange = str(values_second_table[3]).replace("Day's Range", '').strip()
    volume = str(values_second_table[5]).replace("Volume", '').strip()
    totalTrade = str(values_second_table[7]).replace("Total Trade", "").strip()
    market_capital = str(values_second_table[9]).replace("Market Cap in BDT*", "").strip()

    #########      WE ARE DONE WITH MARKET INFO TABLE #####################

    ################## BASIC INFORMATION ########################
    basicinfo_table_params = {"border":"1", "width":"100%", "bgcolor":"#C0C0C0"}
    basicinfo_table = soup.find("table", basicinfo_table_params)
    values_basic_info = []
    for tr in basicinfo_table.find_all("tr"):
        for td in tr.find_all("td"):
            values_basic_info.append(td)
    values = []
    basicinfo_table = values_basic_info[0].find("table")
    for row in basicinfo_table.find_all("tr"):
        cells = row.find_all("td")
        for cell in cells:
            if(cell.get_text().strip()!=""):
                values.append(cell.get_text().strip())

    authorized_capital =  values[2]
    paidupvalue = values[6]
    weekRange = values[4]
    facevalue = values[9]
    marketLot =  values[11]
    noofsecurities =  values[13]
    segment = values[15]
    ############### END OF BASIC INFORMATION ############




    ################ P/E Ratio ######################

    peratio_table_params = {"width":"422", "border":"1"}
    peratio_table = soup.find("table", peratio_table_params)


    values = []
    for row in peratio_table.find_all("tr"):
        cells = row.find_all("td")
        for cell in cells:

                values.append(cell.get_text().strip())
    peratio_basic = values[4]
    peratio_diluted = values[5]
    print peratio_diluted


    ############################ FINANCIAL PERFORMANCE ##########################
    table_params = {'border':"1", 'width':"100%", 'cellspacing':"0", 'cellpadding':"0"}

    fp_table = soup.find_all("table", table_params)[1]
    values = []
    for row in fp_table.find_all("tr"):
        cells = row.find_all("td")
        for cell in cells:

                values.append(cell.get_text().strip())

    #2013 Year index - 131
    eps_2013 = values[132]
    netassetvalue_2013 = values[136]

    netprofit_continue_2013 = values[138]

    netprofit_extraordinary_2013 = values[139]
    #2014 Year Index - 140

    eps_2014 = values[141]
    netassetvalue_2014 = values[145]
    netprofit_continue_2014 = values[147]
    netprofit_extraordinary_2014 = values[148]

    ######## DIVIDEND ##############
    table_params = {'border':"1", 'width':"100%", 'cellspacing':"0", 'cellpadding':"0"}

    dividend_table = soup.find_all("table", table_params)[2]
    values = []
    for row in dividend_table.find_all("tr"):
        cells = row.find_all("td")
        for cell in cells:
                values.append(cell.get_text().strip())


    dividend_2014 = values[80]
    dividend_2013 = values[75]
    dividend_2012 = values[70]
    dividend_2011 = values[65]
    dividend_2010 = values[60]
    dividend_2009 = values[55]

    #################### HISTORY AND OTHERS #########################
    table_params = {'border':"1", 'width':"100%", 'cellspacing':"0", 'cellpadding':"0"}

    history_table = soup.find_all("table", table_params)[0]

    values = []
    for row in history_table.find_all("tr"):
        cells = row.find_all("td")
        for cell in cells:
                values.append(cell.get_text().strip())

    lastAgm =  values[0].replace("Last AGM Held:", '').strip()
    bonusIssue = values[3]
    rightIssue = values[7]
    yearEnd = values[11]
    reserveandsurplus = values[15]

    ################## SHARE PERCENTAGE ####################
    table_params = {"border":"1", "cellpadding":"0", "cellspacing":"0", "width":"100%", "bgcolor":"#C0C0C0"}
    sp_table = soup.find_all("table", table_params)[1]
    values = []
    for row in sp_table.find_all("tr"):
        cells = row.find_all("td")
        for cell in cells:
                values.append(cell.get_text().strip())

    marketCatagory = values[7]
    sponsor = values[16].replace("Sponsor/Director",'').strip();
    govt = values[17].replace("Govt.", '').strip()
    institute = values[18].replace("Institute", '').strip()
    foreign = values[19].replace("Foreign", '').strip()
    public = values[20].replace("Public", "").strip()


    ####### GATHER ALL AND ADDEM TOGETHER
    final_result["data1"] = closePrice
    final_result["data2"] = yesterday_close_price
    final_result["data3"] = open_price
    final_result["data4"] = adjust_open_price
    final_result["data5"] = daysRange
    final_result["data6"] = volume
    final_result["data7"] = totalTrade
    final_result["data8"] = market_capital
    final_result["data9"] = authorized_capital
    final_result["data10"] = paidupvalue
    final_result["data11"] = facevalue
    final_result["data12"] = noofsecurities
    final_result["data13"] = weekRange
    final_result["data14"] = marketLot
    final_result["data15"] = segment
    final_result["data16"] = rightIssue
    final_result["data17"] = yearEnd
    final_result["data18"] = reserveandsurplus
    final_result["data19"] = bonusIssue
    final_result["data20"] = company_name
    final_result["data21"] = lastTrade
    final_result["data22"] = change_num
    final_result["data23"] = change_percentage
    final_result["data24"] = lastAgm
    final_result["p_e_ratio_basic"] = peratio_basic
    final_result["p_e_ratio_diluted"] = peratio_diluted
    final_result["marketcatagory"] = marketCatagory
    final_result["fp2013_epscontinueoperation"] = eps_2013
    final_result["fp2013_NAV"] = netassetvalue_2013
    final_result["fp2013_NPATcontinueoperation"] = netprofit_continue_2013
    final_result["fp2013_NPATextraordinaryincome"] = netprofit_extraordinary_2013
    final_result["fp2014_epscontinueoperation"] = eps_2014
    final_result["fp2014_NAV"] = netassetvalue_2014
    final_result["fp2014_NPATextraordinaryincome"] = netprofit_extraordinary_2014
    final_result["fp2014_NPATcontinueoperation"] = netprofit_continue_2014
    final_result["fpcontinue_dividend_2009"] = dividend_2009
    final_result["fpcontinue_dividend_2010"] = dividend_2010
    final_result["fpcontinue_dividend_2011"] = dividend_2011
    final_result["fpcontinue_dividend_2012"] = dividend_2012
    final_result["fpcontinue_dividend_2013"] = dividend_2013
    final_result["fpcontinue_dividend_2014"] = dividend_2014
    final_result["sp_sponsor_director"] = sponsor
    final_result["sp_govt"] = govt
    final_result["sp_institute"] = institute
    final_result["sp_foreign"] = foreign
    final_result["sp_public"] = public
    final_result["value(mn)"] = value

    json_converted = json.dumps(final_result)
    #f = open("/var/www/html/dev/smartdsefiles/dsex_items/" + item_name + ".txt", "w+")
    f = open(item_name + ".txt", "w+")
    f.write("[" + json_converted + "]")
    f.close()
except:
    pass


#rows = soup.find("table").find("tbody").find_all("tr")

#i = 0
#for row in rows:
#    cells = row.find_all("td")

#    print cells[0].find_all("tr")




