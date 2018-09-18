import pandas as pd
import xlrd
from warranty.models import Sales

def clean_sn(sn):
    new_sn=sn.strip('-')
    return new_sn

def convt(excel_time):
    print(excel_time)
    ret=(pd.to_datetime('1899-12-30') + pd.to_timedelta(excel_time,'D')).to_pydatetime()
    print(excel_time)
    return ret

data=xlrd.open_workbook('P21 Sales.xlsx')
t=data.sheets()[0]
r_max=t.nrows
c_max=t.ncols

for i in range(1,r_max):
    sn=t.cell(i,1).value
    if sn!="NULL":
        newsale=Sales()
        
        newsale.sn=sn.replace("-","")
        newsale.item_id=t.cell(i,2).value
        newsale.branch_id=t.cell(i,3).value
        newsale.customer_id=t.cell(i,4).value
        newsale.bill2_name=t.cell(i,5).value
        newsale.transaction=t.cell(i,6).value
        tt=t.cell(i,7).value
        time=(pd.to_datetime('1899-12-30') + pd.to_timedelta(tt,'D')).to_pydatetime()
        #print(sn,time)
        newsale.date=time
        newsale.ship2_contact=t.cell(i,8).value
        newsale.ship2_name=t.cell(i,9).value
        newsale.ship2_address1=t.cell(i,10).value
        newsale.ship2_address2=t.cell(i,11).value
        newsale.ship2_city=t.cell(i,12).value
        newsale.ship2_state=t.cell(i,13).value
        newsale.ship2_zip=t.cell(i,14).value
        newsale.save()

    
    

    



