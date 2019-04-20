import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = "chatbotmlai@gmail.com"

def send_details_to_user(toaddr, restaurants):
    print("sending email to "+toaddr)
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Food has restaurants for you"
    restaurant_names = restaurants['restaurant_name'].values
    restaurant_photo = restaurants['restaurant_photo'].values
    restaurant_location = restaurants['restaurant_address'].values
    restaurant_url = restaurants['restaurant_url'].values
    restaurant_budget = restaurants['budget_for2people'].values
    restaurant_rating = restaurants['restaurant_rating'].values
    body =u'<h2>Foodie has found few restaurants for you:</h2>'
    for i in range(len(restaurant_names)):
        name = restaurant_names[i]
        location = restaurant_location[i]
        image = restaurant_photo[i]
        url = restaurant_url[i]
        budget = restaurant_budget[i]
        rating = restaurant_rating[i]
        #msg.body +="This is final test"
        body += u'<h3>{name} (Rating: {rating})</h3>'.format(name = name, rating = rating)
        body += u'<h4>Address: {locality}</h4>'.format(locality = location)
        body += u'<h4>Average Budget for 2 people: Rs{budget}</h4>'.format(budget = budget)
        body += u'<div dir="ltr">''<a href={url}><img height = "325", width = "450", src={image}></a><br></div>'.format(url = url, image = image)
    msg.attach(MIMEText(body, 'html'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("chatbotmlai@gmail.com", "chatbot123")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)