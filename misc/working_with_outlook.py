import os
import win32com.client

mapi = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

def itermsg(folder, folderName):
    if folder.Folders.Count > 0:
        for subfolder in folder.Folders:
            for msg in itermsg(subfolder, folderName):
                yield msg
    elif folder.Name == folderName:
        for msg in folder.Items:
            yield msg

for msg in mapi.Folders["maxchen@example.com"].Folders["Inbox"].Items:
    print("From:", msg.Sender, msg.SenderEmailAddress)
    print("Sent:", msg.SentOn)
    print("To:", msg.To)
    print("Cc:", msg.Cc)
    print("Subject:", msg.Subject)
    print("--------------------------------------------------------------------------------")
    print(msg.Body)
    for attachment in msg.Attachments:
        attachment.SaveAsFile(os.path.join(outdir, attachment.FileName))

# https://docs.microsoft.com/en-us/office/vba/api/outlook.mailitem
