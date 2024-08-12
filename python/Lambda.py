Members = [{"name": "Chioma Opara", "Spouse Name": "Obinna Opara", "Location": "Lagos, Nigeria"},
           {"name": "Chika Anosike", "Spouse Name": "Benson Newman", "Location": "Abuja, Nigeria"},
           {"name": "Amarachi Egemonye", "Spouse Name": "Ebuka Egemonye", "Location": "Kaduna, Nigeria"}]


Members.sort(key = lambda member : member["Location"])

print(Members)