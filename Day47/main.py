from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

URL = "https://www.amazon.in/BennettTM-Shoulder-Messenger-Repellent-Charcoal/dp/B09CV24TMK/ref=sr_1_3?adgrpid=64471928812&ext_vrnc=hi&gclid=Cj0KCQjwnbmaBhD-ARIsAGTPcfWko3tXaobLgwASa7a2iY80aDXCawTCunu_lcfvASueaLtJSFtp29oaArBpEALw_wcB&hvadid=398029155303&hvdev=m&hvlocphy=9061675&hvnetw=g&hvqmt=e&hvrand=15764430260151565001&hvtargid=kwd-333783408956&hydadcr=13040_1996776&keywords=mens%2Blaptop%2Bshoulder%2Bbags&qid=1677167343&sr=8-3&th=1"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(response.content, "lxml")
price = soup.find(class_="a-price-whole").getText()

price_as_float = float(price)

# selqbukyrgymnokj

if price_as_float > 100:
    email = "punitmann9599@gmail.com"
    password = "selqbukyrgymnokj"

# email = "punit.kumar@knowlarity.com"
# password = "Punit@mann"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password = password)
        connection.sendmail(
            from_addr=email,
            to_addrs="punitmann9599@gmail.com",
            msg="Subject:Email check\n\n Hurry up!."
        )
    connection.quit()