import cookies as c

cookies = c.Cookies()

#read table cookies total 10
cookies.get_all()

#placeholders for name, quantity, price
cookies.insert_cookies('chocolate chip', '4 dozen', 15)

#placeholders for name and price
cookies.update_cookies('coconut macaroons', 5)

#delete id_cookies 7 sugar cookies
cookies.delete_cookies(7)
