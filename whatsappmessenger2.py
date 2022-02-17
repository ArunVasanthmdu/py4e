import pywhatkit
import pandas
df = pandas.read_csv(r'c:\temp\contacts.csv')
for index, row in df.iterrows():
  print("Sending message to ",row['contactname'])
  mobileno=row['mobileno']
  mobileno=mobileno.replace("#","")
  mycaption="We thank you for your continued support for our DMK-led alliance.Urban local body election is approaching on 19 Feb 2022. Our DMK alliance congress canditate ✋ Mr.K.BALASUBRAMANIAM is contesting in urban local body election to serve to our society. Please support us with your valuable votes. - By Election Task Team."
  #Note: This is promotion message for upcoming election will, you will receive few posters for few days. If you dont like please reply with DND,we stop sending messages. Thank you!
  #pywhatkit.sendwhats_image(phone_no= mobileno, img_path=r'C:\Temp\poster1.jpeg', caption = mycaption,tab_close =True)
  pywhatkit.sendwhats_image(phone_no= mobileno, img_path=r'C:\Temp\poster1.jpeg')
  print("Sent message to ",row['contactname'])
