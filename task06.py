emails = (("Ali", "ali@gmail.com"), 
          ("Vali", "vali@yandex.ru"), 
          ("Sami", "sami@mail.ru"))
domains = [email.split("@")[1] for _, email in emails]
print(domains)