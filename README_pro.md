# scraping sentimen on x

> [!NOTE]  
> disini aku udah sediain buat versi [berbayar](/README_pro.md) sama versi [gratis-nya](/README.md).
> yang ini adalah versi *berbayar-nya*.

sebelum mulai pastikan untuk menginstall dependency yang diperlukan seperti :
- dotenv
- tweepy
- textblob
- snscrape (optional)
```bash
pip install dotenv
pip install tweepy
pip install textblob
```
```bash
pip install snscrape
```

jadi begini mas bro, ini kan aku udah nyoba scraping pake API punyanya x toh, di web [Developer Portal X](https://developer.x.com/en/portal/dashboard)
![](/image/Group%2037.png)

nah, ini tuh aku udah nyoba buat generate API key-nya.
jadi pas di **Project & Apps**
![](/image/Screenshot%20from%202025-01-13%2022-31-46.png)
> generate API key-nya
![](/image/Group%2040.png)
> generate AccessToken-nya
![](/image/Group%2039.png)

Jangan lupa nanti habis ngeclone repository ku, kamu bikin file **.env** dulu buat nyimpen API Key sama AccessToken-nya 
> Bisa kayak gini
> Kalo ngeclone
```bash 
    cp .env.example .env
```
atau, bisa bikin manual 
```bash
touch .env
```
contoh formatnya :
```bash
API_KEY=your_api_key_here
API_SECRET=your_api_secret_here
ACCESS_TOKEN=your_access_token_here
ACCESS_TOKEN_SECRET=your_access_token_secret_here
BEARER_TOKEN=your_bearer_token_here
```

Copy *API Key dan Secret Key-nya* dari Developer Portal ke *.env* yang ada didalam kode mu
![](/image/Screenshot%20from%202025-01-13%2022-51-13.png)

Lalu jalankan kode python yang ada [di sini](/pro_main.py)
```bash
python pro_main.py
```
disini, karena aku gk pake yang berbayar, karena ***MAHAL~*** 😭
jadi aku gk bisa tunjukin gimana hasilnya.
