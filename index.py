import pandas as pd
import datetime
import smtplib




GMAIL_ID = '8228935781r@gmail.com'
GMAIL_PSWD = '****add****'

def sendEmail(to,sub,msg):
    print(f"Email to {to} sent with subject: {sub} and message {msg}" )
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(GMAIL_ID,GMAIL_PSWD)
    s.sendmail(GMAIL_ID, to, f"subject : {sub}\n\n{msg}")
    s.quit()
    




if __name__=="__main__":
    sendEmail(GMAIL_ID,"subject","text message")
    
    
    
    df = pd.read_excel("Book1.xlsx")
    today = datetime.datetime.now().strftime("%d-%m")
    for index, item in df.iterrows():
        bday = item['Birthday'].strftime("%d-%m")
        # print(bday)
        if(today == bday):
            sendEmail(item['Email'],"Happy Birthday",item['Dialogue'])
            