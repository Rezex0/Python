#Comprehensive 


Domain = ['www.Goggle.com' , 
          'openai.com,'
          'local.host',
          'www.DatawithRupam.com']



cleaned = [
    #Data Transformation
    # For Loop
    # Data Filtering
    d.lower().replace('www.', '')
    for d in Domain
    if '.' in d
]

print(cleaned)