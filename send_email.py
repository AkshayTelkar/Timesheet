import win32com.client


def send_email(receipient,subject):
    const = win32com.client.constants
    obj = win32com.client.Dispatch("Outlook.Application")
    newMail = obj.CreateItem(0)
    newMail.Subject = subject
    newMail.To = receipient
    newMail.send