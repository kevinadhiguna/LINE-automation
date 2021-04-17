# Import 'requests' library to send an HTTP request
import requests

# Import 'datetime' library to to work with dates
import datetime

# Put datetime in your timezone to a variable
time = datetime.datetime.now(pytz.timezone('Europe/Paris')) # <- Please change to your timezone. Reference of pytz timezone : https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568

# Format datetime
formattedTime = time.strftime('%Y-%m-%d %H:%M:%S') # <- For example, this will format 'datetime.datetime(2021, 4, 17, 19, 59, 23, 402043, tzinfo=<DstTzInfo 'Europe/Paris' CEST+2:00:00 DST>)' to '2021-04-17 19:59:23'

# Place your LINE Notify token here
token = 'YOUR_LINE_Notify_TOKEN'

# The API url of LINE Notify
api_url = 'https://notify-api.line.me/api/notify'

# Send the formatted datetime as a message that will be sent
message = formattedTime # <- Feel free to replace this with any kind of message that you want. For instance, 'Are you happy today ? Take care.'

# Convert LINE Notify token to dictionary
token_dict = { 'Authorization': 'Bearer' + ' ' + token }

# Convert message to dictionary
msg_dict = { 'message': message }

# Place the image filename (Supported image format are png and jpeg, according to the LINE Notify API docs)
image = './my-picture.png'

# Open the image in binary format for reading
binary = open(image, mode='rb')

# Convert your image file to dictionary
img_dict = { 'imageFile': binary }

# Send the image and the message
requests.post(
  api_url,            # <- Send to the API url : 'https://notify-api.line.me/api/notify'
  headers=token_dict, # <- Set the LINE Notify token to the headers (for authentication)
  data=msg_dict,      # <- Send your message through a LINE Notify account
  files=img_dict      # <- Send your image through a LINE Notify account
)

# HTTP Response Status -> 200: success, 400: Bad request, 401: Invalid access token
