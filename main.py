from tkinter import Tk
import view
import send_email
import datetime
import sys


if __name__ == '__main__':
    datetime = datetime.datetime.now()
    date = datetime.strftime('%d/%m/%Y')


    projects = {'PDM Report':1,'Brio to SSRS':2,'CPE -NA':3,'CPE- SAPL':4,'Evergreen':5,'QV Monitoring':6,'QV-Power BI':7,'WebFocus':8,
                'IICE':9,'Sales Cube':10,'DMM':11,'Learning':12,'Cognos-PBI':13,'IO Modelling':14,'FIDO':15,'DBA':16,'Bedrock':17}
    receipient = 'akshay.telkar@intimetec.com'

    window = Tk()
    view.createwindowpane(window)

    if view.status == 'submit':
        prjhours = ''
        for i in range(len(view.finallist)):
            if i == 0:
                prjhours = prjhours + str(projects[view.finallist[i]]) + ' ' + str(view.hours[i])
            else:
                prjhours = prjhours + ',' + str(projects[view.finallist[i]]) + ' ' + str(view.hours[i])

        send_email.send_email(receipient, 'Timesheet ' + prjhours + ' ' + str(date))
    else:
        sys.exit()
