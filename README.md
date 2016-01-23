# Test_Affinite
Test - Affine


Requirements:
1. Python 2.7.6
2. Django 1.9
3. Pillow - To store images.


Process:

Urls:
1. 127.0.0.1:8000/ - Home page (welcome page for Buyers).
2. 127.0.0.1:8000/shoe_list   - This API will return all the shoe list in the paginator format.
3. 127.0.0.1:8000/filter   - By using this API we can filter the Shoes based on Gender(Male/female) and Based on Brand(Puma, Adidas..)
4. 127.0.0.1:8000/buy  - After choosing item, will proceed with Payment
5. 127.0.0.1:8000/proceed  - To the Payment(not implemented).


Uses:
1. This application can handle the search criteria based on Brand/Gender.
2. We can store the Images of the shoes.
3. allows the integration with other Services like Auth0.(Under process)





