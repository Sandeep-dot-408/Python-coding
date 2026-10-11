import smtplib

my_email = "sandeep.kannan1220@gmail.com"
password = "tpmc ohps tlgi cngf"

connection = smtplib.SMTP("smtp.gmail.com", 587)

connection.starttls()

connection.login(my_email, password)

connection.sendmail(
    from_addr=my_email,
    to_addrs="sandeep.kannan1220@gmail.com",
    msg="Subject: Birthday Wishes\n\nHello"
)

connection.close()